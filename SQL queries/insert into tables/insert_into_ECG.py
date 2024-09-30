import pandas as pd
import pyodbc

connection_string = (
"DRIVER={ODBC Driver 17 for SQL Server};"
"SERVER=DESKTOP-F9SAMSI\SQLEXPRESS;"  
"DATABASE=stressFeatures;"  
"Trusted_Connection=yes;" 
)

csv_file_path = 'final_preprocessed_ecg.csv'
data = pd.read_csv(csv_file_path)
def insert_into_table(gender,schema,tablename):
    temp_filtered_data = data[data['Gender'] == gender]
    filtered_data = temp_filtered_data[ temp_filtered_data['Segment'] == schema]
    conn = pyodbc.connect( connection_string )

    table_name = "["+schema+"].["+tablename+"]"

    insert_query = f'''
        INSERT INTO {table_name} ([SubjectNO],[Mean HR (BPM)]
        ,[AVNN (ms)],[SDNN (ms)],[NN50 (beats)],[pNN50 (%)],[RMSSD (ms)]
        ,[LF (ms2)],[LF Norm (n.u.)],[HF (ms2)],[HF Norm (n.u.)],[LF/HF Ratio] )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''

    cursor = conn.cursor()

    for index, row in filtered_data[['Subject NO.', 'Mean HR (BPM)','AVNN (ms)','SDNN (ms)','NN50 (beats)','pNN50 (%)','RMSSD (ms)','LF (ms2)','LF Norm (n.u.)','HF (ms2)','HF Norm (n.u.)','LF/HF Ratio']].iterrows():
        cursor.execute(insert_query, (row['Subject NO.'],row['Mean HR (BPM)']
        ,row['AVNN (ms)'],row['SDNN (ms)'],row['NN50 (beats)'],row['pNN50 (%)'],row['RMSSD (ms)']
        ,row['LF (ms2)'],row['LF Norm (n.u.)'],row['HF (ms2)'],row['HF Norm (n.u.)'],row['LF/HF Ratio']))

    conn.commit()

    cursor.close()
    conn.close()

insert_into_table("Male","EO","ECG(Males)")
insert_into_table("Female","EO","ECG(Females)")
insert_into_table("Male","AC1","ECG(Males)")
insert_into_table("Female","AC1","ECG(Females)")
insert_into_table("Male","AC2","ECG(Males)")
insert_into_table("Female","AC2","ECG(Females)")