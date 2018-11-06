use Policja
GO

BULK INSERT dbo.Adresy FROM 'C:\Users\Felo\Desktop\TMP_HD\Nowy-Generator-HD\Pliki_sql\Inserts\bulktest.bulk' WITH (KEEPIDENTITY,FIELDTERMINATOR='|',ROWTERMINATOR = '\n')