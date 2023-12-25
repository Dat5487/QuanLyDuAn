from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import shutil
import tkinter as tk
from tkinter import filedialog
import os
from tkinter import messagebox

class View_FormHoSoDuAn:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\HoSoDuAn\frame0")
    def __init__(self):
        self.root = Tk()
        self.root.title("Hồ sơ dự án")

    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def open_file_browser(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.save_file_copy(self.file_path)

    def destroy(self):
        self.root.destroy()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Bạn chắc chắn muốn thoát chương trình ?"):
            self.root.destroy()

    def create_controller(self, controller):
        self.controller = controller

    def open_copied_file(self,file):
        self.file_path = "C:/Users/dat54/source/repos/QuanLyDuAn/Controller/files/" + file
        os.startfile(self.file_path)

    def save_file_copy(self,file_path):
        destination_path = "C:/Users/dat54/source/repos/QuanLyDuAn/Controller/files/"
        filename = os.path.basename(file_path)
        destination_file_path = os.path.join(destination_path, filename)
        shutil.copy2(file_path, destination_file_path)
        self.filename_label.config(text=filename)
        self.button_xemtep.config(state=tk.NORMAL)
        print('File copied successfully.')

    def validate_input(self,char):
        if char.isdigit() or char == "/":
            return True
        else:
            return False
        
    def create_view(self,mode,loaitaikhoan,data=None):
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
        # date_batdau = tb.DateEntry(self.root)
        # date_batdau.place(x=665,y=220)

        # date_ketthuc = tb.DateEntry(self.root,bootstyle="danger")
        # date_ketthuc.place(x=665,y=357)

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
        button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        button_image_4 = PhotoImage(
                file=self.relative_to_assets("button_4.png"))

        if mode == "themhoso":
            self.button_huy = Button(
                image=button_image_3,
                borderwidth=0,
                highlightthickness=0,
                command=self.controller.quay_lai_danh_sach,
                relief="flat"
            )
            self.button_huy.place(
                x=1015.0,
                y=329.0,
                width=177.0,
                height=45.0
            )
            
            self.button_luu = Button(
                image=button_image_4,
                borderwidth=0,
                highlightthickness=0,
                command=self.controller.them_ho_so,
                relief="flat"
            )
            self.button_luu.place(
                x=1015.0,
                y=269.0,
                width=177.0,
                height=45.0
            )     
        elif mode == "suahoso":
            self.button_huy = Button(
                image=button_image_3,
                borderwidth=0,
                highlightthickness=0,
                command=self.controller.thoat_sua_ho_so,
                relief="flat"
            )
            self.button_huy.place(
                x=1015.0,
                y=329.0,
                width=177.0,
                height=45.0
            )
            
            self.button_luu = Button(
                image=button_image_4,
                borderwidth=0,
                highlightthickness=0,
                command=lambda:self.controller.sua_ho_so(data[0]),
                relief="flat"
            )
            self.button_luu.place(
                x=1015.0,
                y=269.0,
                width=177.0,
                height=45.0
            )
            
        elif mode == "quanlyhoso":
            button_image_1 = PhotoImage(
                file=self.relative_to_assets("button_1.png"))
            self.button_xoa = Button(
                image=button_image_1,
                borderwidth=0,
                highlightthickness=0,
                command=self.controller.xoa_ho_so,
                relief="flat"
            )
            self.button_xoa.place(
                x=1015.0,
                y=264.0,
                width=177.0,
                height=45.0
            )
            button_image_2 = PhotoImage(
                file=self.relative_to_assets("button_2.png"))
            self.button_sua = Button(
                image=button_image_2,
                borderwidth=0,
                highlightthickness=0,
                command=self.controller.view_sua_ho_so,
                relief="flat"
            )
            self.button_sua.place(
                x=1015.0,
                y=200.0,
                width=177.4276123046875,
                height=47.00007629394531
            )
            button_image_7 = PhotoImage(
                file=self.relative_to_assets("button_7.png"))
            self.button_quaylai = Button(
                image=button_image_7,
                borderwidth=0,
                highlightthickness=0,
                command=self.controller.quay_lai_danh_sach,
                relief="flat"
            )
            self.button_quaylai.place(
                x=1015.0,
                y=326.0,
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
            831.0,
            550.0,
            image=image_image_4
        )

        canvas.create_text(
            744.883544921875,
            466.0,
            anchor="nw",
            text="File đính kèm",
            fill="#000000",
            font=("RobotoRoman SemiBold", 16 * -1)
        )

        image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(
            404.0,
            550.0,
            image=image_image_5
        )

        entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            411.0,
            561.0,
            image=entry_image_1
        )
        self.textarea_mota = Text(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0,
            font=('roboto',12)
        )
        self.textarea_mota.place(
            x=141.0,
            y=488.0,
            width=540.0,
            height=144.0
        )

        canvas.create_text(
            130.0,
            463.0,
            anchor="nw",
            text="Mô tả",
            fill="#000000",
            font=("RobotoRoman SemiBold", 16 * -1)
        )

        image_image_6 = PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        image_6 = canvas.create_image(
            784.0,
            370.0,
            image=image_image_6
        )

        canvas.create_text(
            657.0,
            330.0,
            anchor="nw",
            text="Thời gian dự kiến hoàn thành",
            fill="#000000",
            font=("RobotoRoman SemiBold", 16 * -1)
        )

        image_image_7 = PhotoImage(
            file=self.relative_to_assets("image_7.png"))
        image_7 = canvas.create_image(
            357.0,
            370.0,
            image=image_image_7
        )
        
        entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            359.5,
            380.0,
            image=entry_image_2
        )
        self.textarea_vitri = Text(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0,
            font=('roboto',12)
        )
        self.textarea_vitri.place(
            x=136.0,
            y=350.0,
            width=447.0,
            height=58.0
        )

        canvas.create_text(
            126.0,
            324.0,
            anchor="nw",
            text="Vị trí của dự án",
            fill="#000000",
            font=("RobotoRoman SemiBold", 16 * -1)
        )

        image_image_8 = PhotoImage(
            file=self.relative_to_assets("image_8.png"))
        image_8 = canvas.create_image(
            784.0,
            233.0,
            image=image_image_8
        )

        canvas.create_text(
            657.0,
            193.0,
            anchor="nw",
            text="Thời gian bắt đầu",
            fill="#000000",
            font=("RobotoRoman SemiBold", 16 * -1)
        )

        image_image_9 = PhotoImage(
            file=self.relative_to_assets("image_9.png"))
        image_9 = canvas.create_image(
            357.0,
            233.0,
            image=image_image_9
        )

        entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            359.5,
            248.0,
            image=entry_image_3
        )
        self.textarea_ten = Text(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0,
            font=('roboto',12)
        )
        self.textarea_ten.place(
            x=136.0,
            y=218.0,
            width=447.0,
            height=58.0
        )

        canvas.create_text(
            120.0,
            191.0,
            anchor="nw",
            text="Tên dự án",
            fill="#000000",
            font=("RobotoRoman SemiBold", 16 * -1)
        )

        image_image_10 = PhotoImage(
            file=self.relative_to_assets("image_10.png"))
        image_10 = canvas.create_image(
            515.0,
            76.0,
            image=image_image_10
        )
        self.lable = tk.Label(self.root, text="Tên tệp: ")
        self.lable.place(x=745,y=496)
        self.filename_label = tk.Label(self.root, text="")
        self.filename_label.place(x=790,y=496)

        button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        self.button_xemtep = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:self.open_copied_file(self.filename_label.cget("text")), state=tk.DISABLED,
            relief="flat",
            bg="#FFFFFF"
        )
        self.button_xemtep.place(
            x=774.0,
            y=579.0,
            width=106.0,
            height=26.112503051757812
        )

        button_image_6 = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        self.button_chontep = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_file_browser,
            relief="flat",
            bg="#FFFFFF"
        )
        self.button_chontep.place(
            x=774.0,
            y=542.0,
            width=106.0,
            height=26.112503051757812
        )
        canvas.create_text(
            745.0,
            496.0,
            anchor="nw",
            text="Tên tệp :",
            fill="#000000",
            font=("RobotoRoman SemiBold", 12 * -1)
        )

        value_var1 = tk.StringVar()
        value_var2 = tk.StringVar()
        vcmd = (self.root.register(self.validate_input), "%S")


        entry_image_4 = PhotoImage(
            file=self.relative_to_assets("entry_4.png"))
        entry_bg_4 = canvas.create_image(
            783.0,
            247.0,
            image=entry_image_4
        )
        self.entry_ngaybatdau = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_ngaybatdau.place(
            x=676.0,
            y=227.0,
            width=214.0,
            height=38.0
        )

        entry_image_5 = PhotoImage(
            file=self.relative_to_assets("entry_5.png"))
        entry_bg_5 = canvas.create_image(
            783.0,
            381.0,
            image=entry_image_5
        )
        self.entry_ngayhoanthanh = Entry(
            bd=0,
            bg="#F4F4F4",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_ngayhoanthanh.place(
            x=676.0,
            y=361.0,
            width=214.0,
            height=38.0
        )

        self.textarea_ten.configure(bg="#F4F4F4",fg="#000716",highlightthickness=0,font=('roboto',12))
        self.textarea_mota.configure(bg="#F4F4F4",fg="#000716",highlightthickness=0,font=('roboto',12))
        self.textarea_vitri.configure(bg="#F4F4F4",fg="#000716",highlightthickness=0,font=('roboto',12))
        self.entry_ngaybatdau.configure(bg="#F4F4F4",fg="#000716",highlightthickness=0,font=('roboto',12))
        self.entry_ngayhoanthanh.configure(bg="#F4F4F4",fg="#000716",highlightthickness=0,font=('roboto',12))
        if data is not None or mode!="themhoso":
            self.insert_data(data)

        if mode=="themhoso" or mode=="suahoso":
            self.button_luu.configure(bg="#FFFFFF")
            self.button_huy.configure(bg="#FFFFFF")
        elif mode=="quanlyhoso":
            self.textarea_ten.config(state= "disabled")
            self.textarea_mota.config(state= "disabled")
            self.textarea_vitri.config(state= "disabled")
            self.entry_ngaybatdau.config(state="disabled")
            self.entry_ngayhoanthanh.config(state="disabled")
            self.button_xoa.configure(bg="#FFFFFF")
            self.button_sua.configure(bg="#FFFFFF")
            self.button_quaylai.configure(bg="#FFFFFF")
            self.button_chontep.config(state="disabled")

        if(mode == "suahoso" or mode == "quanlyhoso"):
            if data[6] != "":
                self.button_xemtep.configure(state=tk.NORMAL)
                
        if loaitaikhoan == "Người xem":
            self.button_sua.configure(state="disabled")
            self.button_xoa.configure(state="disabled")

        self.button_xemtep.configure(bg="#FFFFFF")
        self.button_chontep.configure(bg="#FFFFFF")
        self.lable.configure(bg="#FFFFFF")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.resizable(False, False)
        self.root.mainloop()

    def insert_data(self,data):
        self.textarea_ten.insert("1.0", data[1])
        self.textarea_vitri.insert("1.0", data[2])
        self.entry_ngaybatdau.insert(0, data[3])
        self.entry_ngayhoanthanh.insert(0, data[4])
        self.textarea_mota.insert("1.0", data[5])
        self.filename_label.config(text=data[6])

