from tkinter import *

window = Tk()

window.geometry("800x600")
window.title("Gerar faturamento em python usando tkinter")

username_var = StringVar()
password_var = StringVar()

def Admin_login():
    title_label = Label(window, text = "Faturamento", font="Arial 30", fg="green")
    title_label.grid (row= 0, column= 1, columnspan=3, pady=(10, 0))
    
    add_button = Button(window, text= "Adicionar itens", width=15, height=2)
    add_button.grid(row=1, column=0, padx=(10, 0), pady=(10,0))
    
    login_button_logout = Button(window, text="Sair", width= 15, heigth=2)
    login_button_logout.grid(row=1, column=4, pady=(10, 0))
    
    login_label = Label(window, text = "Administrador login:", font="Arial 30")
    login_label.grid(row= 1, column= 2, padx= (50, 0),columnspan=2, pady= 10)
    
    username_label = Label(window, text= "Nome:", font="Arial 10")
    username_label.grid(row= 2, column=2,  padx=20, pady=5)
    
    password_label = Label(window, text = "Senha:", font="Arial 10")
    password_label.grid(row= 3, column=2, padx=20, pady=5)
    
    username_entry = Entry(window, textvariable= username_var)
    username_entry.grid(row= 2, column= 3, padx=20, pady=5)
    
    password_entry = Entry(window, textvariable= password_var, show= "*")
    password_entry.grid(row= 3, column= 3, padx=20, pady=5)
    
    login_button = Button(window, text= "Login", width= 20, height= 2)
    login_button.grid(row=4, column=3, columnspan=2, padx=20, pady=5)
    
    
    
def main_window():
    title_label = Label(window, text = "Faturamento", font="Arial 30", fg="green")
    title_label.grid (row= 0, column= 3, padx=(30, 0) ,pady=(10, 0))
    
    login_label = Label(window, text = "Administrador login:", font="Arial 30")
    login_label.grid(row= 1, column= 2, padx= (50, 0),columnspan=2, pady= 10)
    
    username_label = Label(window, text= "Nome:", font="Arial 10")
    username_label.grid(row= 2, column=2,  padx=20, pady=5)
    
    password_label = Label(window, text = "Senha:", font="Arial 10")
    password_label.grid(row= 3, column=2, padx=20, pady=5)
    
    username_entry = Entry(window, textvariable= username_var)
    username_entry.grid(row= 2, column= 3, padx=20, pady=5)
    
    password_entry = Entry(window, textvariable= password_var, show= "*")
    password_entry.grid(row= 3, column= 3, padx=20, pady=5)
    
    login_button = Button(window, text= "Login", width= 20, height= 2)
    login_button.grid(row=4, column=3, columnspan=2, padx=20, pady=5)

Admin_login()
window.mainloop()