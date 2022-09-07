#Wymagane biblioteki sys, PyQt5, mysql
import sys
from PyQt5.QtWidgets import QApplication, QTableWidgetItem,QAbstractItemView
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QDate, Qt
import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import QMessageBox

#Pliki interfejsu
from bazaGUI import Ui_MainWindow
import klientForm
import zapisyGUI

class recordsForm():
    def __init__(self):
        self.extraWin = QMainWindow(flags = Qt.FramelessWindowHint)
        self.extraUi = zapisyGUI.Ui_clientWindow()
        self.extraUi.setupUi(self.extraWin)
        self.extraUi.actionClient.clicked.connect(self.getData)
        self.extraUi.closeBtn.clicked.connect(self.closeWindow)
        self.extraUi.searchBtn.clicked.connect(self.findId)
        
    def show(self):
        self.extraWin.show()

    def closeWindow(self):
        MainWindow.enableWin(main_win)
        self.extraWin.close()

    def findId(self):   #wyszukanie id klienta po imieniu i nazwisku
        id = MainWindow.getClientId(main_win,self.extraUi.nameClient.text(),self.extraUi.lastnameClient.text())
        if id is not None:
            self.extraUi.idClient.setText(str(id[0]))
        else:
            self.closeWindow()

    def getData(self):  #pobranie danych z okna
        listOfValues = []
        listOfValues.append(self.extraUi.offClient.currentIndex()+1)
        listOfValues.append(self.extraUi.idClient.text())
        if MainWindow.checkActive(main_win,listOfValues[1]) == True and MainWindow.checkSpace(main_win,self.extraUi.offClient.currentText()) == True: #sprawdzenie wymogów
            for i in range(len(listOfValues)):
                if listOfValues[i] == "":
                    QMessageBox.about(self.extraWin, "Błąd", "Dane nie zostały prawidłowo uzupełnione")
                    listOfValues = []
                    break

            if listOfValues != []:
                MainWindow.addRows(main_win,listOfValues)
        elif MainWindow.checkSpace(main_win,self.extraUi.offClient.currentText()) == False:
            QMessageBox.about(self.extraWin, "Błąd", "Brak miejsc na zajęcia")
        else:
            QMessageBox.about(self.extraWin, "Błąd", "Klient nie jest aktywny lub nie ma odpowiedniego karnetu")
        self.closeWindow()
    

