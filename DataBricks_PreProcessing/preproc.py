import pandas as pd

# Paths for the ECG data files in Databricks File System (DBFS)
ecg_file_path = "/dbfs/mnt/stressdata/ECG (EO, AC1, AC2).xlsx"

# Load the ECG data from the specified file with different sheets
ecg_eo = pd.read_excel(ecg_file_path, sheet_name='EO')
ecg_ac1 = pd.read_excel(ecg_file_path, sheet_name='AC1')
ecg_ac2 = pd.read_excel(ecg_file_path, sheet_name='AC2')

# Add prefixes to the column names to indicate the period
ecg_eo = ecg_eo.add_prefix('EO_')
ecg_ac1 = ecg_ac1.add_prefix('AC1_')
ecg_ac2 = ecg_ac2.add_prefix('AC2_')

# Rename the subject number and gender columns back to their original names for joining
ecg_eo = ecg_eo.rename(columns={'EO_Subject NO.': 'Subject NO.', 'EO_Gender': 'Gender'})
ecg_ac1 = ecg_ac1.rename(columns={'AC1_Subject NO.': 'Subject NO.', 'AC1_Gender': 'Gender'})
ecg_ac2 = ecg_ac2.rename(columns={'AC2_Subject NO.': 'Subject NO.', 'AC2_Gender': 'Gender'})

# Merge the data on the 'Subject NO.' and 'Gender' columns
ecg_merged = ecg_eo.merge(ecg_ac1.drop(columns=['Gender']), on='Subject NO.', how='outer') \
                    .merge(ecg_ac2.drop(columns=['Gender']), on='Subject NO.', how='outer')

# Save the merged data to a CSV file in the new mounted container /mnt/processedstressdata
ecg_merged.to_csv('/dbfs/mnt/processedstressdata/ecg_merged.csv', index=False)

# Display the first few rows of the merged data to ensure correctness
display(ecg_merged.head())



# Load the ecg_merged.csv file
ecg_merged = pd.read_csv('/dbfs/mnt/processedstressdata/ecg_merged.csv')

# Columns without segment prefixes
columns_without_segment = ['Subject NO.', 'Gender']

# Define the order of the columns as per your provided format
final_column_order = ['Subject NO.', 'Gender', 'Mean HR (BPM)', 'AVNN (ms)', 'SDNN (ms)', 'NN50 (beats)', 
                      'pNN50 (%)', 'RMSSD (ms)', 'LF (ms2)', 'LF Norm (n.u.)', 'HF (ms2)', 
                      'HF Norm (n.u.)', 'LF/HF Ratio', 'Segment']

# Extract the columns for each segment (EO, AC1, AC2)
eo_columns = [col for col in ecg_merged.columns if 'EO_' in col]
ac1_columns = [col for col in ecg_merged.columns if 'AC1_' in col]
ac2_columns = [col for col in ecg_merged.columns if 'AC2_' in col]

# Remove the EO_, AC1_, and AC2_ prefixes from the columns for consistency
eo_data = ecg_merged[columns_without_segment + eo_columns].copy()
ac1_data = ecg_merged[columns_without_segment + ac1_columns].copy()
ac2_data = ecg_merged[columns_without_segment + ac2_columns].copy()

# Rename the columns to standardize "Mean HR (BPM)" for all segments
# Standardize 'Mean HR' column name and handle case insensitivity
eo_data.columns = columns_without_segment + [col.replace('EO_', '').replace('Mean HR (BPM)', 'Mean HR (BPM)').replace('Mean HR (bpm)', 'Mean HR (BPM)') for col in eo_columns]
ac1_data.columns = columns_without_segment + [col.replace('AC1_', '').replace('Mean HR (bpm)', 'Mean HR (BPM)') for col in ac1_columns]
ac2_data.columns = columns_without_segment + [col.replace('AC2_', '').replace('Mean HR (bpm)', 'Mean HR (BPM)') for col in ac2_columns]

# Add a Segment column to each dataset
eo_data['Segment'] = 'EO'
ac1_data['Segment'] = 'AC1'
ac2_data['Segment'] = 'AC2'

# Ensure that the final column order is consistent across all datasets
# Only keep the columns that are present in both the data and the final_column_order
eo_data = eo_data[[col for col in final_column_order if col in eo_data.columns]]
ac1_data = ac1_data[[col for col in final_column_order if col in ac1_data.columns]]
ac2_data = ac2_data[[col for col in final_column_order if col in ac2_data.columns]]

# Concatenate the data for all segments
final_preprocessed_ecg = pd.concat([eo_data, ac1_data, ac2_data], ignore_index=True)

# Save the final preprocessed ECG data to a CSV file
final_preprocessed_ecg.to_csv('/dbfs/mnt/processedstressdata/final_preprocessed_ecg.csv', index=False)

# Display the first few rows to ensure everything is correct
display(final_preprocessed_ecg.head())




# Path to the normalized EEG data
eeg_file_path = '/dbfs/mnt/stressdata/EEG (EO, AC1, AC2).xlsx'

# Load the normalized EEG data
eeg_data = pd.read_excel(eeg_file_path, sheet_name='Normalize')

# Drop the first row that contains extra headers (electrode positions)
eeg_data = eeg_data.drop([0]).reset_index(drop=True)

# Extract the proper column names using the headers from the first row of the sheet
header_rows = pd.read_excel(eeg_file_path, sheet_name='Normalize').iloc[0, :]

