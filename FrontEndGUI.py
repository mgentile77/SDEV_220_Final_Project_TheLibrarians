import tkinter as tk
from tkinter import *
from tkinter import ttk
import Library_Mods as lb
from Library_Mods import *
from tkinter import messagebox 

class MenuMain(tk.Tk):#Marshall wrote this code block
    def __init__(self):
        super().__init__()
        width = 380
        height = 205
        screen_wid = self.winfo_screenwidth()
        screen_hei = self.winfo_screenheight()
        x = (screen_wid/2) - (width/2)
        y = (screen_hei/2) - (height/2)
        self.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.style = ttk.Style()
        self.style2 = ttk.Style()
        self.style.configure('nbutton.TButton', background = '#e1d8b9', width = 18, height = 34)
        self.style2.configure('n2button.TButton', background = '#e1d8b9')
        self.configure(bg = '#e1d8b9')
        self.title("Public Library")
        self.set_up()
        
    def set_up(self):
        
        self.frame_start = tk.Frame(bg = '#e1d8b9')#Frame for start welcome and instructions
        self.frame_start.pack(padx = (0,10))
        tk.Label(self.frame_start, text = "Thank You for Visiting Your",
                  bg = '#e1d8b9', font = ('Baskerville Old Face', '12', 'bold')).grid(row = 0, column = 0, columnspan = 2)
        tk.Label(self.frame_start, text = "Anderson Public Library",
                  bg = '#e1d8b9', font = ('Baskerville Old Face', '24', 'bold')).grid(row = 1, column = 0, columnspan = 2)
        tk.Label(self.frame_start, text = "What Would You Like To Access",
                  bg = '#e1d8b9', font = ('Baskerville Old Face', '12', 'bold')).grid(row = 2, column = 0, columnspan = 2)
        
        self.but_horde = ttk.Button(self.frame_start, style = 'nbutton.TButton', text = "Reports", command = self.report)
        self.but_horde.grid(row = 3, column = 0, sticky = 'nsew')
        
        self.but_char = ttk.Button(self.frame_start, style = 'nbutton.TButton',text = "Catalog", command = self.catalog)
        self.but_char.grid(row = 3, column = 1, sticky = 'nsew')

        self.but_member = ttk.Button(self.frame_start, style='nbutton.TButton', text="Members", command=self.members_window)
        self.but_member.grid(row=4, column=0, columnspan = 2)

        ttk.Button(self.frame_start, text = 'Exit', style = 'n2button.TButton',command = lambda : exit()).grid(row = 5, column = 0, columnspan = 2)
    
    def report(self):#opens report window
        self.show_reports()
    
    def show_reports(self):
        main_geometry = self.geometry()
        # Create an instance of Reports when the button is clicked
        new_win1 = Reports(self)
        new_win1.grab_set()
        self.report_instance = new_win1

    def catalog(self):#opens Catalog Window
        new_win2 = Book_Catalog(self)
        new_win2.grab_set()

    def members_window(self):#opens members Window
        new_win3 = Members(self)
        new_win3.grab_set()

    #Creates parent class instructions for other windows    
    def clear_frame(frame):#Destroys child window on exit 
        for widgets in frame.winfo_children():
            widgets.destroy() 


class Reports(tk.Toplevel):#Marshall wrote this code block
    
    def __init__(self, parent):
        super().__init__(parent)
        self.width = 380
        self.height = 205
        self.screen_wid = self.winfo_screenwidth()
        self.screen_hei = self.winfo_screenheight()
        self.geometry(f"{self.screen_wid-25}x{self.screen_hei-60}")

        self.configure(bg = '#e1d8b9')
        self.style = ttk.Style()
        self.style.configure('nbutton.TButton', background = '#e1d8b9', width = 18, height = 34)
        self.title("Reports")
        self.report_window()
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        

    def report_window(self):
        
        self.frame_head3 = tk.Frame(self, bg = '#e1d8b9')#Frame for image
        self.frame_head3.grid(row = 0, sticky='nsew')

        self.frame_buttons = tk.Frame(self, bg = '#e1d8b9', height=50)#Frame for image
        self.frame_buttons.grid(row = 1, sticky='nsew')
        self.frame_buttons.grid_columnconfigure(0, weight=1)
        self.frame_buttons.grid_columnconfigure(1, weight=1)
        tk.Label(self.frame_head3, text = "Which Report Would",
                  bg = '#e1d8b9', font = ('Baskerville Old Face', '18', 'bold')).pack(fill='x')
        tk.Label(self.frame_head3, text = "You Like to View",
                  bg = '#e1d8b9', font = ('Baskerville Old Face', '12')).pack(fill='x')

        ttk.Button(self.frame_buttons, text='Books Out', style='nbutton.TButton', 
                   command=self.books_out).grid(row=0, column=0, sticky='e')
        ttk.Button(self.frame_buttons, text='Books Late', style='nbutton.TButton', 
                   command=self.books_late).grid(row=0, column=1, sticky= 'w')
        
        ttk.Button(self.frame_buttons, text='Return to Main Menu', style='n2button.TButton', 
                   command=self.destroy).grid(row=1, column=0, columnspan=2, padx=10)
        self.results2 = tk.Frame(self, bg = '#e1d8b9')#setting up results panel
        self.results2.grid(row=2, padx=10, pady=10,sticky='nsew')

    def books_out(self):
        pass

        
    def books_late(self):
        MenuMain.clear_frame(self.results2)
        my_results = Report().bks_late()
        my_scrollbar = tk.Scrollbar(self.results2)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        text_box = Text(
            self.results2,yscrollcommand=my_scrollbar.set)
        text_box.pack(expand=True, fill='both')
        text_box.insert('end', my_results)
        text_box.config(state='disabled')
        my_scrollbar.config(command=text_box.yview)
        
        
class Book_Catalog(tk.Toplevel):
    pass

class Members(tk.Toplevel):
    pass

def main():#starts program and begins run            
    app = MenuMain()
    app.mainloop()
    
if __name__ == "__main__": main()