class clientForm(): #okno obsługujące klienta
    def __init__(self,choice):
        self.c = choice
        self.extraWin = QMainWindow(flags = Qt.FramelessWindowHint)
        self.extraUi = klientForm.Ui_clientWindow()
        self.extraUi.setupUi(self.extraWin)
        self.extraUi.actionClient.clicked.connect(self.getData)
        self.result = []
        self.extraUi.months.valueChanged.connect(self.calculateDate)
        self.extraUi.closeBtn.clicked.connect(self.closeWindow)
        if self.c == 1:     #mod
            self.extraUi.dateToday.setReadOnly(True)
            self.extraUi.actionClient.setText("Zmodyfikuj klienta")
        else:   #add
            self.extraUi.dateToday.setDate(QDate.currentDate())
            self.extraUi.actionClient.setText("Dodaj nowego klienta")
        
    def show(self):
        self.extraWin.show()

    def closeWindow(self):
        MainWindow.enableWin(main_win)
        self.extraWin.close()

    def calculatePrice(self):   #oblicze cene karnetu (cena za msc zależna od pakietu * ilość miesięcy)
        vals = MainWindow.getPrices(main_win)
        x = 0
        if self.extraUi.offClient.currentIndex() == 1:
            x = 0.3
        m = self.extraUi.months.value()
        for z in vals[self.extraUi.typeClient.currentIndex()]:
            pass
        cost = m * (float(z)- (float(z) * x))
        self.extraUi.sumClient.setText(str(cost))

    def calculateDate(self):    #wyznacza date
        x = self.extraUi.dateToday.date().addMonths(self.extraUi.months.value())
        self.extraUi.dateClient.setText(x.toString("yyyy-MM-dd"))
        self.calculatePrice()

    def getData(self): #pobranie danych z okna oraz wybór operacji dodaj/modif
        listOfValues = []
        listOfValues.append(self.extraUi.nameClient.text())
        listOfValues.append(self.extraUi.lastnameClient.text())
        listOfValues.append(self.extraUi.phoneClient.text())
        if self.extraUi.offClient.currentIndex() == 1:
            listOfValues.append(0.3)
        else:
            listOfValues.append(0)
       
        self.calculateDate()
        listOfValues.append(self.extraUi.dateClient.text())
        listOfValues.append(self.extraUi.typeClient.currentIndex()+1)

        for i in range(len(listOfValues)):
            if listOfValues[i] == "":
                QMessageBox.about(self.extraWin, "Błąd", "Dane nie zostały prawidłowo uzupełnione")
                listOfValues = []
                break
        self.closeWindow()

        if listOfValues != []:
            if self.c == 0:
                MainWindow.addRows(main_win,listOfValues)
            elif self.c == 1:
                MainWindow.modRows(main_win,listOfValues)

    def setData(self):  #pobiera dane do okna dla modifikacji
    
        vals = MainWindow.getRowValues(main_win)
        
        self.extraUi.nameClient.setText(vals[1])
        self.extraUi.lastnameClient.setText(vals[2])
        self.extraUi.phoneClient.setText(vals[3])

        if vals[4] == 0.3:
            self.extraUi.offClient.currentIndex() == 1
        else:
            self.extraUi.offClient.currentIndex() == 0
            self.extraUi.dateToday.setDate(QDate.fromString(vals[5], "yyyy-MM-dd"))
            self.extraUi.typeClient.setCurrentText(vals[6])

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.p1)

        #Przyciski
        self.ui.loginBtn.clicked.connect(self.login)
        self.ui.logoutBtn.clicked.connect(self.logout)
        self.ui.addRowsBtn.clicked.connect(self.addButton)
        self.ui.deleteRowsBtn.clicked.connect(self.deleteRows)
        self.ui.clientViewBtn.clicked.connect(self.showClientView)
        self.ui.deleteProcBtn.clicked.connect(self.showDeleteProc)
        self.ui.freeSlotsProcBtn.clicked.connect(self.showFreeSlotsProc)
        self.ui.modBtn.clicked.connect(self.modButton)

        self.ui.tableList.currentTextChanged.connect(self.showTable)
        self.ui.toolBox.setCurrentIndex(0)
        
        self.addClientForm = clientForm(0) #okno klienta dla dodawania
        self.modClientForm = clientForm(1) #okno klienta dla modyfikowania
        self.addRecordForm = recordsForm() #okno zapisów dla dodawania

        #Stworzenie listy kolumn dla odpowiednich tabel
        self.columnListKarnety = ["ID_karnet","Nazwa_karnetu","Silownia","Basen","Zajecia","Sauna","Cena_msc"]
        self.columnListKlienci = ["ID_klient","Imie","Nazwisko","Nr_telefonu","Znizka","Data_wygasniecia","Typ_karnetu"]
        self.columnListSale = ["ID_sali","Nazwa_sali","Data_maintenance","Max_osob"]
        self.columnListTrenerzy = ["ID_trener","Imie","Nazwisko","Nr_telefonu"]
        self.columnListZajecia = ["ID_zajec", "Nazwa_zajec", "Max_miejsc","Dzien_tygodnia","Godzina","Trener","Sala"]
        self.columnListZapisy = ["Zajecia","Klient"]
        self.columnListWidok = ["ID_klient","Imie","Nazwisko","Silownia","Basen","Zajecia","Sauna","Czy_aktywny"]
        
    def show(self):
        self.main_win.show()




#-----------------------------Logowanie-------------------------#

    def logout(self):   #bezpieczne wyjście z aplikacji
        if self.connection:
                self.connection.close()
        sys.exit()

    def connect(self):  #funkcja łącząca z serwerem
            try:
                self.connection = mysql.connector.connect(host = self.host, user = self.user, password = self.password, database = self.database)
            except Error as e:
                QMessageBox.about(self.main_win, "Błąd", "Kod błędu: " + str(e))
                return False      
            else:
                return True

    def login(self):
        
        if(self.ui.tableList.count != 0):
            self.ui.tableList.clear()

            self.user = self.ui.username.text()
            self.password = self.ui.database.text()
            self.database = self.ui.password.text()
            self.host= self.ui.address.text()
            
            if self.ui.database.text() == "test": #testowe dane logowania
                self.host = "192.168.56.101"
                self.user = "pracownik"
                self.password = "pass"
                self.database = "CentrumSportowe"
        
            if self.connect() == True:
                db_Info = self.connection.get_server_info()
                self.ui.recentHistory.append("====>Połączono do serwera MySQL wersji: "  + db_Info)

                mycursor = self.connection.cursor()
                query = "SELECT table_name FROM information_schema.tables WHERE table_schema = '" + self.database + "' AND table_name NOT LIKE 'Widok%' ;"
                mycursor.execute(query) #pobranie nazw tabel

                for tables in mycursor.fetchall():
                    self.ui.tableList.addItem(tables[0])    #wyświetlenie nazw tabel w gui

                self.ui.usernameLabel.setText(self.user)
                self.ui.stackedWidget.setCurrentWidget(self.ui.p2)

                mycursor.callproc("usunZapisy") #automatyczne usuwanie nieaktywnych klientów z zapisów
                self.connection.commit()
                mycursor.close()

            else:
                QMessageBox.about(self.main_win, "Błąd", "Nie udało się zalogować do bazy danych")

