import tkinter as t
from tkinter import *
from PIL import Image,ImageTk



def inv_page():
    inv=inventory()


def menu_page():
    
    menu=menu_window()

def raw_page():
    raw=raw_window()    



class menu_window():
    def __init__(self):
        self.menu_win=t.Toplevel()
        self.menu_win.title('Menu Items')
        self.menu_win.geometry('800x600+370+0')
        self.menu_win.config(bg='white')
        self.title_frame=Frame(self.menu_win,bg='black')
        self.banner_img=ImageTk.PhotoImage(Image.open('icons/menu_banner.jpg'))
        self.banner_lbl=Label(self.title_frame, image=self.banner_img)
        self.banner_lbl.grid(row=0,column=0)
        self.title_frame.grid(row=0,column=0)


        #---------------Icons-------------------
        self.add_icon=ImageTk.PhotoImage(Image.open('icons/add.jpg'))
        self.edit_icon=ImageTk.PhotoImage(Image.open('icons/edit.jpg'))
        self.view_icon=ImageTk.PhotoImage(Image.open('icons/view.jpg'))
        self.search_icon=ImageTk.PhotoImage(Image.open('icons/search.jpg'))
        self.delete_icon=ImageTk.PhotoImage(Image.open('icons/delete.jpg'))


        #---------------Frames & Buttons------------------

        self.body_frame=Frame(self.menu_win,bg='white')
        self.body_frame.grid(row=2,column=0,pady=30)

        self.frame1=Frame(self.body_frame)
        self.frame1.grid(row=0,column=0,pady=50,padx=60)
        self.frame2=Frame(self.body_frame)
        self.frame2.grid(row=0,column=1,pady=10,padx=60)
        self.frame3=Frame(self.body_frame)
        self.frame3.grid(row=0,column=2,pady=10,padx=60)
        self.frame4=Frame(self.body_frame)
        self.frame4.grid(row=1,columnspan=2,padx=60,pady=60)
        self.frame5=Frame(self.body_frame)
        self.frame5.grid(row=1,column=1,columnspan=2,pady=10,padx=60)

        self.add_menu_btn=Button(self.frame1,image=self.add_icon,font="helvetica 20",bd=0,highlightthickness=0)
        self.add_menu_btn.grid(row=0,column=0)
        self.edit_menu_btn=Button(self.frame2,image=self.edit_icon,font="helvetica 20",bd=0,highlightthickness=0)
        self.edit_menu_btn.grid(row=0,column=0)
        self.view_menu_btn=Button(self.frame3,image=self.view_icon,font="helvetica 20",bd=0,highlightthickness=0)
        self.view_menu_btn.grid(row=0,column=0)
        self.search_menu_btn=Button(self.frame4,image=self.search_icon,font="helvetica 20",bd=0,highlightthickness=0)
        self.search_menu_btn.grid(row=0,column=0)
        self.delete_menu_btn=Button(self.frame5,image=self.delete_icon,font="helvetica 20",bd=0,highlightthickness=0)
        self.delete_menu_btn.grid(row=0,column=0)


        self.menu_win.mainloop()


