# Stress Detection and Analysis Project

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

#### Security:
- OAuth 2.0 authentication is used to ensure secure access.
- Credentials are managed via environment variables.

### 2. Data Mounting in Databricks

#### Mounting Process:
The **raw data** and **processed data** containers were mounted to Databricks for direct access to the data without needing manual downloads.

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

#### Processing:
- Both datasets were cleaned, merged, and exported back to the processed-data container.
- Important metrics, such as the ratio of Alpha and Beta power in EEG, were calculated.

## How to Run the Blob Storage App

We developed a Python application for easy access to the Azure Blob Storage containers, allowing for the upload, download, and deletion of files.

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

