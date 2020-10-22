import tkinter as t
from tkinter import *
from PIL import Image,ImageTk
class Home:
    def __init__(self,background):
        self.home_window=t.Tk()
        self.home_window.geometry("1400x1200")
        self.home_window.title("Main menu")
        self.load=Image.open("background.jpg")
        self.render=ImageTk.PhotoImage(self.load)
        self.img=t.Label(self.home_window,image=self.render)
        self.img.place(x=0,y=0)
        #---------------Icons-------------------

        #---------------Buttons------------------
        self.frame1=Frame(self.home_window)
        self.frame1.grid(row=3,column=0,padx=230,pady=210)
        self.frame2=Frame(self.home_window)
        self.frame2.grid(row=3,column=1)
        self.frame3=Frame(self.home_window)
        self.frame3.grid(row=3,column=3)
        self.frame4=Frame(self.home_window)
        self.frame4.grid(row=4,columnspan=3)
        self.frame5=Frame(self.home_window)
        self.frame5.grid(row=4,column=2)
        self.quick_bill=Button(self.frame1,text="quick bill",bd=0,font="helvetica 20")
        self.quick_bill.grid(row=0,column=0)
        self.items=Button(self.frame2,text="Items/Inventory",bd=0,font="helvetica 20")
        self.items.grid(row=0,column=0)
        self.takesaway=Button(self.frame3,text="Takesaway",bd=0,font="helvetica 20")
        self.takesaway.grid(row=0,column=0)
        self.report=Button(self.frame4,text="Report",bd=0,font="helvetica 20")
        self.report.grid(row=0,column=0)
        self.settings=Button(self.frame5,text="Settings",bd=0,font="helvetica 20")
        self.settings.grid(row=0,column=0)



        self.home_window.state('zoomed')
        self.home_window.overrideredirect(False)
        self.home_window.config(bg=background)
        self.home_window.mainloop()
if __name__ == "__main__":
    Home("lightsteelblue")