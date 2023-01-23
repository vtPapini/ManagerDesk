from tkinter import *   # Tk, Frame, Button, Label, Place, Entry, Scrollbar
from tkinter import ttk
from tkcalendar import Calendar
from Funcs1 import Funcs
from DB_.CRUDs import *

root = Tk()

class Interface_funcs:
    def open_calendar(self):
        self.calendar1 = Calendar(self.frame_1, date_pattern='y-mm-dd')
        self.calendar1.place(relx=0.35, rely=0.32)

        self.bt_Date_select = Button(
            self.frame_1,
            text='Select',
            border=5,
            font=(9),
            fg='Green',
            command=self.select_Date,
        )
        self.bt_Date_select.place(
            relx=0.05, rely=0.42, relwidth=0.3, relheight=0.05
        )

    def select_Date(self):
        date_choosed = self.calendar1.get_date()
        self.calendar1.destroy()
        self.calendar_entry.delete(0, END)
        self.calendar_entry.insert(END, date_choosed)
        self.bt_Date_select.destroy()

class Application(Interface_funcs,Funcs):
    def __init__(self):
        self.root = root
        self.screen()
        self.screen_frames()
        self.widgets_frame1()
        self.widgets_frame2()
        root.mainloop()

    def screen(self):
        self.root.title('Manager Desk')
        self.root.configure(background='#B0C4DE')
        self.root.geometry('900x700')
        self.root.minsize(width=900, height=700)

    def screen_frames(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.46, relheight=0.96)
        self.frame_2 = Frame(self.root)
        self.frame_2.place(relx=0.50, rely=0.02, relwidth=0.46, relheight=0.96)

    def widgets_frame1(self):
        #######################Label Insert the Stock codes#######################
        self.lb_stockCodes = Label(
            self.frame_1, text='Insert the stock codes separating with ","'
        )
        self.lb_stockCodes.place(relx=0.05, rely=0.05)

        self.stockCodes_entry = Text(self.frame_1)
        self.stockCodes_entry.place(
            relx=0.05, rely=0.1, relwidth=0.90, relheight=0.15
        )

        ########################Genarate Button#######################
        self.bt_genarate = Button(self.frame_1, text='Genarate',command=self.wallet_df_generate)
        self.bt_genarate.place(
            relx=0.05, rely=0.26, relwidth=0.425, relheight=0.05
        )
        
        ########################Export Button#######################
        self.bt_export_csv = Button(self.frame_1, text='Export to CSV')
        self.bt_export_csv.place(
            relx=0.525, rely=0.26, relwidth=0.425, relheight=0.05
        )

        ########################Destroy Button#######################
        self.bt_destroy = Button(
            self.frame_1, font=(10), text='DESTROY', border=5, fg='#8B0000'
        )
        self.bt_destroy.place(
            relx=0.05, rely=0.42, relwidth=0.90, relheight=0.04
        )
 
        ########################Insert Weigths Button#######################
        self.bt_insert_W = Button(self.frame_1, text='Insert')
        self.bt_insert_W.place(
            relx=0.05, rely=0.59, relwidth=0.425, relheight=0.05
        )
        
        ########################Delete Weigths Button#######################
        self.bt_Delete_W = Button(self.frame_1, text='Delete Weights')
        self.bt_Delete_W.place(
            relx=0.525, rely=0.59, relwidth=0.425, relheight=0.05
        )
        
        ########################Calendar Date Select Button#######################
        self.bt_calendar_select = Button(
            self.frame_1, text='Select Date', command=self.open_calendar
        )
        self.bt_calendar_select.place(
            relx=0.525, rely=0.365, relwidth=0.425, relheight=0.04
        )

        self.calendar_entry = Entry(self.frame_1)
        self.calendar_entry.place(
            relx=0.05, rely=0.365, relwidth=0.425, relheight=0.04
        )

        #######################Label Insert the Start Date#######################
        self.lb_start_date = Label(
            self.frame_1, text='Choose the Start Date (YYYY-MM-DD) :'
        )
        self.lb_start_date.place(relx=0.05, rely=0.33)

        #######################Label Insert the Weights#######################
        self.lb_insert_w = Label(
            self.frame_1,
            text='Insert the weights separating with "/" \n(On the same order of the stocks) Ex.: 0.25/0.25/0.50',
            justify='left'
        )
        self.lb_insert_w.place(relx=0.05, rely=0.49)

        self.weigth_entry = Entry(self.frame_1)
        self.weigth_entry.place(relx=0.05, rely=0.55, relwidth=0.90)

        ####################### Weights List #######################
        
        tree_head_stocks = ['ID','Stock','Weight']

        self.weight_list = ttk.Treeview(self.frame_2,selectmode='extended', height=3, columns=tree_head_stocks,show='headings')
        self.weight_list.place( relx=0.05, rely=0.1, relwidth=0.90, relheight=0.85)

        h=[1,40,60]
        n=0
        for col in tree_head_stocks:
            self.weight_list.heading(col, text=col, anchor=CENTER)
            # adjust the column's width to the header string
            self.weight_list.column(col, width=h[n],anchor="center")
            n+=1   
                
        #scrool bars
        self.scroolV_Stock_List = Scrollbar(self.frame_2, orient='vertical')
        self.scroolH_Stock_List = Scrollbar(self.frame_2, orient='horizontal')
        self.weight_list.configure( yscrollcommand=self.scroolV_Stock_List.set,
                                    xscrollcommand=self.scroolH_Stock_List.set)
        self.scroolV_Stock_List.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.scroolH_Stock_List.place(relx=0.05, rely=0.95, relwidth=0.90, relheight=0.04)

    def widgets_frame2(self):
        ####################### Wallet List #######################
        
        tree_head_wallets = ['ID','Wallet Name']

        self.list_stocks = ttk.Treeview(self.frame_1,selectmode='extended', height=3, columns=tree_head_wallets,show='headings')
        self.list_stocks.place(relx=0.05, rely=0.65, relwidth=0.90, relheight=0.3)

        h=[30,270]
        n=0
        for col in tree_head_wallets:
            self.list_stocks.heading(col, text=col, anchor=CENTER)
            # adjust the column's width to the header string
            self.list_stocks.column(col, width=h[n],anchor="center")
            n+=1   
             
        #scrool bar
        self.scroolV_Wallet_List = Scrollbar(self.frame_1, orient='vertical')
        self.list_stocks.configure(yscrollcommand=self.scroolV_Wallet_List.set)
        self.scroolV_Wallet_List.place(
            relx=0.96, rely=0.65, relwidth=0.04, relheight=0.3
        )
                
        







Application()
