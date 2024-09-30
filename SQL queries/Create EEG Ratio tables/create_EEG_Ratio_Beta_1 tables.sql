use stressFeatures
GO

IF OBJECT_ID ( 'create_EEG_Ratio_Beta_1_tables_storedProcedure', 'P' ) IS NOT NULL
    DROP PROCEDURE create_EEG_Ratio_Beta_1_tables_storedProcedure;
GO

CREATE PROCEDURE create_EEG_Ratio_Beta_1_tables_storedProcedure
AS
BEGIN

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'EO' 
and TABLE_NAME = 'EEG_Ratio_Beta_1(Males)')
BEGIN
    CREATE TABLE EO.[EEG_Ratio_Beta_1(Males)] (
    SubjectNO INT PRIMARY KEY,
    "Fp1 - Fp2" FLOAT,
    "F3 - F4" FLOAT,
    "T3 - T4" FLOAT,
    "P3 - P4" FLOAT,

    FOREIGN KEY (SubjectNO) REFERENCES Members(SubjectNO)
    )
END

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'EO' 
and TABLE_NAME = 'EEG_Ratio_Beta_1(Females)')
BEGIN
    SELECT *
    INTO EO.[EEG_Ratio_Beta_1(Females)]
    FROM EO.[EEG_Ratio_Beta_1(Males)]
    WHERE 1 = 0;
END 

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'AC1' 
and TABLE_NAME = 'EEG_Ratio_Beta_1(Males)')
BEGIN
    SELECT *
    INTO AC1.[EEG_Ratio_Beta_1(Males)]
    FROM EO.[EEG_Ratio_Beta_1(Males)]
    WHERE 1 = 0;
END 

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'AC1' 
and TABLE_NAME = 'EEG_Ratio_Beta_1(Females)')
BEGIN
    SELECT *
    INTO AC1.[EEG_Ratio_Beta_1(Females)]
    FROM EO.[EEG_Ratio_Beta_1(Males)]
    WHERE 1 = 0;
END

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'AC2' 
and TABLE_NAME = 'EEG_Ratio_Beta_1(Males)')
BEGIN
    SELECT *
    INTO AC2.[EEG_Ratio_Beta_1(Males)]
    FROM EO.[EEG_Ratio_Beta_1(Males)]
    WHERE 1 = 0;
END 

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'AC2' 
and TABLE_NAME = 'EEG_Ratio_Beta_1(Females)')
BEGIN
    SELECT *
    INTO AC2.[EEG_Ratio_Beta_1(Females)]
    FROM EO.[EEG_Ratio_Beta_1(Males)]
    WHERE 1 = 0;
END
END