#-----------------------------Inne funkcje-------------------------#

    def getPrices(self):    #wprowadza ceny do listy do późniejszych operacji
        mycursor = self.connection.cursor()
        query = "SELECT Cena_msc FROM Karnety ORDER BY Cena_msc;"
        mycursor.execute(query)
        result = []
        for i in mycursor.fetchall():
            result.append(i)
        return result

    def getRowValues(self): ##wprowadza dane do listy dla okna edycji klienta
        vals = []
        for i in range(self.ui.tableWidget.columnCount()):
            vals.append(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),i).text())
        return vals

    def disableAll(self): #wyłącza możliwość edycji
            self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.ui.addRowsBtn.setDisabled(True)
            self.ui.deleteRowsBtn.setDisabled(True)
            self.ui.modBtn.setDisabled(True)

    def enableAll(self): #wyłącza możliwość edycji
            self.ui.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
            self.ui.tableWidget.setEditTriggers(QAbstractItemView.EditKeyPressed)
            self.ui.tableWidget.setEditTriggers(QAbstractItemView.AnyKeyPressed)
            self.ui.addRowsBtn.setDisabled(False)
            self.ui.deleteRowsBtn.setDisabled(False)
            self.ui.modBtn.setDisabled(False)

    def enableWin(self): #wyłącza możliwość klikania na głównym oknie
        self.ui.centralwidget.setDisabled(False)

    def checkActive(self,id):   #sprawdzenie czy klient o id jest aktywny i ma większy pakiet niż miedziany
        try:
            mycursor = self.connection.cursor()
            query = "SELECT Czy_aktywny FROM Widok_rozpiska_klientow WHERE ID_klient = %s AND Zajecia = 'T';"
            mycursor.execute(query,(id,))
            for result in mycursor.fetchall():
                if str(result[0]) == "Aktywny":
                    return True
            return False
        except Error as e:
            QMessageBox.about(self.main_win, "Błąd", "Kod błędu: " + str(e))

    def checkSpace(self,id):    #sprawdza wynik procedury dla nazwy zajęć (id)
        try:
            mycursor = self.connection.cursor()
            mycursor.callproc("sprawdzMiejsca")
            for result in mycursor.stored_results():
                pass
            for i in result.fetchall():
                if i[0] == id:
                    if i[1] > 0:
                        return True

            return False
        except Error as e:
            QMessageBox.about(self.main_win, "Błąd", "Kod błędu: " + str(e))

