import tkinter as tk
from tkinter import *
from tkinter import ttk
import Library_Mods as lb
from Library_Mods import *
from tkinter import messagebox 

class MenuMain(tk.Tk):
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
        # self.protocol("WM_DELETE_WINDOW", self.disable_Xclose)
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
        tk.Label(self.frame_start, text = "What Would You Like To Do",
                  bg = '#e1d8b9', font = ('Baskerville Old Face', '12', 'bold')).grid(row = 2, column = 0, columnspan = 2)
        
        self.but_horde = ttk.Button(self.frame_start, style = 'nbutton.TButton', text = "Reports", command = self.report)
        self.but_horde.grid(row = 3, column = 0, sticky = 'nsew')
        
        self.but_char = ttk.Button(self.frame_start, style = 'nbutton.TButton',text = "Catalog", command = self.catalog)
        self.but_char.grid(row = 3, column = 1, sticky = 'nsew')
        ttk.Button(self.frame_start, text = 'Exit', style = 'n2button.TButton',command = lambda : exit()).grid(row = 4, column = 0, columnspan = 2)
       
    def report(self):#opens Horde window
        new_win1 = Reports(self)
        new_win1.grab_set()
        
    def catalog(self):#opens Character Window
        new_win2 = Book_Catalog(self)
        new_win2.grab_set()

    #Creates parent class instructions for other windows    
    def clear_frame(frame):#Destroys child window on exit 
        for widgets in frame.winfo_children():
            widgets.destroy() 


class Reports(tk.Toplevel):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.width = 410
        self.height = 265
        self.screen_wid = self.winfo_screenwidth()
        self.screen_hei = self.winfo_screenheight()
        self.x = (self.screen_wid/2) - (self.width/2)
        self.y = (self.screen_hei/2) - (self.height/2)
        self.geometry("%dx%d+%d+%d" % (self.width, self.height, self.x, self.y))
        self.configure(bg = '#e1d8b9')
        self.style = ttk.Style()
        self.style.configure('nbutton.TButton', background = '#e1d8b9', width = 18, height = 34)
        self.title("Reports")
        self.report_window()
        
    def report_window(self):
        
        self.frame_head3 = tk.Frame(self, bg = '#e1d8b9')#Frame for image
        self.frame_head3.grid(row = 0, column = 0)

        tk.Label(self.frame_head3, text = "Which Report Would",
                  bg = '#e1d8b9', font = ('Baskerville Old Face', '18', 'bold')).grid(row = 0, column = 0, columnspan = 2)
        tk.Label(self.frame_head3, text = "You Like to View",
                  bg = '#e1d8b9', font = ('Baskerville Old Face', '12')).grid(row = 1, column = 0, columnspan = 2)
        
        self.but_horde = ttk.Button(self.frame_head3, style = 'nbutton.TButton', text = "Books Currently Out", command = self.books_out)
        self.but_horde.grid(row = 3, column = 0, sticky = 'nsew')
        
        self.but_char = ttk.Button(self.frame_head3, style = 'nbutton.TButton',text = "Member with Late Books", command = self.books_late)
        self.but_char.grid(row = 3, column = 1, sticky = 'nsew')
        ttk.Button(self.frame_head3, text = 'Exit', style = 'n2button.TButton',command = lambda : exit()).grid(row = 4, column = 0, columnspan = 2)
        self.results2 = tk.Frame(self, bg = '#e1d8b9')#setting up results panel
        self.results2.grid(row = 1, column = 0)

    def books_out(self):
        self.count = 4 #Counter variable
        MenuMain.clear_frame(self.results2)#Clears results frame
        new_height = self.winfo_screenheight()
        new_width = self.winfo_screenheight()
        new_y = (self.screen_hei/2) - (new_height/2)
        self.geometry("%dx%d+%d+%d" % (new_width, new_height, self.x, new_y))
        report1 = lb.Report().bks_out_emails()
        self.report1_results = tk.Label(self.results2, text = report1,
                  bg = '#e1d8b9').grid(row = 0, column = 0)
        
    def books_late(self):
        self.count = 4 #Counter variable
        MenuMain.clear_frame(self.results2)#Clears results frame
        new_height = self.winfo_screenheight()
        new_width = self.winfo_screenheight()
        new_y = (self.screen_hei/2) - (new_height/2)
        self.geometry("%dx%d+%d+%d" % (new_width, new_height, self.x, new_y))
        report1 = Report().bks_late()
        self.report1_results = tk.Label(self.results2, text = report1,
                  bg = '#e1d8b9').grid(row = 0, column = 0)
    
        
        
class Book_Catalog(tk.Toplevel):
    pass


def main():#starts program and begins run            
    app = MenuMain()
    app.mainloop()
    
if __name__ == "__main__": main()