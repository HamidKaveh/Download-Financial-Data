# Importing Libraries:
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import tkinter.font as font
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import yfinance as yf
import datetime
from pandas_datareader import data as pdd
import mplfinance as mpf
from PIL import ImageTk, Image
#---------------------------------------------------------
# Main Loop:
master = Tk()
master.config(background='#FCFCFC')
master.title('Data Collection')
master.resizable(False,FALSE)
label = Label(master, text="Select the Market", font=('Courier 14 bold'))
label.grid(row =0, columnspan= 3, padx = 2, pady = 2, ipadx= 1, ipady=1)
label.config(justify=CENTER, background='#FCFCFC')
#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Stock Market:
def Stock():
    # TK stage:
    win = Toplevel()
    win.title("Stock Market")
    label = Label(win, text = 'Getting Stock Market Data', font=('Courier 14 bold'))
    label.grid(row =0, columnspan= 3, padx = 2, pady = 2, ipadx= 1, ipady=1)
    
    # The Main Function For Getting Data:
    sym = StringVar()
    Time_Frame = StringVar()

    def InputData():
        Symbol = sym.get()
        Symbol = Symbol.upper()
        TimeFrame = Time_Frame.get()
        data = yf.download(tickers= Symbol, start=Start_Date[0] , end=End_Date[0], interval=TimeFrame )
        data.to_csv(Symbol+'.csv')

    # Creating and Arranging the Input Column:

    # Symbol:
    SymbolLabel = Label(win, text = "Enter the Symbol", font = ('Courier 11 bold')).grid(row =1, columnspan= 3, padx = 2, pady = 2, ipadx= 1, ipady=1)
    SymbolEntry = Entry(win, textvariable= sym ,bg = "#E4EBF1", bd = 2,font = ('Courier 10 bold'), fg = "black", justify = 'center').grid(row =2, columnspan= 3, padx = 2, pady = 2, ipadx= 1, ipady=1)

    # Start and End Date:
    Start_Date = []
    def calendar_view():
        def GettingDate():
            start= cal.selection_get()
            Start_Date.append(start.strftime('%Y-%m-%d'))
            top.destroy()
        
        top = Toplevel(win)
        cal = Calendar(top, font=('Courier 10 bold'), selectmode='day', year=2018, month=1, day=1)
        cal.grid()
        ttk.Button(top, text="OK", command=GettingDate).grid(ipadx=2, ipady=2)
    ttk.Button(win, text='From', command=calendar_view).grid(row =4, column= 0, padx = 1, pady = 1, ipadx= 1, ipady=1)

    End_Date=[]
    def calendar_view_():
        def GettingEnd():
            End= cal.selection_get()
            End_Date.append(End.strftime('%Y-%m-%d'))
            top.destroy()

        top = Toplevel(win)
        cal = Calendar(top, font="Arial 9", selectmode='day')
        cal.grid()

        ttk.Button(top, text="ok", command=GettingEnd).grid()
    ttk.Button(win, text='To', command=calendar_view_).grid(row =4, column= 1, padx = 1, pady = 1, ipadx= 1, ipady=1)

    # Time_Frame Box:
    TimeFrames = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
    TimeFrameLabel = Label(win, text = "Time-Frame:", font = ('Consolas 10 bold')).grid(row =5, column= 0, padx = 1, pady = 1, ipadx= 1, ipady=1)
    TF = ttk.Combobox(win, values=TimeFrames, textvariable=Time_Frame, state = 'readonly').grid(row =5, column= 1, padx = 1, pady = 1, ipadx= 1, ipady=1)
    
    # Period:
    '''
    period: data period to download (either use period parameter or use start and end) Valid periods are:
    “1d”, “5d”, “1mo”, “3mo”, “6mo”, “1y”, “2y”, “5y”, “10y”, “ytd”, “max”
    '''
    
    # Start Button:
    Button_ = ttk.Button(win, text = '.CSV Output', command=InputData).grid(row =7, column= 2, padx = 1, pady = 1, ipadx= 1, ipady=1)
    Another_Market = ttk.Button(win, text='Markets', command=win.destroy).grid(row =8, column= 2, padx = 1, pady = 1, ipadx= 1, ipady=1)
    Exit = ttk.Button(win, text='Exit', command=master.destroy).grid(row =9, column= 2, padx = 1, pady = 1, ipadx= 1, ipady=1)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# Foreign Exchange Market (Farex):

