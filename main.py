import tkinter as t
from tkinter import *
from tkinter.font import Font
from tkinter import font
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
from csv import DictWriter,writer
from datetime import date,time,datetime
import csv,os
import random
import mysql.connector
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import reportlab
import os
import webbrowser
from sys import *
from completion_script import AutocompleteCombobox
#-----------Functions--------






def correct(inp):
    if inp.isdigit():
        return True
    elif inp =="":
        return True
    else:
        return False 
def themes_data():
    filename="themes_collection.csv"
    file_exists=os.path.isfile(filename)
    if not file_exists:
        return "white","black"
    with open(filename,"r") as f2:
        csv_data=list(csv.reader(f2))
        bg=csv_data[len(csv_data)-1][0]
        fg=csv_data[len(csv_data)-1][1]
        return bg,fg

data=themes_data()
background=str(data[0])
foreground=str(data[1])

#------------Connection-------------
if True:
    mydb=mysql.connector.connect(
        host='localhost',
        username='root',
        password='Password_mysql',
        )
my_cursor=mydb.cursor()
my_cursor.execute('''create database if not exists Restaurant_db''')
my_cursor.execute('''use Restaurant_db''')
mydb.commit()
#---------------------------------





class Home:
    global background,foreground
    def __init__(self):
        self.home_window=Tk()
        self.home_window.title("Restaurant  Billing System (KOT/POS)")
        self.home_window.state('zoomed')
        self.frame_banner=Frame(self.home_window,bg=background)
        self.frame_banner.grid(row=0,column=0)
        self.banner_img=Image.open('icons\\home_ban.jpg')
        self.banner_img=self.banner_img.resize((self.home_window.winfo_screenwidth(),150),Image.ANTIALIAS)
        self.main_banner=ImageTk.PhotoImage(self.banner_img)        
        self.banner_btn=Button(self.frame_banner,image=self.main_banner,bg=background,bd=0,activebackground=background,command=self.slideshow)
        self.banner_btn.grid(row=0,column=0)
        #---------------Icons-------------------
        self.quick_bill_icon=ImageTk.PhotoImage(Image.open('icons\\billing.png'))
        self.inventory_icon=ImageTk.PhotoImage(Image.open('icons\\kitchen.png'))
        self.takeaway_icon=ImageTk.PhotoImage(Image.open('icons\\takeaway.png'))
        self.reports_icon=ImageTk.PhotoImage(Image.open('icons\\report.png'))
        self.setting_icon=ImageTk.PhotoImage(Image.open('icons\\settings.png'))
        self.Exit_icon=ImageTk.PhotoImage(Image.open('icons\\exit.png'))
        #---------------Frames & Buttons------------------
        self.body_frame=Frame(self.home_window,bg=background)
        self.body_frame.grid(row=1,column=0)
        self.frame1=Frame(self.body_frame,bg=background)
        self.frame1.grid(row=0,column=0)
        self.frame2=Frame(self.body_frame,bg=background)
        self.frame2.grid(row=0,column=1,padx=150,pady=70)
        self.frame3=Frame(self.body_frame,bg=background)
        self.frame3.grid(row=0,column=2)
        self.frame4=Frame(self.body_frame,bg=background)
        self.frame4.grid(row=1, column=0)
        self.frame5=Frame(self.body_frame,bg=background)
        self.frame5.grid(row=1,column=1)
        self.frame6=Frame(self.body_frame,bg=background)
        self.frame6.grid(row=1,column=2)
        main_font=Font(family="candara",size=25,weight="bold")
        self.quick_bill=Button(self.frame1,text="Billing",image=self.quick_bill_icon,bd=0,bg=background,fg=foreground,activebackground=background,compound="top",font=main_font,command=self.billing_func)
        self.quick_bill.grid(row=0,column=0)
        self.items=Button(self.frame2,text="Inventory",image=self.inventory_icon,bd=0,bg=background,fg=foreground,activebackground=background,command=self.inv_page,compound="top",font=main_font)
        self.items.grid(row=0,column=0)
        self.takesaway=Button(self.frame3,text="Takesaway",image=self.takeaway_icon,bd=0,bg=background,fg=foreground,activebackground=background,compound="top",font=main_font)
        self.takesaway.grid(row=0,column=0)
        self.report=Button(self.frame4,text="Report",image=self.reports_icon,bd=0,bg=background,fg=foreground,activebackground=background,compound="top",font=main_font,command=self.report_window)
        self.report.grid(row=0,column=0)
        self.settings=Button(self.frame5,text="Settings",image=self.setting_icon,bd=0,bg=background,fg=foreground,activebackground=background,compound="top",font=main_font,command=self.setting_page)
        self.settings.grid(row=0,column=0)
        self.Exit_b=Button(self.frame6,text="Exit",image=self.Exit_icon,bd=0,bg=background,fg=foreground,activebackground=background,command=self.exit,compound="top",font=main_font)
        self.Exit_b.grid(row=0,column=0)
        #self.home_window.overrideredirect(True)
        self.home_window.resizable(0,0)
        self.home_window.config(bg=background)
        self.home_window.bind("<Escape>",self.exit_s)
        self.home_window.protocol('WM_DELETE_WINDOW',self.disabled)
        self.home_window.mainloop()
    def slideshow(self):
        self.banners_collection=['icons\\home_ban.jpg','icons\\ban2.jpg','icons\\ban3.jpg']
        self.current_img=Image.open(random.choice(self.banners_collection))
        self.current_img=self.current_img.resize((self.home_window.winfo_screenwidth(),150),Image.ANTIALIAS)
        self.current_main_banner=ImageTk.PhotoImage(self.current_img)
        self.banner_btn.configure(image=self.current_main_banner)
    def disabled(self):
        pass
    def inv_page(self):
        Inventory()
    def setting_page(self):
        Settings()
    def billing_func(self):
        BILLING()
    def report_window(self):
        Report()    
    def exit(self):
        if messagebox.askyesno(parent=self.home_window,title="Exit",message="Are You Sure!"):
            self.home_window.destroy()
    def exit_s(self,event):
        if messagebox.askyesno(parent=self.home_window,title="Exit",message="Are You Sure!"):
            self.home_window.destroy()
class Themes:
    def __init__(self):
        self.themes_win=Toplevel()
        self.themes_win.title("Themes Menu")
        self.themes_win.geometry('400x400+450+200')
        self.theme_label=Label(self.themes_win,text="Select your choice",font='helvetica 19 bold',fg='black',bg='white')
        self.theme_label.grid(row=0,column=0,padx=100,pady=20)
        self.values=('white','grey','lightgrey','blue')
        self.theme_combobox=ttk.Combobox(self.themes_win,width=15,font="helvetica 16",state='readonly')
        self.theme_combobox["values"]=('white','grey','lightgrey','blue','mint cream','lavender','bisque2','dark sea green')
        self.theme_combobox.option_add('*TCombobox*Listbox.font',("consolas",16))
        self.theme_combobox.grid(row=1,column=0,padx=100,pady=10) 
        self.theme_combobox.current(0)
        self.save=Button(self.themes_win,text="save",width=6,font="hevetica 16",command=self.save_func)
        self.save.grid(row=4,column=0,pady=25)
        self.back=Button(self.themes_win,text="Back",width=6,font="hevetica 16",command=self.themes_win.destroy)
        self.back.grid(row=6,column=0)
        self.themes_win.config(bg='white')
        self.themes_win.focus_force()
        self.themes_win.attributes('-toolwindow', True)
    def save_func(self):
        flag_status=False
        filename="themes_collection.csv"
        file_exists=os.path.isfile(filename)
        with open(filename,"a",newline="") as f:
            csv_writer=DictWriter(f,fieldnames=['background_current_status','foreground_current_status'])
            if not file_exists:
                csv_writer.writeheader()
            csv_writer.writerow({
                'background_current_status':str(self.theme_combobox.get()),
                'foreground_current_status':'black',
            })
            flag_status=True
        if flag_status is True:
            if messagebox.askyesno(parent=self.themes_win,title="Save Changes",message="would you like to restart to see changes"):
                python = sys.executable
                os.execl(python, python, * sys.argv)
class Inventory:
    def __init__(self):
        self.inventory_win=Toplevel()
        self.inventory_win.title("Inventory Menu")
        self.inventory_win.state("zoomed")
        self.inventory_win.config(bg=background)
        self.frame_banner=Frame(self.inventory_win,bg=background)
        self.frame_banner.grid(row=0,column=0)
        self.banner_img=Image.open('icons\\home_ban.jpg')
        self.banner_img=self.banner_img.resize((self.inventory_win.winfo_screenwidth(),150),Image.ANTIALIAS)
        self.main_banner=ImageTk.PhotoImage(self.banner_img)
        self.add_item_img=ImageTk.PhotoImage(Image.open('icons\\menu.png'))
        self.raw_item_img=ImageTk.PhotoImage(Image.open('icons\\raw.png'))
        self.employee_img=ImageTk.PhotoImage(Image.open('icons\\employe.png'))
        self.category_img=ImageTk.PhotoImage(Image.open('icons\\category.png'))
        self.Exit_icon=ImageTk.PhotoImage(Image.open('icons\\back.png'))
        self.inv_banner=ImageTk.PhotoImage(Image.open('icons\\menu_ico.png'))
        self.banner_lbl=Label(self.frame_banner,image=self.main_banner,bg=background)
        self.banner_lbl.grid(row=0,column=0)
        self.body_frame=Frame(self.inventory_win,bg=background)
        self.body_frame.grid(row=1,column=0)
        self.inventory_win.focus_force()
        self.ban=Label(self.frame_banner,text="  INVENTORY ",font="Helvetica 40 bold",compound="left",bg=background,fg=foreground,image=self.inv_banner)
        self.ban.grid(row=1,column=0,pady=10)
        self.add_item=Button(self.body_frame,text=" Items \n Registration ",font="Helvetica 20 bold",image=self.add_item_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background, command=self.add_item_func)
        self.add_item.grid(row=2,column=0,pady=20,padx=40)
        self.add_rawitem=Button(self.body_frame,text="  Raw Materials ",font="Helvetica 20 bold",image=self.raw_item_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background)
        self.add_rawitem.grid(row=4,column=0,pady=30,padx=40)
        self.employee=Button(self.body_frame,text="  Employee \n  Registeration ",font="Helvetica 20 bold",image=self.employee_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background,command=self.employee_reg_func)
        self.employee.grid(row=4,column=1,pady=30,padx=40)
        self.category=Button(self.body_frame,text="  Category \n  Registeration ",font="Helvetica 20 bold",image=self.category_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background, command=self.category_reg_func)
        self.category.grid(row=2,column=1,pady=20,padx=40)
        self.back=Button(self.body_frame,image=self.Exit_icon,compound="top",bg=background,fg=foreground,bd=0,activebackground=background,command=self.inventory_win.destroy)
        self.back.grid(row=6,column=0,columnspan=2,padx=70)
        self.inventory_win.bind("<Escape>",self.destroy)
        self.inventory_win.resizable(0,0)
        self.inventory_win.attributes('-toolwindow', True)
        #self.inventory_win.mainloop()
    def destroy(self,event):
        self.inventory_win.destroy()
    def add_item_func(self):
        Item_reg()
    def category_reg_func(self):
        category_reg_win()
    def employee_reg_func(self):
        Employee_reg()    
