from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

class View_CapNhatNganSach:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\CapNhatNganSach\frame0")

    def __init__(self):
        self.root = Tk()
        self.root.title("Cập nhật ngân sách")

    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def destroy(self):
        self.root.destroy()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Bạn chắc chắn muốn thoát chương trình ?"):
            self.root.destroy()

    def create_controller(self, controller):
        self.controller = controller

    def create_treeview(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", highlightthickness=0, bd=0, font=('robota', 12)) # Modify the font of the body
        style.configure("Treeview.Heading", background="#3B71CA", foreground="white", font=('robota', 14))
        style.map("Treeview",background=[("selected","#9FA6B2")])
        style.map("Treeview.Heading",background=[("selected","#3B71CA")],foreground=[("selected","#white")])
        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("mangansach", "maduan", "ngansachmoi", "noidung", "thoigian")

        self.tree.column("mangansach",width=0, stretch="no")
        self.tree.column("maduan",width=0, stretch="no")
        self.tree.column("noidung",width=0, stretch="no")
        self.tree.column("ngansachmoi", width=165)
        self.tree.column("thoigian", width=145)
        
        self.tree.heading("ngansachmoi", text="Ngân sách mới", anchor=CENTER)
        self.tree.heading("thoigian", text="Ngày cập nhật", anchor=CENTER)

        self.tree.bind('<<TreeviewSelect>>', self.controller.on_select)
        self.tree['show'] = 'headings'
        self.tree.place(x=110,y=175,height=275)
        self.controller.update_treeview()

    def create_view(self,data=None):
        self.root.configure(bg = "#FFFFFF")
        window_height = 500
        window_width = 800
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, 0))

        canvas = Canvas(
            self.root,
            bg = "#FFFFFF",
            height = 500,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        canvas.place(x = 0, y = 0)
        self.create_treeview()

        image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            408.0,
            248.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            265.0,
            292.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        button_quaylai = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.quay_lai_khoan_chi,
            relief="flat"
        )
        button_quaylai.place(
            x=526.0,
            y=402.0,
            width=177.0,
            height=48.0
        )

        button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        button_capnhat = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.cap_nhat_ngan_sach,
            relief="flat"
        )
        button_capnhat.place(
            x=526.0,
            y=339.0,
            width=177.0,
            height=48.0
        )

        entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            614.5,
            161.0,
            image=entry_image_1
        )
        self.entry_sotien = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_sotien.place(
            x=507.0,
            y=143.0,
            width=215.0,
            height=34.0
        )

        image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            418.0,
            59.0,
            image=image_image_3
        )

        entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            615.0,
            263.5,
            image=entry_image_2
        )
        self.textarea_noidung = Text(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0
        )
        self.textarea_noidung.place(
            x=486.0,
            y=216.0,
            width=258.0,
            height=97.0
        )
        self.entry_sotien.configure(bd=0,bg="#F4F4F4",fg="#000716",highlightthickness=0,font=('roboto',12))
        self.textarea_noidung.configure(bd=0,bg="#F4F4F4",fg="#000716",highlightthickness=0,font=('roboto',12))
        button_capnhat.configure(background="#F5F5F5")
        button_quaylai.configure(background="#F5F5F5")
        if data!=None:
            self.entry_sotien.insert(0, self.format_currency2(data[2]))
            self.textarea_noidung.insert("1.0", data[3])
        self.entry_sotien.bind('<KeyRelease>', self.format_currency)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.resizable(False, False)
        self.root.mainloop()


    def format_currency(self,event):
        number = self.entry_sotien.get()
        number = number.replace(".", "")
        number_str = str(number)
        decimal_part = ""
        
        if "." in number_str:
            number_str, decimal_part = number_str.split(".")
        
        formatted_number = ""
        while len(number_str) > 3:
            formatted_number = "." + number_str[-3:] + formatted_number
            number_str = number_str[:-3]
        
        formatted_number = number_str + formatted_number
        if decimal_part:
            formatted_number += "." + decimal_part
        
        self.entry_sotien.delete(0, END)
        self.entry_sotien.insert(0, formatted_number)

    def format_currency2(self,number):
        number_str = str(number)
        decimal_part = ""
        
        if "." in number_str:
            number_str, decimal_part = number_str.split(".")
        
        formatted_number = ""
        while len(number_str) > 3:
            formatted_number = "." + number_str[-3:] + formatted_number
            number_str = number_str[:-3]
        
        formatted_number = number_str + formatted_number
        if decimal_part:
            formatted_number += "." + decimal_part
        
        return formatted_number