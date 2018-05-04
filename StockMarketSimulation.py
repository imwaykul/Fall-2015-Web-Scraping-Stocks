

from tkinter import *
import pymysql
from tkinter import messagebox
import csv
import random
import string
import time
import datetime
import urllib.request


class IntroSQL:

    def __init__(self):
        self.LoginPage()

    def LoginPage(self):
        self.win = Tk()
        self.win.wm_title("GT Brokers Login Page")
        self.Frame1 = Frame(self.win, bg="gold")
        self.Frame1.grid(row = 0, column = 0)
        
        self.Frame2 = Frame(self.win)
        self.Frame2.grid(row = 3, column = 0)
        self.aPhoto = PhotoImage(file = "Login.gif")
        self.loginLabel = Label(self.Frame1, image = self.aPhoto)
        self.loginLabel.aPhoto = self.aPhoto
        self.loginLabel.grid(row=0,column=0,sticky=E,columnspan=2)
        self.Frame2 = Frame(self.win, bg= "gold")
        self.Frame2.grid(row=1,column=0,sticky=E)
        self.username = Label(self.Frame1, text = "Username:",bg="gold")
        self.username.grid(row=1,column=0,sticky = E,padx = 5, pady=5)
        self.password = Label(self.Frame1, text = "Password:",bg="gold")
        self.password.grid(row=2,column=0,sticky = E,padx = 5, pady =5)
        self.userEntry = Entry(self.Frame1,state = "normal",width=30)
        self.userEntry.grid(row=1,column=1,sticky = E,padx = 5, pady =5)
        self.passEntry = Entry(self.Frame1, state = "normal",width=30)
        self.passEntry.grid(row=2,column=1,sticky = E, padx = 5, pady =5)
        self.cancelButton = Button(self.Frame2, text = "Cancel", command = self.cancelMethod)
        self.cancelButton.grid(row=3,column=0)
        self.registerButton = Button(self.Frame2, text = "Register", command = self.showRegister)
        self.registerButton.grid(row=3,column=1)
        self.loginButton = Button(self.Frame2,text="Login",command=self.LoginCheck)
        self.loginButton.grid(row=3,column=2)
    def cancelMethod(self):
        self.win.withdraw()

    def showRegister(self):
        self.win.withdraw()
        self.RegisterPage()

    def RegisterPage(self):
        try:
            if self.xval == 0:
                self.registerWin2.withdraw()
                self.riddlerz()
            elif self.xval == 1:
                self.registerWin.withdraw()
                self.captcha()
        except:
            self.captcha()
            


    def riddlerz(self):
        self.registerWin2.withdraw()
        self.someList = []
        self.someAnswers = []
        self.xval = 1
        self.opening = open("riddles.csv")
        self.csvReader = csv.reader(self.opening, delimiter= ",")
        for y in self.csvReader:
            self.someList.append(y[0])
            self.someAnswers.append(y[1])
        self.registerWin = Toplevel()
        self.registerWin.wm_title("GT Brokers Register Page")
        self.FrameBack = Frame(self.registerWin, bg="gold")
        self.FrameBack.grid(row=0,column=0,rowspan=6,columnspan=2)
        self.registerpic = PhotoImage(file = "registerpic.gif")
        self.registerlabel = Label(self.FrameBack,image=self.registerpic)
        self.registerlabel.registerpic = self.registerpic
        self.registerlabel.grid(row=0,column=0,sticky=E)
        self.fullName = Label(self.FrameBack, text="Full Name:",bg="gold")
        self.fullName.grid(row=0,column=1,padx=5,pady=5,sticky=E)
        self.fullNameEntry = Entry(self.FrameBack, state = "normal",width=60)
        self.fullNameEntry.grid(row=0,column=2,padx=5,pady=5)
        self.anotherusername = Label(self.FrameBack,text="Username:",bg="gold")
        self.anotherusername.grid(row=1,column=1,padx=5,pady=5,sticky=E)
        self.anotheruserEntry = Entry(self.FrameBack, state = "normal",width=60)
        self.anotheruserEntry.grid(row=1,column=2,padx=5,pady=5)
        self.anotherpassword = Label(self.FrameBack, text = "Password:",bg="gold")
        self.anotherpassword.grid(row=2,column=1,padx=5,pady=5,sticky=E)
        self.anotherpassEntry = Entry(self.FrameBack, state = "normal",width=60)
        self.anotherpassEntry.grid(row=2,column=2,padx=5,pady=5)
        self.somepassword = Label(self.FrameBack, text = "Confirm Password:",bg="gold")
        self.somepassword.grid(row=3, column = 1, padx=5, pady =5,sticky=E)
        self.somepassEntry = Entry(self.FrameBack, state = "normal",width=60)
        self.somepassEntry.grid(row=3,column=2,padx=5,pady=5)
        self.proofHuman = Label(self.FrameBack, text= "Prove you're a Human:",bg="gold")
        self.proofHuman.grid(row=4,column=1,padx=5,pady=5,sticky=E)
        self.proofEntry = Entry(self.FrameBack, state = "normal",width=60)
        self.someNumber = random.randrange(1,len(self.someList)-1)
        self.proofEntry.insert(0,self.someList[self.someNumber])
        self.proofEntry.config(state = "readonly")
        self.proofEntry.grid(row=4,column=2,padx=5,pady=5)
        self.riddle = Label(self.FrameBack, text = "Answer my riddle to gain admission:",bg="gold")
        self.riddle.grid(row=5,column=1,padx=5,pady=5,sticky=E)
        self.riddleanswer = Entry(self.FrameBack, state="normal",width=60)
        self.riddleanswer.grid(row=5,column=2,padx=5,pady=5)
        self.lastFrame = Frame(self.registerWin)
        self.lastFrame.grid(row=6,column=0,sticky=N+S+E+W)
        self.newCancel = Button(self.lastFrame, text="Cancel", command = self.riddleLogin,width=30)
        self.newCancel.grid(row=6,column=0)
        self.newRegister = Button(self.lastFrame, text= "Register", command = self.RegisterNew,width=30)
        self.newRegister.grid(row=6,column=1)
        self.riddler = Button(self.lastFrame, text = "Captcha", command = self.RegisterPage,width=30)
        self.riddler.grid(row=6,column=2)
        

        
        
        
    def callLogin(self):
        self.registerWin2.withdraw()
        self.win.deiconify()

    def riddleLogin(self):
        self.registerWin.withdraw()
        self.win.deiconify()
        
    def LoginCheck(self):
        self.isThere = False
        self.usernameStuff = self.userEntry.get()
        self.passwordStuff = self.passEntry.get()
        self.Connect()
        self.cursor = self.db.cursor()
        self.sql = "SELECT * FROM GTBrokerageUsers WHERE Username = '{}' AND Password = '{}'".format(self.usernameStuff,self.passwordStuff)
        self.cursor.execute(self.sql)
        for x in self.cursor:
            if len(x[1]) > 0 and len(x[2]) > 0:
                self.isThere = True
        if self.isThere == True:
            messagebox.showwarning("Success","You Have Successfully Logged In")
            self.Driver()
        else:
            messagebox.showwarning("Sorry","No Credentials were Found in this Database")

    def Driver(self):
        self.win.withdraw()
        self.GetStockSymbols()
        self.keys = list(self.GTBSymbol.keys())
        self.val = list(self.GTBSymbol.values())
        self.unlistedval = []
        self.finalList = []
        #print(self.val)
        #print(self.keys)
        self.CloseOrCurrentPrice = []
        self.previousCloseList = []
        self.highList = []
        self.lowList = []
        for x in self.keys:
            self.GetPrices(x)
        #print(self.CloseOrCurrentPrice)
        #print(self.previousCloseList)
        #print(self.highList)
        #print(self.lowList)
        for item in self.val:
            for a in item:
                self.unlistedval.append(a)
        for x in range(len(self.keys)):
            self.GTBSymbol[self.keys[x]].append(self.CloseOrCurrentPrice[x])
            self.GTBSymbol[self.keys[x]].append(self.previousCloseList[x])
            self.GTBSymbol[self.keys[x]].append(self.highList[x])
            self.GTBSymbol[self.keys[x]].append(self.lowList[x])
        self.HomePage()
        

    def MarketOpen(self):
        self.open = False
        self.dayCheck = False
        ts = time.time()
        self.wholeThing = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
        #print(self.wholeThing)
        self.OpenDays = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
        self.date = self.wholeThing[0:len(self.wholeThing)-8]
        self.timeString = datetime.datetime.now().strftime("%I:%M%p")
        self.timing = self.timeString[0:len(self.timeString)-2]
        self.AMorPM = self.timeString[len(self.timeString)-2:len(self.timeString)]
        if self.AMorPM == "AM":
            self.timevalue = 0
        else:
            self.timevalue = 12
        self.hourValue = int(self.timing[0:2])
        self.minuteValue = int(self.timing[len(self.timing)-2:len(self.timing)])
        if self.hourValue == 12:
            self.hourValue = 0
        self.gateDoor = 60*(self.hourValue+self.timevalue)+self.minuteValue
        #9:30 AM to 4 PM
        if 570 <= self.gateDoor < 960:
            self.open = True
        for x in self.OpenDays:
            if x in self.wholeThing:
                self.dayCheck = True
        #print(self.open)
        if (self.open == True and self.dayCheck == True):
            #print("The Market is Open")
            self.checkOpen = True
        else:
            #print("Sorry The Market is Closed")
            self.checkOpen = False

    def GetStockSymbols(self):
        self.holdsymbol = []
        self.companyNames = []
        
        self.request = urllib.request.Request("http://www.nasdaq.com/markets/most-active.aspx")
        self.urlOpen = urllib.request.urlopen(self.request)
        self.html = self.urlOpen.read()
        self.Text = self.html.decode(errors="replace")
        self.GTBSymbol = {}
        self.symbol = re.findall(r'MostActiveByShareVolume_[0-9]{1,}_summaryquotes_[0-9]{1,}" href="http://www.nasdaq.com/symbol/[a-z]{1,}">[A-Z]{2,}',self.Text)
        #print(self.Text)
        self.companyName = re.findall(r"symbol/[a-z]{1,}'>[A-Z'a-z.\s,()0-9!&]{1,}",self.Text)
        for x in self.symbol:
            #print("STUFF")
            #print(x)
            char = len(x)-1
            self.extract = ""
            while x[char] != ">":
                self.extract = self.extract + x[char]
                char = char - 1
            self.holdsymbol.append(self.extract[::-1])
        for y in range(20):
            #print(self.companyName[y])
            index = len(self.companyName[y])-1
            self.aString = ""
            while self.companyName[y][index] != ">":
                self.aString += self.companyName[y][index]
                index -= 1
            self.companyNames.append(self.aString[::-1])
        #print("THE LIST OF SYMBOLS")
        #print(self.holdsymbol)
        #print(self.companyNames)
        #print(len(self.companyNames))
        #print(len(self.holdsymbol))
        for x in range(len(self.companyNames)):
            self.someBox = [self.companyNames[x]]
            self.GTBSymbol[self.holdsymbol[x]] = self.someBox
        #print(self.GTBSymbol)
        
                                    
    def GetPrices(self,StockSymbol):
        self.MarketOpen()
        if (self.checkOpen == True):
            self.rtweb = "http://www.nasdaq.com/symbol/" + StockSymbol + "/real-time"
            #print(self.rtweb)
            
        else:
            self.rtweb = "http://www.nasdaq.com/symbol/" + StockSymbol
            #print(self.rtweb)
            
        self.req = urllib.request.Request(self.rtweb)
        self.someurl = urllib.request.urlopen(self.req)
        self.htmlstuff = self.someurl.read()
        self.priceText = self.htmlstuff.decode(errors="replace")
        #print(self.priceText)
        if (self.checkOpen == False):
            self.currentorClose = re.findall(r'closing price for NASDAQ-listed issues.[A-Z\s</a-z>="$&;]*[0-9.]*</td>',self.priceText)
            #count = 0
            for a in self.currentorClose:
                #count+= 1
                #print(a)
                #print(count)
                indexVal = len(a)-6
                self.anotherStrings = ""
                while a[indexVal] != ";":
                    self.anotherStrings = self.anotherStrings + a[indexVal]
                    #print(self.anotherStrings)
                    indexVal = indexVal - 1
                self.CloseOrCurrentPrice.append(self.anotherStrings[::-1])
            self.previousClose = re.findall(r'last reported trade price during official trading hours.[\s]*</span>[a-z="A-Z/<>$&;\s]*[0-9.]*',self.priceText)
            for z in self.previousClose:
                newIndex = len(z)-1
                self.prevString = ""
                while z[newIndex] != ";":
                    self.prevString += z[newIndex]
                    newIndex -= 1
                self.previousCloseList.append(self.prevString[::-1])
            self.todaysHigh = re.findall(r'<label id="Label3">[$&]*nbsp;[0-9.]*',self.priceText)
            for e in self.todaysHigh:
                indexBacking = len(e) - 1
                self.aString = ""
                while e[indexBacking] != ";":
                    self.aString += e[indexBacking]
                    indexBacking -= 1
                self.highList.append(self.aString[::-1])
            self.todaysLow = re.findall(r'<label id="Label1">[$&]*nbsp;[0-9.]*',self.priceText)
            for l in self.todaysLow:
                substring = len(l) - 1
                self.newSub = ""
                while l[substring] != ";":
                    self.newSub += l[substring]
                    substring -= 1
                self.lowList.append(self.newSub[::-1])
        else:
            self.currentorClose = re.findall(r'display:inline-block;">[0-9.]*', self.priceText)
            for g in self.currentorClose:
                someLen = len(g) - 1
                self.someString = ""
                while g[someLen] != ">":
                    self.someString += g[someLen]
                    someLen -= 1
                self.CloseOrCurrentPrice.append(self.someString[::-1])
            self.previousClose = re.findall(r'left__PreviousClose">[0-9.]*', self.priceText)
            for a in self.previousClose:
                #print(a)
                gen = len(a) - 1
                self.anotherString = ""
                while a[gen] != ">":
                    self.anotherString += a[gen]
                    gen -= 1
                self.previousCloseList.append(self.anotherString[::-1])
            self.todaysHigh = re.findall(r'left__TodaysHigh">[0-9.]*',self.priceText)
            for y in self.todaysHigh:
                indexBacking = len(y) - 1
                self.aString = ""
                while y[indexBacking] != ">":
                    self.aString += y[indexBacking]
                    indexBacking -= 1
                self.highList.append(self.aString[::-1])
            self.todaysLow = re.findall(r'left__TodaysLow">[0-9.]*',self.priceText)
            for a in self.todaysLow:
                index = len(a) - 1
                self.str = ""
                while a[index] != ">":
                    self.str += a[index]
                    index -= 1
                self.lowList.append(self.str[::-1])
                
        
        
            
        
                                              
        
        
        
        #If the market is open then self.open = True otherwise it is False.
    def captcha(self):
        self.xval = 0
        self.someList = []
        self.someAnswers = []
        self.opening = open("captchaList.csv")
        self.csvReader = csv.reader(self.opening, delimiter= ",")
        for y in self.csvReader:
            self.someList.append(y[0])
            self.someAnswers.append(y[1])
        self.registerWin2 = Toplevel()
        self.registerWin2.wm_title("GT Brokers Register Page")
        self.FrameBack2 = Frame(self.registerWin2, bg="gold")
        self.FrameBack2.grid(row=0,column=0,rowspan=6,columnspan=2)
        self.registerpic = PhotoImage(file = "registerpic.gif")
        self.registerlabel = Label(self.FrameBack2,image=self.registerpic)
        self.registerlabel.registerpic = self.registerpic
        self.registerlabel.grid(row=0,column=0,sticky=E)
        self.fullName = Label(self.FrameBack2, text="Full Name:",bg="gold")
        self.fullName.grid(row=0,column=1,padx=5,pady=5,sticky=E)
        self.fullNameEntry = Entry(self.FrameBack2, state = "normal",width=60)
        self.fullNameEntry.grid(row=0,column=2,padx=5,pady=5)
        self.anotherusername = Label(self.FrameBack2,text="Username:",bg="gold")
        self.anotherusername.grid(row=1,column=1,padx=5,pady=5,sticky=E)
        self.anotheruserEntry = Entry(self.FrameBack2, state = "normal",width=60)
        self.anotheruserEntry.grid(row=1,column=2,padx=5,pady=5)
        self.anotherpassword = Label(self.FrameBack2, text = "Password:",bg="gold")
        self.anotherpassword.grid(row=2,column=1,padx=5,pady=5,sticky=E)
        self.anotherpassEntry = Entry(self.FrameBack2, state = "normal",width=60)
        self.anotherpassEntry.grid(row=2,column=2,padx=5,pady=5)
        self.somepassword = Label(self.FrameBack2, text = "Confirm Password:",bg="gold")
        self.somepassword.grid(row=3, column = 1, padx=5, pady =5,sticky=E)
        self.somepassEntry = Entry(self.FrameBack2, state = "normal",width=60)
        self.somepassEntry.grid(row=3,column=2,padx=5,pady=5)
        self.proofHuman = Label(self.FrameBack2, text= "Prove you're a Human:",bg="gold")
        self.proofHuman.grid(row=4,column=1,padx=5,pady=5,sticky=E)
        
        self.someNumber = random.randrange(1,len(self.someList)-1)
        self.ranMessage = self.someList[self.someNumber]
        self.randPhoto = PhotoImage(file = self.ranMessage)
        self.proofeEntry = Label(self.FrameBack2, image=self.randPhoto)
        self.proofeEntry.grid(row=4,column=2)

        

        
        self.riddle = Label(self.FrameBack2, text = "Enter the text clearly displayed above:",bg="gold")
        self.riddle.grid(row=5,column=1,padx=5,pady=5,sticky=E)
        self.riddleanswer = Entry(self.FrameBack2, state="normal",width=60)
        self.riddleanswer.grid(row=5,column=2,padx=5,pady=5)
        self.finalFrame = Frame(self.registerWin2)
        self.finalFrame.grid(row=6,column=0,sticky=N+S+E+W)
        self.newCancel = Button(self.finalFrame, text="Cancel", command = self.callLogin,width=30)
        self.newCancel.grid(row=6,column=0)
        self.newRegister = Button(self.finalFrame, text= "Register", command = self.RegisterNew,width=30)
        self.newRegister.grid(row=6,column=1)
        self.riddler = Button(self.finalFrame, text = "Riddler", command = self.RegisterPage,width=30)
        self.riddler.grid(row=6,column=2)
        

    
    def RegisterNew(self):
        self.Connect()
        self.fullNameFinal = self.fullNameEntry.get()
        self.userNameFinal = self.anotheruserEntry.get()
        self.passwordFinal = self.anotherpassEntry.get()
        self.confirmpassFinal = self.somepassEntry.get()
        self.theanswer = self.riddleanswer.get()
        self.finalanswer = self.someAnswers[self.someNumber]
        self.brokerageValue = 100000
        self.someuserlist = []
        self.cursor3 = self.db.cursor()
        self.moresql = "Select Username FROM GTBrokerageUsers"
        self.cursor3.execute(self.moresql)
        self.uppercounter = 0
        self.digitcounter = 0
        for x in self.cursor3:
            for a in x:
                a = a.lower()
                self.someuserlist.append(a)
        self.checkbool = True
        self.userNameFinal = self.userNameFinal.lower()
        if self.xval == 1:
            self.theanswer = self.theanswer.lower()
            self.finalanswer = self.finalanswer.lower()
        for index in self.passwordFinal:
            if index in list(string.ascii_uppercase):
                self.uppercounter += 1
            if index in list(string.digits):
                self.digitcounter += 1
        if len(self.userNameFinal) == 0 or len(self.passwordFinal) == 0 or len(self.theanswer) == 0 or len(self.confirmpassFinal) == 0:
            self.checkbool = False
            messagebox.showwarning("Invalid","One Or More Of Your Entries Are Blank")
        elif self.passwordFinal != self.confirmpassFinal:
            self.checkbool = False
            messagebox.showwarning("Invalid","Your Confirmed Password Does Not Match")
        elif self.uppercounter < 1:
            self.checkbool = False
            messagebox.showwarning("Invalid","Please Have Atleast One Uppercase Letter in Your Password!")
        elif self.digitcounter < 1:
            self.checkbool = False
            messagebox.showwarning("Invalid","Please Have Atleast One Digit in Your Password!")
        elif self.theanswer != self.finalanswer:
            self.checkbool = False
            messagebox.showwarning("Invalid","Wrong Answer!")
        elif self.userNameFinal in self.someuserlist:
            self.checkbool = False
            messagebox.showwarning("Invalid","This User Already Exists!")
        elif len(self.userNameFinal) > 30:
            self.checkbool = False
            messagebox.showwarning("Invalid","Your Username Cannot Exceed 30 Characters")
        elif len(self.fullNameFinal) > 30:
            self.checkbool = False
            messagebox.showwarning("Invalid","Your Full Name Cannot Exceed 30 Characters")
        elif len(self.passwordFinal) > 30 or len(self.confirmpassFinal) > 30:
            self.checkbool = False
            messagebox.showwarning("Invalid","Your Password Cannot Exceed 30 Characters")
        if self.checkbool == True:
            self.someString = "INSERT INTO GTBrokerageUsers (Fullname,Username,Password,Balance) VALUES ('{}','{}','{}','{}')".format(self.fullNameFinal,self.userNameFinal,self.passwordFinal,self.brokerageValue)
            self.cursor4 = self.db.cursor()
            self.cursor4.execute(self.someString)
            self.db.commit()
            self.db.close()
            messagebox.showwarning("Success!", "Welcome To The Database!")
            if self.xval == 1:
                self.riddleLogin()
            else:
                self.callLogin()

    def HomePage(self):
        self.homePageWindow = Toplevel()
        self.firstphoto = PhotoImage(file = "otherpic.gif")
        self.firstButton = Button(self.homePageWindow, image = self.firstphoto, text = "Butler, show me my portfolio",command = self.myportfolio,compound = TOP)
        self.firstButton.grid(row=0,column=0)
        self.secondphoto = PhotoImage(file = "wallst.gif")
        self.secondButton = Button(self.homePageWindow, image = self.secondphoto, text = "Take me to Wall Street", command = self.tradeplace, compound = TOP)
        self.secondButton.grid(row=0,column=1)
        self.thirdphoto = PhotoImage(file = "competitors.gif")
        self.thirdButton = Button(self.homePageWindow, image = self.thirdphoto, text = "Most Active Stocks in GT Brokerage", command = self.active, compound = BOTTOM)
        self.thirdButton.grid(row=1,column=0)
        self.fourthphoto = PhotoImage(file = "money.gif")
        self.fourthButton = Button(self.homePageWindow, image = self.fourthphoto, text = "Help me make some money", command = self.stats, compound = BOTTOM)
        self.fourthButton.grid(row=1,column=1)
        
    def myportfolio(self):
        #print("welcome to my portfolio")
        self.homePageWindow.withdraw()
        self.putListofCompany = []
        self.portdb = self.db.cursor()
        self.sqlmessage = "SELECT Fullname FROM GTBrokerageUsers WHERE Username = %s AND Password = %s"
        self.fullTuple = (self.usernameStuff, self.passwordStuff)
        self.portdb.execute(self.sqlmessage,self.fullTuple)
        for x in self.portdb:
            #print("HERE IS YOUR FULL NAME: ")
            for y in x:
                self.theName = y
        self.cursor2 = self.db.cursor()
        self.whatToDo = "SELECT Balance FROM GTBrokerageUsers WHERE Username = %s AND Password = %s"
        self.balancetuple = (self.usernameStuff,self.passwordStuff)
        self.cursor2.execute(self.whatToDo,self.balancetuple)
        for y in self.cursor2:
            for a in y:
                self.amountofbalance = str(a)
        self.myportWindow = Toplevel()
        self.welcomeMessage = "Welcome, " + self.theName
        self.welcomeTitle = self.theName + "'s Portfolio"
        self.myportWindow.wm_title(self.welcomeTitle)
        self.myportWindow.config(bg="gold")
        self.welcomesign = Label(self.myportWindow, text = self.welcomeMessage, bg = "gold")
        self.welcomesign.grid(row=0,column=0,sticky=W)
        self.balancemensaje = "Available to trade: $" + self.amountofbalance
        self.welcomesign = Label(self.myportWindow, text = self.balancemensaje, bg = "gold")
        self.welcomesign.grid(row=1,column=0,sticky=W)
        self.currentport = Label(self.myportWindow, text = "Current Portfolio:", bg = "gold")
        self.currentport.grid(row=2,column=0,sticky=N+S+E+W)
        self.stockname1 = Label(self.myportWindow, text = "Stock Name", bg= "gold")
        self.stockname1.grid(row=3,column=0,sticky=N+S+E+W)
        self.totprice1 = Label(self.myportWindow, text= "Sum of Total Price", bg= "gold")
        self.totprice1.grid(row=3,column=1,sticky=N+S+E+W)
        self.sumquant1 = Label(self.myportWindow, text ="Sum of Quantity", bg = "gold")
        self.sumquant1.grid(row=3,column=2,sticky=N+S+E+W)
        self.currentworth1 = Label(self.myportWindow, text = "Current Worth if Sold", bg = "gold")
        self.currentworth1.grid(row=3,column=3,sticky=N+S+E+W)
        self.companynamemyStock = "SELECT StockName FROM GTBrokerageActivity WHERE ListingUser = %s"
        self.moredb = self.db.cursor()
        self.moredb.execute(self.companynamemyStock,(self.usernameStuff))
        for x in self.moredb:
            for company in x:
                if company not in self.putListofCompany:
                    self.putListofCompany.append(company)
        #print(self.putListofCompany)
        for y in range(len(self.putListofCompany)):
            self.eachCompanybought = []
            self.eachCompanysell = []
            self.totalCompany = []
            self.quantityBought = []
            self.quantitySold = []
            self.currentWorth = []
            self.buycompanyMessage = "SELECT TotalPrice FROM GTBrokerageActivity WHERE ListingUser = %s AND Buy = 1 AND StockName = %s"
            self.buycursor = self.db.cursor()
            self.sellcursor = self.db.cursor()
            self.buycursor.execute(self.buycompanyMessage,(self.usernameStuff,self.putListofCompany[y]))
            for a in self.buycursor:
                for b in a:
                    self.eachCompanybought.append(b)
            self.sellcompanyMessage = "SELECT TotalPrice FROM GTBrokerageActivity WHERE ListingUser = %s AND Buy = 0 AND StockName = %s"
            self.sellcursor.execute(self.sellcompanyMessage,(self.usernameStuff,self.putListofCompany[y]))
            for e in self.sellcursor:
                for f in e:
                    self.eachCompanysell.append(f)
            #print(self.putListofCompany[y])
            self.boughtSum = sum(self.eachCompanybought)
            self.sellSum = sum(self.eachCompanysell)
            #print(self.boughtSum)
            #print(self.sellSum)
            self.totalamt = float(self.boughtSum)- float(self.sellSum)
            self.amtLabel1 = Label(self.myportWindow, text = self.putListofCompany[y], bg = "gold",width=30)
            self.amtLabel1.grid(row=y+4, column = 0,sticky=N+S+E+W)
            self.realamount1 = Label(self.myportWindow,text = self.totalamt, bg="gold",width =15)
            self.realamount1.grid(row=y+4,column=1,sticky=N+S+E+W)
            self.quantitytimeB = "SELECT Quantity FROM GTBrokerageActivity WHERE ListingUser = %s AND Buy = 1 AND StockName = %s"
            self.quantitycursorB = self.db.cursor()
            self.quantitycursorB.execute(self.quantitytimeB,(self.usernameStuff,self.putListofCompany[y]))
            for m in self.quantitycursorB:
                for word in m:
                    self.quantityBought.append(word)
            self.quantitycursorS = self.db.cursor()
            self.quantitytimeS = "SELECT Quantity FROM GTBrokerageActivity WHERE ListingUser = %s AND Buy = 0 AND StockName = %s"
            self.quantitycursorS.execute(self.quantitytimeS,(self.usernameStuff,self.putListofCompany[y]))
            for x in self.quantitycursorS:
                for a in x:
                    self.quantitySold.append(a)
            self.qBSum = sum(self.quantityBought)
            self.qSSum = sum(self.quantitySold)
            self.realquant = self.qBSum - self.qSSum
            self.quantLabelle = Label(self.myportWindow,text = self.realquant, bg= "gold",width=15)
            self.quantLabelle.grid(row=y+4,column=2,sticky=N+S+E+W)
            self.cworth = "SELECT Symbol FROM GTBrokerageActivity WHERE ListingUser = %s AND StockName = %s"
            self.cworther = self.db.cursor()
            self.cworther.execute(self.cworth, (self.usernameStuff,self.putListofCompany[y]))
            for a in self.cworther:
                for z in a:
                    self.sacredSymbol = z
            try:
                self.theListofStuff = self.GTBSymbol[self.sacredSymbol]
                self.thegreatprice = float(self.theListofStuff[1])
                self.conditionalselling = self.realquant * self.thegreatprice
                self.finalLabel1 = Label(self.myportWindow, text= self.conditionalselling,bg="gold",width=15)
                self.finalLabel1.grid(row=y+4,column=3,sticky=N+S+E+W)
                self.closingTime = Button(self.myportWindow, text = "Close", command = self.myportfolioToHome)
                self.closingTime.grid(row=len(self.putListofCompany)+4, column = 3,sticky=E)
            except:
                self.GetPrices(self.sacredSymbol)
                self.thegreatpriceindexer = self.CloseOrCurrentPrice
                self.thegreatprice = float(self.thegreatpriceindexer[y])
                self.conditionalselling = self.realquant*self.thegreatprice
                self.finalLabel1 = Label(self.myportWindow, text= self.conditionalselling, bg="gold",width=15)
                self.finalLabel1.grid(row=y+4,column=3,sticky=N+S+E+W)
                self.closingTime = Button(self.myportWindow,text = "Close", command = self.myportfolioToHome)
                self.closingTime.grid(row=len(self.putListofCompany)+4,column=3,sticky=E)
                
                
                
            
        
        
            
            
                
            
            
            
            
                            
        
    def myportfolioToHome(self):
        self.myportWindow.withdraw()
        self.homePageWindow.deiconify()
        
        

    def tradeplace(self):
        self.homePageWindow.withdraw()
        self.tradeGUI = Toplevel()
        self.anothercursor = self.db.cursor()
        self.transactiveCursor = self.db.cursor()
        self.oneMoreCursor = self.db.cursor()
        self.quantities = []
        #to list all the transactions
        self.ent = StringVar()
        
        self.finaldictKeys = list(self.GTBSymbol.keys())
        self.finaldictVals = list(self.GTBSymbol.values())
        for x in range(len(self.finaldictVals)):
            self.finaldictVals[x].append(self.finaldictKeys[x])
        self.combinedDictVal = sorted(self.finaldictVals)
            
        #print(self.finaldictKeys)
        #print(self.finaldictVals)
        self.boughtqlist = []
        self.soldqlist = []
        self.portfoliowriteuplist = []
        #To sum up all bought transactions per company:
        for x in range(len(self.combinedDictVal)):
            try:
                self.boughtsql = "SELECT SUM(Quantity) FROM GTBrokerageActivity WHERE ListingUser = '{}' AND Symbol = '{}' AND Buy = 1".format(self.usernameStuff,self.combinedDictVal[x][5])
                self.transactiveCursor.execute(self.boughtsql)
                #for item in self.transactiveCursor:
                    #self.bought = item
                    #print("BOUGHT")
                #(Decimal('14'))
                for x in self.transactiveCursor:
                    #print(x, "OTHER STUFF BOUGHT")
                    g = str(x)
                    emptyString = ""
                    for a in g:
                        #print(a)
                        if a in ['0','1','2','3','4','5','6','7','8','9']:
                            emptyString += a
                    if emptyString == "":
                        emptyString = "0"
                    self.boughtqlist.append(emptyString)
            except:
                self.bought = "0"
                self.boughtqlist.append(self.bought)
        for y in range(len(self.combinedDictVal)):
            try:
                self.soldsql = "SELECT SUM(Quantity) FROM GTBrokerageActivity WHERE ListingUser = %s AND Symbol = %s AND Buy = %s"
                self.tupleStuff = (self.usernameStuff,self.combinedDictVal[y][5],0)
                self.oneMoreCursor.execute(self.soldsql,self.tupleStuff)
                #self.transactiveCursor.execute(self.soldsql)
                #for item in self.transactiveCursor:
                    #print("SOLD")
                for x in self.oneMoreCursor:
                    #print(x, "STUFF SOLD")
                    g = str(x)
                    emptyString = ""
                    for a in g:
                        #print(a)
                        if a in ['0','1','2','3','4','5','6','7','8','9']:
                            emptyString += a
                    if emptyString == "":
                        emptyString = "0"
                    self.soldqlist.append(emptyString)
                    #print(g)
            except:
                self.sold = "0"
                self.soldqlist.append(self.sold)
        for x in range(len(self.boughtqlist)):
            self.portfoliowriteuplist.append(int(self.boughtqlist[x]) - int(self.soldqlist[x]))
        
            
                
        #To find the balance of the user
        self.moresql = "Select * FROM GTBrokerageUsers WHERE Username = '{}'".format(self.usernameStuff)
        self.anothercursor.execute(self.moresql)
        self.optionsFrame = Frame(self.tradeGUI,bg="gold",relief=RAISED,borderwidth=1)
        self.optionsFrame.pack(side=TOP ,fill=BOTH)
        for x in self.anothercursor:
            self.firstbalance = x[3]
        self.availableString = "Available to trade: $" + str(self.firstbalance)
        self.availableBalance = Label(self.optionsFrame, text = self.availableString, bg="gold",borderwidth=1)
        self.availableBalance.grid(row=0,column=0)
        self.dateTime = Label(self.optionsFrame, text = self.date,bg = "gold")
        self.dateTime.grid(row=0,column=1)
        self.actionLabel = Label(self.optionsFrame,text = "Action:", bg="gold")
        self.actionLabel.grid(row=1,column=0)
        self.var = IntVar()
        self.firstradio = Radiobutton(self.optionsFrame, text = "Buy",variable = self.var, value = 1, bg = "gold")
        self.firstradio.grid(row = 1, column = 1,sticky=N+S+E+W)
        self.secondradio = Radiobutton(self.optionsFrame, text = "Sell", variable = self.var, value = 0, bg = "gold")
        self.secondradio.grid(row =1, column = 2,sticky=N+S+E+W)
        self.someFrame = Frame(self.tradeGUI, bg= "gold",relief=RAISED,borderwidth=1)
        self.someFrame.pack(side=TOP,fill=BOTH)
        self.quanLabel = Label(self.someFrame,text = "Quantity", bg="gold",width=15)
        self.quanLabel.grid(row=0,column=0,sticky=N+S+E+W)
        self.portLabel = Label(self.someFrame, text= "Portfolio", bg="gold",width=15)
        self.portLabel.grid(row=0,column=1,sticky=N+S+E+W)
        self.stockLabel = Label(self.someFrame, text = "Stocknames", bg="gold",width=30)
        self.stockLabel.grid(row=0,column=2,sticky=N+S+E+W)
        self.previousLabel = Label(self.someFrame, text= "Previous Close", bg="gold",width=15)
        self.previousLabel.grid(row=0,column=3,sticky=N+S+E+W)
        self.currentHighLabel = Label(self.someFrame, text = "Current High", bg="gold",width=15)
        self.currentHighLabel.grid(row=0,column=4,sticky=N+S+E+W)
        self.currentLowLabel = Label(self.someFrame, text = "Current Low", bg="gold",width=15)
        self.currentLowLabel.grid(row=0,column=5,sticky=N+S+E+W)
        self.currentPriceLabel = Label(self.someFrame, text = "Current Price", bg="gold",width=15)
        self.currentPriceLabel.grid(row=0,column=6,sticky=N+S+E+W)
        self.profitLabel = Label(self.someFrame, text= "Profit", bg="gold",width=15)
        self.profitLabel.grid(row=0,column=7,sticky=N+S+E+W)
        self.bigFrame = Frame(self.tradeGUI, bg="gold",relief=RAISED,borderwidth=1)
        self.bigFrame.pack(side=TOP, fill=BOTH)
        for x in range(20):
            self.profcolor = ""
            self.yetanotherFrame = Frame(self.bigFrame, bg="gold",relief=RAISED)
            self.yetanotherFrame.pack(anchor=W, fill=BOTH)
            self.currentEntry = Entry(self.yetanotherFrame, state = "normal", bg="gold",width=15)
            self.currentEntry.grid(row=0,column=0)
            self.quantities.append(self.currentEntry)
            self.portfolioStuff = Label(self.yetanotherFrame, text = self.portfoliowriteuplist[x], bg="gold",width=15)
            self.portfolioStuff.grid(row=0,column=1,sticky=N+S+E+W)
            self.stockNameStuff = Label(self.yetanotherFrame, text = self.combinedDictVal[x][0], bg="gold",width=30)
            self.stockNameStuff.grid(row=0,column=2,sticky=N+S+E+W)
            self.prevcloseStuff = Label(self.yetanotherFrame, text = str(self.combinedDictVal[x][2]), bg="gold",width=15)
            self.prevcloseStuff.grid(row=0,column=3,sticky=N+S+E+W)
            self.currenthighStuff = Label(self.yetanotherFrame, text = str(self.combinedDictVal[x][3]), bg = "gold",width=15)
            self.currenthighStuff.grid(row=0,column=4,sticky=N+S+E+W)
            self.currentlowStuff = Label(self.yetanotherFrame, text = str(self.combinedDictVal[x][4]), bg = "gold",width=15)
            self.currentlowStuff.grid(row=0,column=5,sticky=N+S+E+W)
            self.currentpriceStuff = Label(self.yetanotherFrame, text = str(self.combinedDictVal[x][1]), bg = "gold",width=15)
            self.currentpriceStuff.grid(row=0,column=6,sticky=N+S+E+W)
            self.profitValue = float(self.combinedDictVal[x][1])-float(self.combinedDictVal[x][2])
            self.roundedprofitValue = "%.2f" %self.profitValue
            self.backtoprofit = float(self.roundedprofitValue)
            if self.backtoprofit >= 0:
                self.profcolor = "green"
            else:
                self.profcolor = "red"
            self.profitStuff = Label(self.yetanotherFrame, text = self.roundedprofitValue, bg=self.profcolor)
            self.profitStuff.grid(row=0,column=7,sticky=N+S+E+W)
        self.lastFrame = Frame(self.tradeGUI, bg = "gold",relief=RAISED,borderwidth=1)
        self.lastFrame.pack(side=BOTTOM)
        self.cancelWS = Button(self.lastFrame, text = "Cancel", command = self.cancelWS)
        self.cancelWS.grid(row=0,column=0,sticky=E)
        self.clearQTButton = Button(self.lastFrame, text = "Clear", command = self.clearQuantity)
        self.clearQTButton.grid(row=0,column=1,sticky=E)
        self.orderButton = Button(self.lastFrame, text = "Place Order", command = self.transaction)
        self.orderButton.grid(row=0,column=2,sticky=E)
                                        
            
        
        
        
    def clearQuantity(self):
        for items in self.quantities:
            items.delete(0,END)
            items.insert(0,"0")
        

    def cancelWS(self):
        self.clearQuantity()
        self.tradeGUI.withdraw()
        self.homePageWindow.deiconify()

    def clearQuantity2(self):
        for items in self.quantities:
            items.delete(0,END)
            items.insert(0,"0")

    def cancelWS2(self):
        self.clearQuantity2()
        self.tradeGUI.withdraw()
        self.homePageWindow.deiconify()

    def transaction(self):
        print("Transaction")
        self.notEnoughFunds = False
        self.notEnoughStocks = False
        self.notInt = False
        self.everyCheck = False
        self.checkStuffFinal = True
        self.keepBoxOfPurchases = []
        self.keepBoxOfSellings = []
        self.validPortfolio = []
        self.validpurchases = 0
        self.validsells = 0
        self.floatfirstbalance = float(self.firstbalance)
        
        #BUYING STOCKS
        if self.var.get() == 1:
            #print("YOU CLICKED BUY")
            for x in range(len(self.quantities)):
                self.ordering = self.quantities[x].get()
                #print(self.ordering, "IS SELF.ORDERING")
                try:
                    self.intordering = int(self.ordering)
                except:
                    messagebox.showwarning("Impossible!","You can't buy a fraction of a stock :P")
                if ("." in self.ordering):
                    self.notInt = True
                self.companyName = self.combinedDictVal[x][0]
                self.stockPrice = self.combinedDictVal[x][2]
                self.floatstockPrice = float(self.stockPrice)
                self.floatfirstbalance = self.floatfirstbalance - (self.intordering*self.floatstockPrice)
                if self.floatfirstbalance < 0:
                    self.notEnoughFunds = True
                self.keepBoxOfPurchases.append(self.intordering)
                
            if self.notEnoughFunds == True:
                messagebox.showwarning("Impossible!","Good try but you don't have the $$Cash money$$")
            elif self.notInt:
                messagebox.showwarning("Impossible!","You can't buy a fraction of a stock :P")  
            else:
                #self.availableString = "Available to trade: $" + str(self.floatfirstbalance)
                self.someCursor = self.db.cursor()
                self.balancestatement = "UPDATE GTBrokerageUsers SET Balance = %s WHERE Username = %s"
                self.someCursor.execute(self.balancestatement,(self.floatfirstbalance,self.usernameStuff))
                #self.availableBalance['text'] = self.availableString
                for x in range(len(self.quantities)):
                    self.someintordering = int(self.quantities[x].get())
                    #self.boughtqlist[x] = str(int(self.boughtqlist[x]) + int(self.keepBoxOfPurchases[x]))
                    #self.portfoliowriteuplist[x] = str(int(self.portfoliowrietuplist[x]) + int(self.keepBoxOfPurchases[x]))
                    self.totalQuan = self.someintordering*float(self.combinedDictVal[x][1])
                    #print("THE QUANTITY IS ", self.someintordering)
                    self.sometuple = (self.usernameStuff,self.combinedDictVal[x][0],self.combinedDictVal[x][5],self.combinedDictVal[x][1],datetime.datetime.now(),self.totalQuan,self.someintordering,1)
                    self.anothersql = "INSERT INTO GTBrokerageActivity (ListingUser,StockName,Symbol,Price,Time_stamp,TotalPrice,Quantity,Buy) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"                    #print(self.anothersql)
                    self.aCursor = self.db.cursor()
                    self.aCursor.execute(self.anothersql,self.sometuple)
                self.db.commit()
        
                    
        #SELLING STOCKS
        if self.var.get() == 0:
            #print("YOU CLICKED SELL!")
            for x in range(len(self.quantities)):
                self.ordering = self.quantities[x].get()
                print("HOW MUCH YOU WANT TO SELL ", self.ordering)
                try:
                    self.intordering = int(self.ordering)
                except:
                    messagebox.showwarning("Impossible!","You can't buy a fraction of a stock :P")
                if ("." in self.ordering):
                    self.notInt = True
                self.companyName = self.combinedDictVal[x][0]
                self.stockPrice = self.combinedDictVal[x][2]
                self.floatstockPrice = float(self.stockPrice)
            if self.notInt:
                messagebox.showwarning("Impossible!","You can't sell a fraction of a stock :P")
            for z in range(len(self.keepBoxOfSellings)):
                #print(self.keepBoxOfSellings[x], " TOTAL SELLINGS")
                print(self.portfoliowriteuplist[z], " PORTFOLIO AMOUNT")
                if int(self.keepBoxOfSellings[z]) > int(self.portfoliowriteuplist[z]):
                    self.notEnoughStocks = True
            if(self.notEnoughStocks == True):
                messagebox.showwarning("Impossible!","Getta outta here! You cannot sell a stock you do not own!")
            
            if(self.notEnoughStocks == False and self.notInt == False):
                self.balancestatement = "UPDATE GTBrokerageUsers SET Balance = %s WHERE Username = %s"
                self.sellbalancecursor = self.db.cursor()
                self.sellbalancecursor.execute(self.balancestatement,(self.floatfirstbalance,self.usernameStuff))
                for x in range(len(self.keepBoxOfSellings)):
                    #self.soldqlist[x] = str(int(self.soldqlist[x]) + int(self.keepBoxOfSellings[x]))
                    #self.portfoliowriteuplist[x] = str(int(self.portfoliowriteuplist[x]) - int(self.keepBoxOfSellings[x]))
                    self.someintordering = int(self.quantities[x].get())
                    print(self.someintordering)
                    self.sellstatement = "INSERT INTO GTBrokerageActivity (ListingUser,StockName,Symbol,Price,Time_stamp,TotalPrice,Quantity,Buy) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                    self.finalcursor = self.db.cursor()
                    self.totalQuan2 = self.someintordering*float(self.combinedDictVal[x][1])
                    self.sometuple = (self.usernameStuff,self.combinedDictVal[x][0],self.combinedDictVal[x][5],self.combinedDictVal[x][1],datetime.datetime.now(),self.totalQuan2,self.someintordering,0)
                    self.finalcursor.execute(self.sellstatement,self.sometuple)
                self.db.commit()
        self.cancelWS2()
                    
                    
               
            
            
                
        

    def active(self):
        #print("active function")
        self.homePageWindow.withdraw()
        self.someWindow = Toplevel()
        self.someWindow.wm_title("Top 10 Most Active Stocks in GT Brokerage")
        self.someWindow.config(bg= "gold")
        self.stockLabel2 = Label(self.someWindow, text = "Stock Name", bg = "gold",width = 30)
        self.stockLabel2.grid(row = 0, column = 0, sticky = N+S+E+W)
        self.avprice2 = Label(self.someWindow, text = "Average Price", bg = "gold",width = 15)
        self.avprice2.grid(row=0,column=1,sticky=N+S+E+W)
        self.quantityStock2 = Label(self.someWindow, text = "Quantity of Stock", bg = "gold",width=15)
        self.quantityStock2.grid(row=0,column=2,sticky=N+S+E+W)
        self.stockCurrentValue = Label(self.someWindow, text = "Stock Current Value", bg = "gold", width=15)
        self.stockCurrentValue.grid(row=0,column=3,sticky=N+S+E+W)
        self.aCoolButton = Button(self.someWindow, text = "Close", command=self.activeToHome)
        self.aCoolButton.grid(row=1,column=4,sticky=E)
                                     

    def stats(self):
        print("stats function")

    def activeToHome(self):
        self.someWindow.withdraw()
        self.homePageWindow.deiconify()
                                
        
        
        

    def Connect(self):
        try:
            self.db = pymysql.connect(host = "academic-mysql.cc.gatech.edu",passwd="YaRNb9jd",user="iwaykul3",db="cs2316db")
            return self.db
        except:
            messagebox.showwarning("Cannot Connect", "Check Your Internet Connection")

        
    

a = IntroSQL()