class Item_reg:
    def __init__(self):
        self.add_item_win=Toplevel()
        self.add_item_win.title("Items Register")
        self.add_item_win.state("zoomed")
        self.add_item_win.config(bg=background)
        self.frame_banner=Frame(self.add_item_win,bg=background)
        self.frame_banner.grid(row=0,column=0)
        self.banner_img=Image.open('icons\\home_ban.jpg')
        self.back_icon=ImageTk.PhotoImage(Image.open('icons\\back.png'))
        self.banner_img=self.banner_img.resize((self.add_item_win.winfo_screenwidth(),150),Image.ANTIALIAS)
        self.main_banner=ImageTk.PhotoImage(self.banner_img)
        self.banner_lbl=Label(self.frame_banner,image=self.main_banner,bg=background)
        self.banner_lbl.grid(row=0,column=0)
        self.frame_main=Frame(self.add_item_win,bg=background)
        self.frame_main.grid(row=1,column=0)
        main_font=Font(family="candara",size=16,weight='normal')
        self.body_frame=LabelFrame(self.frame_main,bg=background,text="Item Description",font="calibri 35 bold",fg=foreground,bd=5)
        self.body_frame.grid(row=0,column=0,ipadx=30)
        self.regn_l=Label(self.body_frame,text="Reg. No *",font=main_font,bg=background,bd=1,fg=foreground)
        self.regn_l.grid(row=1,column=0,pady=10,padx=20,sticky=t.W)
        self.item_name_l=Label(self.body_frame,text="Item Name *",font=main_font,bg=background,fg=foreground)
        self.item_name_l.grid(row=2,column=0,pady=10,padx=20,sticky=t.W)
        self.rate_l=Label(self.body_frame,text="Rate *",font=main_font,bg=background,fg=foreground)
        self.rate_l.grid(row=3,column=0,pady=10,padx=20,sticky=t.W)
        self.cat_l=Label(self.body_frame,text="Category",font=main_font,bg=background,fg=foreground)
        self.cat_l.grid(row=4,column=0,pady=10,padx=20,sticky=t.W)
        #-----------Entry boxes--------------------------
        self.regn_e=Entry(self.body_frame,font=main_font,width=15,bd=2,bg='white',fg=foreground)
        self.regn_e.grid(row=1,column=1,pady=10,sticky=t.W)
        #---------------registration no fetch------------------
        self.regn_e.insert(END,'IT-01')
        self.regn_e.focus()
        self.regn_e.bind("<Return>",lambda event: self.item_name_e.focus())
        self.regn_e.bind("<Down>",lambda event: self.item_name_e.focus())
        self.regn_e.bind("<Up>",lambda event: self.cat_combobox.focus())

        self.item_name_e=Entry(self.body_frame,font=main_font,width=15,bd=2,bg='white',fg=foreground)
        self.item_name_e.grid(row=2,column=1,pady=10,sticky=t.W)
        self.item_name_e.bind("<Return>",lambda event: self.rate_e.focus())
        self.item_name_e.bind("<Down>",lambda event: self.rate_e.focus())
        self.item_name_e.bind("<Up>",lambda event: self.regn_e.focus())


        self.rate_e=Entry(self.body_frame,font=main_font,width=15,bd=2,background='white',foreground=foreground)
        self.rate_e.grid(row=3,column=1,pady=10,sticky=t.W)
        self.reg=self.rate_e.register(correct)                                # Input only Integer type
        self.rate_e.config(validate="key",validatecommand=(self.reg,"%P"))
        self.rate_e.bind("<Return>",lambda event: self.cat_combobox.focus())
        self.rate_e.bind("<Down>",lambda event: self.cat_combobox.focus())
        self.rate_e.bind("<Up>",lambda event: self.item_name_e.focus())
        #Fetch category list
        self.combo_values=[]
        try:
            my_cursor.execute('SELECT Unit_name FROM Category_Record')
            self.Category_list=my_cursor.fetchall()
            
            for cat in self.Category_list:
                self.combo_values.append(cat[0])
        except:
            self.combo_values.append("None")
        #-----------------------------------
        self.cat_combobox=ttk.Combobox(self.body_frame,width=14,font=main_font,state="readonly")
        self.cat_combobox["values"]=self.combo_values 
        self.cat_combobox.option_add('*TCombobox*Listbox.font',("candara",16))
        self.cat_combobox.grid(row=4,column=1,pady=20,sticky=t.W) 
        self.cat_combobox.current(0)
        self.cat_combobox.bind("<Return>",lambda event: self.Add_func())
        self.cat_combobox.bind("<Up>",lambda event: self.rate_e.focus())

        self.add=Button(self.body_frame,text="Add",bg=background,fg=foreground,bd=2,font="candara 16 bold",width=8,activebackground=background,command=self.Add_func)
        self.add.grid(row=5,column=0,padx=75,pady=10,sticky=t.W)
        self.clear=Button(self.body_frame,text="Clear",bg=background,fg=foreground,bd=2,font="candara 16 bold",width=8,activebackground=background,command=self.clear_func)
        self.clear.grid(row=5,column=1,padx=20,pady=10,sticky=t.E)
        #-------Tree view style-----------------
        self.saved_item_frame=LabelFrame(self.frame_main,bg=background,text="Saved Items",font="candara 35 bold",fg=foreground,bd=5)
        self.saved_item_frame.grid(row=0,column=1,padx=30,pady=30)
        self.style=ttk.Style()
        self.style.configure('mystyle.Treeview',highlightthickness=0,bd=0,background=background,fielfbackground="blue",font=('candara',12))
        self.style.configure('mystyle.Treeview.Heading',font=('candara',14,'bold'))
        self.style.layout('mystyle.Treeview',[('mystyle.Treeview.treearea',{'sticky':'nswe'})])
        #---------------scrollbar with treeview----
        self.tree_frame=Frame(self.saved_item_frame)
        self.tree_frame.grid()
        self.vertical_scrollbar=ttk.Scrollbar(self.tree_frame)
        self.vertical_scrollbar.grid(row=0,column=1,sticky='ns')
        self.data_tree=ttk.Treeview(self.tree_frame,style="mystyle.Treeview",yscrollcommand=self.vertical_scrollbar.set)
        self.vertical_scrollbar.config(command=self.data_tree.yview)
        #-----Decorate headings and Columns------------
        self.data_tree['columns']=('0','1','2','3')
        self.data_tree.column("#0",width=1)
        self.data_tree.column("0",width=100)
        self.data_tree.column("1",width=200)
        self.data_tree.column("2",width=100)
        self.data_tree.column("3",width=150)
        self.data_tree.heading("0",text="Reg No")
        self.data_tree.heading("1",text="Item Name")
        self.data_tree.heading("2",text="Rate (INR)")
        self.data_tree.heading("3",text='Category')
        #---------insert data------------
        self.insert_treeview() 
        self.data_tree.grid(row=0,column=0)      
        #------------buttons------------
        self.delete=Button(self.saved_item_frame,text="Delete",bg=background,fg=foreground,bd=2,font="candara 16 bold",width=8,activebackground=background,command=self.delete_func)
        self.delete.grid(row=2,column=0,pady=10,sticky=t.W,padx=150)
        self.delete_all=Button(self.saved_item_frame,text="Delete all",width=10,bg=background,fg=foreground,bd=2,font="candara 16 bold",activebackground=background,command=self.delete_all_func)
        self.delete_all.grid(row=2,column=0,pady=10,sticky=t.E,padx=150)
        self.back=Button(self.frame_main,image=self.back_icon,bg=background,fg=foreground,bd=0,activebackground=background,command=self.add_item_win.destroy)
        self.back.grid(row=4,column=1,sticky=t.W,padx=40)
        self.add_item_win.bind("<Escape>",self.back_b)
        self.add_item_win.attributes('-toolwindow', True)
        self.add_item_win.mainloop()
    #----Add data in Database----
    def Add_func(self):
        if self.rate_e.get() =="":
            self.rate_e.focus()

        if self.item_name_e.get() =="":
            self.item_name_e.focus()

        elif int(self.rate_e.get()) > 100000:
            messagebox.showerror(parent=self.add_item_win,title='Error',message='Maximum Size Reached')
            self.rate_e.delete(0,END)
            self.rate_e.focus()
        else:
            my_cursor.execute(
                '''CREATE TABLE IF NOT EXISTS 
            Items_Record(
                Regn_no varchar(255),
                Item_name varchar(255),
                Rate int,
                Category varchar(255)
                )'''
            )
            self.add_query='INSERT INTO Items_Record(Regn_no,Item_name,Rate,Category) VALUES(%s,%s,%s,%s)'
            my_cursor.execute(self.add_query,
            (self.regn_e.get(),self.item_name_e.get(),self.rate_e.get(),self.cat_combobox.get())
            )
            mydb.commit()
            self.treeview_data()
            self.clear_func()
    def clear_func(self):
        self.item_name_e.delete(0,END)
        self.rate_e.delete(0,END)
        self.regn_e.focus()
    #-----Delete item from selection---
    def delete_func(self):
        try:
            self.delete_data=self.data_tree.item(self.data_tree.focus())['values']     # getting the list of selected area 
            self.delete_query='DELETE FROM Items_Record WHERE Item_name=%s AND Rate=%s'
            my_cursor.execute(self.delete_query,(self.delete_data[1],self.delete_data[2]))
            mydb.commit()
            self.treeview_data()
        except:
            messagebox.showerror(parent=self.add_item_win,title='Error',message="Please Select any Item")  
    def delete_all_func(self):
        if messagebox.askyesno(parent=self.add_item_win,title='Clear everything',message='Are you sure?'):
            my_cursor.execute('DROP TABLE Items_Record')
            mydb.commit()
        #clear the treeview
            for child in self.data_tree.get_children():
                self.data_tree.delete(child)
            self.data_tree.insert("","end",text="",values=("","","",""))
    #----insert treeview-----
    def insert_treeview(self):
        #Check table is exists or not
        self.item_table = 'ITEMS_RECORD'
        self.table_show_query = 'SHOW TABLES'
        my_cursor.execute(self.table_show_query)
        self.tables_list = my_cursor.fetchall()
        self.results_list = [item[0] for item in self.tables_list] # Conversion to list of str
        if self.item_table in str(self.results_list).upper():
            self.treeview_data()     #table found then update treview data
        else:
            self.data_tree.insert("","end",text="",values=("","","",""))    #table not found then insert empty line
    #----Udate treeview-------
    def treeview_data(self):
        # delete old data 
        for child in self.data_tree.get_children():
            self.data_tree.delete(child)
        #input new data from database
        my_cursor.execute('SELECT Regn_no,Item_name,Rate,Category FROM Items_Record')
        self.results=my_cursor.fetchall()
        for record in self.results:
            self.data_tree.insert("","end",text="",values=(record[0],record[1],record[2],record[3]))

    def back_b(self,event):
        self.add_item_win.destroy()
