import os

# Variabili
stringSpacing = 16
lineLen = 76
ext = ".txt"

# Dichiarazione delle funzioni

# Crea un nuovo file
def createFile(fileName):
        file = open(fileName + ext, "w")
        file.close()

# Apre un file già esistente, non crea nuovi files
def openFile(fileName):
        fileDoExist = False
        while not fileDoExist:
                if os.path.exists(fileName + ext):
                        file = open(fileName + ext, "a+")
                        fileDoExist = True
                        print("\nFile aperto: ", file.name)
                else:
                        quitCheck(fileName)
                        choice = input("File non trovato! Crearlo(s/n)? ").lower()
                        if choice == "s":
                                createFile(fileName)
                        elif choice == "n":
                                fileName = input("Nome del file da aprire: ")
                        else:
                                quitCheck()
                                print("Risposta non esistente!")

        return file

# Legge un file aperto in precedenza
def readFile(file):
        file.seek(0)
        fileData = file.read()
        userList = fileData.split()
        print("\n")
        print("|" + "Cognome".center(stringSpacing) + " | " + "Paga oraria".center(stringSpacing) + " | " + "Ore di lavoro".center(stringSpacing) + " | " + "Prospetto paga".center(stringSpacing) + " | ")
        print("-" * lineLen)
        for i in range(len(userList)):
                user = userList[i].split(",")
                prospetto = int(user[1]) * int(user[2])
                print("|" + user[0].center(stringSpacing) + " | " + user[1].center(stringSpacing) + " | " + user[2].center(stringSpacing) + " | " + str(prospetto).center(stringSpacing) + " | ")
                print("-" * lineLen)
                i += 1
        print("\n")

# Rinomina un file esistente, non crea nuovi files
def renameFile():
        oldName = input("Nome del file da rinominare: ")
        quitCheck(oldName)
        while not os.path.exists(oldName + ext):
                oldName = input("File non trovato.\nNome del file da rinominare: ")
                quitCheck(oldName)
        newName = input("Rinomina con: ")
        quitCheck(newName)
        os.rename(oldName + ext, newName + ext)

def modifyFile(file):
        jobDone = False
        while not jobDone:
                answer = input("a) Aggiungi un lavoratore\nb) Modifica lavoratori ed orari\nx) Menù principale\nq) Esci").lower()
                if answer == "a":
                        workerName = addWorker(file)
                        modifyWorker(workerName)
                        jobDone = True
                elif answer == "b":
                        workerName = input("Nome lavoratore da modificare: ")
                        modifyWorker(workerName)
                        jobDone = True
                elif answer == "x":
                        jobDone = True
                else:
                        quitCheck()
                        print("Risposta non esistente!")

# Aggiunge un lavoratore
def addWorker(file):
        file.seek(0)
        fileData = file.read()
        jobDone = False
        workerName = input("Cognome: ").strip(" ,.")
        while not jobDone:
                if fileData.find(workerName) == -1:
                        hourPay = input("Paga oraria: ").strip(" ")
                        hourWorked = input("Ore lavorate mese corrente: ").strip(" ")
                        if fileData > 0:
                                file.write("\n")
                        file.write(workerName + "," + hourPay + "," + hourWorked)
                        jobDone = True
                else:
                        workerName = fixExistingWorker(workerName)
                        if workerName == True:
                                jobDone = True

def fixExistingWorker(workerName):
        jobDone = False
        while not jobDone:
                job = input("Lavoratore gia esistente!\na)Cambia cognome\nb)Modifica lavoratore esistente\nx) Menù principale\nq) Esci").lower()
                match job:
                        case "a":
                                workerName = input("Cognome: ").strip(" ,.")
                                return workerName
                        case "b":
                                modifyWorker(workerName)
                                jobDone = True
                                return jobDone
                        case "x":
                                jobDone = True
                                return jobDone
                        case _:
                                quitCheck()
                                print("Risposta non esistente!")

# Funzione principale per la modifica dei files
def modifyWorker(workerName):
        file = openFile()
        file.seek(0)
        fileData = file.read()
        jobDone = False
        while not jobDone:
                if fileData.find(workerName) > -1:
                        print("Lavoratore: " + workerName)
                        job = input("a) Aggiungi ore\nb) Sottrai ore\nc) Modifica ore lavorate\nd) Modifica cognome\ne) Modifica paga oraria\nf) Mostra file\nx) Menù principale\nq) Esci").lower()
                        match job:
                                case "a":
                                        break
                                case "b":
                                        break
                                case "c":
                                        break
                                case "d":
                                        break
                                case "e":
                                        break
                                case "f":
                                        break
                                case "x":
                                        break
                                case "q":
                                        break
                        jodDone = True
                else:
                        answer = input("Lavoratore non trovato. Aggiungerlo(s/n)? ").lower()
                        if answer == "s":
                                addWorker(file)
                        elif answer != "n":
                                quitCheck(answer)
                                print("Risposta non esistente!")

# Controllo della pressione del tasto 'q' per uscire dal programma
def quitCheck(answer):
        if answer.lower() == "q":
                quit()

# PROGRAM START
print("Puoi sempre scrivere 'q' per uscire dal programma")
while True:
        print("\nPROSPETTI LAVORATORI AZIENDA\n")
        answer = input("a) Mostra un file\nb) Crea nuovo file\nc) Rinomina file\nd) Modifica file\nq) Esci\n---> ").lower()

        match answer:
                case "a":
                        fileName = input("Nome del file da aprire: ")
                        file = openFile(fileName)
                        readFile(file)
                        modifyFile(file)
                        file.close()
                case "b":
                        fileName = input("Nome del file da creare: ")
                        quitCheck(fileName)
                        createFile(fileName)
                        jobDone = False
                        while not jobDone:
                                doOpenFile = input("Aprire il file appena creato(s/n)\n---> ").lower()
                                if doOpenFile == "s":
                                        file = openFile(fileName)
                                        readFile(file)
                                        modifyFile(file)
                                        jobDone = True
                                elif doOpenFile == "n":
                                        jobDone = True
                                else:
                                        quitCheck()
                                        print("Risposta non esistente!")
                case "c":
                        renameFile() #
                case "d":
                        file = openFile()
                        modifyFile(file)
                case "q": #
                        quit() 
                case _: #
                        print("Risposta non esistente!")