class raw_window():
    def __init__(self):
        self.raw_win=t.Toplevel()
        self.raw_win.title('Raw Materials')
        self.raw_win.geometry('800x600+370+0')
        self.raw_win.config(bg='white')
        self.title_frame=Frame(self.raw_win,bg='black')
        self.banner_img=ImageTk.PhotoImage(Image.open('icons/raw_banner.jpg'))
        self.banner_lbl=Label(self.title_frame, image=self.banner_img)
        self.banner_lbl.grid(row=0,column=0)
        self.title_frame.grid(row=0,column=0)


        #---------------Icons-------------------
        self.add_icon=ImageTk.PhotoImage(Image.open('icons/add.jpg'))
        self.edit_icon=ImageTk.PhotoImage(Image.open('icons/edit.jpg'))
        self.view_icon=ImageTk.PhotoImage(Image.open('icons/view.jpg'))
        self.search_icon=ImageTk.PhotoImage(Image.open('icons/search.jpg'))
        self.delete_icon=ImageTk.PhotoImage(Image.open('icons/delete.jpg'))

        #---------------Frames & Buttons------------------

        self.body_frame=Frame(self.raw_win,bg='white')
        self.body_frame.grid(row=2,column=0,pady=30)

        self.frame1=Frame(self.body_frame)
        self.frame1.grid(row=0,column=0,pady=50,padx=60)
        self.frame2=Frame(self.body_frame)
        self.frame2.grid(row=0,column=1,pady=10,padx=60)
        self.frame3=Frame(self.body_frame)
        self.frame3.grid(row=0,column=2,pady=10,padx=60)
        self.frame4=Frame(self.body_frame)
        self.frame4.grid(row=1,columnspan=2,padx=60,pady=60)
        self.frame5=Frame(self.body_frame)
        self.frame5.grid(row=1,column=1,columnspan=2,pady=10,padx=60)

        self.add_raw_btn=Button(self.frame1,image=self.add_icon,font="helvetica 20",bd=0,highlightthickness=0)
        self.add_raw_btn.grid(row=0,column=0)
        self.edit_raw_btn=Button(self.frame2,image=self.edit_icon,bd=0,font="helvetica 20",highlightthickness=0)
        self.edit_raw_btn.grid(row=0,column=0)
        self.view_raw_btn=Button(self.frame5,image=self.view_icon,font="helvetica 20",bd=0,highlightthickness=0)
        self.view_raw_btn.grid(row=0,column=0)
        self.search_raw_btn=Button(self.frame3,image=self.search_icon,bd=0,font="helvetica 20",highlightthickness=0)
        self.search_raw_btn.grid(row=0,column=0)
        self.delete_raw_btn=Button(self.frame4,image=self.delete_icon,bd=0,font="helvetica 20",highlightthickness=0)
        self.delete_raw_btn.grid(row=0,column=0)
        




        self.raw_win.mainloop()        



class inventory:
        def __init__(self):
            self.inventory_win=t.Toplevel()
            self.inventory_win.title('Inventory')
            self.inventory_win.geometry('400x400+550+130')
            self.inventory_win.config(bg='white')
            self.title_frame=Frame(self.inventory_win,bg='black')
            self.banner_img=ImageTk.PhotoImage(Image.open('icons/inv_banner.jpg'))
            self.banner_lbl=Label(self.title_frame, image=self.banner_img)
            self.banner_lbl.grid(row=0,column=0)
            self.title_frame.grid(row=0,column=0)


            #---------------Icons-------------------
            self.menu_items_icon=ImageTk.PhotoImage(Image.open('icons/menu_items.jpg'))
            self.raw_materials_icon=ImageTk.PhotoImage(Image.open('icons/raw_materials.jpg'))


            #---------------Frames & Buttons------------------
            self.body_frame=Frame(self.inventory_win,bg='white')
            self.body_frame.grid(row=1,column=0)

            self.menu_btn=Button(self.body_frame,image=self.menu_items_icon,highlightthickness=0,bd=0,command=menu_page)
            self.menu_btn.grid(row=0,column=0,pady=40)
            self.raw_btn=Button(self.body_frame,image=self.raw_materials_icon,highlightthickness=0,bd=0,command=raw_page)
            self.raw_btn.grid(row=1,column=0)
            
    

            self.inventory_win.mainloop()
                    
       


class Home:

    


    def __init__(self,background):
        self.home_window=t.Tk()
        self.home_window.geometry("1400x1200+70+0")
        self.home_window.minsize(width=1400,height=1200)
        self.home_window.maxsize(width=1400,height=1200)
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



        #---------------Frames & Buttons------------------
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

        
        
        self.quick_bill=Button(self.frame1,image=self.quick_bill_icon,font="helvetica 20", borderwidth=0,border=0,highlightthickness=0)
        self.quick_bill.grid(row=0,column=0)
        self.items=Button(self.frame2,image=self.inventory_icon,bd=0,font="helvetica 20",highlightthickness=0, command=inv_page)
        self.items.grid(row=0,column=0)
        self.takesaway=Button(self.frame3,image=self.takeaway_icon,bd=0,font="helvetica 20",highlightthickness=0)
        self.takesaway.grid(row=0,column=0)
        self.report=Button(self.frame4,image=self.reports_icon,bd=0,font="helvetica 20",highlightthickness=0)
        self.report.grid(row=0,column=0)
        self.settings=Button(self.frame5,image=self.setting_icon,bd=0,font="helvetica 20",highlightthickness=0)
        self.settings.grid(row=0,column=0)



        # self.home_window.state('zoomed')
        self.home_window.overrideredirect(False)
        self.home_window.config(bg=background)
        self.home_window.mainloop()

    


         


    




















if __name__ == "__main__":
    Home("White")
    