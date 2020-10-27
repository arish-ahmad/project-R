import tkinter as t
from tkinter import *
from tkinter.font import Font
from tkinter import font
from PIL import Image,ImageTk
from tkinter import messagebox
background="lightsteelblue"
foreground="black"
class Home:
    global background,foreground
    def __init__(self,master):
        self.home_window=master
        self.home_window.state('zoomed')
        self.frame_banner=Frame(self.home_window,bg=background)
        self.frame_banner.grid(row=0,column=0)
        self.banner_img=Image.open('icons\\home_ban.jpg')
        self.banner_img=self.banner_img.resize((self.home_window.winfo_screenwidth(),150),Image.ANTIALIAS)
        self.main_banner=ImageTk.PhotoImage(self.banner_img)
        self.banner_lbl=Label(self.frame_banner,image=self.main_banner)
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
        self.settings=Button(self.frame5,text="Settings",image=self.setting_icon,bd=0,bg=background,fg=foreground,activebackground=background,compound="top",font=main_font)
        self.settings.grid(row=0,column=0)
        self.Exit_b=Button(self.frame6,text="Exit",image=self.Exit_icon,bd=0,bg=background,fg=foreground,activebackground=background,command=self.exit,compound="top",font=main_font)
        self.Exit_b.grid(row=0,column=0)
        self.home_window.overrideredirect(True)
        self.home_window.config(bg=background)
        self.home_window.bind("<Escape>",self.exit_s)
        self.home_window.mainloop()
    def inv_page(self):
        Inventory()
    def exit(self):
        if messagebox.askyesno(parent=self.home_window,title="Exit",message="Are You Sure!"):
            self.home_window.destroy()
    def exit_s(self,event):
        if messagebox.askyesno(parent=self.home_window,title="Exit",message="Are You Sure!"):
            self.home_window.destroy()
class Inventory:
    def __init__(self):
        self.inventory_win=Toplevel()
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
        self.banner_lbl=Label(self.frame_banner,image=self.main_banner)
        self.banner_lbl.grid(row=0,column=0)
        self.body_frame=Frame(self.inventory_win,bg=background)
        self.body_frame.grid(row=1,column=0)
        self.inventory_win.focus_force()
        self.ban=Label(self.frame_banner,text="  INVENTORY ",font="Helvetica 40 bold",compound="left",bg=background,fg=foreground,image=self.inv_banner)
        self.ban.grid(row=1,column=0,pady=10)
        self.add_item=Button(self.body_frame,text="  Menu Items ",font="Helvetica 28 bold",image=self.add_item_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background, command=self.menu_page)
        self.add_item.grid(row=1,column=0,pady=20,sticky=t.W)
        self.add_rawitem=Button(self.body_frame,text="  Raw Materials ",font="Helvetica 28 bold",image=self.raw_item_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background, command=self.raw_page)
        self.add_rawitem.grid(row=2,column=0,sticky=t.W)
        self.employee=Button(self.body_frame,text="  Employee \n  Registeration ",font="Helvetica 28 bold",image=self.employee_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background, command=self.raw_page)
        self.employee.grid(row=3,column=0,pady=20,sticky=t.W)
        self.category=Button(self.body_frame,text="  Category \n  Registeration ",font="Helvetica 28 bold",image=self.category_img,compound="left",bg=background,fg=foreground,bd=0,activebackground=background, command=self.raw_page)
        self.category.grid(row=4,column=0,pady=20,sticky=t.W)
        self.back=Button(self.body_frame,font="Times 22 bold",image=self.Exit_icon,compound="top",bg=background,fg=foreground,bd=0,activebackground=background,command=self.inventory_win.destroy)
        self.back.grid(row=5,column=0)
        self.inventory_win.bind("<Escape>",self.destroy)
        self.inventory_win.resizable(0,0)
        self.inventory_win.overrideredirect(True)
        self.inventory_win.mainloop()

    def destroy(self,event):
        self.inventory_win.destroy()   

    def menu_page(self):
        menu_items()

    def raw_page(self):
        raw_items()


class menu_items:
    def __init__(self):
        self.menu_win=Toplevel()
        self.menu_win.title("Menu Items")
        self.menu_win.state("zoomed")
        self.menu_win.config(bg=background)
        self.frame_banner=Frame(self.menu_win,bg=background)
        self.frame_banner.grid(row=0,column=0)
        self.banner_img=Image.open('icons\\home_ban.jpg')
        self.banner_img=self.banner_img.resize((self.menu_win.winfo_screenwidth(),150),Image.ANTIALIAS)
        self.main_banner=ImageTk.PhotoImage(self.banner_img)
        self.banner_lbl=Label(self.frame_banner,image=self.main_banner)
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
        self.add_item=Button(self.body_frame,image=self.add_icon,bd=0,bg=background,fg=foreground,activebackground=background)
        self.add_item.grid(row=1,column=0,pady=15)
        self.edit_item=Button(self.body_frame,image=self.edit_icon,bd=0,bg=background,fg=foreground,activebackground=background)
        self.edit_item.grid(row=2,column=0,pady=15)
        self.view_item=Button(self.body_frame,image=self.view_icon,bd=0,bg=background,fg=foreground,activebackground=background)
        self.view_item.grid(row=3,column=0,pady=15)
        self.delete_item=Button(self.body_frame,image=self.delete_icon,bd=0,bg=background,fg=foreground,activebackground=background)
        self.delete_item.grid(row=4,column=0,pady=15)
        self.back=Button(self.body_frame,image=self.back_icon,command=self.menu_win.destroy,bd=0,bg=background,fg=foreground,activebackground=background)
        self.back.grid(row=5,column=0,pady=15)
        self.menu_win.bind("<Escape>",self.destroy)
        self.menu_win.overrideredirect(1)
        self.menu_win.mainloop()

    def destroy(self,event):
        self.menu_win.destroy()


class raw_items:
    def __init__(self):
         
        self.raw_win=Toplevel()
        self.raw_win.title("Menu Items")
        self.raw_win.state("zoomed")
        self.raw_win.config(bg=background)
        self.frame_banner=Frame(self.raw_win,bg=background)
        self.frame_banner.grid(row=0,column=0)
        self.banner_img=Image.open('icons\\home_ban.jpg')
        self.banner_img=self.banner_img.resize((self.raw_win.winfo_screenwidth(),150),Image.ANTIALIAS)
        self.main_banner=ImageTk.PhotoImage(self.banner_img)
        self.banner_lbl=Label(self.frame_banner,image=self.main_banner)
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
        self.raw_win.overrideredirect(1)
        self.raw_win.mainloop()

    def destroy(self,event):
        self.raw_win.destroy()    





        
if __name__ == "__main__":
    window=Tk()
    Home(window)