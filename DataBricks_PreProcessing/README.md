# Data Preprocessing and Data Mounting in Databricks

## Data Mounting in Databricks

### Purpose of Mounting

Mounting Azure Blob Storage in Databricks allows users to access large datasets stored in Blob Storage directly from Databricks. This approach ensures seamless data access without manually downloading the data each time. The storage is mounted as a filesystem in Databricks, making it easy to read and write files directly.

### Key Steps for Mounting:

#### Authentication:
We used OAuth 2.0 authentication for secure access to Azure Blob Storage. This requires:
- **client_id**: Application (client) ID.
- **tenant_id**: Directory (tenant) ID.
- **client_secret**: A secret to authenticate the client.

#### Mounting Raw Data:
We mounted the `raw-data` container from Azure Blob Storage to Databricks. The container holds the original ECG and EEG files. The `dbutils.fs.mount()` function is used in Databricks to perform this operation. After mounting, the data is accessible via a path (`/mnt/stressdata`).

#### Mounting Processed Data:
Similarly, we mounted the `processed-data` container to store and access processed data after the initial cleaning and transformation. This mount point is `/mnt/processedstressdata`.

### Why We Mount:
By mounting the Blob Storage, we avoid the overhead of downloading large datasets repeatedly. Databricks can work directly with data in Blob Storage as if it were local, ensuring scalability and reducing processing time for large-scale datasets like EEG and ECG.

## Data Preprocessing

### Overview of Data
The project deals with EEG and ECG data related to stress detection in participants. The data is organized into three segments:
- **EO (Baseline)**: The participants are in a relaxed state.
- **AC1 (Low Stress)**: The participants perform arithmetic tasks.
- **AC2 (High Stress)**: The participants repeat the tasks with auditory distractions.

Each segment is recorded for both EEG (brain activity) and ECG (heart rate variability), making it essential to preprocess and clean the data for further analysis and machine learning models.

### Why We Process the Data

#### Data Consistency:
Each data file (ECG, EEG) contains several columns corresponding to different signals or metrics. To ensure consistency and compatibility, we cleaned the column names and standardized them across different segments (EO, AC1, AC2).

#### Merging:
Since data is segmented into three parts for each participant (EO, AC1, AC2), we merged the data for each participant across all segments, allowing for a unified dataset that could be used for model training.

#### Handling Missing Data:
During preprocessing, special care was taken to handle any missing values or inconsistencies, ensuring that the datasets are clean and reliable for further analysis.

#### CSV Exports:
After preprocessing, the cleaned and merged datasets were saved as CSV files back into the `processed-data` container in Azure Blob Storage. This allows for easy access in future processing steps or machine learning models.

### Processed Data:

#### ECG Preprocessing:
The ECG data across three segments was loaded, prefixes were added for better organization, and the data was merged across the different time segments (EO, AC1, AC2). The cleaned data includes important ECG metrics such as heart rate variability (HRV), AVNN, and LF/HF Ratio, which are critical in understanding stress levels.

#### EEG Preprocessing:
Similar to the ECG, EEG data was cleaned and reorganized. Important frequency bands were extracted and organized by electrodes (Fp1, Fp2, F3, etc.). These bands include Delta, Theta, Alpha, Beta, and Gamma, each offering insights into brain activity under stress.

#### Ratio Alpha Beta Preprocessing:
In addition to raw EEG and ECG data, the Ratio of Alpha and Beta Power was calculated and reshaped. This metric is useful in quantifying mental workload and stress levels.

## Security Measures

### OAuth 2.0 Authentication:
Azure’s `DefaultAzureCredential` is used for secure access to the Blob Storage account. Sensitive details such as the `client_id`, `tenant_id`, and `client_secret` are used to ensure that only authorized users can access the data.

### Environment Variables:
The sensitive authentication information is stored in environment variables, ensuring it is not exposed in the codebase or the repository.

### Credential Management:
We employed a client secret for authentication instead of shared keys, which adds an extra layer of security by rotating client secrets periodically and monitoring access logs.

## How to Use This App

### Mounting Data:
Ensure your Databricks workspace has access to the Azure Blob Storage account by mounting the containers (`raw-data` and `processed-data`) as described.

### Running Preprocessing:
Once the data is mounted, run the preprocessing scripts provided in the repository to clean and merge the EEG and ECG data.

### Security Considerations:
Credentials for accessing Blob Storage are not stored in the repository. Please contact ME to obtain access to the `azure_credentials.txt` file that holds the necessary credentials for mounting the Blob Storage account.

## Contact Information:
If you need further information about the setup or credentials, feel free to reach out via my profile info:

- **GitHub**: [https://github.com/AbdelrahmanAboegela](https://github.com/AbdelrahmanAboegela)
- **LinkedIn**: [https://www.linkedin.com/in/abdelrahman-alshames-635aa3277/](https://www.linkedin.com/in/abdelrahman-alshames-635aa3277/)
