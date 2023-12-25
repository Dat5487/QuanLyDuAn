from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import customtkinter

class View_QuanLyTaiKhoan:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\QuanLyTaiKhoan\frame0")
    def __init__(self):
        self.root = Tk()
        self.root.title("Quản lý tài khoản")

    def create_controller(self, controller):
        self.controller = controller

    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def destroy(self):
        self.root.destroy()
        
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Bạn chắc chắn muốn thoát chương trình ?"):
            self.root.destroy()

    def create_treeview(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", highlightthickness=0, bd=0, font=('robota', 12)) # Modify the font of the body
        style.configure("Treeview.Heading", background="#3B71CA", foreground="white", font=('robota', 14))
        style.map("Treeview",background=[("selected","#9FA6B2")])
        style.map("Treeview.Heading",background=[("selected","#3B71CA")],foreground=[("selected","#white")])
        self.tree = ttk.Treeview(self.root)

        self.tree["columns"] = ("one", "two")
        self.tree.column("one", width=200)
        self.tree.column("two", width=250)
        self.tree.heading("one", text="Tên đăng nhập", anchor=CENTER)
        self.tree.heading("two", text="Loại tài khoản", anchor=CENTER)
        self.tree.bind('<<TreeviewSelect>>', self.controller.on_select)
        self.tree['show'] = 'headings'
        self.tree.place(x=100,y=210,height=460)
        self.controller.update_treeview()

    def create_view(self):
        self.root.configure(bg = "#FFFFFF")
        window_height = 720
        window_width = 1280
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, 0))

        canvas = Canvas(
            self.root,
            bg = "#FFFFFF",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        canvas.place(x = 0, y = 0)
        self.create_treeview()

        image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            638.0,
            361.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            934.0,
            400.0,
            image=image_image_2
        )
        


        button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_xoa = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.xoa_tai_khoan,
            relief="flat"
        )
        self.button_xoa.place(
            x=1040.0,
            y=303.0,
            width=123.0,
            height=34.0
        )

        button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.button_sua = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.sua_tai_khoan,
            relief="flat"
        )
        self.button_sua.place(
            x=1040.0,
            y=245.0,
            width=123.0,
            height=34.0
        )

        button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.button_them = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.them_tai_khoan,
            relief="flat"
        )
        self.button_them.place(
            x=1040.0,
            y=189.0,
            width=122.744384765625,
            height=34.0
        )

        button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        self.button_clear = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.clear,
            relief="flat"
        )
        self.button_clear.place(
            x=1041.0,
            y=359.0,
            width=122.744384765625,
            height=34.0
        )

        button_image_6 = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        button_dangxuat = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.dang_xuat,
            relief="flat"
        )
        button_dangxuat.place(
            x=1041.0,
            y=473.0,
            width=122.7443618774414,
            height=34.0
        )
        image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            328.0,
            446.0,
            image=image_image_3
        )

        entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            841.0,
            233.0,
            image=entry_image_1
        )
        self.entry_tendangnhap = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0,
            font=("roboto 12")
        )
        self.entry_tendangnhap.place(
            x=729.0,
            y=211.0,
            width=224.0,
            height=42.0
        )

        entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            841.0,
            322.0,
            image=entry_image_2
        )
        self.entry_matkhau = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0,
            font=("roboto 12")
        )
        self.entry_matkhau.place(
            x=729.0,
            y=300.0,
            width=224.0,
            height=42.0
        )
        
        entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            324.0,
            147.0,
            image=entry_image_3
        )
        self.entry_timkiem = Entry(
            bd=0,
            bg="#F4F4F4",
            highlightthickness=0,
            font=("roboto 12")
        )
        self.entry_timkiem.place(
            x=145.0,
            y=125.0,
            width=358.0,
            height=42.0
        )

        image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(
            662.0,
            57.0,
            image=image_image_4
        )

        customtkinter.set_appearance_mode("light")
        self.combobox_loaitaikhoan = customtkinter.CTkComboBox(self.root, values=["Người xem", "Người chỉnh sửa","Quản trị viên"],width=250,height=42,state="readonly",font=("roboto",12))
        self.combobox_loaitaikhoan.place(x=720,y=390)
        self.combobox_loaitaikhoan.set("Người xem")

        self.entry_tendangnhap.focus_set()
        self.entry_timkiem.bind('<KeyRelease>', self.controller.tim_kiem_tai_khoan)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.resizable(False, False)
        self.root.mainloop()



