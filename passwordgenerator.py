import customtkinter
import random
import pyperclip
from tkinter import *
from tkinter.ttk import *


root = customtkinter.CTk()
root.title("Random Password Generator")
root.geometry("230x315")
root.config(bg='gray20')
var = IntVar()
var1 = IntVar()


def weak():
	entry.delete(0, END)
	length = var1.get()
	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password = ""
	if var.get() == 1:
		for i in range(0, length):
			password = password + random.choice(lower)
		return password

	elif var.get() == 0:
		for i in range(0, length):
			password = password + random.choice(upper)
		return password

	elif var.get() == 3:
		for i in range(0, length):
			password = password + random.choice(digits)
		return password
	else:
		print("Please choose an option")


def generate():
	password1 = weak()
	entry.insert(10, password1)


def copy1():
	random_password = entry.get()
	pyperclip.copy(random_password)


c_label = Label(root, text="Password Length")
c_label.grid(pady=5)

combo = Combobox(root, textvariable=var1)
combo['values'] = (6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(pady=5)

radio_weak = Radiobutton(root, text="Weak", variable=var, value=1)
radio_weak.grid(pady=5)

radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(pady=5)

radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(pady=5)

generate_button = customtkinter.CTkButton(root, text_color="#050505", text="Generate", command=generate, fg_color="#66cd00", hover_color="#458b00", bg_color="#09112e", cursor="hand2", width=48)
generate_button.grid(pady=5)

Random_password = Label(root, text="Password")
Random_password.grid(pady=5)
entry = Entry(root)
entry.grid(pady=5)

copy_button = customtkinter.CTkButton(root, text_color="#050505", text="Copy", command=copy1, fg_color="#eee8cd", hover_color="#a9a9a9", width=48)
copy_button.grid(pady=5)

root.mainloop()
