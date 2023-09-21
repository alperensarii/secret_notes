from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def save_and_encrypt_notes():
    title = title_entry.get()
    message = secret_text.get("1.0",END)
    master_secret = master_entry.get()

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all info")
    else:
        #encryption
        try:
            with open("mysecret.txt","a") as data_file:
                data_file.write(f"\n{title}\n{message}")
        except FileNotFoundError:
            with open("mysecret.txt","a") as data_file:
                data_file.write(f"\n{title}\n{message}")
        finally:
            title_entry.delete(0,END)
            master_entry.delete(0,END)
            secret_text.delete("1.0",END)

window = Tk()
window.title("Secret Notes")
window.geometry("400x750")
window.config(padx=20, pady=30)
image = Image.open("top-secret-removebg-preview.png")

img = image.resize((120,120))

my_img = ImageTk.PhotoImage(img)

label = Label(window, image=my_img)
label.pack()

title_label = Label(text="Enter your title")
title_label.config(pady=8,padx=20)
title_label.pack()

title_entry = Entry(width=25)
title_entry.pack()

secret_label = Label(text="Enter your secret")
secret_label.config(padx=8,pady=20)
secret_label.pack()

secret_text = Text(width=40, height=20)
secret_text.pack()

key_label = Label(text="Enter master key")
key_label.pack()

master_entry = Entry()
master_entry.config(width=25)
master_entry.pack()

save_button = Button(text="Save & Encrypt",command=save_and_encrypt_notes)
save_button.pack()

decrypt_button = Button(text="Decrypt")
decrypt_button.pack()


window.mainloop()