class Settings:
    def __init__(self):
        self.settings_win=Toplevel()
        self.settings_win.title("Settings/Costomization")
        self.settings_win.state("zoomed")
        self.settings_win.config(bg=background)
        self.frame_banner=Frame(self.settings_win,bg=background)
        self.frame_banner.grid(row=0,column=0)
        self.banner_img=Image.open('icons\\home_ban.jpg')
        self.banner_img=self.banner_img.resize((self.settings_win.winfo_screenwidth(),150),Image.ANTIALIAS)
        self.main_banner=ImageTk.PhotoImage(self.banner_img)
        self.cd_img=ImageTk.PhotoImage(Image.open('icons\\company.png'))
        self.printer_img=ImageTk.PhotoImage(Image.open('icons\\printer.png'))
        self.theme_img=ImageTk.PhotoImage(Image.open('icons\\theme.png'))
        self.help_img=ImageTk.PhotoImage(Image.open('icons\\help.png'))
        self.about_img=ImageTk.PhotoImage(Image.open('icons\\about.png'))
        self.Exit_icon=ImageTk.PhotoImage(Image.open('icons\\back.png'))
        self.inv_banner=ImageTk.PhotoImage(Image.open('icons\\settings_ico.png'))
        self.banner_lbl=Label(self.frame_banner,image=self.main_banner,bg=background)
        self.banner_lbl.grid(row=0,column=0)
        self.body_frame=Frame(self.settings_win,bg=background)
        self.body_frame.grid(row=1,column=0,pady=20)
        self.ban=Label(self.frame_banner,text="  SETTINGS ",font="Candara 40 bold",compound="left",bg=background,fg=foreground,image=self.inv_banner)
        self.ban.grid(row=1,column=0)
        self.cd=Button(self.body_frame,text="  Company Details ",font="Helvetica 20 bold",image=self.cd_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background)
        self.cd.grid(row=1,column=1,pady=15,padx=30,sticky=t.W)
        self.printer_b=Button(self.body_frame,text="  Add Printer ",font="Helvetica 20 bold",image=self.printer_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background)
        self.printer_b.grid(row=1,column=0,pady=15,padx=10,sticky=t.W)
        self.theme_b=Button(self.body_frame,text="  Change Theme ",font="Helvetica 20 bold",image=self.theme_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background,command=self.theme_page)
        self.theme_b.grid(row=2,column=0,pady=15,padx=10,sticky=t.W)
        self.help=Button(self.body_frame,text="  Help ",font="Helvetica 20 bold",image=self.help_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background)
        self.help.grid(row=2,column=1,pady=15,padx=30,sticky=t.W)
        self.about=Button(self.body_frame,text="  About Us ",font="Helvetica 20 bold",image=self.about_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background)
        self.about.grid(row=3,column=0,pady=15,padx=10,sticky=t.W)
        self.back=Button(self.body_frame,image=self.Exit_icon,compound="top",bg=background,fg=foreground,bd=0,activebackground=background,command=self.settings_win.destroy)
        self.back.grid(row=4,column=1,sticky=t.W,pady=20)
        self.settings_win.bind("<Escape>",self.destroy)
        self.settings_win.resizable(0,0)
        self.settings_win.attributes('-toolwindow', True)
        #self.settings_win.mainloop()
    def theme_page(self):
        Themes()
    def destroy(self,event):
        self.settings_win.destroy()
class Employee_reg:
    def __init__(self):
        self.empl_reg_win=Toplevel()
        self.empl_reg_win.title("Employee Registration")
        self.empl_reg_win.state("zoomed")
        self.empl_reg_win.config(bg=background)
        self.frame_banner=Frame(self.empl_reg_win,bg=background)
        self.frame_banner.grid(row=0,column=0)
        self.banner_img=Image.open('icons\\home_ban.jpg')
        self.back_icon=ImageTk.PhotoImage(Image.open('icons\\back.png'))
        self.banner_img=self.banner_img.resize((self.empl_reg_win.winfo_screenwidth(),150),Image.ANTIALIAS)
        self.main_banner=ImageTk.PhotoImage(self.banner_img)
        self.banner_lbl=Label(self.frame_banner,image=self.main_banner,bg=background)
        self.banner_lbl.grid(row=0,column=0)
        self.frame_main=Frame(self.empl_reg_win,bg=background)
        self.frame_main.grid(row=1,column=0)
        main_font=Font(family="candara",size=16,weight='normal')
        self.body_frame=LabelFrame(self.frame_main,bg=background,text="Employee Registration",font="calibri 25 bold",fg=foreground,bd=5)
        self.body_frame.grid(row=0,column=0,padx=20,pady=30)
        self.id_l=Label(self.body_frame,text="Employee ID*",font=main_font,bg=background,bd=1,fg=foreground)
        self.id_l.grid(row=1,column=0,pady=10,padx=20,sticky=t.W)
        self.emp_name_l=Label(self.body_frame,text="Employee Name *",font=main_font,bg=background,fg=foreground)
        self.emp_name_l.grid(row=2,column=0,pady=10,padx=20,sticky=t.W)
        self.gender_l=Label(self.body_frame,text="Gender",font=main_font,bg=background,fg=foreground)
        self.gender_l.grid(row=3,column=0,pady=10,padx=20,sticky=t.W)
        self.mob_l=Label(self.body_frame,text="Mobile Number",font=main_font,bg=background,fg=foreground)
        self.mob_l.grid(row=4,column=0,pady=10,padx=20,sticky=t.W)
        self.address_l=Label(self.body_frame,text="Adress",font=main_font,bg=background,fg=foreground)
        self.address_l.grid(row=5,column=0,pady=10,padx=20,sticky=t.W)
        self.types_l=Label(self.body_frame,text="Type",font=main_font,bg=background,fg=foreground)
        self.types_l.grid(row=6,column=0,pady=10,padx=20,sticky=t.W)
        #-----------Entry boxes--------------------------
        self.id_e=Entry(self.body_frame,font=main_font,width=15,bd=2,bg='white',fg=foreground)
        self.id_e.grid(row=1,column=1,pady=10,sticky=t.W)
        self.id_e.insert(END,'EM-01')
        self.id_e.focus()
        self.id_e.bind("<Return>",lambda event: self.emp_name_e.focus())
        self.id_e.bind("<Down>",lambda event: self.emp_name_e.focus())
        self.id_e.bind("<Up>",lambda event: self.gen_combobox.focus())

        self.emp_name_e=Entry(self.body_frame,font=main_font,width=15,bd=2,bg='white',fg=foreground)
        self.emp_name_e.grid(row=2,column=1,pady=10,sticky=t.W)
        self.emp_name_e.bind("<Return>",lambda event: self.gen_combobox.focus())
        self.emp_name_e.bind("<Down>",lambda event: self.gen_combobox.focus())
        self.emp_name_e.bind("<Up>",lambda event: self.gen_combobox.focus())

        self.gen_combobox=ttk.Combobox(self.body_frame,width=14,font=main_font,state="readonly")
        self.gen_combobox["values"]=('Male','Female','Other') 
        self.gen_combobox.option_add('*TCombobox*Listbox.font',('candara',16))
        self.gen_combobox.grid(row=3,column=1,pady=10,sticky=t.W) 
        self.gen_combobox.current(0)
        self.gen_combobox.bind("<Return>",lambda event: self.mob_e.focus())
        self.gen_combobox.bind("<Up>",lambda event: self.emp_name_e.focus())

        self.mob_e=Entry(self.body_frame,font=main_font,width=15,bd=2,bg='white',fg=foreground)
        self.mob_e.grid(row=4,column=1,pady=10,sticky=t.W)
        self.reg=self.mob_e.register(correct)                                # Input only Integer type
        self.mob_e.config(validate="key",validatecommand=(self.reg,"%P"))
        self.mob_e.bind("<Return>",lambda event: self.address_e.focus())
        self.mob_e.bind("<Down>",lambda event: self.address_e.focus())
        self.mob_e.bind("<Up>",lambda event: self.gen_combobox.focus())

        self.address_e=Entry(self.body_frame,font=main_font,width=15,bd=2,bg='white',fg=foreground)
        self.address_e.grid(row=5,column=1,pady=10,sticky=t.W)
        self.address_e.bind("<Return>",lambda event: self.types_combobox.focus())
        self.address_e.bind("<Down>",lambda event: self.types_combobox.focus())
        self.address_e.bind("<Up>",lambda event: self.mob_e.focus())

        self.types_combobox=ttk.Combobox(self.body_frame,width=14,font=main_font,state="readonly")
        self.types_combobox["values"]=('Waiter','Employee','Staff') 
        self.types_combobox.option_add('*TCombobox*Listbox.font',("candara",16))
        self.types_combobox.grid(row=6,column=1,pady=10,sticky=t.W) 
        self.types_combobox.current(0)
        self.types_combobox.bind("<Return>",lambda event: self.Add_func())
        self.types_combobox.bind("<Up>",lambda event: self.address_e.focus())

        self.add=Button(self.body_frame,text="Add",bg=background,fg=foreground,bd=2,font="candara 16 bold",width=8,activebackground=background,command=self.Add_func)
        self.add.grid(row=8,column=0,padx=100,pady=10,sticky=t.W)
        self.clear=Button(self.body_frame,text="Clear",bg=background,fg=foreground,bd=2,font="candara 16 bold",width=8,activebackground=background,command=self.clear_func)
        self.clear.grid(row=8,column=1,pady=10,padx=10,sticky=t.W)
        #-------Tree view style-----------------
        self.saved_item_frame=LabelFrame(self.frame_main,bg=background,text="Registered Employees",font="calibri 25 bold",fg=foreground,bd=5)
        self.saved_item_frame.grid(row=0,column=1)
        self.style=ttk.Style()
        self.style.configure('mystyle.Treeview',highlightthickness=0,bd=0,background=background,fielfbackground="blue",font=('candara',12))
        self.style.configure('mystyle.Treeview.Heading',font=('candara',14,'bold'))
        self.style.layout('mystyle.Treeview',[('mystyle.Treeview.treearea',{'sticky':'nswe'})])
        #---------------scrollbar with treeview----
        self.tree_frame=Frame(self.saved_item_frame,bg=background)
        self.tree_frame.grid()
        self.vertical_scrollbar=ttk.Scrollbar(self.tree_frame)
        self.vertical_scrollbar.grid(row=0,column=1,sticky='ns',pady=45)
        self.data_tree=ttk.Treeview(self.tree_frame,style="mystyle.Treeview",yscrollcommand=self.vertical_scrollbar.set)
        self.vertical_scrollbar.config(command=self.data_tree.yview)

        #-----Decorate headings and Columns------------
        self.data_tree['columns']=('0','1','2','3','4','5')
        self.data_tree.column("#0",width=1)
        self.data_tree.column("0",width=50)
        self.data_tree.column("1",width=150,anchor='center')
        self.data_tree.column("2",width=70)
        self.data_tree.column("3",width=150,anchor='center')
        self.data_tree.column("4",width=150)
        self.data_tree.column("5",width=100)
        self.data_tree.heading("0",text="ID")
        self.data_tree.heading("1",text="Name")
        self.data_tree.heading("2",text="Gender")
        self.data_tree.heading("3",text='Mobile No.')
        self.data_tree.heading("4",text='Address')
        self.data_tree.heading("5",text='Type')
        #---------insert data------------
        self.insert_treeview() 
        self.data_tree.grid(row=0,column=0,pady=45)      
        #------------buttons------------
        self.buttons_frame=Frame(self.saved_item_frame,bg=background)
        self.buttons_frame.grid(row=2,column=0,pady=10)
        self.delete=Button(self.buttons_frame,text="Delete",bg=background,fg=foreground,bd=2,font="candara 16 bold",activebackground=background,command=self.delete_func)
        self.delete.grid(row=0,column=0,padx=15)
        self.delete_all=Button(self.buttons_frame,text="Delete all",width=10,bg=background,fg=foreground,bd=2,font="candara 16 bold",activebackground=background,command=self.delete_all_func)
        self.delete_all.grid(row=0,column=1,padx=30)
        self.back=Button(self.frame_main,image=self.back_icon,bg=background,fg=foreground,bd=0,activebackground=background,command=self.empl_reg_win.destroy)
        self.back.grid(row=9,column=1,sticky=t.W,padx=20)
        self.empl_reg_win.bind("<Escape>",self.back_b)
        self.empl_reg_win.attributes('-toolwindow', True)
        self.empl_reg_win.mainloop()
    #----Add data in Database----
    def Add_func(self):
        if str(self.mob_e.get())=="":
                self.mob_e.focus()
        if self.emp_name_e.get()=="":
            self.emp_name_e.focus()
        if len(str(self.mob_e.get())) > 10 or len(str(self.mob_e.get())) < 10:
            messagebox.showerror(parent=self.empl_reg_win,title='Error',message='Mobile No Should Be in 10 Digits')
            self.mob_e.focus()
        else:
            my_cursor.execute(
                '''CREATE TABLE IF NOT EXISTS 
            Employees_Record(
                Empl_id varchar(255),
                Empl_name varchar(255),
                Empl_gender varchar(255),
                Empl_number varchar(255),
                Empl_address varchar(255),
                Empl_type varchar(255)
                )'''
            )
            self.add_query='INSERT INTO Employees_Record(Empl_id,Empl_name,Empl_gender,Empl_number,Empl_address,Empl_type) VALUES(%s,%s,%s,%s,%s,%s)'
            my_cursor.execute(self.add_query,
            (self.id_e.get(),self.emp_name_e.get(),self.gen_combobox.get(),str(self.mob_e.get()),self.address_e.get(),self.types_combobox.get())
            )
            mydb.commit()
            self.treeview_data()
            self.clear_func()
    def clear_func(self):
        self.emp_name_e.delete(0,END)
        self.mob_e.delete(0,END)
        self.address_e.delete(0,END)
        self.id_e.focus()

    #-----Delete item from selection---
    def delete_func(self):
        try:
            self.delete_data=self.data_tree.item(self.data_tree.focus())['values']     # getting the list of selected area 
            self.delete_query='DELETE FROM Employees_Record WHERE Empl_id=%s AND Empl_name=%s'
            my_cursor.execute(self.delete_query,(self.delete_data[0],self.delete_data[1]))
            mydb.commit()
            self.treeview_data()
        except:
            messagebox.showerror(parent=self.empl_reg_win,title='Error',message="Please Select any Item")  
    def delete_all_func(self):
        if messagebox.askyesno(parent=self.empl_reg_win,title='Clear everything',message='Are you sure?'):
            my_cursor.execute('DROP TABLE Employees_Record')
            mydb.commit()
        #clear the treeview
            for child in self.data_tree.get_children():
                self.data_tree.delete(child)
            self.data_tree.insert("","end",text="",values=("","","","","",""))
    #----insert treeview-----
    def insert_treeview(self):
        #Check table is exists or not
        self.item_table = 'EMPLOYEES_RECORD'
        self.table_show_query = 'SHOW TABLES'
        my_cursor.execute(self.table_show_query)
        self.tables_list = my_cursor.fetchall()
        self.results_list = [item[0] for item in self.tables_list] # Conversion to list of str
        if self.item_table in str(self.results_list).upper():
            self.treeview_data()     #table found then update treview data
        else:
            self.data_tree.insert("","end",text="",values=("","","","","",""))    #table not found then insert empty line
    #----Udate treeview-------
    def treeview_data(self):
        # delete old data 
        for child in self.data_tree.get_children():
            self.data_tree.delete(child)
        #input new data from database
        my_cursor.execute('SELECT Empl_id,Empl_name,Empl_gender,Empl_number,Empl_address,Empl_type FROM Employees_Record')
        self.results=my_cursor.fetchall()
        for record in self.results:
            self.data_tree.insert("","end",text="",values=(record[0],record[1],record[2],record[3],record[4],record[5]))
    def back_b(self,event):
        self.empl_reg_win.destroy()
