import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import sys

sys.path.insert(1, f'./database')
import database

db = database.Database()

class App:
    def __init__(self, root):
        self.root = root
        self.title = "Python Programing Club"
        self.root.title(self.title)
        width=353
        height=197
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        title_highlite=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=14)
        title_highlite["font"] = ft
        title_highlite["fg"] = "#333333"
        title_highlite["justify"] = "center"
        title_highlite["text"] = "Delete Member"
        title_highlite.place(x=0,y=0,width=353,height=43)

        enter_s_id=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=13)
        enter_s_id["font"] = ft
        enter_s_id["fg"] = "#ff0303"
        enter_s_id["justify"] = "center"
        enter_s_id["text"] = "Enter Student ID"
        enter_s_id.place(x=20,y=65,width=119,height=35)

        self.s_id=tk.Entry(self.root)
        self.s_id["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.s_id["font"] = ft
        self.s_id["fg"] = "#333333"
        self.s_id["justify"] = "center"
        self.s_id.place(x=170,y=60,width=155,height=35)

        Cancel_button=tk.Button(self.root)
        Cancel_button["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=10)
        Cancel_button["font"] = ft
        Cancel_button["fg"] = "#000000"
        Cancel_button["justify"] = "center"
        Cancel_button["text"] = "Cancel"
        Cancel_button.place(x=250,y=150,width=70,height=25)
        Cancel_button["command"] = self.Cancel_button_command

        Delete_button=tk.Button(self.root)
        Delete_button["bg"] = "#ff0f0f"
        ft = tkFont.Font(family='Times',size=10)
        Delete_button["font"] = ft
        Delete_button["fg"] = "#000000"
        Delete_button["justify"] = "center"
        Delete_button["text"] = "Delete"
        Delete_button.place(x=170,y=150,width=70,height=25)
        Delete_button["command"] = self.Delete_button_command


    def Cancel_button_command(self):
        value = messagebox.askyesno(title=self.title, message="Do you want to destroy this window?")
        if value == True:
            self.root.destroy()

    def Delete_button_command(self):
        student_id = self.s_id.get()
        value = messagebox.askquestion(title= self.title, message=f'Club member {student_id} will delete! Are you sure?')

        if value == 'yes':
            db.remove_member(student_id)
            messagebox.showinfo(title= self.title, message=f'Club member {student_id} is delete!')
            self.root.destroy()        

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()
