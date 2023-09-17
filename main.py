import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk 

janela = ctk.CTk()

class Application():
    def __init__(self):
        self.janela=janela
        self.tema()
        self.tela()
        self.tela_de_login()
        janela.mainloop()


    def tema(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

    def tela(self):
        janela.geometry("800x500")
        janela.resizable(False, False)
        janela.title("Sistema de Login") 

    def tela_de_login(self):
        image = ctk.CTkImage(Image.open("imagem4.png"),size=(400,420)) 
        image_label = ctk.CTkLabel(janela, text="", image=image).place(x=0, y=35)

        # Frame
        login_frame = ctk.CTkFrame(janela, width=380, height=400, border_width=1, border_color="#B0C4DE")
        login_frame.place(x=400, y=50)

        # Frame Widgets
        label = ctk.CTkLabel(login_frame, text="Sistema de Login")
        label.place(x=65, y=35)
        label.configure(font=("Lato", 30))

        # Área do login do cliente
        entry_usuario = ctk.CTkEntry(login_frame, placeholder_text="Usuário", width=300).place(x=40, y=115)
        entry_usuario = ctk.CTkLabel(login_frame, text_color="#4169E1", text="*O campo usuário é obrigatório*").place(x=40, y=145)

        entry_senha = ctk.CTkEntry(login_frame, placeholder_text="Senha", width=300, show="*").place(x=40, y=185)
        entry_senha = ctk.CTkLabel(login_frame, text_color="#4169E1", text="*O campo senha é obrigatório*").place(x=40, y=215)

        check_box = ctk.CTkCheckBox(login_frame, text="Lembrar a senha").place(x=40, y=255)

        login_button = ctk.CTkButton(login_frame, text="Login", width=300).place(x=40, y=300)

        register_span = ctk.CTkLabel(login_frame, text="Caso não tenha conta.").place(x=50, y=350)
        register_button = ctk.CTkButton(login_frame, text="Cadastre-se", width=150, fg_color="#228B22", hover_color="#006400").place(x=190, y=350)


Application()
