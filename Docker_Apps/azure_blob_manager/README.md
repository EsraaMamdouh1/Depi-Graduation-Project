# Azure Blob Storage Manager

This application allows users to easily manage Azure Blob Storage containers and files via a graphical user interface (GUI). You can perform operations such as:

- Listing containers
- Uploading files to containers
- Downloading files from containers
- Deleting files and containers

The application is built with Python and Docker and includes additional security measures to ensure sensitive information like Azure credentials remains protected.

## How to Run the Application

### Prerequisites:

1. **Docker**: Ensure that Docker is installed on your system. If not, download and install it from [Docker's official site](https://www.docker.com/).
2. **Azure Credentials**: You will need the following Azure credentials:
   - Client ID
   - Tenant ID
   - Client Secret
3. These credentials are required for authentication with Azure. **Note**: You won't find the `azure_credentials.txt` in the repository. If you need access to the credentials for testing or deployment, please contact me via the contact information provided in my profile.

4. **Display Server**: The application uses a GUI based on Tkinter. If you're using Docker on Windows, ensure you have X11 forwarding set up with VcXsrv or an alternative X Server. For setup details, refer to the [X11 documentation](https://sourceforge.net/projects/vcxsrv/).

### Steps to Run:

1. **Pull the Docker Image**: If you're working as part of my team, pull the Docker image by running the following command:

    ```bash
    docker pull apdoelepe/azure_blob_manager
    ```

2. **Run the Docker Container**: To run the container, execute the following command:

    ```bash
    docker run -p 5000:5000 -e DISPLAY=host.docker.internal:0.0 -v "C:/path/to/your/azure_credentials.txt:/app/azure_credentials.txt" apdoelepe/azure_blob_manager
    ```

    - Make sure to replace `"C:/path/to/your/azure_credentials.txt"` with the actual path to your credentials file. You must have the `azure_credentials.txt` file that contains the necessary credentials.

### Interacting with the App:

- The GUI allows you to perform various operations with your Azure Blob Storage account.
- You can list containers, upload, download, delete files, and manage containers.

### For Team Members:

- Team members can follow the same instructions to run the container.
- If you don't have access to the credentials, please contact me to get access via my profile information.

## Security Measures:

- **Azure Credentials**: The app uses Azure's `DefaultAzureCredential` for secure authentication. The credentials are not hardcoded and are securely stored in the `azure_credentials.txt` file.
- **Environment Variables**: The Docker image does not store sensitive information directly in environment variables. All credentials are read from the mounted file.
- **X11 GUI**: Since Docker cannot directly run Tkinter GUIs on Windows, an X Server is used to display the GUI. Ensure proper setup as detailed in the prerequisites.

## Contact Information:

If you encounter any issues or need access to the Azure credentials, feel free to reach out via my GitHub or LinkedIn profiles:

- **GitHub**: [https://github.com/AbdelrahmanAboegela](https://github.com/AbdelrahmanAboegela)
- **LinkedIn**: [https://www.linkedin.com/in/abdelrahman-alshames-635aa3277/](https://www.linkedin.com/in/abdelrahman-alshames-635aa3277/)
