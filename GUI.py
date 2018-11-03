#NOTE: IF THERE IS ANY GRAMMAR ERROR IT IS BECAUSE THE COMMENTS ARE WRITEN TOO FAAAAAAST, SO SHOULD YOU FIND ANY, I WILL THANK YOU FOR CORRECTING IT :D
#
#this program has the simple task of controlling the adicional option on the robot such as safety mode, if the lights go on and off considering the amount of light in the
#environment, show the distance of the closest object at the front part, the amount of luminosity, if it is moving or not and the brgihtness of the lights
#the part that says test is just a small idea (not sure if it is going to stay). It is like a small prompt to control addicional options
#there is still the third part which will only be implemented if the is enought time. It's a small animation tha will demonstrate the position of the car

#the message will be sent in the form of a string which will have this structure
# 1.security mode
# 2.Automatic light mode
# 3.light scale
#
#final format
# "1,2,3"

#it will also receive a string from the arduino, which will have:
# 1. the distance of the closest object
# 2. Luminosity
# 3. the info that will transmit if it is moving or not
#
#final format
# "1,2,3"

from tkinter import *
import psycopg2


def dummyFunctionWithTerm(termo):
    #FIX ME
    conn = psycopg2.connect('dbname=miniproj')
    cur = conn.cursor()


    cur.execute('SELECT * FROM armario2 WHERE name LIKE lower('%TermoDeProcura%')')

    results = cur.fetchall()

    cur.close()
    
    '''Devolver na forma de uma lista os seguintes elementos:
            ->Nome
            ->Prateleira nº
            ->Quantia'''

    return results

def dummyFunctionWithShelf(prateleira):
    #FIX ME
    return [["Reles", "40", "42"],["LDR","18","10"], ["LED Branco","31","40"]]

def dummyFunction2(termo, valor):
    #FIX ME
    pass


resultados = []

def search(searchTerm, prateleira,firstRow, bgColor):
    #print(searchTerm)
    #print(prateleira)
    print("\a")

    global resultados

    resultsName = []
    currentShell = firstRow
    ordem = 0
    for result in resultados:
        result.destroy()


    if prateleira == 0:
        resultsName = dummyFunctionWithTerm(searchTerm) #FIX ME
    elif prateleira == 1:
        try:
            numShelf = int(searchTerm)
        except ValueError:
            return
        if numShelf < 0:
            return

        resultsName = dummyFunctionWithShelf(numShelf) #FIX ME

    shellEntry.delete(0, 'end')
    resultados = []
    for result in resultsName:
        resultados = resultados + [searchResult(result[0],result[1],result[2],currentShell,0,bgColor, ordem)]
        ordem += 1
        currentShell += len(resultados[0])



mainWindow= Tk()

bgColor = 'snow'
lengthWindowInCell = 2
firstRowForSearch = 5



class searchResult:
    def __init__(self, resultado, prateleira, quantia, linha, coluna, cor, ordem):
        self.termo = resultado
        self.retirado = StringVar()
        self.ordem = ordem
        self.quantia = int(quantia)
        self.linha = linha
        self.cor = cor
        self.coluna = coluna

        self.division = Label(mainWindow, text = "==========================", background = cor)

        self.result = Label(mainWindow, text = resultado,  background = cor)
        self.prateleira = Label(mainWindow, text = ("Prateleira: " + prateleira), background = cor)
        self.quantidade = Label(mainWindow, text = "Quantia: " + quantia, background = cor)
        self.entrada = Entry(mainWindow,  textvariable=self.retirado, borderwidth = 3)
        self.retirar = Button(mainWindow, text = "Adicionar/Retirar", bg = "light grey",highlightbackground= cor, command = lambda : self.addRemove(self.retirado.get(),self.termo))


        self.division.grid(row = linha, column = coluna, sticky = W, columnspan = 2)
        self.result.grid(row = linha + 1, column = coluna, sticky = W, columnspan = 2)
        self.prateleira.grid(row = linha + 2, column = coluna, sticky = W, columnspan = 2)
        self.quantidade.grid(row = linha + 3, column = coluna, sticky = W, columnspan = 2)

        self.entrada.grid(row = linha + 4, column = coluna, sticky = W)
        self.retirar.grid(row = linha + 4, column = coluna + 1, sticky = W)

    def addRemove(self, quantia, termoDePesquisa):
        print(quantia)
        try:
            value = int(quantia)
        except ValueError:
            return

        if self.quantia + value < 0:
            return
        self.entrada.delete(0, 'end')
        dummyFunction2(self.termo, value)    #FIX ME
        self.quantia = value + self.quantia
        #print(self.quantia)
        self.quantidade.destroy()
        self.quantidade = Label(mainWindow, text = "Quantia: " + str(self.quantia), background = self.cor)
        self.quantidade.grid(row = self.linha + 3, column = self.coluna, sticky = W, columnspan = 2)

    def destroy(self):
        self.division.destroy()
        self.result.destroy()
        self.prateleira.destroy()
        self.quantidade.destroy()
        self.entrada.destroy()
        self.retirar.destroy()
        #print("Deleted")

    def __len__(self):
        return 5

#definitions of the main window

closed = False

def isClosed():
    global closed
    closed = True

mainWindow.protocol("WM_DELETE_WINDOW", isClosed)

mainWindow.geometry("365x600")
mainWindow.resizable(False, False)
mainWindow.title("Inventário Eletrónico Junitec")

img = PhotoImage(file='icon.PNM')
mainWindow.iconphoto(True, img)


mainWindow.configure(background= bgColor)

#Description for search
infoTitle  = Label(mainWindow, text = "Barra de Pesquisa", background= bgColor)
infoTitle.config(font=("Courier", 20))



inputString = StringVar()
prateleiraStatus = IntVar()



shellEntry = Entry(mainWindow,  textvariable=inputString, borderwidth = 3)

searchButton = Button(mainWindow, width = 18, text = "Procurar", bg = "light grey",highlightbackground=bgColor, command = lambda: search(inputString.get(),prateleiraStatus.get(), firstRowForSearch,bgColor))

prateleira = Checkbutton(mainWindow, text = "Pesquisar por Prateleria", variable=prateleiraStatus, bg= bgColor, borderwidth=0, highlightbackground=bgColor)

divisoria  = Label(mainWindow, text = "",width = 45,  background= "gray", highlightbackground=bgColor)

results  = Label(mainWindow, text = "Resultados: ", background= bgColor, width = 20)
results.config(font=("Courier", 15))



infoTitle.grid(row = 0, column = 0, columnspan = lengthWindowInCell, sticky = W)
shellEntry.grid(row = 1, columnspan = lengthWindowInCell,column = 0, sticky = W+E )
searchButton.grid(row = 2, column = 0, sticky = W + E)
prateleira.grid(row = 2, column = 1, sticky = W)
divisoria.grid(row = 3, column = 0, columnspan = lengthWindowInCell, sticky = W )
results.grid(row = 4, column = 0, sticky = W, columnspan = lengthWindowInCell)



#teste = searchResult("Transistor NPN","1","10",5,0,bgColor, 0)
#teste2 = searchResult("Resistência 100k-500k", "42","20",10,0,bgColor, 1)
#teste.destroy()



while not closed:
    mainWindow.update()
    mainWindow.update_idletasks()
