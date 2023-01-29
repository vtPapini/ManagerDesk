import tkinter as tk
import sqlite3




class LOGIN_():
     def __init__(self):
        
        self.user_ = []

        # Criação da janela principal
        root_log = tk.Tk()
        root_log.title("Login")

        # Criação da tabela no banco de dados
        conn = sqlite3.connect('Login_sistem\DB_Login.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
        conn.commit()

        # Função para verificar as informações de login
        def login():
            username = entry_username.get()
            password = entry_password.get()
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            if cursor.fetchone() is not None:
                label_result.config(text="Login bem-sucedido!", fg="green")
###############################################
                root_log.destroy()
                self.user_ = username
###############################################
            else:
                label_result.config(text="Usuário ou senha inválidos!", fg="red")
            entry_username.delete(0, tk.END)
            entry_password.delete(0, tk.END)

        # Função para adicionar um novo usuário
        def add_user():
            new_username = entry_new_username.get()
            new_password = entry_new_password.get()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_username, new_password))
            conn.commit()
            entry_new_username.delete(0, tk.END)
            entry_new_password.delete(0, tk.END)
            label_result.config(text="Usuário criado com sucesso!", fg="green")

        # Criação de labels e entry para username e password
        label_username = tk.Label(root_log, text="Username:")
        label_username.grid(row=0, column=0)
        entry_username = tk.Entry(root_log)
        entry_username.grid(row=0, column=1)

        label_password = tk.Label(root_log, text="Password:")
        label_password.grid(row=1, column=0)
        entry_password = tk.Entry(root_log, show="*")
        entry_password.grid(row=1, column=1)

        # Criação do botão de login
        button_login = tk.Button(root_log, text="Login", command=login)
        button_login.grid(row=2, column=0)

        # Criação de labels e entry para novo usuário e nova senha
        label_new_username = tk.Label(root_log, text="Novo usuário:")
        label_new_username.grid(row=3, column=0)
        entry_new_username = tk.Entry(root_log)
        entry_new_username.grid(row=3, column=1)

        label_new_password = tk.Label(root_log, text="Nova senha:")
        label_new_password.grid(row=4, column=0)
        entry_new_password = tk.Entry(root_log, show="*")
        entry_new_password.grid(row=4, column=1)

        # Criação do botão para adicionar um novo usuário
        button_add_user = tk.Button(root_log, text="Criar Usuário", command=add_user)
        button_add_user.grid(row=5, column=0)

        # Criação do label para mostrar o resultado do login ou criação de usuário
        label_result = tk.Label(root_log)
        label_result.grid(row=6, column=1)

        root_log.mainloop()
