from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
from tkinter import messagebox

class View_FormKhoanChi:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\ThemKhoanChi\frame0")

    def __init__(self):
        self.root = Tk()
        self.root.title("Khoản chi")

    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def destroy(self):
        self.root.destroy()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Bạn chắc chắn muốn thoát chương trình ?"):
            self.root.destroy()

    def create_controller(self, controller):
        self.controller = controller

    def create_view(self, mode, data = None):
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
        image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            400.0,
            248.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            268.0,
            291.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        button_quaylai = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= self.controller.quay_lai_quan_ly_ngan_sach,
            background="#EB8B85",
            relief="flat"
        )
        button_quaylai.place(
            x=550.0,
            y=218.0,
            width=177.0,
            height=45.0
        )
        if(mode=="themkhoanchi"):
            button_image_3 = PhotoImage(
                file=self.relative_to_assets("button_3.png"))
            button_them = Button(
                image=button_image_3,
                borderwidth=0,
                highlightthickness=0,
                command=self.controller.them_khoan_chi,
                background="#EB8B85",
                relief="flat"
            )
            button_them.place(
                x=550.0,
                y=149.0,
                width=177.0,
                height=48.0
            )

        if mode == "themkhoanchi":
            image_image_4 = PhotoImage(
                file=self.relative_to_assets("image_4.png"))
            image_4 = canvas.create_image(
                409.0,
                59.0,
                image=image_image_4
            )
        else:
            image_image_5 = PhotoImage(
                file=self.relative_to_assets("image_5.png"))
            image_5 = canvas.create_image(
                409.0,
                59.0,
                image=image_image_5
)

        entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            261.5,
            388.0,
            image=entry_image_1
        )
        self.textarea_noidung = Text(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0
        )
        self.textarea_noidung.place(
            x=93.0,
            y=328.0,
            width=337.0,
            height=124.0
        )

        entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            261.5,
            263.5,
            image=entry_image_2
        )
        self.entry_sotien = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_sotien.place(
            x=93.0,
            y=242.0,
            width=337.0,
            height=45.0
        )

        entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            261.5,
            182.5,
            image=entry_image_3
        )
        self.entry_ten = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_ten.place(
            x=93.0,
            y=161.0,
            width=337.0,
            height=45.0
        )
        
        button_quaylai.configure(background="#EB8B85")
        self.entry_sotien.configure(bd=0,bg="#F4F4F4",highlightthickness=0,font=('roboto',12))
        self.entry_ten.configure(bd=0,bg="#F4F4F4",highlightthickness=0,font=('roboto',12))
        self.textarea_noidung.configure(bd=0,bg="#F4F4F4",highlightthickness=0,font=('roboto',12))
        if(mode == "themkhoanchi"):
            button_them.configure(background="#EB8B85")
        elif(mode == "xemkhoanchi"):
            self.insert_data(data)
            self.entry_ten.configure(state="disabled")
            self.entry_sotien.configure(state="disabled")
            self.textarea_noidung.configure(state="disabled")

        self.entry_sotien.bind('<KeyRelease>', self.format_currency)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.resizable(False, False)
        self.root.mainloop()

    def insert_data(self,data):
        self.entry_ten.insert(0, data[0])
        self.entry_sotien.insert(0, data[1])
        self.textarea_noidung.insert("1.0", data[2])

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