<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stress Detection Project Database Setup</title>
</head>
<body>

<h1>Stress Detection Project Database Setup</h1>

<p>This project involves creating a database for stress detection based on EEG and ECG data. The process includes creating tables using stored procedures, importing data into these tables, and automating these tasks using Python scripts.</p>

<h2>Prerequisites</h2>
<p>Before proceeding with the setup, ensure the following are installed and running:</p>
<ul>
    <li>SQL Server (for database management)</li>
    <li>Python (with necessary libraries such as <code>pandas</code>, <code>pyodbc</code>)</li>
    <li>SQL Server Management Studio (SSMS) (optional for manual operations)</li>
    <li>Windows Authentication or access credentials for connecting to SQL Server</li>
</ul>

<h2>Setting Up the Database</h2>

<h3>Step 1: Create the Database</h3>
<p>First, create a database named <code>stressFeatures</code> where all the tables will be stored. Run the following SQL command:</p>
<pre>
<code>
CREATE DATABASE stressFeatures;
</code>
</pre>

<p>After creating the database, connect to it by running:</p>
<pre>
<code>
USE stressFeatures;
</code>
</pre>

<h3>Step 2: Run SQL Scripts to Create Tables</h3>
<p>Create tables using stored procedures provided in SQL scripts.</p>

<ol>
    <li>Run the scripts to create the stored procedures using your preferred tool (e.g., SQL Server Management Studio). The following scripts must be executed:
        <ul>
            <li><code>create schemas.sql</code></li>
            <li><code>create ECG tables.sql</code></li>
            <li><code>create EEG_Alpha tables.sql</code>, <code>create EEG_Beta_1 tables.sql</code>, etc.</li>
            <li><code>create EEG_Ratio_Alpha tables.sql</code>, <code>create EEG_Ratio_Beta_1 tables.sql</code>, etc.</li>
        </ul>
    </li>
    <li>Execute the stored procedures to create the actual tables in the <code>stressFeatures</code> database. For example:
<pre>
<code>
EXEC create_ecg_tables;
EXEC create_eeg_alpha_tables;
EXEC create_eeg_beta_1_tables;
</code>
</pre>
    </li>
    <li>Verify that the tables were created by running this query:
<pre>
<code>
SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_TYPE = 'BASE TABLE';
</code>
</pre>
    </li>
</ol>

<p>The following tables should be present:</p>
<ul>
    <li><code>Members</code></li>
    <li><code>ECG</code></li>
    <li><code>EEG_Alpha</code>, <code>EEG_Beta_1</code>, <code>EEG_Beta_2</code>, etc.</li>
    <li><code>EEG_Ratio_Alpha</code>, <code>EEG_Ratio_Beta_1</code>, <code>EEG_Ratio_Beta_2</code>, etc.</li>
</ul>

<h3>Step 3: Insert Data using Python Scripts</h3>
<p>Once the tables are created, you can insert data into these tables using Python scripts.</p>

<h4>Insert Members Data</h4>
<p>Use the <code>insert_into_members.py</code> script to insert member information into the <code>Members</code> table. Ensure the connection details are correct.</p>
<p>To run:</p>
<pre>
<code>
python insert_into_members.py
</code>
</pre>

<h4>Insert ECG Data</h4>
<p>Use the <code>insert_into_ECG.py</code> script to insert ECG data into the <code>ECG</code> table. Ensure the <code>final_preprocessed_ecg.csv</code> file is available.</p>
<p>To run:</p>
<pre>
<code>
python insert_into_ECG.py
</code>
</pre>

<h4>Insert EEG Data</h4>
<p>Use the <code>insert_into_EEG.py</code> script to insert EEG data into the respective EEG tables. Ensure the <code>preprocessed_EEG_data.csv</code> file is available.</p>
<p>To run:</p>
<pre>
<code>
python insert_into_EEG.py
</code>
</pre>

<h4>Insert EEG Ratio Data</h4>
<p>Use the <code>insert_into_ratio_EEG.py</code> script to insert EEG ratio data. Ensure the <code>preprocessed_ratio_alpha_beta_power.csv</code> file is available.</p>
<p>To run:</p>
<pre>
<code>
python insert_into_ratio_EEG.py
</code>
</pre>

<h3>Step 4: Verify Data Insertion</h3>
<p>After running the Python scripts, verify that the data has been inserted correctly by querying the tables. For example, to check data in the <code>Members</code> table:</p>
<pre>
<code>
SELECT * FROM Members;
</code>
</pre>

<p>Repeat for other tables like <code>ECG</code>, <code>EEG_Alpha</code>, <code>EEG_Ratio_Alpha</code>, etc.</p>

<h2>Notes</h2>
<ul>
    <li>The Python scripts use <code>pyodbc</code> for database connections. Ensure that the correct SQL Server ODBC Driver is installed on your machine.</li>
    <li>Make sure the paths to the CSV files (for ECG, EEG, and Ratio data) are configured correctly in the Python scripts.</li>
    <li>The project supports both Windows Authentication and SQL Server Authentication. Ensure the correct method is being used in the Python script connection strings.</li>
</ul>

<h2>Troubleshooting</h2>
<p>If you encounter errors like:</p>
<pre>
<code>
pyodbc.ProgrammingError: ('42S02', "[42S02] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]Invalid object name 'Members'.")
</code>
</pre>
<p>This indicates that the <code>Members</code> table may not exist or the name is incorrect. Double-check the stored procedures and table names to resolve the issue.</p>

</body>
</html>
