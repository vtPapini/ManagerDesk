import sqlite3 as lite

class CRUD:
    def creat_user(self,phone:int,name:str):
        
        con = lite.connect('DB_\DB_.db')
        cur = con.cursor()

        cur.execute(
                    """INSERT INTO TB_USER (Name,Phone_num) 
                    VALUES ('{}',{})""".format(name,phone)
                    )

        con.commit()
        con.close()


    def creat_wallet(self,phone:int,wallet_name:str,):
        con = lite.connect('DB_\DB_.db')
        cur = con.cursor()

        cur.execute(
                    """INSERT INTO TB_WALLET (Phone_num,Wallet_name) 
                    VALUES ({},'{}');""".format(phone,wallet_name)
                    )

        con.commit()
        con.close()

    def add_stocks(self,wallet_ID:int,stocks_code:str,weights:str):
        code_stock = stocks_code.split('/')
        code_weight = weights.split('/')
        
        con = lite.connect('DB_\DB_.db')
        cur = con.cursor()

        for index1,index2 in zip(code_stock,code_weight) :
            cur.execute(
                        """INSERT INTO TB_CODE (WALLET_ID,STOCK_CODE,WEIGHT) 
                    VALUES ({},'{}',{});""".format(wallet_ID,index1,float(index2))
                        )

        con.commit()
        con.close()

    def select_(self,target_table:str,target_colunm:str='*',wallet_id=int):
        info = []
        con = lite.connect('DB_\DB_.db')
        cur = con.cursor()
        query ="""SELECT {} FROM {} WHERE WALLET_ID = {};""".format(target_colunm,target_table,wallet_id)

        try:
            cur.execute(query)
            tables = cur.fetchall()
            for indx in tables:
                info.append(indx)
            
            con.commit()
            con.close()
            return info
        except:
            return 'ERROR SELECT'

    def select_user(Phone_num):
        con = lite.connect('DB_\DB_.db')
        cur = con.cursor()
        query ="""SELECT * FROM TB_USER WHERE PHONE_NUM = {};""".format(Phone_num)

        cur.execute(query)
        tables = cur.fetchall()
        con.commit()
        con.close()
        print(tables)
        
#creat_user(13,'Victor')
#creat_wallet(13,'Fundo Imobiliário')
#add_stocks(5,'fff/ççç','0.50/0.50')
