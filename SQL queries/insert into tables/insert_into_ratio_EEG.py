import pandas as pd
import pyodbc

connection_string = (
"DRIVER={ODBC Driver 17 for SQL Server};"
"SERVER=DESKTOP-F9SAMSI\SQLEXPRESS;"  
"DATABASE=stressFeatures;"  
"Trusted_Connection=yes;" 
)

csv_file_path = 'preprocessed_ratio_alpha_beta_power.csv'
data = pd.read_csv(csv_file_path)
def insert_into_table(gender,schema,tablename,type):
    temp_filtered_data = data[data['Gender'] == gender]
    filtered_data = temp_filtered_data[ temp_filtered_data['Segment'] == schema]
    conn = pyodbc.connect( connection_string )

    table_name = "["+schema+"].["+tablename+"]"

    insert_query = f'''
        INSERT INTO {table_name} ([SubjectNO],[Fp1 - Fp2],
        [F3 - F4],[T3 - T4],[P3 - P4])
        VALUES (?, ?, ?, ?, ?)
    '''

    cursor = conn.cursor()

    for index, row in filtered_data[['Subject NO.',type+'_(Fp 1 - Fp 2)',type+'_(F 3 - F 4)',type+'_(T 3 - T 4)',type+'_(P 3 - P 4)']].iterrows():
        cursor.execute(insert_query, (row['Subject NO.'] ,row[type+'_(Fp 1 - Fp 2)'],row[type+'_(F 3 - F 4)'],row[type+'_(T 3 - T 4)'],row[type+'_(P 3 - P 4)']))

    conn.commit()

    cursor.close()
    conn.close()

insert_into_table("Male","EO","EEG_Ratio_Alpha(Males)","Alpha")
insert_into_table("Female","EO","EEG_Ratio_Alpha(Females)","Alpha")
insert_into_table("Male","AC1","EEG_Ratio_Alpha(Males)","Alpha")
insert_into_table("Female","AC1","EEG_Ratio_Alpha(Females)","Alpha")
insert_into_table("Male","AC2","EEG_Ratio_Alpha(Males)","Alpha")
insert_into_table("Female","AC2","EEG_Ratio_Alpha(Females)","Alpha")

insert_into_table("Male","EO","EEG_Ratio_Beta_1(Males)","Beta1")
insert_into_table("Female","EO","EEG_Ratio_Beta_1(Females)","Beta1")
insert_into_table("Male","AC1","EEG_Ratio_Beta_1(Males)","Beta1")
insert_into_table("Female","AC1","EEG_Ratio_Beta_1(Females)","Beta1")
insert_into_table("Male","AC2","EEG_Ratio_Beta_1(Males)","Beta1")
insert_into_table("Female","AC2","EEG_Ratio_Beta_1(Females)","Beta1")

insert_into_table("Male","EO","EEG_Ratio_Beta_2(Males)","Beta2")
insert_into_table("Female","EO","EEG_Ratio_Beta_2(Females)","Beta2")
insert_into_table("Male","AC1","EEG_Ratio_Beta_2(Males)","Beta2")
insert_into_table("Female","AC1","EEG_Ratio_Beta_2(Females)","Beta2")
insert_into_table("Male","AC2","EEG_Ratio_Beta_2(Males)","Beta2")
insert_into_table("Female","AC2","EEG_Ratio_Beta_2(Females)","Beta2")