class category_reg_win:
    def __init__(self):
        self.menu_win=Toplevel()
        self.menu_win.title("Category Registration")
        self.menu_win.geometry('420x470+465+180')
        self.menu_win.config(bg=background)
        self.back_icon=ImageTk.PhotoImage(Image.open('icons\\back.png'))
        self.main_frame=Frame(self.menu_win,bg=background)
        self.main_frame.grid(row=0,column=0,pady=5)
        self.body_frame=Frame(self.menu_win,bg=background)
        self.body_frame.grid(row=1,column=0)
        main_font=Font(family="candara",size=14,weight='normal')
        self.regno_l=Label(self.body_frame,text="Regristration No. *",font=main_font,bg=background,bd=1,fg=foreground)
        self.regno_l.grid(row=1,column=0,pady=10,padx=10,sticky=t.W)
        self.reg_e=Entry(self.body_frame,font=main_font,width=14,bd=2,bg='white',fg=foreground)
        self.reg_e.grid(row=1,column=1,pady=10,padx=2,sticky=t.W)
        self.reg_e.focus()
        self.reg_e.insert(END,"CAT-01")
        self.reg_e.bind("<Return>",lambda event: self.unit_combobox.focus())
        self.reg_e.bind("<Down>",lambda event: self.unit_combobox.focus())
        self.unit_l=Label(self.body_frame,text="Unit *",font=main_font,bg=background,bd=1,fg=foreground)
        self.unit_l.grid(row=2,column=0,pady=10,padx=10,sticky=t.W)
        self.unit_combobox=ttk.Combobox(self.body_frame,width=13,font=main_font)
        self.unit_combobox["values"]=('Piece','Plate','Bottle','Cup','Kilogram') 
        self.unit_combobox.option_add('*TCombobox*Listbox.font',("candara",16))
        self.unit_combobox.grid(row=2,column=1,pady=10,padx=5,sticky=t.W)
        self.unit_combobox.insert(END,"")
        self.unit_combobox.bind("<Return>",lambda event: self.Add_func())
        self.add=Button(self.body_frame,text="Add",bg=background,fg=foreground,bd=2,font="candara 12 bold",width=5,activebackground=background,command=self.Add_func)
        self.add.grid(row=3,column=0)
        self.delete=Button(self.body_frame,text="Delete",bg=background,fg=foreground,bd=2,font="candara 12 bold",width=8,activebackground=background,command=self.delete_func)
        self.delete.grid(row=3,column=1,sticky=t.W,padx=20)
        
        self.saved_item_frame=LabelFrame(self.body_frame,bg=background,font="candara 20",fg=foreground,bd=0)
        self.saved_item_frame.grid(row=4,column=0,padx=50,pady=10,columnspan=2)
        self.style=ttk.Style()  
        self.style.configure('mystyle.Treeview',highlightthickness=0,bd=0,background=background,fieldfbackground=background,foreground=foreground,font=('candara',12))
        self.style.configure('mystyle.Treeview.Heading',font=('candara',14,'bold'))
        self.style.layout('mystyle.Treeview',[('mystyle.Treeview.treearea',{'sticky':'nswe'})])
        self.tree_frame=Frame(self.saved_item_frame,bg=background)
        self.tree_frame.grid()
        self.vertical_scrollbar=ttk.Scrollbar(self.tree_frame)
        self.vertical_scrollbar.grid(row=0,column=1,sticky='ns')
        self.data_tree=ttk.Treeview(self.tree_frame,style="mystyle.Treeview",yscrollcommand=self.vertical_scrollbar.set)
        self.vertical_scrollbar.config(command=self.data_tree.yview)
        self.data_tree['columns']=('0','1')
        self.data_tree.column("#0",width=20,stretch=NO)
        self.data_tree.column("0",width=100,stretch=NO)
        self.data_tree.column("1",width=200,stretch=NO)
        self.data_tree.heading("0",text="Reg No",anchor=t.W)
        self.data_tree.heading("1",text="Units",anchor=t.W)
        #---------insert data------------
        self.insert_treeview() 
        self.data_tree.grid(row=0,column=0)      
        self.back=Button(self.saved_item_frame,text='Back',font='candara 12 bold',bd=2,width=5,bg=background,fg=foreground,activebackground=background,command=self.menu_win.destroy)
        self.back.grid(row=1,column=0,pady=10,sticky=t.W,padx=40)
        self.delete_all=Button(self.saved_item_frame,text="Delete all",width=10,bg=background,fg=foreground,bd=2,font="candara 12 bold",activebackground=background,command=self.delete_all_func)
        self.delete_all.grid(row=1,column=0,padx=40,sticky=t.E)
        self.menu_win.bind("<Escape>",self.back_b)
        self.menu_win.focus()
        self.menu_win.resizable(0,0)
        self.menu_win.attributes('-toolwindow', True)
    #----Add data in Database----
    def Add_func(self):
        my_cursor.execute(
            '''CREATE TABLE IF NOT EXISTS 
        Category_Record(
            Regn_no varchar(255),
            Unit_name varchar(255)
            )'''
        )
        self.add_query='''INSERT INTO Category_Record(Regn_no,Unit_name) VALUES(%s,%s)'''
        my_cursor.execute(self.add_query,
        (self.reg_e.get(),str(self.unit_combobox.get()).title())
        )
        mydb.commit()
        self.treeview_data()
        self.reg_e.delete(0,END)
        self.unit_combobox.delete(0,END)
    #-----Delete item from selection---
    def insert_treeview(self):
        #Check table is exists or not
        self.item_table = 'CATEGORY_RECORD'
        self.table_show_query = 'SHOW TABLES'
        my_cursor.execute(self.table_show_query)
        self.tables_list = my_cursor.fetchall()
        self.results_list = [item[0] for item in self.tables_list] # Conversion to list of str
        if self.item_table in str(self.results_list).upper():
            self.treeview_data()     #table found then update treview data
        else:
            self.data_tree.insert("","end",text="",values=("",""))    #table not found then insert empty line
    #----Udate treeview-------
    def treeview_data(self):
        # delete old data 
        for child in self.data_tree.get_children():
            self.data_tree.delete(child)
        #input new data from database
        my_cursor.execute('SELECT Regn_no,Unit_name from Category_Record')
        self.results=my_cursor.fetchall()
        for record in self.results:
            self.data_tree.insert("","end",text="",values=(record[0],record[1]))
    def back_b(self,event):
        self.menu_win.destroy()
    def delete_func(self):
        try:
            self.delete_data=self.data_tree.item(self.data_tree.focus())['values']     # getting the list of selected area 
            self.delete_query='DELETE FROM Category_Record WHERE Regn_no=%s AND Unit_name=%s'
            my_cursor.execute(self.delete_query,(self.delete_data[0],self.delete_data[1]))
            mydb.commit()
            self.treeview_data()
        except:
            messagebox.showerror(parent=self.menu_win,title='Error',message="Please Select any Item") 

    def delete_all_func(self):
        if messagebox.askyesno(parent=self.menu_win,title='Clear everything',message='Are you sure?'):
            my_cursor.execute('DROP TABLE Category_Record')
            mydb.commit()
        #clear the treeview
            for child in self.data_tree.get_children():
                self.data_tree.delete(child)
            self.data_tree.insert("","end",text="",values=("",""))
    #----insert treeview-----         
