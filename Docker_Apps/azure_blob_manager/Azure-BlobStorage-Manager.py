import os
from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient
from tkinter import filedialog, Tk, Button, Label, Listbox, Scrollbar, Entry, messagebox
import tkinter as tk

# Global variable to store the selected container
selected_container = None

# Function to load Azure credentials from a text file
def load_azure_credentials(file_path='azure_credentials.txt'):
    try:
        with open(file_path, 'r') as f:
            lines = f.read().splitlines()
        if len(lines) < 3:
            raise ValueError("Not enough credentials found in the file.")
        client_id = lines[0]
        tenant_id = lines[1]
        client_secret = lines[2]
        return client_id, tenant_id, client_secret
    except Exception as e:
        raise ValueError(f"Error reading credentials: {e}")

# Initialize the BlobServiceClient using ClientSecretCredential
def initialize_blob_service():
    try:
        client_id, tenant_id, client_secret = load_azure_credentials()

        # Using ClientSecretCredential for secure authentication
        credential = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
        blob_service_client = BlobServiceClient(account_url="https://stressdetectionstorage.blob.core.windows.net", credential=credential)
        return blob_service_client
    except Exception as ex:
        print(f"Error connecting to Blob Storage: {ex}")
        return None

# Function to list all containers
def list_containers():
    try:
        blob_service_client = initialize_blob_service()
        containers = blob_service_client.list_containers()
        return [container.name for container in containers]
    except Exception as ex:
        label_status.config(text=f"Error listing containers: {ex}")
        return []

# Function to list blobs in a container
def list_files_in_container(container_name):
    try:
        blob_service_client = initialize_blob_service()
        container_client = blob_service_client.get_container_client(container_name)
        blobs = container_client.list_blobs()
        return [blob.name for blob in blobs]
    except Exception as ex:
        label_status.config(text=f"Error listing files: {ex}")
        return []

# Function to handle container selection
def on_container_select(event):
    global selected_container
    try:
        if container_listbox.curselection():  # Check if a container is selected
            selected_container = container_listbox.get(container_listbox.curselection())
            label_status.config(text=f"Selected container: {selected_container}")
            load_files_in_container(selected_container)
    except Exception as ex:
        label_status.config(text=f"Error selecting container: {ex}")

# Function to load files into the file listbox
def load_files_in_container(container_name):
    file_listbox.delete(0, tk.END)
    files = list_files_in_container(container_name)
    if not files:
        label_status.config(text=f"No files found in container '{container_name}'")
    else:
        for file in files:
            file_listbox.insert(tk.END, file)

# Function to upload a file to the selected container
def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path and selected_container:  # Check if a container is selected
        blob_name = os.path.basename(file_path)
        try:
            blob_service_client = initialize_blob_service()
            blob_client = blob_service_client.get_blob_client(container=selected_container, blob=blob_name)

            # Upload file
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data)
                label_status.config(text=f"File uploaded: {blob_name}")
                load_files_in_container(selected_container)

        except Exception as ex:
            label_status.config(text=f"Error uploading file: {ex}")
    else:
        label_status.config(text="No container selected for upload.")

# Function to download a selected file from the container
def download_file():
    if file_listbox.curselection():  # Check if a file is selected
        file_name = file_listbox.get(file_listbox.curselection())
        save_path = filedialog.askdirectory()

        if file_name and save_path and selected_container:  # Check if a container is selected
            try:
                blob_service_client = initialize_blob_service()
                blob_client = blob_service_client.get_blob_client(container=selected_container, blob=file_name)

                download_file_path = os.path.join(save_path, file_name)
                with open(download_file_path, "wb") as file:
                    file.write(blob_client.download_blob().readall())
                    label_status.config(text=f"File downloaded: {download_file_path}")

            except Exception as ex:
                label_status.config(text=f"Error downloading file: {ex}")
        else:
            label_status.config(text="No container or file selected for download.")
    else:
        label_status.config(text="No file selected for download.")

