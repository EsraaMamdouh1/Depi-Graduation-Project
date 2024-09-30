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

conn = pyodbc.connect( connection_string )

table_name = "Members"

insert_query = f'''
    INSERT INTO {table_name} ([SubjectNO], [Gender])
    VALUES (?, ?)
'''

check_query = f'''
    SELECT COUNT(*) FROM {table_name} WHERE SubjectNO = ?
'''
cursor = conn.cursor()

for index, row in data[['Subject NO.', 'Gender']].iterrows():
    cursor.execute(check_query, row['Subject NO.'])
    exists = cursor.fetchone()[0]

    if exists > 0:
        break
    else:
        cursor.execute(insert_query, (row['Subject NO.'], row['Gender']))

conn.commit()

cursor.close()
conn.close()