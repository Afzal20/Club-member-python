import tkinter as tk
import tkinter.font as tkFont
import sys

sys.path.insert(1, f'./database')
import database

db = database.Database()

class App:
    def __init__(self, root):
        root.title("Python Programing Club")
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        #componants 
        self.L_Label=tk.Label(root)
        self.s_name_text=tk.Label(root)
        self.s_name_entry=tk.Entry(root)
        self.s_id_text=tk.Label(root)
        self.s_id_entry=tk.Entry(root)
        self.s_class_text=tk.Label(root)
        self.s_class_entry=tk.Entry(root)
        self.s_batch_text=tk.Label(root)
        self.s_batch_entry=tk.Entry(root)
        self.Button=tk.Button(root)

        # font-size and font-family
        self.textfont = tkFont.Font(family='Times',size=22)
        self.entryfont = tkFont.Font(family='Times',size=20)

        # Highligth of title
        titlefont = tkFont.Font(family='Times',size=34)
        self.L_Label["font"] = titlefont
        self.L_Label["fg"] = "#333333"
        self.L_Label["justify"] = "left"
        self.L_Label["text"] = "Member management"
        self.L_Label.place(x=100,y=10,width=389,height=66)

        self.s_name_text["font"] = self.textfont
        self.s_name_text["fg"] = "#333333"
        self.s_name_text["justify"] = "left"
        self.s_name_text["text"] = "Student Name"
        self.s_name_text.place(x=70,y=150,width=174,height=41)

        self.s_name_entry["borderwidth"] = "1px"
        self.s_name_entry["font"] = self.entryfont
        self.s_name_entry["fg"] = "#333333"
        self.s_name_entry["justify"] = "left"
        self.s_name_entry.place(x=80,y=210,width=154,height=34)

        self.s_id_text["font"] = self.textfont
        self.s_id_text["fg"] = "#333333"
        self.s_id_text["justify"] = "left"
        self.s_id_text["text"] = "Student ID"
        self.s_id_text.place(x=80,y=270,width=127,height=33)

        self.s_id_entry["borderwidth"] = "1px"
        self.s_id_entry["font"] = self.entryfont
        self.s_id_entry["fg"] = "#333333"
        self.s_id_entry["justify"] = "left"
        self.s_id_entry.place(x=80,y=320,width=146,height=34)

        self.s_class_text["font"] = self.textfont
        self.s_class_text["fg"] = "#333333"
        self.s_class_text["justify"] = "left"
        self.s_class_text["text"] = "Student Class"
        self.s_class_text.place(x=370,y=150,width=161,height=45)

        self.s_class_entry["borderwidth"] = "1px"
        self.font = tkFont.Font(family='Times',size=20)
        self.s_class_entry["font"] = self.entryfont
        self.s_class_entry["fg"] = "#333333"
        self.s_class_entry["justify"] = "left"
        self.s_class_entry.place(x=380,y=210,width=149,height=33)

        self.s_batch_text["font"] = self.textfont
        self.s_batch_text["fg"] = "#333333"
        self.s_batch_text["justify"] = "left"
        self.s_batch_text["text"] = "Batch"
        self.s_batch_text.place(x=380,y=270,width=68,height=35)

        self.s_batch_entry["borderwidth"] = "1px"
        self.s_batch_entry["font"] = self.entryfont
        self.s_batch_entry["fg"] = "#333333"
        self.s_batch_entry["justify"] = "left"
        self.s_batch_entry.place(x=380,y=320,width=149,height=31)

        self.Button["bg"] = "#393d49"
        self.Button["cursor"] = "arrow"
        self.Button["font"] = tkFont.Font(family='Times',size=22)
        self.Button["fg"] = "#ffffff"
        self.Button["justify"] = "center"
        self.Button["text"] = "Submit"
        self.Button.place(x=190,y=400,width=170,height=45)
        self.Button["command"] = self.buttonCmd

    def buttonCmd(self):
        name    = self.s_name_entry.get()
        Id      = self.s_id_entry.get()
        Class   = self.s_class_entry.get()
        batch   = self.s_batch_entry.get()
        
        db.insert_member(name, Class, Id, batch)
        
                                                       

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

# AddMember()