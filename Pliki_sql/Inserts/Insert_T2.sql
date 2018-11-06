use Policja
GO



BULK INSERT dbo.Adresy FROM 'Adresy.bulk' WITH (FIELDTERMINATOR='|',ROWTERMINATOR = '\n')
BULK INSERT dbo.Osoby FROM 'Osoby.bulk' WITH (FIELDTERMINATOR='|',ROWTERMINATOR = '\n')
BULK INSERT dbo.Funkcjonariusz FROM 'Funkcjonariusz.bulk' WITH (FIELDTERMINATOR='|',ROWTERMINATOR = '\n')
BULK INSERT dbo.Komisariat FROM 'Komisariat.bulk' WITH (FIELDTERMINATOR='|',ROWTERMINATOR = '\n')
BULK INSERT dbo.Wystawianie_mandatow FROM 'Wystawianie_mandatow.bulk' WITH (FIELDTERMINATOR='|',ROWTERMINATOR = '\n')
BULK INSERT dbo.Przebywanie_w_areszcie FROM 'Przebywanie_w_areszcie.bulk' WITH (FIELDTERMINATOR='|',ROWTERMINATOR = '\n')