# Function to delete a selected file from the container
def delete_file():
    if file_listbox.curselection():  # Check if a file is selected
        file_name = file_listbox.get(file_listbox.curselection())
        if file_name and selected_container:  # Check if a container is selected
            try:
                blob_service_client = initialize_blob_service()
                blob_client = blob_service_client.get_blob_client(container=selected_container, blob=file_name)
                blob_client.delete_blob()
                label_status.config(text=f"File deleted: {file_name}")
                load_files_in_container(selected_container)

            except Exception as ex:
                label_status.config(text=f"Error deleting file: {ex}")
        else:
            label_status.config(text="No container or file selected for deletion.")
    else:
        label_status.config(text="No file selected for deletion.")

# Function to create a new container
def create_container():
    container_name = container_entry.get()
    if container_name:
        try:
            blob_service_client = initialize_blob_service()
            container_client = blob_service_client.create_container(container_name)
            label_status.config(text=f"Container created: {container_name}")
            container_listbox.insert(tk.END, container_name)

        except Exception as ex:
            label_status.config(text=f"Error creating container: {ex}")

# Function to delete a container
def delete_container():
    global selected_container
    if container_listbox.curselection():  # Check if a container is selected
        container_name = container_listbox.get(container_listbox.curselection())
        if container_name:
            try:
                blob_service_client = initialize_blob_service()
                blob_service_client.delete_container(container_name)
                label_status.config(text=f"Container deleted: {container_name}")
                container_listbox.delete(container_listbox.curselection())
                file_listbox.delete(0, tk.END)
                selected_container = None  # Clear the selected container

            except Exception as ex:
                label_status.config(text=f"Error deleting container: {ex}")
    else:
        label_status.config(text="No container selected for deletion.")


# Tkinter GUI setup
def create_gui():
    global label_status, container_listbox, file_listbox, container_entry

    root = Tk()
    root.title("Azure Blob Storage Manager")

    label_status = Label(root, text="Azure Blob Storage Manager", font=("Arial", 12))
    label_status.pack(pady=10)

    # Container Listbox
    label_container = Label(root, text="Select a Container:", font=("Arial", 10))
    label_container.pack(pady=5)

    container_listbox = Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
    container_listbox.pack(pady=5)
    container_scrollbar = Scrollbar(root)
    container_scrollbar.pack(side="right", fill="y")
    container_listbox.config(yscrollcommand=container_scrollbar.set)
    container_scrollbar.config(command=container_listbox.yview)

    # Load containers into the listbox
    containers = list_containers()
    for container in containers:
        container_listbox.insert(tk.END, container)

    # Bind the container selection to the load files function
    container_listbox.bind('<<ListboxSelect>>', on_container_select)

    # File Listbox
    label_files = Label(root, text="Files in the Selected Container:", font=("Arial", 10))
    label_files.pack(pady=5)

    file_listbox = Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
    file_listbox.pack(pady=5)
    file_scrollbar = Scrollbar(root)
    file_scrollbar.pack(side="right", fill="y")
    file_listbox.config(yscrollcommand=file_scrollbar.set)
    file_scrollbar.config(command=file_listbox.yview)

    # Container Management
    container_entry = Entry(root, width=30)
    container_entry.pack(pady=5)
    container_entry.insert(0, "Enter new container name")

    create_container_button = Button(root, text="Create Container", command=create_container, width=20)
    create_container_button.pack(pady=5)

    delete_container_button = Button(root, text="Delete Container", command=delete_container, width=20)
    delete_container_button.pack(pady=5)

    # Buttons for file operations
    upload_button = Button(root, text="Upload File", command=upload_file, width=20)
    upload_button.pack(pady=5)

    download_button = Button(root, text="Download File", command=download_file, width=20)
    download_button.pack(pady=5)

    delete_file_button = Button(root, text="Delete File", command=delete_file, width=20)
    delete_file_button.pack(pady=5)

    root.mainloop()

# Main function to run the script
if __name__ == "__main__":
    create_gui()
