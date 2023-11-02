# Синхронный Код (окно зависает тк ожидает завершения продолжительного по времени "действия")
import tkinter as tk
from tkinter import ttk
from time import sleep

root = tk.Tk()
root.geometry('300x300+150+150')

def sleep_func():
    sleep(10)
    lab['text'] = 'TEXT after sleep'

button = ttk.Button(root, text='Run', command=sleep_func)
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

lab = ttk.Label(root, text='TEXT before push')
lab.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

root.mainloop()