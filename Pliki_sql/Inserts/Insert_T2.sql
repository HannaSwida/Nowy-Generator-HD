use Policja
GO

BULK INSERT dbo.Adresy FROM 'C:\Users\Felo\Desktop\TMP_HD\Nowy-Generator-HD\t2\Adresy.bulk' WITH (FIELDTERMINATOR='|',ROWTERMINATOR = '\n')
BULK INSERT dbo.Osoby FROM 'C:\Users\Felo\Desktop\TMP_HD\Nowy-Generator-HD\t2\Osoby.bulk' WITH (FIELDTERMINATOR='|',ROWTERMINATOR = '\n')
BULK INSERT dbo.Funkcjonariusz FROM 'C:\Users\Felo\Desktop\TMP_HD\Nowy-Generator-HD\t2\Funkcjonariusz.bulk' WITH (FIELDTERMINATOR='|',ROWTERMINATOR = '\n')
BULK INSERT dbo.Komisariat FROM 'C:\Users\Felo\Desktop\TMP_HD\Nowy-Generator-HD\t2\Komisariat.bulk' WITH (FIELDTERMINATOR='|',ROWTERMINATOR = '\n')
BULK INSERT dbo.Wystawianie_mandatow FROM 'C:\Users\Felo\Desktop\TMP_HD\Nowy-Generator-HD\t2\WystawienieMandatu.bulk' WITH (FIELDTERMINATOR='|',ROWTERMINATOR = '\n')
BULK INSERT dbo.Przebywanie_w_areszcie FROM 'C:\Users\Felo\Desktop\TMP_HD\Nowy-Generator-HD\t2\PrzebywanieWAreszcie.bulk' WITH (FIELDTERMINATOR='|',ROWTERMINATOR = '\n')
