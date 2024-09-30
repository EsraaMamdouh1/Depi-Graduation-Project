# Stress Detection and Analysis Project

## Table of Contents
1. [Project Overview](#project-overview)
2. [Key Components](#key-components)  
    2.1 [Azure Blob Storage](#1-azure-blob-storage)  
        2.1.1 [Storage Setup](#storage-setup)  
        2.1.2 [Security](#security)  
    2.2 [Data Mounting in Databricks](#2-data-mounting-in-databricks)  
        2.2.1 [Mounting Process](#mounting-process)  
        2.2.2 [Mount Points](#mount-points)  
        2.2.3 [Security](#databricks-security)  
    2.3 [Data Preprocessing](#3-data-preprocessing)  
        2.3.1 [Data Types](#data-types)  
        2.3.2 [Processing](#processing)  
3. [How to Run the Blob Storage App](#how-to-run-the-blob-storage-app)  
4. [Security Considerations](#security-considerations)  
5. [Contact Information](#contact-information)

## Project Overview

This project focuses on **Stress Detection and Analysis** using EEG (Electroencephalogram) and ECG (Electrocardiogram) data. The goal is to preprocess this data and use it for developing machine learning models that can classify stress levels in individuals. We are leveraging Azure services for storage, computation, and model development.

### Current Stage:
We have completed the data collection, storage setup, and preprocessing. The next steps involve model development and deployment.

## Key Components

### 1. Azure Blob Storage

#### Storage Setup:
Two containers have been created:
- **raw-data**: Contains the original EEG and ECG files.
- **processed-data**: Contains the processed data, which has been cleaned and organized for analysis.

You can check out the code for managing Azure Blob Storage here:  
[Azure Blob Manager](https://github.com/AbdelrahmanAboegela/Depi-Graduation-Project/tree/main/Docker_Apps/azure_blob_manager)

#### Security:
- OAuth 2.0 authentication is used to ensure secure access.
- Credentials are managed via environment variables.

### 2. Data Mounting in Databricks

#### Mounting Process:
The **raw data** and **processed data** containers were mounted to Databricks for direct access to the data without needing manual downloads.

You can find the data mounting scripts here:  
[Databricks PreProcessing](https://github.com/AbdelrahmanAboegela/Depi-Graduation-Project/tree/main/DataBricks_PreProcessing)

#### Mount Points:
- `/mnt/stressdata`: For raw data.
- `/mnt/processedstressdata`: For processed data.

#### Security:
The Azure credentials (client ID, tenant ID, and client secret) were securely used for mounting the Blob Storage.

### 3. Data Preprocessing

#### Data Types:
The project deals with two primary types of data:
- **ECG Data**: Heart rate variability and other metrics.
- **EEG Data**: Brainwave frequencies (Delta, Theta, Alpha, Beta, Gamma).

You can find the preprocessing scripts here:  
[Preprocessing Code](https://github.com/AbdelrahmanAboegela/Depi-Graduation-Project/tree/main/DataBricks_PreProcessing)

#### Processing:
- Both datasets were cleaned, merged, and exported back to the processed-data container.
- Important metrics, such as the ratio of Alpha and Beta power in EEG, were calculated.

## How to Run the Blob Storage App

We developed a Python application for easy access to the Azure Blob Storage containers, allowing for the upload, download, and deletion of files.

You can find the application here:  
[Azure Blob Manager App](https://github.com/AbdelrahmanAboegela/Depi-Graduation-Project/tree/main/Docker_Apps/azure_blob_manager)

### Steps:
1. Clone the repository containing the app.
2. Ensure Docker is installed on your machine.
3. To run the app, use the following command:
    ```bash
    docker run -p 5000:5000 -e DISPLAY=host.docker.internal:0.0 apdoelepe/azure_blob_manager
    ```
4. If the app requires Azure credentials for access, contact me via GitHub or LinkedIn to provide the `azure_credentials.txt`.

## Security Considerations

- **OAuth 2.0 Authentication** ensures that only authorized users can access the Azure Blob Storage.
- **Environment Variables** are used for handling sensitive information like client secrets, ensuring that they are not exposed in the codebase.
- **Docker Deployment**: The app is containerized using Docker for easy deployment across different environments, ensuring that the same version is available to the entire team.

## Contact Information

For any questions or access to the credentials, you can reach out to me via:

- **GitHub**: [AbdelrahmanAboegela](https://github.com/AbdelrahmanAboegela)
- **LinkedIn**: [Abdelrahman Alshames](https://www.linkedin.com/in/abdelrahman-alshames-635aa3277/)