class raw_items:
    def __init__(self):
        self.raw_win=Toplevel()
        self.raw_win.title("Raw Items Register")
        self.raw_win.state("zoomed")
        self.raw_win.config(bg=background)
        self.frame_banner=Frame(self.raw_win,bg=background)
        self.frame_banner.grid(row=0,column=0)
        self.banner_img=Image.open('icons\\home_ban.jpg')
        self.banner_img=self.banner_img.resize((self.raw_win.winfo_screenwidth(),150),Image.ANTIALIAS)
        self.main_banner=ImageTk.PhotoImage(self.banner_img)
        self.banner_lbl=Label(self.frame_banner,image=self.main_banner,bg=background)
        self.banner_lbl.grid(row=0,column=0)
        self.body_frame=Frame(self.raw_win,bg=background)
        self.body_frame.grid(row=1,column=0,pady=15)
        self.add_icon=ImageTk.PhotoImage(Image.open('icons\\add.png'))
        self.edit_icon=ImageTk.PhotoImage(Image.open('icons\\edit.png'))
        self.view_icon=ImageTk.PhotoImage(Image.open('icons\\view.png'))
        self.back_icon=ImageTk.PhotoImage(Image.open('icons\\back.png'))
        self.delete_icon=ImageTk.PhotoImage(Image.open('icons\\delete.png'))
        self.menu_banner_image=ImageTk.PhotoImage(Image.open('icons\\menu_ico.png'))
        self.menu_ban=Label(self.body_frame,text=" RAW MATERIALS",font="Helvetica 40 bold",image=self.menu_banner_image,compound="left",bd=0,bg=background,fg=foreground,activebackground=background)
        self.menu_ban.grid(row=0,column=0,pady=15)
        self.add_item=Button(self.body_frame,image=self.add_icon,bd=0,bg=background,fg=foreground,activebackground=background)
        self.add_item.grid(row=1,column=0,pady=15)
        self.edit_item=Button(self.body_frame,image=self.edit_icon,bd=0,bg=background,fg=foreground,activebackground=background)
        self.edit_item.grid(row=2,column=0,pady=15)
        self.view_item=Button(self.body_frame,image=self.view_icon,bd=0,bg=background,fg=foreground,activebackground=background)
        self.view_item.grid(row=3,column=0,pady=15)
        self.delete_item=Button(self.body_frame,image=self.delete_icon,bd=0,bg=background,fg=foreground,activebackground=background)
        self.delete_item.grid(row=4,column=0,pady=15)
        self.back=Button(self.body_frame,image=self.back_icon,command=self.raw_win.destroy,bd=0,bg=background,fg=foreground,activebackground=background)
        self.back.grid(row=5,column=0,pady=15)
        self.raw_win.bind("<Escape>",self.destroy)
        self.raw_win.attributes('-toolwindow', True)
       #self.raw_win.mainloop()
    def destroy(self,event):
        self.raw_win.destroy()  

#_____________________________________________BILLING___________________________________________________________________
class BILLING:
    def __init__(self):
        self.billing_win=Toplevel()
        self.billing_win.state('zoomed')
        self.billing_win.config(bg=background)
        self.frame_banner=Frame(self.billing_win,bg=background)
        self.frame_banner.grid(row=0,column=0)
        self.banner_img=Image.open('icons\\home_ban.jpg')
        self.banner_img=self.banner_img.resize((self.billing_win.winfo_screenwidth(),150),Image.ANTIALIAS)
        self.main_banner=ImageTk.PhotoImage(self.banner_img)
        self.Exit_icon=ImageTk.PhotoImage(Image.open('icons\\back.png'))
        self.kot_icon=ImageTk.PhotoImage(Image.open('icons\\kot_ico.png'))
        self.pos_icon=ImageTk.PhotoImage(Image.open('icons\\pos_ico.png'))
        self.paymnet_icon=ImageTk.PhotoImage(Image.open('icons\\payment_ico.png'))
        self.invoice_setting_icon=ImageTk.PhotoImage(Image.open('icons\\invoice_setting_ico.png'))
        self.banner_lbl=Label(self.frame_banner,image=self.main_banner,bg=background)
        self.banner_lbl.grid(row=0,column=0)
        self.body_frame=Frame(self.billing_win,bg=background)
        self.body_frame.grid(row=1,column=0) 
        self.frame1=Frame(self.body_frame,bg=background)
        self.frame1.grid(row=0,column=0,sticky=t.W,pady=60,padx=70)
        self.frame2=Frame(self.body_frame,bg=background)
        self.frame2.grid(row=0,column=2,padx=50)
        self.frame3=Frame(self.body_frame,bg=background)
        self.frame3.grid(row=1,column=0,sticky=t.W,padx=50)
        self.frame4=Frame(self.body_frame,bg=background)
        self.frame4.grid(row=1, column=2,padx=50)
        self.billing_font=Font(family="candara",size=20,weight="bold")
        self.kot_b=Button(self.frame1,text='KOT',image=self.kot_icon,bg=background,fg=foreground,bd=0,font=self.billing_font,activebackground=background,compound='top',command=self.kot_func)
        self.kot_b.grid()
        self.pos_b=Button(self.frame2,text='POS',bg=background,image=self.pos_icon,fg=foreground,bd=0,font=self.billing_font,activebackground=background,compound='top',command=self.pos_func)
        self.pos_b.grid()
        self.payment_b=Button(self.frame3,text='Payment',image=self.paymnet_icon,bg=background,fg=foreground,bd=0,font=self.billing_font,activebackground=background,compound='top')
        self.payment_b.grid()
        self.invoice_setting_b=Button(self.frame4,text='Invoice setting',image=self.invoice_setting_icon,bg=background,fg=foreground,bd=0,font=self.billing_font,activebackground=background,compound='top')
        self.invoice_setting_b.grid()
        self.back_b=Button(self.body_frame,image=self.Exit_icon,bg=background,fg=foreground,bd=0,font=self.billing_font,activebackground=background,command=self.billing_win.destroy)
        self.back_b.grid(row=2,column=1,pady=20)
        self.billing_win.bind("<Escape>",lambda event: self.billing_win.destroy())
        self.billing_win.resizable(0,0)
        self.billing_win.attributes('-toolwindow', True)
    def kot_func(self):
        KOT()
    def pos_func(self):
        POS()    
