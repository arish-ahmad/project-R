import tkinter as t
from tkinter import *
from tkinter.font import Font
from tkinter import font
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
from csv import DictWriter,writer
import csv,os
#-----------Functions-------------
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
        self.banner_lbl=Label(self.frame_banner,image=self.main_banner,bg=background)
        self.banner_lbl.grid(row=0,column=0)
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

        main_font=Font(family="Helvetica",size=25,weight="bold")
        self.quick_bill=Button(self.frame1,text="Billing",image=self.quick_bill_icon,bd=0,bg=background,fg=foreground,activebackground=background,compound="top",font=main_font)
        self.quick_bill.grid(row=0,column=0)
        self.items=Button(self.frame2,text="Inventory",image=self.inventory_icon,bd=0,bg=background,fg=foreground,activebackground=background,command=self.inv_page,compound="top",font=main_font)
        self.items.grid(row=0,column=0)
        self.takesaway=Button(self.frame3,text="Takesaway",image=self.takeaway_icon,bd=0,bg=background,fg=foreground,activebackground=background,compound="top",font=main_font)
        self.takesaway.grid(row=0,column=0)
        self.report=Button(self.frame4,text="Report",image=self.reports_icon,bd=0,bg=background,fg=foreground,activebackground=background,compound="top",font=main_font)
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
    def disabled(self):
        pass
    def inv_page(self):
        Inventory()
    def setting_page(self):
        Settings()
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
        self.theme_combobox["values"]=('white','grey','lightgrey','blue')
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
        self.add_item=Button(self.body_frame,text="  Menu Items ",font="Helvetica 20 bold",image=self.add_item_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background, command=self.menu_page)
        self.add_item.grid(row=1,column=0,pady=20,sticky=t.W)
        self.add_rawitem=Button(self.body_frame,text="  Raw Materials ",font="Helvetica 20 bold",image=self.raw_item_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background, command=self.raw_page)
        self.add_rawitem.grid(row=2,column=0,sticky=t.W)
        self.employee=Button(self.body_frame,text="  Employee \n  Registeration ",font="Helvetica 20 bold",image=self.employee_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background, command=self.raw_page)
        self.employee.grid(row=3,column=0,pady=20,sticky=t.W)
        self.category=Button(self.body_frame,text="  Category \n  Registeration ",font="Helvetica 20 bold",image=self.category_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background, command=self.raw_page)
        self.category.grid(row=4,column=0,pady=20,sticky=t.W)
        self.back=Button(self.body_frame,image=self.Exit_icon,compound="top",bg=background,fg=foreground,bd=0,activebackground=background,command=self.inventory_win.destroy)
        self.back.grid(row=5,column=0)
        self.inventory_win.bind("<Escape>",self.destroy)
        self.inventory_win.resizable(0,0)
        self.inventory_win.attributes('-toolwindow', True)
        #self.inventory_win.mainloop()
    def destroy(self,event):
        self.inventory_win.destroy()
    def menu_page(self):
        menu_items()
    def raw_page(self):
        raw_items()
