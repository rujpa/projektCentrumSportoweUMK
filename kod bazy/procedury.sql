DELIMITER //

CREATE PROCEDURE usunNieaktywnych()
BEGIN
	DELETE FROM Klienci WHERE Data_wygasniecia < DATE_SUB(NOW(), INTERVAL 2 YEAR);
END //

CREATE PROCEDURE sprawdzMiejsca()
BEGIN
	SELECT Nazwa_zajec, (Max_miejsc-COUNT(Zapisy_zajecia.ID_zajec)) as Wolne_miejsca
	FROM Zajecia 
	LEFT JOIN Zapisy_zajecia USING(ID_zajec)
	GROUP BY Zajecia.ID_zajec;
END //
DELIMITER ;

CREATE VIEW Widok_rozpiska_klientow AS
	SELECT ID_Klient, Imie, Nazwisko, Silownia, Basen, Zajecia, Sauna, (IF(Data_wygasniecia < Now(), "Nieaktywny", "Aktywny")) as Czy_aktywny
	FROM Klienci
	JOIN Karnety ON Klienci.Typ_karnetu = Karnety.ID_karnet
	ORDER BY ID_Klient;
