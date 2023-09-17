import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk 

# Estilização da nossa janela
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

janela = ctk.CTk()
janela.geometry("800x500")
janela.resizable(False, False)
janela.title("Sistema de Login")

def clique():
    print('Fazer Login')    

# Tratamento da Imagem Central
image = Image.open("imagem4.png") 
image = ImageTk.PhotoImage(image)

image_label = tk.Label(janela, image=image)
image_label.place(x=-100, y=0)

# Frame
frame = ctk.CTkFrame(janela, width=380, height=500, border_width=2)
frame.pack(side="right")

# Frame Widgets
label = ctk.CTkLabel(frame, text="Sistema de Login")
label.place(x=65, y=35)
label.configure(font=("Lato", 30))

# Área do login do cliente
entry1 = ctk.CTkEntry(frame, placeholder_text="Usuário", width=300).place(x=40, y=115)
label1 = ctk.CTkLabel(frame, text_color="#3025D4", text="*O campo usuário é obrigatório*").place(x=40, y=145)

entry2 = ctk.CTkEntry(frame, placeholder_text="Senha", width=300).place(x=40, y=185)
label2 = ctk.CTkLabel(frame, text_color="#3025D4", text="*O campo usuário é obrigatório*").place(x=40, y=215)

check_box = ctk.CTkCheckBox(frame, text="Lembrar a senha").place(x=40, y=255)

button = ctk.CTkButton(frame, text="LOGIN", width=300).place(x=40, y=300)


janela.mainloop()
