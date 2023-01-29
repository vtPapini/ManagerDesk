from tkinter import *   # Tk, Frame, Button, Label, Place, Entry, Scrollbar
from tkinter import ttk
from tkcalendar import Calendar
from Funcs1 import Funcs
from CRUDs import CRUD
import Login_sistem as log



user_status = log.LOGIN_()  


root = Tk()
status = ''
font_=('Arial',10)

class Interface_funcs(CRUD):
    def open_calendar(self):
        self.calendar1 = Calendar(self.frame_1, date_pattern='y-mm-dd')
        self.calendar1.place(relx=0.35, rely=0.6)

        self.bt_Date_select = Button(
            self.frame_1,
            text='Select DATE',
            border=5,
            font=("Helvetica",15),
            fg='Red',
            command=self.select_Date,
        )
        self.bt_Date_select.place(
            relx=0.35, rely=0.55, relwidth=0.6, relheight=0.05
        )
    
    def select_Date(self):
        date_choosed = self.calendar1.get_date()
        self.calendar1.destroy()
        self.calendar_entry.delete(0, END)
        self.calendar_entry.insert(END, date_choosed)
        self.bt_Date_select.destroy()

    def select_user_BUTTON(self):
        try:
            self.user_status = [self.select_user(self.phone_entry.get())]
        except:
            self.user_status = []

class Application(Interface_funcs,Funcs,CRUD):
    
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
        
############################### BUTTONS

        ######################## New User Button#######################
        
        self.bt_new_user = Button(self.frame_1, text='New User',border=2,font=font_, fg='Blue')
        self.bt_new_user.place(
            relx=0.525, rely=0.085, relwidth=0.425, relheight=0.05
        )

        ######################## Delete User Button#######################
        
        self.bt_new_user = Button(self.frame_1, text='Delete User',border=2,font=font_, fg='Red')
        self.bt_new_user.place(
            relx=0.525, rely=0.145, relwidth=0.425, relheight=0.05
        )

        ######################## Select User Button #######################
        
        self.user_status = []
        self.phone_entry =  Entry(self.frame_1)
        self.phone_entry.place(
                               relx=0.05, rely=0.09, relwidth=0.425
                               )
        
        self.bt_select_user = Button(self.frame_1, text='Select User',border=2,font=font_, fg='#0ec268',command=self.select_user_BUTTON())
        self.bt_select_user.place(
            relx=0.525, rely=0.025, relwidth=0.425, relheight=0.05
        )

        ######################## Upload Wallet Button #######################
        
        self.bt_genarate = Button(self.frame_1, text='Upload Wallet',border=5,font=('Arial',13), fg='#0ec268',command=self.wallet_df_generate)
        self.bt_genarate.place(
            relx=0.05, rely=0.87, relwidth=0.425, relheight=0.05
        )
        
        ######################## Export Button #######################
        
        self.bt_export_csv = Button(self.frame_1, text='Export to CSV')
        self.bt_export_csv.place(
            relx=0.525, rely=0.87, relwidth=0.425, relheight=0.05
        )

        ######################## Destroy Button #######################
        
        self.bt_destroy = Button(
            self.frame_1, font=(10), text='DESTROY', border=5, fg='#8B0000'
        )
        self.bt_destroy.place(
            relx=0.05, rely=0.94, relwidth=0.90, relheight=0.04
        )
 
        ######################## Create Wallet Button #######################
        
        self.bt_insert_W = Button(self.frame_1, text='Create Wallet')
        self.bt_insert_W.place(
            relx=0.05, rely=0.47, relwidth=0.425, relheight=0.05
        )
        
        ######################## Delete Wallet Button #######################
        
        self.bt_Delete_W = Button(self.frame_1, text='Delete Wallet')
        self.bt_Delete_W.place(
            relx=0.525, rely=0.47, relwidth=0.425, relheight=0.05
        )
        
        ######################## Calendar Date Select Button #######################
       
        self.bt_calendar_select = Button(
            self.frame_1, text='Select Date', command=self.open_calendar, fg='Red'
        )
        self.bt_calendar_select.place(
            relx=0.525, rely=0.8, relwidth=0.425, relheight=0.04
        )

        self.calendar_entry = Entry(self.frame_1)
        self.calendar_entry.place(
            relx=0.05, rely=0.8, relwidth=0.425, relheight=0.04
        )
############################### LABELS

        ####################### Label Insert the Phone number user #######################
        
        self.lb_Insert_phone = Label(self.frame_1, text="Insert the User's Phone number",font=font_)
        self.lb_Insert_phone.place(relx=0.05, rely=0.025)

        ####################### Label Insert the Stock codes #######################
        
        self.lb_stockCodes = Label(
                                    self.frame_1, text='Insert the stock codes separating with "/"'
                                    )
        self.lb_stockCodes.place(relx=0.05, rely=0.2)

        self.stockCodes_entry = Entry(self.frame_1)
        self.stockCodes_entry.place(
            relx=0.05, rely=0.25, relwidth=0.90, relheight=0.04
        )

        #######################Label Insert the Start Date#######################
        
        self.lb_start_date = Label(
            self.frame_1, text='Choose the Start Date (YYYY-MM-DD) :'
        )
        self.lb_start_date.place(relx=0.05, rely=0.77)

        #######################Label Insert the Weights#######################
        
        self.lb_insert_w = Label(
                                self.frame_1,
                                text='Insert the weights separating with "/" \n(On the same order of the stocks) Ex.: 0.25/0.25/0.25/0.25',
                                justify='left'
                                )
        self.lb_insert_w.place(relx=0.05, rely=0.3)

        self.weigth_entry = Entry(self.frame_1)
        self.weigth_entry.place(relx=0.05, rely=0.36, relwidth=0.90, relheight=0.04)

        ####################### Label Insert the Wallet Name #######################
        
        self.lb_insert_wallet_name = Label(
            self.frame_1,
            text='Insert the Wallet Name to select :',
            justify='right')
        self.lb_insert_wallet_name.place(relx=0.05, rely=0.43)

        self.wallet_name_entry = Entry(self.frame_1)
        self.wallet_name_entry.place(relx=0.5,rely=0.43,relwidth=0.45)
        
        ####################### Label STATUS #######################
        
        self.lb_status = Label(
                                self.frame_1,
                                text='[ STATUS : {} ]'.format(status),
                                justify='center',fg='#0af002',font=("Helvetica", 20)
                                )
        self.lb_status.place(relx=0.05, rely=0.71)
        
        ###################### Label User stats #######################

        self.lb_status = Label(
                                self.frame_1,
                                text='User on: {}'.format(user_status),
                                justify='left',fg='Blue',font=("Helvetica", 15)
                                )
        self.lb_status.place(relx=0.05, rely=0.15)
        

        ####################### Wallet List #######################
        
        tree_head_wallets = ['ID','Wallet Name']

        self.list_stocks = ttk.Treeview(self.frame_1,selectmode='extended', height=3, columns=tree_head_wallets,show='headings')
        self.list_stocks.place(relx=0.05, rely=0.55, relwidth=0.90, relheight=0.15)

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
            relx=0.96, rely=0.55, relwidth=0.04, relheight=0.15
        )

    def widgets_frame2(self):
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
                
Application()
