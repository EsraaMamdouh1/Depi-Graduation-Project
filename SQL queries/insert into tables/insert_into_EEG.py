import pandas as pd
import pyodbc

connection_string = (
"DRIVER={ODBC Driver 17 for SQL Server};"
"SERVER=DESKTOP-F9SAMSI\SQLEXPRESS;"  
"DATABASE=stressFeatures;"  
"Trusted_Connection=yes;" 
)

csv_file_path = 'preprocessed_EEG_data.csv'
data = pd.read_csv(csv_file_path)
def insert_into_table(gender,schema,tablename,type):
    temp_filtered_data = data[data['Gender'] == gender]
    filtered_data = temp_filtered_data[ temp_filtered_data['Segment'] == schema]
    conn = pyodbc.connect( connection_string )

    table_name = "["+schema+"].["+tablename+"]"

    insert_query = f'''
        INSERT INTO {table_name} ([SubjectNO],[Fp1]
        ,[Fp2],[F3],[F4],[T3],[T4]
        ,[P3],[P4])
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''

    cursor = conn.cursor()

    for index, row in filtered_data[['Subject NO.', 'Fp1_'+type,'Fp2_'+type,'F3_'+type,'F4_'+type,'T3_'+type,'T4_'+type,'P3_'+type,'P4_'+type]].iterrows():
        cursor.execute(insert_query, (row['Subject NO.'] ,row['Fp1_'+type],row['Fp2_'+type],row['F3_'+type],row['F4_'+type],row['T3_'+type],row['T4_'+type],row['P3_'+type],row['P4_'+type]))

    conn.commit()

    cursor.close()
    conn.close()

insert_into_table("Male","EO","EEG_Delta(Males)","Delta (1-4 Hz)")
insert_into_table("Female","EO","EEG_Delta(Females)","Delta (1-4 Hz)")
insert_into_table("Male","AC1","EEG_Delta(Males)","Delta (1-4 Hz)")
insert_into_table("Female","AC1","EEG_Delta(Females)","Delta (1-4 Hz)")
insert_into_table("Male","AC2","EEG_Delta(Males)","Delta (1-4 Hz)")
insert_into_table("Female","AC2","EEG_Delta(Females)","Delta (1-4 Hz)")

insert_into_table("Male","EO","EEG_Theta(Males)","Theta (4-8 Hz)")
insert_into_table("Female","EO","EEG_Theta(Females)","Theta (4-8 Hz)")
insert_into_table("Male","AC1","EEG_Theta(Males)","Theta (4-8 Hz)")
insert_into_table("Female","AC1","EEG_Theta(Females)","Theta (4-8 Hz)")
insert_into_table("Male","AC2","EEG_Theta(Males)","Theta (4-8 Hz)")
insert_into_table("Female","AC2","EEG_Theta(Females)","Theta (4-8 Hz)")

insert_into_table("Male","EO","EEG_Alpha(Males)","Alpha (8-12 Hz)")
insert_into_table("Female","EO","EEG_Alpha(Females)","Alpha (8-12 Hz)")
insert_into_table("Male","AC1","EEG_Alpha(Males)","Alpha (8-12 Hz)")
insert_into_table("Female","AC1","EEG_Alpha(Females)","Alpha (8-12 Hz)")
insert_into_table("Male","AC2","EEG_Alpha(Males)","Alpha (8-12 Hz)")
insert_into_table("Female","AC2","EEG_Alpha(Females)","Alpha (8-12 Hz)")

insert_into_table("Male","EO","EEG_Beta_1(Males)","Beta 1 (12-20 Hz)")
insert_into_table("Female","EO","EEG_Beta_1(Females)","Beta 1 (12-20 Hz)")
insert_into_table("Male","AC1","EEG_Beta_1(Males)","Beta 1 (12-20 Hz)")
insert_into_table("Female","AC1","EEG_Beta_1(Females)","Beta 1 (12-20 Hz)")
insert_into_table("Male","AC2","EEG_Beta_1(Males)","Beta 1 (12-20 Hz)")
insert_into_table("Female","AC2","EEG_Beta_1(Females)","Beta 1 (12-20 Hz)")

insert_into_table("Male","EO","EEG_Beta_2(Males)","Beta 2 (20-30 Hz)")
insert_into_table("Female","EO","EEG_Beta_2(Females)","Beta 2 (20-30 Hz)")
insert_into_table("Male","AC1","EEG_Beta_2(Males)","Beta 2 (20-30 Hz)")
insert_into_table("Female","AC1","EEG_Beta_2(Females)","Beta 2 (20-30 Hz)")
insert_into_table("Male","AC2","EEG_Beta_2(Males)","Beta 2 (20-30 Hz)")
insert_into_table("Female","AC2","EEG_Beta_2(Females)","Beta 2 (20-30 Hz)")

insert_into_table("Male","EO","EEG_Gamma_1(Males)","Gamma (30-60 Hz)")
insert_into_table("Female","EO","EEG_Gamma_1(Females)","Gamma (30-60 Hz)")
insert_into_table("Male","AC1","EEG_Gamma_1(Males)","Gamma (30-60 Hz)")
insert_into_table("Female","AC1","EEG_Gamma_1(Females)","Gamma (30-60 Hz)")
insert_into_table("Male","AC2","EEG_Gamma_1(Males)","Gamma (30-60 Hz)")
insert_into_table("Female","AC2","EEG_Gamma_1(Females)","Gamma (30-60 Hz)")

insert_into_table("Male","EO","EEG_Gamma_2(Males)","Gamma 2 (60-100 Hz)")
insert_into_table("Female","EO","EEG_Gamma_2(Females)","Gamma 2 (60-100 Hz)")
insert_into_table("Male","AC1","EEG_Gamma_2(Males)","Gamma 2 (60-100 Hz)")
insert_into_table("Female","AC1","EEG_Gamma_2(Females)","Gamma 2 (60-100 Hz)")
insert_into_table("Male","AC2","EEG_Gamma_2(Males)","Gamma 2 (60-100 Hz)")
insert_into_table("Female","AC2","EEG_Gamma_2(Females)","Gamma 2 (60-100 Hz)")