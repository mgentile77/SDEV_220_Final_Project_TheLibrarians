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
        # self.image_start = tk.Label(self.frame_start, bg = '#e1d8b9', image = self.back_image)
        # self.image_start.grid(row = 0, column = 0, rowspan = 5, sticky = 'nsew')
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
        self.but_member.grid(row=4, column=0, sticky = 'nsew')

        ttk.Button(self.frame_start, text = 'Exit', style = 'n2button.TButton',command = lambda : exit()).grid(row = 5, column = 0, columnspan = 2)
    
    def report(self):#opens report window
        self.show_reports()
    
    def show_reports(self):
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


class Reports(tk.Toplevel):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.width = 380
        self.height = 205
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
        self.results2 = tk.Frame(self, bg='#e1d8b9')
        self.results2.grid(row=1, column=0, columnspan=2)
        self.borfile = ...  # Initialize borfile
        self.mfile = ...    # Initialize mfile
        self.bfile = ...    # Initialize bfile

    def report_window(self):
        
        self.frame_head3 = tk.Frame(self, bg = '#e1d8b9')#Frame for image
        self.frame_head3.grid(row = 0, column = 0, columnspan = 2)

        # self.image_start = tk.Label(self.frame_start, bg = '#e1d8b9', image = self.back_image)
        # self.image_start.grid(row = 0, column = 0, rowspan = 5, sticky = 'nsew')
        tk.Label(self.frame_head3, text = "Which Report Would",
                  bg = '#e1d8b9', font = ('Baskerville Old Face', '18', 'bold')).grid(row = 0, column = 0, columnspan = 2)
        tk.Label(self.frame_head3, text = "You Like to View",
                  bg = '#e1d8b9', font = ('Baskerville Old Face', '12')).grid(row = 1, column = 0, columnspan = 2)

        ttk.Button(self.frame_head3, text='Books Out', style='nbutton.TButton', command=self.books_out).grid(row=2, column=0)
        ttk.Button(self.frame_head3, text='Books Late', style='nbutton.TButton', command=self.books_late).grid(row=2, column=1)
        
        ttk.Button(self.frame_head3, text='Return to Main Menu', style='n2button.TButton', command=self.destroy).grid(row=4, column=0, columnspan=2)
        self.results2 = tk.Frame(self, bg = '#e1d8b9')#setting up results panel
        self.results2.grid(row = 1, column = 0, columnspan = 2)

    def books_out(self):
        self.count = 4 #Counter variable
        MenuMain.clear_frame(self.results2)#Clears results frame
        new_height = self.winfo_screenheight()
        new_width = self.winfo_screenwidth()
        new_y = (self.screen_hei/2) - (new_height/2)
        self.geometry("%dx%d+%d+%d" % (new_width, new_height, self.x, new_y))
        result_text = Report().bks_out_emails()
        result_text_widget = tk.Text(self.results2, wrap="word", height=10, width=50)
        result_text_widget.insert(tk.END, result_text)
        result_text_widget.grid(row=2, column=0, columnspan=2)

        report_instance = self.master.report_instance
        result_df = report_instance.bks_out_emails()
        self.display_dataframe(result_df)

        result_text = report_instance.bks_out_emails()
        result_text_widget = tk.Text(self.results2, wrap="word", height=10, width=50)
        result_text_widget.insert(tk.END, result_text)
        result_text_widget.grid(row=2, column=0, columnspan=2)

        # Optionally, display DataFrame if needed
        result_df = report_instance.bks_out_emails()
        self.display_dataframe(result_df)

        
    def books_late(self):
        MenuMain.clear_frame(self.results2)
        report_instance = self.master.report_instance
        
        result_text = Report().bks_late()
        result_text_widget = tk.Text(self.results2, wrap="word", height=10, width=50)
        result_text_widget.insert(tk.END, result_text)
        result_text_widget.grid(row=2, column=0, columnspan=2)

    def display_dataframe(self, dataframe):
        # Function to display the DataFrame in the Tkinter window
        rows, columns = dataframe.shape
        for i, col in enumerate(dataframe.columns):
            tk.Label(self.results2, text=col, bg='#e1d8b9', font=('Baskerville Old Face', '12', 'bold')).grid(row=0,
                                                                                                               column=i)
            for j in range(rows):
                tk.Label(self.results2, text=dataframe.iloc[j, i], bg='#e1d8b9').grid(row=j + 1, column=i)

    def bks_out_emails(self):
        self.identify_late()
        with pd.option_context('display.max_rows', None, 'display.max_colwidth', 50, 'display.width', 120):
            __all_merge = self.borfile.merge(self.mfile[['Fname', 'Lname', 'Email']], right_index=True,
                                             left_on='Member_ID'
                                             ).merge(self.bfile[['Title', 'Author']], right_index=True,
                                                     left_on='Book_ID').reset_index(level='Book_ID')
            __all_merge['Name'] = (__all_merge['Fname'] + " " + __all_merge['Lname'])
            __all_merge = __all_merge[['Name', 'Email', 'Title', 'Author', 'Date_Due', 'Late']
                                      ].set_index(['Name', 'Email', 'Title'], append=True)

            _rec_count = __all_merge.shape[0]
            result_str = f"{__all_merge}\n\nTotal records in file = {_rec_count}\n"
            
        return result_str
class Book_Catalog(tk.Toplevel):
    pass

class Members(tk.Toplevel):
    pass

def main():#starts program and begins run            
    app = MenuMain()
    app.mainloop()
    
if __name__ == "__main__": main()