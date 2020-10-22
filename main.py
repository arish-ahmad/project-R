import tkinter as t
from tkinter import *
from PIL import Image,ImageTk
class Home:
    def __init__(self,background):
        self.home_window=t.Tk()
        self.home_window.geometry("1400x1200")
        self.home_window.title("Main menu")
        self.frame_banner=Frame(self.home_window)
        self.frame_banner.grid(row=0,column=0)
        self.banner_img=ImageTk.PhotoImage(Image.open('banner.jpg'))
        self.banner_lbl=Label(self.frame_banner, image=self.banner_img)
        self.banner_lbl.grid(row=0,column=0)

        #---------------Icons-------------------
        self.quick_bill_icon=ImageTk.PhotoImage(Image.open('icons/quickbill.png'))
        self.inventory_icon=ImageTk.PhotoImage(Image.open('icons/inventory.png'))
        self.takeaway_icon=ImageTk.PhotoImage(Image.open('icons/takeaway.jpg'))
        self.reports_icon=ImageTk.PhotoImage(Image.open('icons/reports.jpg'))
        self.setting_icon=ImageTk.PhotoImage(Image.open('icons/settings.png'))



        #---------------Buttons------------------
        self.body_frame=Frame(self.home_window,bg='white')
        self.body_frame.grid(row=1,column=0)
        self.frame1=Frame(self.body_frame,bd=0)
        self.frame1.grid(row=0,column=0 ,padx=40,pady=50)
        self.frame2=Frame(self.body_frame)
        self.frame2.grid(row=0,column=1, padx=100)
        self.frame3=Frame(self.body_frame)
        self.frame3.grid(row=0,column=2,padx=50)
        self.frame4=Frame(self.body_frame)
        self.frame4.grid(row=1, columnspan=2,padx=100 )
        self.frame5=Frame(self.body_frame)
        self.frame5.grid(row=1,column=1,columnspan=2,padx=100)

        
        
        self.quick_bill=Button(self.frame1,image=self.quick_bill_icon,text="quick bill",font="helvetica 20", borderwidth=0,border=0,highlightthickness=0)
        self.quick_bill.grid(row=0,column=0)
        self.items=Button(self.frame2,image=self.inventory_icon,text="Items/Inventory",bd=0,font="helvetica 20",highlightthickness=0)
        self.items.grid(row=0,column=0)
        self.takesaway=Button(self.frame3,image=self.takeaway_icon,text="Takesaway",bd=0,font="helvetica 20",highlightthickness=0)
        self.takesaway.grid(row=0,column=0)
        self.report=Button(self.frame4,image=self.reports_icon,text="Report",bd=0,font="helvetica 20",highlightthickness=0)
        self.report.grid(row=0,column=0)
        self.settings=Button(self.frame5,image=self.setting_icon,text="Settings",bd=0,font="helvetica 20",highlightthickness=0)
        self.settings.grid(row=0,column=0)



        # self.home_window.state('zoomed')
        self.home_window.overrideredirect(False)
        self.home_window.config(bg=background)
        self.home_window.mainloop()
if __name__ == "__main__":
    Home("White")