class KOT:
    def __init__(self):
        self.kot_win=Toplevel(class_='AutocompleteEntry demo')
        self.kot_win.state('zoomed')
        self.kot_win.config(bg=background)
        self.frame_banner=Frame(self.kot_win,bg=background)
        self.frame_banner.grid(row=0,column=0)
        self.banner_img=Image.open('icons\\home_ban_copy.jpg')
        self.banner_img=self.banner_img.resize((self.kot_win.winfo_screenwidth(),150),Image.ANTIALIAS)
        self.main_banner=ImageTk.PhotoImage(self.banner_img)
        self.Exit_icon=ImageTk.PhotoImage(Image.open('icons\\back.png'))
        self.banner_lbl=Label(self.frame_banner,image=self.main_banner,bg=background)
        self.banner_lbl.grid(row=0,column=0)
        self.body_frame=Frame(self.kot_win,bg=background)
        self.body_frame.grid(row=1,column=0)
        self.header_frame=Frame(self.body_frame,bg=background)
        self.header_frame.grid(row=0,column=0)
        self.new_kot_label=Label(self.header_frame,text='New KOT Generate    ',font='candara 30 bold',bg=background,fg=foreground)
        self.new_kot_label.grid(row=0,column=0,padx=80)
        #----------icons----------------------
        self.reorder_ico=ImageTk.PhotoImage(Image.open('icons\\re_order.png'))
        self.bill_payment_ico=ImageTk.PhotoImage(Image.open('icons\\bill_payment.png'))
        self.bill_generate_ico=ImageTk.PhotoImage(Image.open('icons\\bill_generate.png'))
        self.new_kot_ico=ImageTk.PhotoImage(Image.open('icons\\delete.png'))
        self.addcart_ico=ImageTk.PhotoImage(Image.open('icons\\add_ico.png'))
        self.submit_ico=ImageTk.PhotoImage(Image.open('icons\\subm.jpg'))
        self.delete_ico=ImageTk.PhotoImage(Image.open('icons\\del.jpg'))
        #----------------Shortcut buttons-----------------
        self.main_font=Font(family="candara",size=16,weight='normal')
        self.reorder=Button(self.header_frame,image=self.reorder_ico,bg=background,activebackground=background,bd=0)
        self.reorder.grid(row=0,column=1,padx=30)
        self.bill_payment=Button(self.header_frame,image=self.bill_payment_ico,bg=background,activebackground=background,bd=0)
        self.bill_payment.grid(row=0,column=2,padx=30)
        self.bill_generate=Button(self.header_frame,image=self.bill_generate_ico,bg=background,activebackground=background,bd=0)
        self.bill_generate.grid(row=0,column=3,padx=30)
        #------------------------------------------------
        self.primary_body_frame=Frame(self.body_frame,bg=background,bd=0)
        self.primary_body_frame.grid(row=1,column=0,pady=40)
        self.disc_body_frame=Frame(self.primary_body_frame,bg=background,bd=0)
        self.disc_body_frame.grid(row=0,column=0)
        self.waiter_l=Label(self.disc_body_frame,text='Waiter Name',bg=background,fg=foreground,bd=0,font=self.main_font)
        self.waiter_l.grid(row=0,column=0,sticky=t.W,padx=15)
        #------------fetch Waiters name----------------
        self.combo_values=[]
        try:
            my_cursor.execute('SELECT Empl_name,Empl_type FROM employees_Record ')
            self.Category_list=my_cursor.fetchall()
            for cat in self.Category_list:
                if cat[1] == 'Waiter':
                    self.combo_values.append(cat[0])
        except:
            self.combo_values.append('None')
        #-----------------------------------
        self.waiter_combobox=AutocompleteCombobox(self.disc_body_frame,width=18,font='candara 17')
        self.waiter_combobox["values"]=self.combo_values
        self.waiter_combobox.option_add('*TCombobox*Listbox.font',("candara",16))
        self.waiter_combobox.grid(row=1,column=0,sticky=t.W,padx=20)
        self.waiter_combobox.set_completion_list(self.combo_values)
        self.waiter_combobox.focus()
        self.waiter_combobox.bind('<Return>',lambda event: self.table_combobox.focus())
        self.waiter_combobox.bind('<Right>',lambda event: self.table_combobox.focus())

        self.table_l=Label(self.disc_body_frame,text='Table *',bg=background,fg=foreground,bd=0,font=self.main_font)
        self.table_l.grid(row=0,column=1,sticky=t.W,padx=20)
        self.table_combobox=ttk.Combobox(self.disc_body_frame,width=16,font='candara 17')
        self.table_combobox["values"]=['1','2','3','4','5']
        self.table_combobox.option_add('*TCombobox*Listbox.font',("candara",16))
        self.table_combobox.grid(row=1,column=1,padx=30)
        self.table_combobox.bind('<Return>',lambda event: self.item_combobox.focus())
        self.table_combobox.bind('<Right>',lambda event: self.date_en.focus())
        self.table_combobox.bind('<Left>',lambda event: self.waiter_combobox.focus())   

        self.kot_l=Label(self.disc_body_frame,text='KOT NO *',bg=background,fg=foreground,bd=0,font=self.main_font)
        self.kot_l.grid(row=0,column=2,sticky=t.W,padx=22)
        self.kot_en=Entry(self.disc_body_frame,width=14,bg='white',fg=foreground,font='candara 17',bd=2)
        self.kot_en.grid(row=1,column=2,padx=30)
        self.kot_en.insert(END,50*random.randint(50,100))
        self.kot_en.config(state='readonly')

        self.date_l=Label(self.disc_body_frame,text='Date Time',bg=background,fg=foreground,bd=0,font=self.main_font)
        self.date_l.grid(row=0,column=3,sticky=t.W,padx=20)
        self.date_en=Entry(self.disc_body_frame,width=17,bg='white',fg=foreground,font='candara 17',bd=2)
        self.date_en.grid(row=1,column=3,sticky=t.E,padx=20)
        self.date_en.insert(END,str(date.today().strftime('%d/%m/%y')+str(' | ')+datetime.now().strftime('%H:%M:%S')))
        self.date_en.bind('<Return>',lambda event: self.item_combobox.focus())
        self.date_en.bind('<Right>',lambda event: self.item_combobox.focus())
        self.date_en.bind('<Left>',lambda event: self.item_combobox.focus())  

        self.empty_l=Label(self.disc_body_frame,bg=background,fg=foreground,bd=0,font=self.main_font)
        self.empty_l.grid(row=2,column=0)
        self.item_l=Label(self.disc_body_frame,text='Item *',bg=background,fg=foreground,bd=0,font=self.main_font)
        self.item_l.grid(row=3,column=0,sticky=t.W,padx=20)
        self.quantity_l=Label(self.disc_body_frame,text='Quantity *',bg=background,fg=foreground,bd=0,font=self.main_font)
        self.quantity_l.grid(row=3,column=1,sticky=t.W,padx=30)
        self.rate_l=Label(self.disc_body_frame,text='Rate *',bg=background,fg=foreground,bd=0,font=self.main_font)
        self.rate_l.grid(row=3,column=2,sticky=t.W,padx=30)
        self.unit_l=Label(self.disc_body_frame,text='Unit',bg=background,fg=foreground,bd=0,font=self.main_font)
        self.unit_l.grid(row=3,column=3,sticky=t.W,padx=30)

       #------------fetch items name----------------
        self.combo_items=[]
        try:
            my_cursor.execute('SELECT Item_name FROM Items_Record')
            self.items_list=my_cursor.fetchall()
            for c in self.items_list:
                self.combo_items.append(c[0])
        except:
            self.combo_items.append('None')
        #-----------------------------------
        self.item_combobox=AutocompleteCombobox(self.disc_body_frame,width=18,font='candara 17')
        self.item_combobox["values"]=self.combo_items
        self.item_combobox.option_add('*TCombobox*Listbox.font',("candara",16))
        self.item_combobox.grid(row=4,column=0,sticky=t.W,padx=20)
        self.item_combobox.set_completion_list(self.combo_items)
        self.item_combobox.focus()
        self.item_combobox.bind('<Right>',lambda event: self.table_combobox.focus())
        self.item_combobox.bind('<Return>',self.item_return)
        self.item_combobox.bind('<Up>',lambda event: self.waiter_combobox.focus())

        self.quantity_en=Entry(self.disc_body_frame,width=17,bg='white',fg=foreground,font='candara 17',bd=2)
        self.quantity_en.grid(row=4,column=1,padx=20)
        self.quantity_validation=self.quantity_en.register(correct)                                # Input only Integer type
        self.quantity_en.config(validate="key",validatecommand=(self.quantity_validation,"%P"))
        self.quantity_en.bind('<Return>',self.quantity_func)

        self.rate_en=Entry(self.disc_body_frame,width=14,bg='white',fg=foreground,font='candara 17',bd=2)
        self.rate_en.grid(row=4,column=2,padx=20)
        self.rate_validation=self.rate_en.register(correct)                                # Input only Integer type
        self.rate_en.config(validate="key",validatecommand=(self.rate_validation,"%P"))
        self.rate_en.bind('<Return>',lambda event: self.addcart_func())

        self.unit_add_frame=Frame(self.disc_body_frame,bg=background,bd=0)
        self.unit_add_frame.grid(row=4,column=3)
        self.unit_en=Entry(self.unit_add_frame,width=11,bg='white',fg=foreground,font='candara 17',bd=2)
        self.unit_en.grid(row=0,column=0)
        self.addcart=Button(self.unit_add_frame,image=self.addcart_ico,bg=background,activebackground=background,bd=0,command=self.addcart_func)
        self.addcart.grid(row=0,column=1)
        self.addcart.bind('<Return>',lambda event: self.addcart_func())
        self.cart_frame=Frame(self.primary_body_frame,bg=background)
        self.cart_frame.grid(row=1,column=0,pady=10)
        self.cart_label=Label(self.cart_frame,bg=background,font='candara 16 bold',bd=0,text='Selected Items List',width=96,fg=foreground)
        self.cart_label.grid(row=1,column=0)
        self.tree_view()
        self.quantity_list=[]
        self.amount_list=[]
        self.total_quantity_value=0
        self.total_amount_value=0
        self.kot_win.bind("<Escape>",lambda event: self.kot_win.destroy())
        self.kot_win.resizable(0,0)
        self.kot_win.attributes('-toolwindow', True)
    def item_return(self,event):
        '''this function check the item in database if not found it return list of items'''
        item_discription=self.item_func()
        if self.item_combobox.get() in  item_discription:
            self.quantity_en.focus()
        else:
            self.item_combobox.focus()
    def item_func(self):
        ''' This function check the item in database if item is found it return Discription of item'''
        my_cursor.execute('SELECT Item_name,Rate,Category FROM Items_Record')
        data=my_cursor.fetchall()
        item_discription=()
        for item in data:
            if self.item_combobox.get() in item:
                item_discription=item
        return item_discription
    def quantity_func(self,event):
        '''This function automate the item rate and unit''' 
        self.item=self.item_func()
        self.rate_en.insert(END,int(self.item[1]))
        self.unit_en.insert(END,self.item[2])
        self.unit_en.config(state='readonly')
        self.addcart.focus()
    def addcart_func(self):
        '''This function insert data in tree view and create buttons'''
        if self.unit_en.get() =="":
            messagebox.showerror(parent=self.kot_win,title='Error',message='Please add Item Discription')
        else:
            self.insert_treeview()
            self.item_combobox.delete(0,END)
            self.quantity_en.delete(0,END)
            self.rate_en.delete(0,END)
            self.unit_en.delete(0,END)
            self.item_combobox.focus()
            self.submit_b=Button(self.cart_frame,bg=background,image=self.submit_ico,activebackground=background,bd=0,command=self.kot)
            self.submit_b.grid(row=4,column=0,sticky=E,pady=10)
            self.delete_b=Button(self.cart_frame,image=self.delete_ico,bg=background,bd=0,activebackground=background)
            self.delete_b.grid(row=4,column=0,sticky=E,padx=150,pady=10)
            self.cart_frame.grid(row=1,column=0)
    def kot(self):   
        dir=os.path.dirname(reportlab.__file__)
        font_folder=os.path.join(dir,'fonts')
        custom_font_folder=os.path.join(font_folder,'sans.ttf')
        custom_font=TTFont('sans',custom_font_folder)
        pdfmetrics.registerFont(custom_font)
        custom_font_folder1=os.path.join(font_folder,'sans bold.ttf')
        custom_font1=TTFont('sans bold',custom_font_folder1)
        pdfmetrics.registerFont(custom_font1)
        self.cart=[]
        for line in self.data_tree.get_children():
            for value in self.data_tree.item(line)['values']:
                self.cart.append(value)
        self.item=[]  
        self.quan=[] 
        self.l=len(self.cart) 
        i=0
        j=1
        while i<self.l:
            self.item.append(self.cart[i])
            i=i+5
        while j<self.l:
            self.quan.append(self.cart[j])
            j=j+5
        pagesize=(58 * mm, (42+(5*len(self.item)))*mm)
        pdf=canvas.Canvas('KOT.pdf',pagesize=pagesize)
        q=((240/92)*(42+(5*len(self.item))))
        pdf=canvas.Canvas('KOT.pdf',pagesize=pagesize)
        pdf.setFont("sans bold",10)
        pdf.drawString(45,q,"ABC RESTUARANT")
        pdf.setFont("sans",8)
        pdf.drawString(15,q-6,"---------------------------------")
        pdf.drawString(22,q-13,"Address line 1, Address line 2")
        pdf.drawString(53,q-22,"Contact details")
        pdf.drawString(15,q-27,"---------------------------------")
        pdf.setFont("sans bold",9)
        pdf.drawString(75,q-38,"KOT")
        pdf.setFont("sans",8)
        pdf.drawString(10,q-50,'Ticket No:')
        pdf.drawString(52,q-50,self.kot_en.get())
        pdf.drawString(100,q-50,"Waiter:")
        pdf.drawString(130,q-50,self.waiter_combobox.get())
        pdf.drawString(10,q-57,'Table No :')
        pdf.drawString(52,q-57,self.table_combobox.get())
        pdf.drawString(10,q-64,"Date :")
        pdf.drawString(35,q-64,self.date_en.get())
        pdf.drawString(9,q-70,"-------------------------------------")
        pdf.setFont("sans",9)
        pdf.drawString(10,q-77,'Item')
        pdf.drawString(120,q-77,'Quantity')
        pdf.setFont("sans",8)
        pdf.drawString(9,q-83,"-------------------------------------")
        for k in self.item:
            s=str(k)
            pdf.drawString(9,y,s)
            y=y-10
        y=q-90   
        for l in self.quan:
            u=str(l) 
            pdf.drawString(135,y,u)
            y=y-10
        y=((q-90)-(len(self.item)*10))
        pdf.drawString(9,y,"-------------------------------------")
        pdf.setFont("sans bold",9)
        pdf.drawString(70,y-8,'Total Quantity :')
        pdf.drawString(133,y-8,str(self.total_quantity_value))
        pdf.setFont("sans",8)
        pdf.drawString(9,y-16,"-------------------------------------")
        pdf.save()
        webbrowser.open_new("KOT.pdf") 
    def tree_view(self):
        '''This function creates the  Empty Tree view'''
        self.style=ttk.Style()  
        self.style.configure('mystyle.Treeview',highlightthickness=0,bd=0,background=background,fieldfbackground=background,foreground=foreground,font=('candara',12))
        self.style.configure('mystyle.Treeview.Heading',font=('candara',14,'bold'))
        self.style.layout('mystyle.Treeview',[('mystyle.Treeview.treearea',{'sticky':'nswe'})])
        self.tree_frame=Frame(self.cart_frame,bg=background)
        self.tree_frame.grid(row=2,column=0)
        self.vertical_scrollbar=ttk.Scrollbar(self.tree_frame)
        self.vertical_scrollbar.grid(row=0,column=1,sticky='ns')
        self.data_tree=ttk.Treeview(self.tree_frame,style="mystyle.Treeview",yscrollcommand=self.vertical_scrollbar.set)
        self.vertical_scrollbar.config(command=self.data_tree.yview)
        self.data_tree['columns']=('0','1','2','3','4')
        self.data_tree.column("#0",width=1)
        self.data_tree.column("0",width=260,anchor='center')
        self.data_tree.column("1",width=200,anchor='center')
        self.data_tree.column("2",width=200,anchor='center')
        self.data_tree.column("3",width=220,anchor='center')
        self.data_tree.column("4",width=160,anchor='center')
        self.data_tree.heading('#0',text='')
        self.data_tree.heading("0",text="Item")
        self.data_tree.heading("1",text="Quantity")
        self.data_tree.heading("2",text="Rate")
        self.data_tree.heading("3",text='Amount')
        self.data_tree.heading("4",text='Unit')
        self.data_tree.grid(row=0,column=0) 
    def insert_treeview(self):
        '''This function insert data in tree view'''
        quantity_var=self.quantity_en.get()
        if self.quantity_en.get() =="":
            quantity_var=1
        #insert new data from entry boxes
        self.data_tree.insert("","end",text="",values=(self.item_combobox.get(),quantity_var,self.rate_en.get(),int(quantity_var)*int(self.rate_en.get()),self.unit_en.get()))
        #fetch total quantity and total amount from treeview data
        self.quantity_list.append(self.data_tree.item(self.data_tree.get_children()[-1])['values'][1])
        self.amount_list.append(self.data_tree.item(self.data_tree.get_children()[-1])['values'][3])
        self.total_quantity_value=sum(self.quantity_list)
        self.total_amount_value=sum(self.amount_list)
        #labels of sub total, total quantity and total amount
        self.total_quantity=Label(self.cart_frame,bg='white',font='candara 16 bold',bd=0,text=str(self.total_quantity_value),width=46,fg=foreground)
        self.total_quantity.grid(row=3,column=0,sticky=W,padx=130)
        self.total_amount=Label(self.cart_frame,bg='white',font='candara 16 bold',bd=0,text=str(self.total_amount_value),width=46,fg=foreground)
        self.total_amount.grid(row=3,column=0,sticky=E)
        self.sub_total_l=Label(self.cart_frame,bg='white',font='candara 16 bold',bd=0,text='Sub Total',width=25,fg=foreground)
        self.sub_total_l.grid(row=3,column=0,sticky=W)
