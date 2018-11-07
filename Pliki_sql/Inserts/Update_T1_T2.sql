UPDATE Osoby SET Nazwisko = Kowalski, Numer = 123456789 WHERE Id = 4;
UPDATE Osoby SET Nazwisko = Nowak WHERE Id = 45; 
UPDATE Osoby SET Nazwisko = Hadryś WHERE Id = 58; 
UPDATE Osoby SET Nazwisko = Strzeszewski, Numer = 987654321 WHERE Id = 32;

UPDATE Funkcjonariusz SET Stopien=Młodszy Aspirant WHERE Id = 57;
UPDATE Funkcjonariusz SET Stopien=Nadkomisarz, Miejsce_przydziału=2 WHERE Id = 98;  
UPDATE Funkcjonariusz SET Stopien=Starszy Posterunkowy, Miejsce_przydziału=3 WHERE Id = 2;  
UPDATE Funkcjonariusz SET Stopien=Generalny Inspektor, Miejsce_przydziału=45 WHERE Id = 0;

UPDATE Wystawianie_mandatow SET Powod=Przekroczenie prędkości WHERE Id = 444;    
UPDATE Wystawianie_mandatow SET Powod=Hałas w strefie ciszy WHERE Id = 470;  
UPDATE Wystawianie_mandatow SET Powod=Nieprawidłowe zaopatrzenie rower w światła WHERE Id = 400;  
UPDATE Wystawianie_mandatow SET Powod=Niszczenie mienia publicznego WHERE Id = 401;  
UPDATE Wystawianie_mandatow SET Powod=Niszczenie mienia publicznego WHERE Id = 409;  

UPDATE Przebywanie_w_areszcie SET Powod=Agresja wobec policjanta, Czas=2017-09-06 21:14:11 WHERE Id = 545;
UPDATE Przebywanie_w_areszcie SET Czas=2017-09-06 21:01:01 WHERE Id = 644;