def Forex():
    # TK stage:
    win = Toplevel()
    win.title("Forex Market")
    label = Label(win, text = 'Getting Foreign Exchange Data', font=('Courier 14 bold'))
    label.grid(row =0, columnspan= 3, padx = 2, pady = 2, ipadx= 1, ipady=1)
    
    # The Main Function For Getting Data:
    sym = StringVar()
    Time_Frame = StringVar()

    def InputData():
        Symbol = sym.get() + '=X'
        Symbol = Symbol.upper()
        TimeFrame = Time_Frame.get()
        data = yf.download(tickers= Symbol, start=Start_Date[0] , end=End_Date[0], interval=TimeFrame )
        data.to_csv(Symbol+'.csv')

    # Creating and Arranging the Input Column:

    # Symbol:
    SymbolLabel = Label(win, text = "Enter the Symbol", font = ('Courier 11 bold')).grid(row =1, columnspan= 3, padx = 2, pady = 2, ipadx= 1, ipady=1)
    SymbolEntry = Entry(win, textvariable= sym ,bg = "#E4EBF1", bd = 2,font = ('Courier 10 bold'), fg = "black", justify = 'center').grid(row =2, columnspan= 3, padx = 2, pady = 2, ipadx= 1, ipady=1)

    # Start and End Date:
    Start_Date = []
    def calendar_view():
        def GettingDate():
            start= cal.selection_get()
            Start_Date.append(start.strftime('%Y-%m-%d'))
            top.destroy()
        
        top = Toplevel(win)
        cal = Calendar(top, font="Arial 9", selectmode='day', year=2018, month=1, day=1)
        cal.grid()
        ttk.Button(top, text="ok", command=GettingDate).grid()
    ttk.Button(win, text='From', command=calendar_view).grid(row =4, column= 0, padx = 1, pady = 1, ipadx= 1, ipady=1)

    End_Date=[]
    def calendar_view_():
        def GettingEnd():
            End= cal.selection_get()
            End_Date.append(End.strftime('%Y-%m-%d'))
            top.destroy()

        top = Toplevel(win)
        cal = Calendar(top, font="Arial 9", selectmode='day')
        cal.grid()

        ttk.Button(top, text="ok", command=GettingEnd).grid()
    ttk.Button(win, text='To', command=calendar_view_).grid(row =4, column= 1, padx = 1, pady = 1, ipadx= 1, ipady=1)

    # Time_Frame Box:
    TimeFrames = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
    TimeFrameLabel = Label(win, text = "Time-Frame:", font = ('Consolas 10 bold')).grid(row =5, column= 0, padx = 1, pady = 1, ipadx= 1, ipady=1)
    TF = ttk.Combobox(win, values=TimeFrames, textvariable=Time_Frame, state = 'readonly').grid(row =5, column= 1, padx = 1, pady = 1, ipadx= 1, ipady=1)

    # Start Button:
    Button_ = ttk.Button(win, text = '.CSV Output', command=InputData).grid(row =7, column= 2, padx = 1, pady = 1, ipadx= 1, ipady=1)
    Another_Market = ttk.Button(win, text='Markets', command=win.destroy).grid(row =8, column= 2, padx = 1, pady = 1, ipadx= 1, ipady=1)
    Exit = ttk.Button(win, text='Exit', command=master.destroy).grid(row =9, column= 2, padx = 1, pady = 1, ipadx= 1, ipady=1)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# CryptoCurrency:

def Crypto():
    # TK stage:
    win = Toplevel()
    win.title("Crypto Market")
    label = Label(win, text = 'Getting Crypto-Currencies Data', font=('Courier 14 bold'))
    label.grid(row =0, columnspan= 3, padx = 2, pady = 2, ipadx= 1, ipady=1)
    
    # The Main Function For Getting Data:
    sym = StringVar()
    Per = StringVar()
    Time_Frame = StringVar()

    def InputData():
        Symbol = sym.get() + '-' + Per.get()
        Symbol = Symbol.upper()
        TimeFrame = Time_Frame.get()
        data = pdd.get_data_yahoo(Symbol, Start_Date[0], End_Date[0])
        data.to_csv(Symbol+'.csv')

    # Creating and Arranging the Input Column:

    # Symbol:
    SymbolLabel = Label(win, text = "Enter the Crypto Symbol", font = ('Courier 10 bold')).grid(row =1, column=0, padx = 2, pady = 2, ipadx= 1, ipady=1)
    SymbolEntry = Entry(win, textvariable= sym ,bg = "#E4EBF1", bd = 2,font = ('Courier 10 bold'), fg = "black", justify = 'center').grid(row =2, column=0, padx = 2, pady = 2, ipadx= 1, ipady=1)

    # Per:
    Pers = ['USD', 'EUR', 'USDT', 'ETH', 'BTC']
    PerLabel = Label(win, text = "/ Per", font = ('Consolas 10 bold')).grid(row =1, column=1, padx = 2, pady = 2, ipadx= 1, ipady=1)
    TF = ttk.Combobox(win, values=Pers, textvariable=Per, state = 'readonly').grid(row =2, column=1, padx = 2, pady = 2, ipadx= 1, ipady=1)

    # Start and End Date:
    Start_Date = []
    def calendar_view():
        def GettingDate():
            start= cal.selection_get()
            Start_Date.append(start.strftime('%Y-%m-%d'))
            top.destroy()
        
        top = Toplevel(win)
        cal = Calendar(top, font="Arial 9", selectmode='day', year=2018, month=1, day=1)
        cal.grid()
        ttk.Button(top, text="ok", command=GettingDate).grid()
    ttk.Button(win, text='From', command=calendar_view).grid(row =5, column= 0, padx = 1, pady = 1, ipadx= 1, ipady=1)

    End_Date=[]
    def calendar_view_():
        def GettingEnd():
            End= cal.selection_get()
            End_Date.append(End.strftime('%Y-%m-%d'))
            top.destroy()

        top = Toplevel(win)
        cal = Calendar(top, font="Arial 9", selectmode='day')
        cal.grid()

        ttk.Button(top, text="ok", command=GettingEnd).grid()
    ttk.Button(win, text='To', command=calendar_view_).grid(row =6, column= 0, padx = 1, pady = 1, ipadx= 1, ipady=1)

    
    # Start Button:
    Button_ = ttk.Button(win, text = '.CSV Output', command=InputData).grid(row =7, column= 1, padx = 1, pady = 1, ipadx= 1, ipady=1)
    Another_Market = ttk.Button(win, text='Markets', command=win.destroy).grid(row =7, column= 2, padx = 1, pady = 1, ipadx= 1, ipady=1)
    Exit = ttk.Button(win, text='Exit', command=master.destroy).grid(row =7, column= 3, padx = 1, pady = 1, ipadx= 1, ipady=1)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Go to the Second Page and Starting the Project:
Stock_Button = ttk.Button(master, text = 'Stocks', command = Stock).grid(row = 1, column=0, padx = 2, pady = 2, ipadx= 1, ipady=1)
Forex_Button = ttk.Button(master, text = 'ForEx', command = Forex).grid(row = 1, column=1, padx = 2, pady = 2, ipadx= 1, ipady=1)
Crypto_Button = ttk.Button(master, text = 'Crypto', command=Crypto).grid(row = 1, column=2, padx = 2, pady = 2, ipadx= 1, ipady=1)
Exit_Button = ttk.Button(master, text = 'Exit',command = master.destroy).grid(row = 2, columnspan=3 , padx = 2, pady = 2, ipadx= 1, ipady=1)

master.mainloop()