class menu_items:
    def __init__(self):
        self.menu_win=Toplevel()
        self.menu_win.title("Items Menu")
        self.menu_win.state("zoomed")
        self.menu_win.config(bg=background)
        self.frame_banner=Frame(self.menu_win,bg=background)
        self.frame_banner.grid(row=0,column=0)
        self.banner_img=Image.open('icons\\home_ban.jpg')
        self.banner_img=self.banner_img.resize((self.menu_win.winfo_screenwidth(),150),Image.ANTIALIAS)
        self.main_banner=ImageTk.PhotoImage(self.banner_img)
        self.banner_lbl=Label(self.frame_banner,image=self.main_banner,bg=background)
        self.banner_lbl.grid(row=0,column=0)

        self.body_frame=Frame(self.menu_win,bg=background)
        self.body_frame.grid(row=1,column=0,pady=15)
        self.add_icon=ImageTk.PhotoImage(Image.open('icons\\add.png'))
        self.edit_icon=ImageTk.PhotoImage(Image.open('icons\\edit.png'))
        self.view_icon=ImageTk.PhotoImage(Image.open('icons\\view.png'))
        self.back_icon=ImageTk.PhotoImage(Image.open('icons\\back.png'))
        self.delete_icon=ImageTk.PhotoImage(Image.open('icons\\delete.png'))
        self.menu_banner_image=ImageTk.PhotoImage(Image.open('icons\\menu_ico.png'))
        self.menu_ban=Label(self.body_frame,text=" ITEMS MENU",font="Helvetica 40 bold",image=self.menu_banner_image,compound="left",bd=0,bg=background,fg=foreground,activebackground=background)
        self.menu_ban.grid(row=0,column=0,pady=15)
        self.add_item=Button(self.body_frame,image=self.add_icon,bd=0,bg=background,fg=foreground,activebackground=background,command=self.Add_)
        self.add_item.grid(row=1,column=0,pady=15)
        self.edit_item=Button(self.body_frame,image=self.edit_icon,bd=0,bg=background,fg=foreground,activebackground=background)
        self.edit_item.grid(row=2,column=0,pady=15)
        self.view_item=Button(self.body_frame,image=self.view_icon,bd=0,bg=background,fg=foreground,activebackground=background)
        self.view_item.grid(row=3,column=0,pady=15)
        self.delete_item=Button(self.body_frame,image=self.delete_icon,bd=0,bg=background,fg=foreground,activebackground=background)
        self.delete_item.grid(row=4,column=0,pady=15)
        self.back=Button(self.body_frame,image=self.back_icon,command=self.menu_win.destroy,bd=0,bg=background,fg=foreground,activebackground=background)
        self.back.grid(row=5,column=0,pady=15)
        self.menu_win.bind("<Escape>",self.destroy_)
        self.menu_win.attributes('-toolwindow', True)
        #self.menu_win.mainloop()
    def destroy_(self,event):
        self.menu_win.destroy()
    def Add_(self):
        Add_Item()
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
class Add_Item:
    def __init__(self):
        self.add_item_win=Toplevel()
        self.add_item_win.title("Items Register")
        self.add_item_win.state("zoomed")
        self.add_item_win.config(bg=background)
        self.frame_banner=Frame(self.add_item_win,bg=background)
        self.frame_banner.grid(row=0,column=0)
        self.banner_img=Image.open('icons\\home_ban.jpg')
        self.banner_img=self.banner_img.resize((self.add_item_win.winfo_screenwidth(),150),Image.ANTIALIAS)
        self.main_banner=ImageTk.PhotoImage(self.banner_img)
        self.banner_lbl=Label(self.frame_banner,image=self.main_banner,bg=background)
        self.banner_lbl.grid(row=0,column=0)
        self.body_frame=LabelFrame(self.add_item_win,bg=background,text="Item Discription",font="Times 40 bold",fg=foreground,bd=0)
        self.body_frame.grid(row=1,column=0,pady=15,sticky=t.W)
        self.regn_l=Label(self.body_frame,text="Reg. No *",font="consolas 20",bg=background,bd=1,fg=foreground)
        self.regn_l.grid(row=1,column=0,pady=20,padx=20,sticky=t.W)
        self.item_name_l=Label(self.body_frame,text="Item Name *",font="consolas 20",bg=background,fg=foreground)
        self.item_name_l.grid(row=2,column=0,pady=20,padx=20,sticky=t.W)
        self.rate_l=Label(self.body_frame,text="Rate *",font="consolas 20",bg=background,fg=foreground)
        self.rate_l.grid(row=3,column=0,pady=20,padx=20,sticky=t.W)
        self.cat_l=Label(self.body_frame,text="Unit *",font="consolas 20",bg=background,fg=foreground)
        self.cat_l.grid(row=4,column=0,pady=20,padx=20,sticky=t.W)
        #-----------Entry boxes--------------------------
        self.regn_e=Entry(self.body_frame,font="consolas 18",width=15,bd=2,bg=background,fg=foreground)
        self.regn_e.grid(row=1,column=1,pady=20,sticky=t.W)
        self.regn_e.focus()
        self.regn_e.bind("<Return>",lambda event: self.item_name_e.focus())
        self.regn_e.bind("<Down>",lambda event: self.item_name_e.focus())
        self.regn_e.bind("<Up>",lambda event: self.cat_combobox.focus())

        self.item_name_e=Entry(self.body_frame,font="consolas 18",width=15,bd=2,bg=background,fg=foreground)
        self.item_name_e.grid(row=2,column=1,pady=20,sticky=t.W)
        self.item_name_e.bind("<Return>",lambda event: self.rate_e.focus())
        self.item_name_e.bind("<Down>",lambda event: self.rate_e.focus())
        self.item_name_e.bind("<Up>",lambda event: self.regn_e.focus())

        self.rate_e=Entry(self.body_frame,font="consolas 18",width=15,bd=2,background=background,foreground=foreground)
        self.rate_e.grid(row=3,column=1,pady=20,sticky=t.W)
        self.reg=self.rate_e.register(correct)                                # Input only Integer type
        self.rate_e.config(validate="key",validatecommand=(self.reg,"%P"))
        self.rate_e.bind("<Return>",lambda event: self.cat_combobox.focus())
        self.rate_e.bind("<Down>",lambda event: self.cat_combobox.focus())
        self.rate_e.bind("<Up>",lambda event: self.item_name_e.focus())

        self.cat_combobox=ttk.Combobox(self.body_frame,width=15,font="consolas 18",state="readonly")
        self.cat_combobox["values"]=('Piece','Plate','Bottle','Siddique','Munna Bhaiya') 
        self.cat_combobox.option_add('*TCombobox*Listbox.font',("consolas",18))
        self.cat_combobox.grid(row=4,column=1,pady=20,sticky=t.W) 
        self.cat_combobox.current(0)
        self.cat_combobox.bind("<Return>",lambda event: self.save.focus())
        self.cat_combobox.bind("<Up>",lambda event: self.rate_e.focus())

        self.save=Button(self.body_frame,text="Save",bg=background,fg=foreground,bd=2,font="consolas 16 bold",width=8,activebackground=background)
        self.save.grid(row=5,column=0,padx=65,pady=20,sticky=t.W)
        self.back=Button(self.body_frame,text="Back",bg=background,fg=foreground,bd=2,font="consolas 16 bold",width=8,activebackground=background,command=self.add_item_win.destroy)
        self.back.grid(row=5,column=1,pady=20,padx=10,sticky=t.W)
        self.add_item_win.bind("<Escape>",self.back_b)
        self.add_item_win.attributes('-toolwindow', True)
        #self.add_item_win.mainloop()
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
        self.inv_banner=ImageTk.PhotoImage(Image.open('icons\\menu_ico.png'))
        self.banner_lbl=Label(self.frame_banner,image=self.main_banner,bg=background)
        self.banner_lbl.grid(row=0,column=0)
        self.body_frame=Frame(self.settings_win,bg=background)
        self.body_frame.grid(row=1,column=0)
        self.ban=Label(self.frame_banner,text=" Settings and customization ",font="Helvetica 40 bold",compound="left",bg=background,fg=foreground,image=self.inv_banner)
        self.ban.grid(row=1,column=0)
        self.cd=Button(self.body_frame,text="  Company Details ",font="Helvetica 20 bold",image=self.cd_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background)
        self.cd.grid(row=1,column=0,pady=10,sticky=t.W)
        self.printer_b=Button(self.body_frame,text="  Add Printer ",font="Helvetica 20 bold",image=self.printer_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background)
        self.printer_b.grid(row=2,column=0,pady=10,sticky=t.W)
        self.theme_b=Button(self.body_frame,text="  Change Theme ",font="Helvetica 20 bold",image=self.theme_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background,command=self.theme_page)
        self.theme_b.grid(row=3,column=0,pady=10,sticky=t.W)
        self.help=Button(self.body_frame,text="  Help ",font="Helvetica 20 bold",image=self.help_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background)
        self.help.grid(row=4,column=0,pady=10,sticky=t.W)
        self.about=Button(self.body_frame,text="  About Us ",font="Helvetica 20 bold",image=self.about_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background)
        self.about.grid(row=5,column=0,pady=10,sticky=t.W)
        self.back=Button(self.body_frame,image=self.Exit_icon,compound="top",bg=background,fg=foreground,bd=0,activebackground=background,command=self.settings_win.destroy)
        self.back.grid(row=6,column=0)
        self.settings_win.bind("<Escape>",self.destroy)
        self.settings_win.resizable(0,0)
        self.settings_win.attributes('-toolwindow', True)
        #self.settings_win.mainloop()
    def theme_page(self):
        Themes()
    def destroy(self,event):
        self.settings_win.destroy()

if __name__ == "__main__":
    Home()
   