#------------------------------------------------------------------------------------------------------------------------
class POS:
    def __init__(self):
        self.pos_win=Toplevel(class_='AutocompleteEntry demo')
        self.pos_win.state('zoomed')
        self.pos_win.config(bg=background)
        self.frame_banner=Frame(self.pos_win,bg=background)
        self.frame_banner.grid(row=0,column=0)
        self.banner_img=Image.open('icons\\home_ban.jpg')
        self.banner_img=self.banner_img.resize((self.pos_win.winfo_screenwidth(),150),Image.ANTIALIAS)
        self.main_banner=ImageTk.PhotoImage(self.banner_img)
        self.Exit_icon=ImageTk.PhotoImage(Image.open('icons\\back.png'))
        self.banner_lbl=Label(self.frame_banner,image=self.main_banner,bg=background)
        self.banner_lbl.grid(row=0,column=0)
        self.body_frame=Frame(self.pos_win,bg=background)
        self.body_frame.grid(row=1,column=0)
        self.header_frame=Frame(self.body_frame,bg=background)
        self.header_frame.grid(row=0,column=0)
        self.new_kot_label=Label(self.header_frame,text='New POS Generate    ',font='candara 30 bold',bg=background,fg=foreground)
        self.new_kot_label.grid(row=0,column=0,padx=80)
        #----------icons----------------------
        self.reorder_ico=ImageTk.PhotoImage(Image.open('icons\\re_order.png'))
        self.bill_payment_ico=ImageTk.PhotoImage(Image.open('icons\\bill_payment.png'))
        self.bill_generate_ico=ImageTk.PhotoImage(Image.open('icons\\bill_generate.png'))
        self.new_kot_ico=ImageTk.PhotoImage(Image.open('icons\\delete.png'))
        self.addcart_ico=ImageTk.PhotoImage(Image.open('icons\\add_ico.png'))
        self.submit_ico=ImageTk.PhotoImage(Image.open('icons\\subm.jpg'))
        self.delete_ico=ImageTk.PhotoImage(Image.open('icons\\del.jpg'))
        #----------------Shortcut buttons-----------------
        self.main_font=Font(family="candara",size=16,weight='normal')
        self.reorder=Button(self.header_frame,image=self.reorder_ico,bg=background,activebackground=background,bd=0)
        self.reorder.grid(row=0,column=1,padx=30)
        self.bill_payment=Button(self.header_frame,image=self.bill_payment_ico,bg=background,activebackground=background,bd=0)
        self.bill_payment.grid(row=0,column=2,padx=30)
        self.bill_generate=Button(self.header_frame,image=self.bill_generate_ico,bg=background,activebackground=background,bd=0)
        self.bill_generate.grid(row=0,column=3,padx=30)
        #------------------------------------------------
        self.primary_body_frame=Frame(self.body_frame,bg=background,bd=0)
        self.primary_body_frame.grid(row=1,column=0,pady=40)
        self.disc_body_frame=Frame(self.primary_body_frame,bg=background,bd=0)
        self.disc_body_frame.grid(row=0,column=0)
        self.item_l=Label(self.disc_body_frame,text='Item *',bg=background,fg=foreground,bd=0,font=self.main_font)
        self.item_l.grid(row=3,column=0,sticky=t.W,padx=30)
        self.item_combo_values=[]
        self.rates=StringVar()
        self.selection=StringVar()
        self.rate=StringVar()
        self.unit=StringVar()
        try:
            my_cursor.execute('SELECT Item_name,Rate FROM Items_Record')
            self.Category_list=my_cursor.fetchall()
            for cat in self.Category_list:
                self.item_combo_values.append(cat[0])
        except:
            self.item_combo_values.append('None')
        self.item_combobox=AutocompleteCombobox(self.disc_body_frame,width=16,font='candara 17')
        self.item_combobox["values"]=self.item_combo_values
        self.item_combobox.option_add('*TCombobox*Listbox.font',("candara",15))
        self.item_combobox.grid(row=4,column=0,sticky=t.W,padx=30)
        self.item_combobox.set_completion_list(self.item_combo_values)
        self.item_combobox.focus()
        self.item_combobox.bind('<Return>',self.item_return)
        self.item_combobox.bind('<Right>',lambda event: self.quantity_en.focus())   
        self.quantity_l=Label(self.disc_body_frame,text='Quantity *',bg=background,fg=foreground,bd=0,font=self.main_font)
        self.quantity_l.grid(row=3,column=1,sticky=t.W,padx=100)
        self.quantity_en=Entry(self.disc_body_frame,width=17,bg='white',fg=foreground,font='candara 17',bd=2)
        self.quantity_en.grid(row=4,column=1,padx=100,sticky=t.W)
        self.quantity_validation=self.quantity_en.register(correct)                                # Input only Integer type
        self.quantity_en.config(validate="key",validatecommand=(self.quantity_validation,"%P"))
        self.quantity_en.bind('<Return>',self.quantity_func)
        self.quantity_en.bind('<Right>',self.quantity_func)
        self.quantity_en.bind('<Left>',lambda event: self.item_combobox.focus())
        self.rate_l=Label(self.disc_body_frame,text='Rate *',bg=background,fg=foreground,bd=0,font=self.main_font)
        self.rate_l.grid(row=3,column=2,sticky=t.W,padx=30)
        self.rate_en=Entry(self.disc_body_frame,width=16,textvariable=self.rate,bg='white',fg=foreground,font='candara 17',bd=2)
        self.rate_en.grid(row=4,column=2,padx=30,sticky=t.W)
        self.rate_validation=self.rate_en.register(correct)                                # Input only Integer type
        self.rate_en.config(validate="key",validatecommand=(self.rate_validation,"%P"))
        self.rate_en.bind('<Return>',lambda event:self.addcart_func())
        self.rate_en.bind('<Left>',lambda event: self.quantity_en.focus())
        self.rate_en.bind('<Right>',lambda event:self.addcart_func())
        self.invoice_l=Label(self.disc_body_frame,text='Invoice No. *',bg=background,fg=foreground,bd=0,font=self.main_font)
        self.invoice_l.grid(row=0,column=0,sticky=t.W,padx=30)
        self.invoice_en=Entry(self.disc_body_frame,width=14,bg='white',fg=foreground,font='candara 17',bd=2)
        self.invoice_en.grid(row=1,column=0,padx=30,sticky=t.W)
        self.invoice_en.insert(END,50*random.randint(50,100))
        self.invoice_en.config(state='readonly')
        self.date_l=Label(self.disc_body_frame,text='Date Time',bg=background,fg=foreground,bd=0,font=self.main_font)
        self.date_l.grid(row=0,column=1,sticky=t.W,padx=100)
        self.date_en=Entry(self.disc_body_frame,width=15,bg='white',fg=foreground,font='candara 17',bd=2)
        self.date_en.grid(row=1,column=1,sticky=t.W,padx=100)
        self.date_en.insert(END,str(date.today().strftime('%d/%m/%y')+str(' | ')+datetime.now().strftime('%H:%M:%S')))
        self.date_en.bind('<Return>',lambda event: self.item_combobox.focus())
        self.date_en.bind('<Right>',lambda event: self.item_combobox.focus())
        self.unit_l=Label(self.disc_body_frame,text='Unit',bg=background,fg=foreground,bd=0,font=self.main_font)
        self.unit_l.grid(row=0,column=2,sticky=t.W,padx=30)
        self.unit_add_frame=Frame(self.disc_body_frame,bg=background,bd=0)
        self.unit_add_frame.grid(row=1,column=2,padx=10)
        self.unit_en=Entry(self.unit_add_frame,textvariable=self.unit,width=11,bg='white',fg=foreground,font='candara 17',bd=2)
        self.unit_en.grid(row=0,column=0)
        self.unit_en.bind('<Return>',lambda event:self.addcart_func())
        self.unit_en.bind('<Up>',lambda event:self.rate_en.focus())
        self.unit_en.bind('<Right>',lambda event:self.rate_en.focus())
        self.addcart=Button(self.unit_add_frame,image=self.addcart_ico,bg=background,activebackground=background,bd=0,command=self.addcart_func)
        self.addcart.grid(row=0,column=1)
        self.addcart.bind('<Return>',lambda event: self.addcart_func())
        self.empty_l=Label(self.disc_body_frame,bg=background,fg=foreground,bd=0,font=self.main_font)
        self.empty_l.grid(row=2,column=0)
        self.cart_frame=Frame(self.primary_body_frame,bg=background)
        self.cart_frame.grid(row=1,column=0,pady=10)
        self.cart_label=Label(self.cart_frame,bg=background,font='candara 16 bold',bd=0,text='Selected Items List',width=96,fg=foreground)
        self.cart_label.grid(row=1,column=0)
        self.tree_view()
        self.quantity_list=[]
        self.amount_list=[]
        self.total_quantity_value=0
        self.total_amount_value=0
        self.pos_win.bind("<Escape>",lambda event: self.pos_win.destroy())
        self.pos_win.resizable(0,0)
        self.pos_win.attributes('-toolwindow', True)
    def item_return(self,event):
        '''this function check the item in database if not found it return list of items'''
        item_discription=self.item_func()
        if self.item_combobox.get() in  item_discription:
            self.quantity_en.focus()
        else:
            self.item_combobox.focus()
    def item_func(self):
        ''' This function check the item in database if item is found it return Discription of item'''
        my_cursor.execute('SELECT Item_name,Rate,Category FROM Items_Record')
        data=my_cursor.fetchall()
        item_discription=()
        for item in data:
            if self.item_combobox.get() in item:
                item_discription=item
        return item_discription
    def quantity_func(self,event):
         '''This function automate the item rate and unit''' 
         self.item=self.item_func()
         self.rate_en.insert(END,int(self.item[1]))
         self.unit_en.delete(0,END)
         self.unit_en.insert(END,self.item[2])
         self.unit_en.config(state='readonly')
         self.addcart.focus()
    def addcart_func(self):
        '''This function insert data in tree view and create buttons'''
        if self.unit_en.get() =="":
            messagebox.showerror(parent=self.pos_win,title='Error',message='Please add Item Discription')
        else:
            self.insert_treeview() 
            self.quantity_en.delete(0,END)
            self.rate_en.delete(0,END)
            self.unit_en.delete(0,END)
            self.item_combobox.set('')
            self.item_combobox.SelectedIndex=-1
            self.item_combobox.focus()
            self.submit_b=Button(self.cart_frame,bg=background,image=self.submit_ico,activebackground=background,bd=0,command=self.pdf)
            self.submit_b.grid(row=4,column=0,sticky=E,pady=10)
            self.delete_b=Button(self.cart_frame,image=self.delete_ico,bg=background,bd=0,activebackground=background)
            self.delete_b.grid(row=4,column=0,sticky=E,padx=150,pady=10)
            self.cart_frame.grid(row=1,column=0)
    def pdf(self):
        dir=os.path.dirname(reportlab.__file__)
        font_folder=os.path.join(dir,'fonts')
        custom_font_folder=os.path.join(font_folder,'sans.ttf')
        custom_font=TTFont('sans',custom_font_folder)
        pdfmetrics.registerFont(custom_font)
        custom_font_folder1=os.path.join(font_folder,'sans bold.ttf')
        custom_font1=TTFont('sans bold',custom_font_folder1)
        pdfmetrics.registerFont(custom_font1)
        self.cart=[]
        for line in self.data_tree.get_children():
            for value in self.data_tree.item(line)['values']:
                self.cart.append(value)
        self.item=[]  
        self.quan=[] 
        self.rate=[]
        self.price=[] 
        self.l=len(self.cart) 
        i=0
        j=1
        k=2
        l=3
        while i<self.l:
            self.item.append(self.cart[i])
            i=i+5
        while j<self.l:
            self.quan.append(self.cart[j])
            j=j+5
        while k<self.l:
            self.rate.append(self.cart[k])
            k=k+5    
        while l<self.l:
            self.price.append(self.cart[l])
            l=l+5    
        pagesize=(58 * mm, (60+(4*len(self.item)))*mm)
        pdf=canvas.Canvas('POS.pdf',pagesize=pagesize)
        pdf.setFont("sans bold",10)
        q=((240/92)*(60+(4*len(self.item))))
        pdf.drawString(45,q,"ABC RESTUARANT")
        pdf.setFont("sans",8)
        pdf.drawString(15,q-6,"---------------------------------")
        pdf.drawString(22,q-13,"Address line 1, Address line 2")
        pdf.drawString(53,q-22,"Contact details")
        pdf.drawString(15,q-27,"---------------------------------")
        pdf.setFont("sans bold",9)
        pdf.drawString(56,q-38,"TAX INVOICE")
        pdf.setFont("sans",8)
        pdf.drawString(10,q-50,"Invoice No : ")
        pdf.drawString(60,q-50,self.invoice_en.get())
        pdf.drawString(10,q-57,"Date : ")
        pdf.drawString(38,q-57,self.date_en.get())
        pdf.drawString(9,q-67,"-------------------------------------")
        pdf.setFont("sans",9)
        pdf.drawString(10,q-75,'Item')
        pdf.drawString(80,q-75,'Qty')
        pdf.drawString(105,q-75,'Rate')
        pdf.drawString(135,q-75,'Price')
        pdf.setFont("sans",8)
        pdf.drawString(9,q-80,"-------------------------------------")
        y=q-88
        for k in self.item:
            s=str(k)
            pdf.drawString(9,y,s)
            y=y-10
        y=q-88
        for n in self.rate:
            p=str(n) 
            pdf.drawString(105,y,p)
            y=y-10    
        y=q-88   
        for l in self.quan:
            u=str(l) 
            pdf.drawString(85,y,u)
            y=y-10
        y=q-88   
        for m in self.price:
            z=str(m)
            pdf.drawString(136,y,z)
            y=y-10   
        y=((q-88)-(len(self.item)*10))
        pdf.drawString(9,y,"-------------------------------------")
        pdf.setFont("sans",9)
        pdf.drawString(60,y-10,'Sub-Total : ')
        pdf.drawString(129,y-10,str(1.000*self.total_amount_value))
        pdf.drawString(60,y-20,'CGST @2.5% : ')
        pdf.drawString(134,y-20,str(0.025*self.total_amount_value))
        pdf.drawString(60,y-30,'SGST @2.5% : ')
        pdf.drawString(134,y-30,str(0.025*self.total_amount_value))
        pdf.setFont("sans",8)
        pdf.drawString(9,y-40,"-------------------------------------")

        pdf.setFont("sans bold",10)
        pdf.drawString(65,y-50,'TOTAL : ')
        pdf.drawString(122,y-50,str(1.00*(self.total_amount_value)+(self.total_amount_value*0.050)))
        pdf.setFont("sans",8)
        pdf.drawString(9,y-60,"-------------------------------------")
        print(y)
        pdf.save()
        webbrowser.open_new("POS.pdf")        
    def tree_view(self):
        '''This function creates the  Empty Tree view'''
        self.style=ttk.Style()  
        self.style.configure('mystyle.Treeview',highlightthickness=0,bd=0,background=background,fieldfbackground=background,foreground=foreground,font=('candara',12))
        self.style.configure('mystyle.Treeview.Heading',font=('candara',14,'bold'))
        self.style.layout('mystyle.Treeview',[('mystyle.Treeview.treearea',{'sticky':'nswe'})])
        self.tree_frame=Frame(self.cart_frame,bg=background)
        self.tree_frame.grid(row=2,column=0)
        self.vertical_scrollbar=ttk.Scrollbar(self.tree_frame)
        self.vertical_scrollbar.grid(row=0,column=1,sticky='ns')
        self.data_tree=ttk.Treeview(self.tree_frame,style="mystyle.Treeview",yscrollcommand=self.vertical_scrollbar.set)
        self.vertical_scrollbar.config(command=self.data_tree.yview)
        self.data_tree['columns']=('0','1','2','3','4')
        self.data_tree.column("#0",width=1)
        self.data_tree.column("0",width=260,anchor='center')
        self.data_tree.column("1",width=200,anchor='center')
        self.data_tree.column("2",width=200,anchor='center')
        self.data_tree.column("3",width=220,anchor='center')
        self.data_tree.column("4",width=160,anchor='center')
        self.data_tree.heading('#0',text='')
        self.data_tree.heading("0",text="Item")
        self.data_tree.heading("1",text="Quantity")
        self.data_tree.heading("2",text="Rate")
        self.data_tree.heading("3",text='Amount')
        self.data_tree.heading("4",text='Unit')
        self.data_tree.grid(row=0,column=0) 
    def insert_treeview(self):
        '''This function insert data in tree view'''
        quantity_var=self.quantity_en.get()
        if self.quantity_en.get() =="":
            quantity_var=1
        #insert new data from entry boxes
        self.data_tree.insert("","end",text="",values=(self.item_combobox.get(),quantity_var,self.rate_en.get(),int(quantity_var)*int(self.rate_en.get()),self.unit_en.get()))
        #fetch total quantity and total amount from treeview data
        self.quantity_list.append(self.data_tree.item(self.data_tree.get_children()[-1])['values'][1])
        self.amount_list.append(self.data_tree.item(self.data_tree.get_children()[-1])['values'][3])
        self.total_quantity_value=sum(self.quantity_list)
        self.total_amount_value=sum(self.amount_list)
        #labels of sub total, total quantity and total amount
        self.total_quantity=Label(self.cart_frame,bg='white',font='candara 16 bold',bd=0,text=str(self.total_quantity_value),width=46,fg=foreground)
        self.total_quantity.grid(row=3,column=0,sticky=W,padx=130)
        self.total_amount=Label(self.cart_frame,bg='white',font='candara 16 bold',bd=0,text=str(self.total_amount_value),width=46,fg=foreground)
        self.total_amount.grid(row=3,column=0,sticky=E)
        self.sub_total_l=Label(self.cart_frame,bg='white',font='candara 16 bold',bd=0,text='Sub Total',width=25,fg=foreground)
        self.sub_total_l.grid(row=3,column=0,sticky=W)
