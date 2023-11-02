# МультиПроцессорность (для обработки ресурсо-емких действий)
import tkinter as tk
from tkinter import ttk
from time import sleep
import multiprocessing as mp

root = tk.Tk()
root.geometry('300x300+150+150')

def check_process(proc):
    if not proc.is_alive():
        lab['text'] = int(lab['text']) + 10
    root.after(2000, check_process, proc)

def process():
    sleep(10)

def new_process():
    proc = mp.Process(target=process)
    proc.start()
    check_process(proc)


if __name__ == '__main__':

    button = ttk.Button(root, text='Run', command=new_process)
    button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    lab = ttk.Label(root, text='0', font=5)
    lab.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    root.mainloop()



