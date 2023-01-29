"""Teste montando frame work"""
import yfinance as yf
import pandas as pd
from tkinter import *
from tkinter import ttk
from CRUDs import *

class Funcs:
    def wallet_df_generate(self):
        ###Verify value of calendar entry
        if len(self.calendar_entry.get().split('-')) != 3:
            return
        else:
            pass
        ###Importing datas 
            self.codes = self.stockCodes_entry.get("1.0",'end-1c')
            self.codes = self.codes.split(',')
            

            self.codes_df = pd.DataFrame()
            for index in self.codes: #self.calendar_entry.get()
                self.codes_df[index] = yf.download(index, start =self.calendar_entry.get())['Close']

        ###List Columns            
            col_number = ''
            colnumber = 1
            for num in range(0,len(self.codes_df.columns)):
                col =',col{}'.format(colnumber)
                col_number = col_number + col
                colnumber += 1
            columns_number = (col_number.split(','))
            columns_number.remove("")
            columns_number = tuple(columns_number)
            
            self.list_stocks = ttk.Treeview(self.frame_2, height=3, columns=columns_number)
            
            #rename the columns
            head_num = 1
            for name in self.codes_df.columns:
                self.list_stocks.heading('#{}'.format(head_num),text='{}'.format(name))
                head_num += 1

            for i in range(len(self.codes_df.index)):
                num = 0
                print(self.codes_df.loc[self.codes_df.index[num]].values)
                price_values = self.codes_df.loc[self.codes_df.index[num]].values
                self.list_stocks.insert(parent="",index='end',values=price_values)
                num = num + 1
                
                    

            self.list_stocks.heading('#0', text=self.codes_df.index.name)
            self.list_stocks.column('#0', minwidth=1)
            self.list_stocks.place(relx=0.05, rely=0.1, relwidth=0.90, relheight=0.85)

            
            #vertical scrool
            self.scroolList_vertical = Scrollbar(self.frame_2, orient='vertical')
            self.list_stocks.configure(yscrollcommand=self.scroolList_vertical.set)
            self.scroolList_vertical.place(
                relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85
            )
            #horizontal scrool
            self.scroolList_horizontal = Scrollbar(self.frame_2, orient='horizontal')
            self.list_stocks.configure(xscrollcommand=self.scroolList_horizontal.set)
            self.scroolList_horizontal.place(
                relx=0.05, rely=0.95, relwidth=0.90, relheight=0.04
            )
   


#ABEV3.SA,ODPV3.SA,VIVT3.SA,PETR3.SA,BBAS3.SA,BOVA11.SA,WEGE3.SA
                #self.listCli.insert('','end', values=data)
#BOVA.SA,MGLU3.SA
