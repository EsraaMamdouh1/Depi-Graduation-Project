USE stressFeatures
GO

IF OBJECT_ID ( 'create_tables_storedProcedure', 'P' ) IS NOT NULL
    DROP PROCEDURE create_tables_storedProcedure;
GO

CREATE PROCEDURE create_tables_storedProcedure
AS
BEGIN

IF NOT EXISTS(SELECT * FROM sys.schemas WHERE name = 'EO')
    BEGIN
      EXEC('CREATE SCHEMA [EO]');
    END

IF NOT EXISTS(SELECT * FROM sys.schemas WHERE name = 'AC1')
    BEGIN
      EXEC('CREATE SCHEMA [AC1]');
    END

IF NOT EXISTS(SELECT * FROM sys.schemas WHERE name = 'AC2')
    BEGIN
      EXEC('CREATE SCHEMA [AC2]');
    END   

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Members' and xtype='U')
BEGIN
    CREATE TABLE dbo.Members (
    SubjectNO INT PRIMARY KEY,
    Gender VARCHAR(9) NOT NULL,
    )
END 

END