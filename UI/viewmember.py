import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk 
import UI.Addmember as addmember
import UI.DeleteMember as DeleteMember
import sys

sys.path.insert(1, f'./database')
import database

db = database.Database()

class App:
    def __init__(self, root):
        root.title("Python Programing Club")
        width=1053
        height=492
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        title_text=tk.Label(root)
        ft = tkFont.Font(family='Times',size=34)
        title_text["font"] = ft
        title_text["fg"] = "#333333"
        title_text["justify"] = "center"
        title_text["text"] = "View Member List"
        title_text.place(x=250,y=0,width=597,height=56)

        descriptions = ('SL', 'Name', 'Class', 'Student ID', "Batch")  
        tree = ttk.Treeview(root, columns = descriptions, show = 'headings')  
        tree.heading('SL', text = 'SL') #Headings  
        tree.heading('Name', text = 'Name of the person')  
        tree.heading('Class', text = 'Class') 
        tree.heading('Student ID', text = 'Student ID') 
        tree.heading('Batch', text = 'Batch') 
        # tree.bind('<<TreeviewSelect>>', selection) 
        tree.place(x=20,y=60,width=1014,height=363) 

        add_button=tk.Button(root)
        add_button["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        add_button["font"] = ft
        add_button["fg"] = "#000000"
        add_button["justify"] = "center"
        add_button["text"] = "Add Student"
        add_button.place(x=950,y=430,width=84,height=32)
        add_button["command"] = self.add_button_command

        DeleteButton=tk.Button(root)
        DeleteButton["bg"] = "#ff0000"
        ft = tkFont.Font(family='Times',size=10)
        DeleteButton["font"] = ft
        DeleteButton["fg"] = "#ffffff"
        DeleteButton["justify"] = "center"
        DeleteButton["text"] = "Delete"
        DeleteButton.place(x=50,y=430,width=84,height=32)
        DeleteButton["command"] = self.DeleteButton_command

        data = db.fech_data()
        index = 1
        for row in data:
            self.name = row[0]
            self.Class = row[1]
            self.Id = row[2]
            self.batch = row[3]

            tree.insert("", tk.END, values=(index, self.name, self.Class, self.Id, self.batch))
            
            index += 1

    def add_button_command(self):
        addmember.main()

    
    def DeleteButton_command(self):
        DeleteMember.main()

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()
