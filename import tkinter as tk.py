import tkinter as tk
from tkinter import *
import Library_Mods as lb
from Library_Mods import *
from testGui import Reports

ws = Tk()
ws.title('PythonGuides')
ws.geometry(f'{ws.winfo_screenwidth()}x{ws.winfo_screenheight()}')
ws.config(bg='#84BF04')
ws.grid_rowconfigure(0, weight=1)
ws.grid_columnconfigure(0, weight=1)
frame = tk.Frame(ws)
frame.grid(row=0, column=0, sticky='news', pady=20, padx=20)




message = Report().bks_late()
my_scrollbar = tk.Scrollbar(frame)
my_scrollbar.pack(side=RIGHT, fill=Y)
text_box = Text(
    frame,yscrollcommand=my_scrollbar.set)
text_box.pack(expand=True, fill='both')
text_box.insert('end', message)
text_box.config(state='disabled')
my_scrollbar.config(command=text_box.yview)

ws.mainloop()