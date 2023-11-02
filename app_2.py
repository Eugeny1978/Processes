# Мульти-Поточность (для обработки НЕ ресурсо-емких но продолжительных действий)
import tkinter as tk
from tkinter import ttk
from time import sleep
from threading import Thread

root = tk.Tk()
root.geometry('300x300+150+150')

def thread_sleep():
    sleep(10)
    lab['text'] = int(lab['text']) + 10

def new_thread():
    th = Thread(target=thread_sleep)
    th.start()

if __name__ == '__main__':

    button = ttk.Button(root, text='Run', command=new_thread)
    button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    lab = ttk.Label(root, text='0', font=5)
    lab.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    root.mainloop()