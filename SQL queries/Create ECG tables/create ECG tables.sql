use stressFeatures;
GO

IF OBJECT_ID ( 'create_ecg_storedProcedure', 'P' ) IS NOT NULL
    DROP PROCEDURE create_ecg_storedProcedure;
GO

CREATE PROCEDURE create_ecg_storedProcedure
AS
BEGIN

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'EO' 
and TABLE_NAME = 'ECG(Males)')
BEGIN
    CREATE TABLE EO.[ECG(Males)] (
    SubjectNO INT PRIMARY KEY,
    "Mean HR (BPM)" FLOAT,
    "AVNN (ms)" FLOAT,
    "SDNN (ms)" FLOAT,
    "NN50 (beats)" FLOAT,
    "pNN50 (%)" FLOAT,
    "RMSSD (ms)" FLOAT,
    "LF (ms2)" FLOAT,
    "LF Norm (n.u.)" FLOAT,
    "HF (ms2)" FLOAT,
    "HF Norm (n.u.)" FLOAT,
    "LF/HF Ratio" FLOAT,

    FOREIGN KEY (SubjectNO) REFERENCES Members(SubjectNO)
    )
END

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'EO' 
and TABLE_NAME = 'ECG(Females)')
BEGIN
    SELECT *
    INTO EO.[ECG(Females)]
    FROM EO.[ECG(Males)]
    WHERE 1 = 0;
END 

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'AC1' 
and TABLE_NAME = 'ECG(Males)')
BEGIN
    SELECT *
    INTO AC1.[ECG(Males)]
    FROM EO.[ECG(Males)]
    WHERE 1 = 0;
END 

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'AC1' 
and TABLE_NAME = 'ECG(Females)')
BEGIN
    SELECT *
    INTO AC1.[ECG(Females)]
    FROM EO.[ECG(Males)]
    WHERE 1 = 0;
END

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'AC2' 
and TABLE_NAME = 'ECG(Males)')
BEGIN
    SELECT *
    INTO AC2.[ECG(Males)]
    FROM EO.[ECG(Males)]
    WHERE 1 = 0;
END 

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'AC2' 
and TABLE_NAME = 'ECG(Females)')
BEGIN
    SELECT *
    INTO AC2.[ECG(Females)]
    FROM EO.[ECG(Males)]
    WHERE 1 = 0;
END
END