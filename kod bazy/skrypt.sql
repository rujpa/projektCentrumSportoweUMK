#Utworzenie bazy danych
CREATE DATABASE CentrumSportowe;
USE DATABASE CentrumSportowe;
#Stworzenie tabel
CREATE TABLE Klienci ( ID_klient INT PRIMARY KEY, Imie VARCHAR(255) NOT NULL, Nazwisko VARCHAR(255) NOT NULL, Nr_telefonu INT NOT NULL, Znizka FLOAT(3) NOT NULL, Data_wygasniecia DATE, Typ_karnetu INT);
CREATE TABLE Trenerzy ( ID_trener INT PRIMARY KEY, Imie VARCHAR(255) NOT NULL, Nazwisko VARCHAR(255) NOT NULL, Nr_telefonu INT NOT NULL);
CREATE TABLE Sale ( ID_sali INT PRIMARY KEY, Nazwa_sali VARCHAR(255) NOT NULL, Data_maintenance DATE NOT NULL, Max_osob INT NOT NULL);
CREATE TABLE Karnety (ID_karnet INT PRIMARY KEY, Nazwa_karnetu VARCHAR(255) NOT NULL, Silownia VARCHAR(1), Basen VARCHAR(1), Zajecia VARCHAR(1), Sauna VARCHAR(1), Cena_msc INT NOT NULL);
CREATE TABLE Zajecia ( ID_zajec INT PRIMARY KEY, Nazwa_zajec VARCHAR(255) NOT NULL, Max_miejsc INT NOT NULL, Dzien_tygodnia VARCHAR(32) NOT NULL, Godzina TIME NOT NULL, ID_trener INT NOT NULL, ID_sali INT NOT NULL);
CREATE TABLE Zapisy_zajecia ( ID_zajec INT NOT NULL, ID_klient INT NOT NULL);
# Podłączenie tabel
ALTER TABLE `Klienci` ADD CONSTRAINT `FK_typ_karnetu` FOREIGN KEY (`Typ_karnetu`) REFERENCES `Karnety` (`ID_karnet`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `Zajecia` ADD CONSTRAINT `FK_id_trener` FOREIGN KEY (`ID_trener`) REFERENCES `Trenerzy` (`ID_trener`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `Zajecia` ADD CONSTRAINT `FK_id_sali` FOREIGN KEY (`ID_sali`) REFERENCES `Sale` (`ID_sali`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `Zapisy_zajecia` ADD CONSTRAINT `FK_zapis_zajecia` FOREIGN KEY (`ID_zajec`) REFERENCES `Zajecia` (`ID_zajec`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `Zapisy_zajecia` ADD CONSTRAINT `FK_zapis_klient` FOREIGN KEY (`ID_klient`) REFERENCES `Klienci` (`ID_klient`) ON DELETE CASCADE ON UPDATE CASCADE;