class Report:
    def __init__(self):
        self.rep_win=Toplevel()
        self.rep_win.state('zoomed')
        self.rep_win.config(bg=background)
        self.frame_banner=Frame(self.rep_win,bg=background)
        self.frame_banner.grid(row=0,column=0)
        self.banner_img=Image.open('icons\\home_ban.jpg')
        self.banner_img=self.banner_img.resize((self.rep_win.winfo_screenwidth(),150),Image.ANTIALIAS)
        self.main_banner=ImageTk.PhotoImage(self.banner_img)
        self.Exit_icon=ImageTk.PhotoImage(Image.open('icons\\back.png'))
        self.banner_lbl=Label(self.frame_banner,image=self.main_banner,bg=background)
        self.banner_lbl.grid(row=0,column=0)
        self.body_frame=Frame(self.rep_win,bg=background)
        self.body_frame.grid(row=1,column=0)
        self.rep_win.bind("<Escape>",lambda event: self.rep_win.destroy())
        self.rep_win.resizable(0,0)
        self.rep_win.attributes('-toolwindow', True)
        
        self.body_frame=Frame(self.rep_win,bg=background)
        self.body_frame.grid(row=1,column=0,pady=15)

        self.menu_banner_image=ImageTk.PhotoImage(Image.open('icons\\report_win_ico.png'))
        self.menu_ban=Label(self.body_frame,text="     REPORTS",font="Candara 40 bold",image=self.menu_banner_image,compound="left",bd=0,bg=background,fg=foreground,activebackground=background)
        self.menu_ban.grid(row=0,column=0)



    
        
        
            








if __name__ == "__main__":
    Home()