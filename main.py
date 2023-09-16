import customtkinter as ctk

# Estilização da nossa janela
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

janela = ctk.CTk()
janela.geometry("700x400")
janela.resizable(False, False)

def clique():
    print('Fazer Login')


title = ctk.CTkLabel(janela, text="Sistema de login")
title.pack(padx=10, pady=10)

email = ctk.CTkEntry(janela, placeholder_text="E-mail")
email.pack(padx=10, pady=10)

senha = ctk.CTkEntry(janela, placeholder_text="Senha", show="*")
senha.pack(padx=10, pady=10)

check = ctk.CTkCheckBox(janela, text="Lembre sua senha")
check.pack()

# Janela do botão com comando pra função clique
botao = ctk.CTkButton(janela, text="Login", command="clique")
botao.pack(padx=10, pady=10)



janela.mainloop()