from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

class View_FormCongViec:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\XemCongViec\frame0")
    def __init__(self):
        self.root = Tk()
        self.root.title("Theo dõi tiến độ")

    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def create_controller(self, controller):
        self.controller = controller

    def destroy(self):
        self.root.update()
        self.root.destroy()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Bạn chắc chắn muốn thoát chương trình ?"):
            self.root.destroy()

    def create_view(self,mode,data = None, loaitaikhoan = None):
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
            1103.0,
            401.0,
            image=image_image_2
        )

        if mode == "themcongviec":
            button_image_5 = PhotoImage(
                file=self.relative_to_assets("button_5.png"))
            button_huy = Button(
                image=button_image_5,
                borderwidth=0,
                highlightthickness=0,
                command=self.controller.quay_lai_theo_doi_tien_do,
                relief="flat"
            )
            button_huy.place(
                x=1015.0,
                y=329.0,
                width=177.0,
                height=45.0
            )

            button_image_4 = PhotoImage(
                file=self.relative_to_assets("button_4.png"))
            button_luu = Button(
                image=button_image_4,
                borderwidth=0,
                highlightthickness=0,
                command=self.controller.them_cong_viec,
                relief="flat"
            )
            button_luu.place(
                x=1015.0,
                y=269.0,
                width=177.0,
                height=45.0
            )

        elif mode == "xemcongviec":
            button_image_1 = PhotoImage(
                file=self.relative_to_assets("button_1.png"))
            button_xoa = Button(
                image=button_image_1,
                borderwidth=0,
                highlightthickness=0,
                command=self.controller.xoa_cong_viec,
                relief="flat"
            )
            button_xoa.place(
                x=1015.0,
                y=264.0,
                width=177.0,
                height=45.0
            )

            button_image_2 = PhotoImage(
                file=self.relative_to_assets("button_2.png"))
            button_quaylai = Button(
                image=button_image_2,
                borderwidth=0,
                highlightthickness=0,
                command=self.controller.quay_lai_theo_doi_tien_do,
                relief="flat"
            )
            button_quaylai.place(
                x=1015.0,
                y=326.0,
                width=177.0,
                height=45.0
            )

            button_image_3 = PhotoImage(
                file=self.relative_to_assets("button_3.png"))
            button_capnhat = Button(
                image=button_image_3,
                borderwidth=0,
                highlightthickness=0,
                command=self.controller.view_sua_cong_viec,
                relief="flat"
            )
            button_capnhat.place(
                x=1015.0,
                y=200.0,
                width=177.4276123046875,
                height=47.00007629394531
            )
        elif mode=="suacongviec":
            button_image_5 = PhotoImage(
                file=self.relative_to_assets("button_5.png"))
            button_huy = Button(
                image=button_image_5,
                borderwidth=0,
                highlightthickness=0,
                command=self.controller.quay_lai_xem_cong_viec,
                relief="flat"
            )
            button_huy.place(
                x=1015.0,
                y=329.0,
                width=177.0,
                height=45.0
            )

            button_image_4 = PhotoImage(
                file=self.relative_to_assets("button_4.png"))
            button_luu = Button(
                image=button_image_4,
                borderwidth=0,
                highlightthickness=0,
                command=self.controller.sua_cong_viec,
                relief="flat"
            )
            button_luu.place(
                x=1015.0,
                y=269.0,
                width=177.0,
                height=45.0
            )

        image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            514.0,
            418.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(
            513.0,
            557.0,
            image=image_image_4
        )

        entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            510.5,
            567.5,
            image=entry_image_1
        )
        self.textarea_chitiet = Text(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0
        )
        self.textarea_chitiet.place(
            x=136.0,
            y=502.0,
            width=749.0,
            height=133.0
        )

        image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(
            784.0,
            374.0,
            image=image_image_5
        )

        image_image_6 = PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        image_6 = canvas.create_image(
            357.0,
            362.0,
            image=image_image_6
        )

        entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            359.5,
            373.5,
            image=entry_image_2
        )
        self.textarea_mota = Text(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0
        )
        self.textarea_mota.place(
            x=136.0,
            y=331.0,
            width=447.0,
            height=87.0
        )

        image_image_7 = PhotoImage(
            file=self.relative_to_assets("image_7.png"))
        image_7 = canvas.create_image(
            784.0,
            233.0,
            image=image_image_7
        )

        entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            777.5,
            240.5,
            image=entry_image_3
        )
        self.entry_tiendotong = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_tiendotong.place(
            x=670.0,
            y=222.0,
            width=215.0,
            height=39.0
        )

        entry_image_4 = PhotoImage(
            file=self.relative_to_assets("entry_4.png"))
        entry_bg_4 = canvas.create_image(
            777.5,
            380.5,
            image=entry_image_4
        )
        self.entry_tiendohientai = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_tiendohientai.place(
            x=670.0,
            y=362.0,
            width=215.0,
            height=39.0
        )

        image_image_8 = PhotoImage(
            file=self.relative_to_assets("image_8.png"))
        image_8 = canvas.create_image(
            357.0,
            220.0,
            image=image_image_8
        )

        entry_image_5 = PhotoImage(
            file=self.relative_to_assets("entry_5.png"))
        entry_bg_5 = canvas.create_image(
            356.5,
            230.3636245727539,
            image=entry_image_5
        )
        self.entry_tencongviec = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_tencongviec.place(
            x=130.0,
            y=209.69696044921875,
            width=453.0,
            height=39.33332824707031
        )

        image_image_9 = PhotoImage(
            file=self.relative_to_assets("image_9.png"))
        image_9 = canvas.create_image(
            539.0,
            76.0,
            image=image_image_9
        )

        if mode == "xemcongviec" or mode == "suacongviec":
            self.insert_data(data)

        if mode == "xemcongviec":
            self.entry_tencongviec.configure(state="disabled")
            self.entry_tiendotong.configure(state="disabled")
            self.entry_tiendohientai.configure(state="disabled")
            self.textarea_mota.configure(state="disabled")
            self.textarea_chitiet.configure(state="disabled")


        self.entry_tencongviec.configure(bg="#F4F4F4",fg="#000716",highlightthickness=0,font=('roboto',12))
        self.entry_tiendohientai.configure(bg="#F4F4F4",fg="#000716",highlightthickness=0,font=('roboto',12))
        self.entry_tiendotong.configure(bg="#F4F4F4",fg="#000716",highlightthickness=0,font=('roboto',12))
        self.textarea_chitiet.configure(bg="#F4F4F4",fg="#000716",highlightthickness=0,font=('roboto',12))
        self.textarea_mota.configure(bg="#F4F4F4",fg="#000716",highlightthickness=0,font=('roboto',12))
        if loaitaikhoan == "Người xem":
            button_capnhat.configure(state="disabled")
            button_xoa.configure(state="disabled")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.resizable(False, False)
        self.root.mainloop()

    def insert_data(self,data):
        self.entry_tencongviec.insert(0, data[0])
        self.entry_tiendotong.insert(0, data[1])
        self.entry_tiendohientai.insert(0, data[2])
        self.textarea_mota.insert("1.0", data[3])
        self.textarea_chitiet.insert("1.0", data[4])