#---------------------------Ładowanie danych----------------------------#
            
    
    def showTable(self):    #pobranie danych z tabeli z serwera
        self.loadTableFrame(self.ui.tableList.currentText())
        mycursor = self.connection.cursor()
      
        tableName =self.ui.tableList.currentText()
        query = ""

        if tableName == "Zajecia":
            query = "SELECT ID_zajec, Nazwa_zajec, Max_miejsc, Dzien_tygodnia, Godzina, CONCAT(Imie,' ', Nazwisko) as Trener, Nazwa_sali as Sala FROM Zajecia JOIN Trenerzy USING(ID_trener) JOIN Sale USING(ID_sali) ORDER BY ID_zajec;"
            mycursor.execute(query)
            self.disableAll()

        elif tableName == "Klienci":
            query = "SELECT ID_klient, Imie, Nazwisko, Nr_telefonu, Znizka, Data_wygasniecia, Nazwa_karnetu as Karnet FROM Klienci JOIN Karnety ON Klienci.Typ_karnetu = Karnety.ID_karnet ORDER BY ID_klient;"
            mycursor.execute(query)
            self.enableAll()

        elif tableName == "Zapisy_zajecia":
            query = "SELECT Nazwa_zajec, CONCAT(ID_klient, ' ' ,Imie, ' ', Nazwisko) as Klient FROM Zapisy_zajecia JOIN Klienci USING(ID_klient) JOIN Zajecia USING(ID_zajec) ORDER BY Nazwa_zajec;"
            mycursor.execute(query)
            self.enableAll()
            self.ui.modBtn.setDisabled(True)
        else:
            query = """SELECT * FROM {};""".format(tableName)
            mycursor.execute(query)
            self.disableAll()

        self.loadData(mycursor)

    def loadTableFrame(self, tableName):   #pobiera strukture aktywnej tabeli
        self.ui.tableWidget.clear()
        listOfNames = []
                                    #Wybór listy kolumn odpowiedniej tabeli
        if tableName == "Klienci":
            listOfNames = self.columnListKlienci
        elif tableName == "Karnety":
            listOfNames = self.columnListKarnety
        elif tableName == "Trenerzy":
            listOfNames = self.columnListTrenerzy
        elif tableName == "Zapisy_zajecia":
            listOfNames = self.columnListZapisy
        elif tableName == "Sale":
            listOfNames = self.columnListSale
        elif tableName == "Widok_rozpiska_klientow":
            listOfNames = self.columnListWidok
        elif tableName == "Zajecia":
            listOfNames = self.columnListZajecia
        
        #przygotowanie tabeli w programie
        self.ui.tableWidget.setColumnCount(len(listOfNames))
        self.ui.tableWidget.setHorizontalHeaderLabels(listOfNames)

    def loadData(self,mycursor): #wczytuje dane do struktury aktywnej tabeli

        self.ui.tableWidget.setRowCount(0)

        for rowNumber, row in enumerate(mycursor.fetchall()):   #wstawienie danych do tabeli
            self.ui.tableWidget.insertRow(rowNumber)
            for columnNumber, data in enumerate(row):
                self.ui.tableWidget.setItem(rowNumber, columnNumber, QTableWidgetItem(str(data)))
    

#-----------------------------Operacje na rekordach-------------------------#
    def modButton(self): #obsługa przycisku modyfikacji
        if self.ui.tableWidget.currentItem() is not None:
            if self.ui.tableList.currentText() == "Klienci":
                self.modClientForm.choice = 1
                self.modClientForm.setData()
                self.modClientForm.show()
                self.ui.centralwidget.setDisabled(True)

    def modRows(self,vals): #modyfikacja klienta
        try:
            query = ""
            data = ()
            mycursor = self.connection.cursor()
            if self.ui.tableList.currentText() == "Klienci":
                id = self.ui.tableWidget.item(self.ui.tableWidget.currentItem().row(),0).text()
                query = "UPDATE Klienci SET  Imie = %s, Nazwisko = %s, Nr_telefonu = %s,Znizka = %s, Data_wygasniecia = %s, Typ_karnetu = %s WHERE ID_klient = %s;"
                data = (vals[0],vals[1],vals[2],vals[3],vals[4],vals[5],id)

            mycursor.execute(query,data)
            self.connection.commit()
            self.ui.recentHistory.append("+Zmodifikowano rekord z tabeli " + self.ui.tableList.currentText()) 
            mycursor.close()
            self.showTable()

        except Error as e:
            QMessageBox.about(self.main_win, "Błąd", "Kod błędu: " + str(e))


    def addButton(self): #obsługa przycisku dodawania
        if self.ui.tableList.currentText() == "Klienci":
            self.addClientForm.choice = 0
            self.addClientForm.show()
            self.ui.centralwidget.setDisabled(True)
        if self.ui.tableList.currentText() == "Zapisy_zajecia":
            self.addRecordForm.show()
            self.ui.centralwidget.setDisabled(True)

    def addRows(self, listV): #dodanie danych z listy danych
        if listV is not None:
            try:
                query = ""
                data = ()
                mycursor = self.connection.cursor()
                if self.ui.tableList.currentText() == "Klienci":
                    id = self.ui.tableWidget.item(self.ui.tableWidget.rowCount()-1,0)
                    id = int(id.text()) +1
                    query = """INSERT INTO Klienci VALUES(%s, %s, %s, %s, %s, %s, %s);"""
                    data = (id,listV[0],listV[1],listV[2],listV[3],listV[4],listV[5])
                if self.ui.tableList.currentText() == "Zapisy_zajecia":
                    query = """INSERT INTO Zapisy_zajecia VALUES(%s, %s);"""
                    data = (listV[0],listV[1])
    

                mycursor.execute(query,data)
                self.connection.commit()
                self.ui.recentHistory.append("+Dodano rekord do tabeli " + self.ui.tableList.currentText()) 
                mycursor.close()
                self.showTable()
            except Error as e:
                QMessageBox.about(self.main_win, "Błąd", "Kod błędu: " + str(e))

        
    def deleteRows(self): 
        try:
            if self.ui.tableWidget.selectedItems() != []: #uniemożliwienie usunięcia niepoprawnego wersu
                idx = self.ui.tableWidget.currentRow()
                mycursor = self.connection.cursor()
                if self.ui.tableList.currentText() == "Zapisy_zajecia":
                    val = self.ui.tableWidget.item(idx,0).text()
                    idZ = self.getClassesId(val)
                    val = self.ui.tableWidget.item(idx,1).text()
                    idK = val.split(" ",1)  #wyznacza numer z ciągu 
                    query = "DELETE FROM Zapisy_zajecia WHERE ID_klient = %s AND ID_zajec = %s;"
                    mycursor.execute(query,(idK[0],idZ[0]))
                else:
                    val = self.ui.tableWidget.item(idx,0).text()
                    query = "DELETE FROM Klienci WHERE ID_klient = %s;"
                    mycursor.execute(query,(val,))

                self.connection.commit()
                self.ui.recentHistory.append("-Usunięto rekord z tabeli " + self.ui.tableList.currentText()) 
                self.showTable()
                mycursor.close()

        except Error as e:
            QMessageBox.about(self.main_win, "Błąd", "Kod błędu: " + str(e))