# Define the correct frequency bands and electrodes for renaming
frequency_bands = ['Delta (1-4 Hz)', 'Theta (4-8 Hz)', 'Alpha (8-12 Hz)', 'Beta 1 (12-20 Hz)', 'Beta 2 (20-30 Hz)', 'Gamma (30-60 Hz)', 'Gamma 2 (60-100 Hz)']
electrodes = ['Fp1', 'Fp2', 'F3', 'F4', 'T3', 'T4', 'P3', 'P4']

# Create the final column names with the correct format
new_column_names = ['Segment', 'Subject NO.', 'Gender']

for band in frequency_bands:
    for electrode in electrodes:
        new_column_names.append(f'{electrode}_{band}')

# Apply the new column names
eeg_data.columns = new_column_names[:len(eeg_data.columns)]

# Correct the "Segment" column for 40 participants across three phases (EO, AC1, AC2)
num_subjects = 40
phases = ['EO', 'AC1', 'AC2']
segment_column = [phase for phase in phases for _ in range(num_subjects)]

# Assign the new 'Segment' column
eeg_data['Segment'] = segment_column[:len(eeg_data)]

# Final cleaned EEG data
eeg_data_cleaned = eeg_data

# Save the preprocessed EEG data to a CSV file in the processed-stressdata container
eeg_data_cleaned.to_csv('/dbfs/mnt/processedstressdata/preprocessed_EEG_data.csv', index=False)

# Display the first few rows to ensure correctness
display(eeg_data_cleaned.head())





# Path to the normalized Ratio Alpha Beta data
ratio_of_alpha_beta_file_path = '/dbfs/mnt/stressdata/Ratio of Alpha _ Beta Power.xlsx'

# Load the normalized data
ratio_alpha_data = pd.read_excel(ratio_of_alpha_beta_file_path, sheet_name = 'Alpha')
ratio_beta1_data = pd.read_excel(ratio_of_alpha_beta_file_path, sheet_name = 'Beta1')
ratio_beta2_data = pd.read_excel(ratio_of_alpha_beta_file_path, sheet_name = 'Beta2')

# Function to drop 12 columns (non-normalized data) after ['Subject (No.)', 'Gender']
def drop_columns(df):
    # Find index of 'Subject (No.)' and 'Gender'
    subject_col_idx = df.columns.get_loc('Subject (No.)')
    gender_col_idx = df.columns.get_loc('Gender')
    
    # Keep 'Subject (No.)', 'Gender' and remove the next 12 columns
    cols_to_keep = list(df.columns[:gender_col_idx + 1]) + list(df.columns[gender_col_idx + 13:])
    
    # Return dataframe with only the required columns
    return df[cols_to_keep]

# Function to preprocess and reshape each sheet for the required structure
def preprocess_and_reshape(df, sheet_name, block_size=40):
    """Preprocess and reshape data from one sheet."""
    
    # Drop the first two rows (metadata) and reset the index
    df = df.drop([0, 1]).reset_index(drop=True)

    # Drop the non-normalized columns
    df = drop_columns(df)
    
    # Ensure the columns are correctly named after the drop
    df.columns = ['Subject NO.', 'Gender', 'EO_Fp 1 - Fp 2', 'EO_F 3 - F 4', 'EO_T 3 - T 4', 'EO_P 3 - P 4',
                  'AC1_Fp 1 - Fp 2', 'AC1_F 3 - F 4', 'AC1_T 3 - T 4', 'AC1_P 3 - P 4',
                  'AC2_Fp 1 - Fp 2', 'AC2_F 3 - F 4', 'AC2_T 3 - T 4', 'AC2_P 3 - P 4']
    
    # Reshape data by periods (EO, AC1, AC2)
    reshaped_data = pd.DataFrame()
    periods = ['EO', 'AC1', 'AC2']
    for period in periods:
        block = df[['Subject NO.', 'Gender',
                    f'{period}_Fp 1 - Fp 2', f'{period}_F 3 - F 4', f'{period}_T 3 - T 4', f'{period}_P 3 - P 4']].copy()
        
        # Rename columns to match the period
        block.columns = ['Subject NO.', 'Gender', f'{sheet_name}_(Fp 1 - Fp 2)', f'{sheet_name}_(F 3 - F 4)',
                         f'{sheet_name}_(T 3 - T 4)', f'{sheet_name}_(P 3 - P 4)']
        
        # Add segment column
        block['Segment'] = period
        
        # Append reshaped period data
        reshaped_data = pd.concat([reshaped_data, block], ignore_index=True)
    
    return reshaped_data

# Preprocess and reshape each sheet
alpha_data = preprocess_and_reshape(ratio_alpha_data, 'Alpha')
beta1_data = preprocess_and_reshape(ratio_beta1_data, 'Beta1')
beta2_data = preprocess_and_reshape(ratio_beta2_data, 'Beta2')

# Merge the three datasets on 'Subject NO.', 'Gender', and 'Segment'
final_df = alpha_data.merge(beta1_data, on=['Subject NO.', 'Gender', 'Segment'])
final_df = final_df.merge(beta2_data, on=['Subject NO.', 'Gender', 'Segment'])

# Move the 'Segment' column to the 3rd position
cols = final_df.columns.tolist()
cols.insert(2, cols.pop(cols.index('Segment')))  # Move 'Segment' to the 3rd position
final_df = final_df[cols]

# Save the preprocessed Ratio Alpha Beta data to a CSV file in the processed-stressdata container
final_df.to_csv('/dbfs/mnt/processedstressdata/preprocessed_ratio_alpha_beta_power.csv', index=False)

# Display the first few rows to ensure correctness
display(final_df)
