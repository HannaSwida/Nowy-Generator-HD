use Policja
GO

BULK INSERT dbo.Adresy FROM 'C:\Users\Felo\Desktop\TMP_HD\Nowy-Generator-HD\t1\Adresy.bulk' WITH (FIELDTERMINATOR='|',ROWTERMINATOR = '\n')
BULK INSERT dbo.Osoby FROM 'C:\Users\Felo\Desktop\TMP_HD\Nowy-Generator-HD\t1\Osoby.bulk' WITH (FIELDTERMINATOR='|',ROWTERMINATOR = '\n')
BULK INSERT dbo.Funkcjonariusz FROM 'C:\Users\Felo\Desktop\TMP_HD\Nowy-Generator-HD\t1\Funkcjonariusz.bulk' WITH (FIELDTERMINATOR='|',ROWTERMINATOR = '\n')
BULK INSERT dbo.Komisariat FROM 'C:\Users\Felo\Desktop\TMP_HD\Nowy-Generator-HD\t1\Komisariat.bulk' WITH (FIELDTERMINATOR='|',ROWTERMINATOR = '\n')
BULK INSERT dbo.Wystawianie_mandatow FROM 'C:\Users\Felo\Desktop\TMP_HD\Nowy-Generator-HD\t1\WystawienieMandatu.bulk' WITH (FIELDTERMINATOR='|',ROWTERMINATOR = '\n')
BULK INSERT dbo.Przebywanie_w_areszcie FROM 'C:\Users\Felo\Desktop\TMP_HD\Nowy-Generator-HD\t1\Przebywanie_w_areszcie.bulk' WITH (FIELDTERMINATOR='|',ROWTERMINATOR = '\n')