#-----------------------------Procedury i widoki-------------------------#
    def getClassesId(self,name): #zwraca id zajęć
        mycursor = self.connection.cursor()
        mycursor.callproc("znajdzZajecia",[name,])
        for result in mycursor.stored_results():
            pass
        mycursor.close()
        final = result.fetchall()
        return final[0]

    def getClientId(self,first,last):   #funkcja wyszukuje id klienta i sprawdza czy jest więcej osób z takim imieniem i nazwiskiem
        mycursor = self.connection.cursor()
        mycursor.callproc("znajdzKlient",[first,last])
        for result in mycursor.stored_results():
            pass
        final = result.fetchall()
        mycursor.close()

        if len(final) != 0:
            if len(final) > 1:
                QMessageBox.about(self.main_win, "Uwaga", "Istnieje więcej niż jeden klient o takim imieniu i nazwisku. Wpisz ręcznie identyfikator")
                return None
            return final[0]
        QMessageBox.about(self.main_win, "Błąd", "Nie istnieje taki klient")
        return None

    def showClientView(self):
        try:
            mycursor = self.connection.cursor()
            self.loadTableFrame('Widok_rozpiska_klientow')
            mycursor.execute("SELECT * FROM Widok_rozpiska_klientow;")
            self.disableAll()
            self.loadData(mycursor)
            mycursor.close()
            self.ui.recentHistory.append("^^Wywołano widok Rozpiska_Klientów") 
        except Error as e:
            QMessageBox.about(self.main_win, "Błąd", "Nie udało się wywołać widoku \nKod błędu: " + str(e))


    def showDeleteProc(self):
        try:
            mycursor = self.connection.cursor()
            mycursor.callproc("usunNieaktywnych")
            QMessageBox.about(self.main_win, "Procedura powiodła się", "Usunięto wszystkie profile klientów nieaktywnych od co najmniej 2 lat" )
            self.connection.commit()
            self.showTable()  #odświeżenie danych
            self.ui.recentHistory.append("@Wywołano procedure 'Usuń nieaktywnych'") 
        except Error as e:
            QMessageBox.about(self.main_win, "Błąd", "Nie udało się wywołać procedury \nKod błędu: " + str(e))

     

    def showFreeSlotsProc(self): #Nie działa
        try:
            self.disableAll()

            listOfNames = ['Zajęcia','Ilość wolnych miejsc']    #stworzenie frame'a dla danych
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setColumnCount(len(listOfNames))
            self.ui.tableWidget.setHorizontalHeaderLabels(listOfNames)

            mycursor = self.connection.cursor()
            mycursor.callproc("sprawdzMiejsca")

            for result in mycursor.stored_results():    #wypisanie danych
                self.loadData(result)
            mycursor.close()
            self.ui.recentHistory.append("@Wywołano procedure 'Wolne miejsca'") 
        except Error as e:
            QMessageBox.about(self.main_win, "Błąd", "Nie udało się wywołać procedury \nKod błędu: " + str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
