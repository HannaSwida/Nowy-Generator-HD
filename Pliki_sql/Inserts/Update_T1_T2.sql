UPDATE Osoby SET Nazwisko = 'Kowalski', Numer_telefonu =123456789 WHERE Id = 4;
UPDATE Osoby SET Nazwisko = 'Nowak' WHERE Id = 45; 
UPDATE Osoby SET Nazwisko = 'Hadryś' WHERE Id = 58; 
UPDATE Osoby SET Nazwisko = 'Strzeszewski', Numer_telefonu = 987654321 WHERE Id = 32;

UPDATE Funkcjonariusz SET Stopien='Młodszy Aspirant' WHERE Id = 57;
UPDATE Funkcjonariusz SET Stopien='Nadkomisarz', Miejsce_przydzialu=2 WHERE Id = 98;  
UPDATE Funkcjonariusz SET Stopien='Starszy Posterunkowy', Miejsce_przydzialu=3 WHERE Id = 2;  
UPDATE Funkcjonariusz SET Stopien='Generalny Inspektor', Miejsce_przydzialu=45 WHERE Id = 78;

UPDATE Wystawianie_mandatow SET Powod='Przekroczenie prędkości' WHERE Id = 15;    
UPDATE Wystawianie_mandatow SET Powod='Hałas w strefie ciszy' WHERE Id = 47;  
UPDATE Wystawianie_mandatow SET Powod='Nieprawidłowe zaopatrzenie rower w światła' WHERE Id = 54;  
UPDATE Wystawianie_mandatow SET Powod='Niszczenie mienia publicznego' WHERE Id = 80;  
UPDATE Wystawianie_mandatow SET Powod='Niszczenie mienia publicznego' WHERE Id = 23;  

UPDATE Przebywanie_w_areszcie SET Powod='Agresja wobec policjanta', Czas=5 WHERE Id = 51;
UPDATE Przebywanie_w_areszcie SET Czas=15 WHERE Id = 45;