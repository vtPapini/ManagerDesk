import sqlite3 as lite


def creat_user(phone:int,name:str):
    
    con = lite.connect('DB_\DB_.db')
    cur = con.cursor()

    cur.execute(
                """INSERT INTO TB_USER (Name,Phone_num) 
                VALUES ('{}',{})""".format(name,phone)
                )

    con.commit()
    con.close()
    
def creat_wallet(phone:int,wallet_name:str,):
    con = lite.connect('DB_\DB_.db')
    cur = con.cursor()

    cur.execute(
                """INSERT INTO TB_WALLET (Phone_num,Wallet_name) 
                VALUES ({},'{}');""".format(phone,wallet_name)
                )

    con.commit()
    con.close()

def add_stocks(wallet_name:str,phone:int,stocks_code:str):
    codes = stocks_code.split('/')
    print(codes)
    con = lite.connect('DB_\DB_.db')
    cur = con.cursor()

    for index in codes:
        cur.execute(
                    """UPDATE TB_WALLET SET STOCK_CODE = '{}' 
                    WHERE PHONE_NUM = {} 
                    AND Wallet_name = '{}';""".format(index,phone,wallet_name)
                    )
    con.commit()
    con.close()



#creat_user(13,'Victor')
creat_wallet(13,'Fundo Varejo')
#add_stocks('Fundo imobiliário',13,'yyyy/KKKK')
