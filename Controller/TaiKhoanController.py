from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from View.View_QuanLyTaiKhoan import View_QuanLyTaiKhoan
from View.View_DanhSachDuAn import View_DanhSachDuAn
from View.View_Login import View_Login
from Model.HoSoModel import HoSoModel
from Controller.HoSoController import HoSoController

class TaiKhoanController:
    def __init__(self, model, viewLogin):
        self.model = model
        self.viewLogin = viewLogin
        self.viewLogin.create_controller(self)
        self.viewLogin.create_view()

    def display_result(self, result):
        messagebox.showinfo("Thông báo", result)

    def get_entry_value(self):
        tendangnhap = self.viewLogin.entry_tendangnhap.get()
        matkhau = self.viewLogin.entry_matkhau.get()
        if not tendangnhap or not matkhau:
            self.display_result("Chưa nhập đủ thông tin!")
            return False
        return [tendangnhap, matkhau]

    def check_account(self,event=None):
        if self.get_entry_value() is False:
            return
        input_values = self.get_entry_value()
        tendangnhap, matkhau = input_values
        result = self.model.DangNhap(tendangnhap, matkhau)
        if result is not False:
            self.viewLogin.destroy()
            if result[2] == "Quản trị viên":
                self.viewQuanLyTaiKhoan = View_QuanLyTaiKhoan()
                self.viewQuanLyTaiKhoan.create_controller(self)
                self.viewQuanLyTaiKhoan.create_view()
            elif result[2] == "Người chỉnh sửa":
                view = View_DanhSachDuAn()
                model = HoSoModel()
                HoSoController(model, view, "Người chỉnh sửa")
            elif result[2] == "Người xem":
                view = View_DanhSachDuAn()
                model = HoSoModel()
                HoSoController(model, view, "Người xem")

        else:
            self.display_result('Thông tin đăng nhập không đúng')
    
    def get_entry_value_QLTK(self):
        tendangnhap = self.viewQuanLyTaiKhoan.entry_tendangnhap.get()
        matkhau = self.viewQuanLyTaiKhoan.entry_matkhau.get()
        loaitaikhoan = self.viewQuanLyTaiKhoan.combobox_loaitaikhoan.get()
        return [tendangnhap, matkhau, loaitaikhoan]

    def update_treeview(self):
        for item in self.viewQuanLyTaiKhoan.tree.get_children():
            self.viewQuanLyTaiKhoan.tree.delete(item)

        data = self.model.get_data_from_database()
        for item in data:
            self.viewQuanLyTaiKhoan.tree.insert("", 0,values=(item[0], item[2]))

    def get_selected_item(self):
        selected_item = self.viewQuanLyTaiKhoan.tree.selection()
        if selected_item:
            return selected_item[0]
        return None

    def them_tai_khoan(self):
        input_values = self.get_entry_value_QLTK()
        tendangnhap, matkhau, loaitaikhoan = input_values
        if not tendangnhap or not matkhau:
            self.display_result("Chưa nhập đủ thông tin!")
            return
        
        if self.model.check_ten_dang_nhap(tendangnhap):
            result = self.model.them_tai_khoan(tendangnhap, matkhau, loaitaikhoan)
            self.display_result("Thêm tài khoản thành công")
            self.update_treeview()
            self.clear()
        else:
            self.display_result('Đã có tên đăng nhập này trong hệ thống')

    def sua_tai_khoan(self):
        selected_item = self.get_selected_item()
        if selected_item:
            tendangnhap = self.viewQuanLyTaiKhoan.entry_tendangnhap.get()
            matkhau = self.viewQuanLyTaiKhoan.entry_matkhau.get()
            loaitaikhoan = self.viewQuanLyTaiKhoan.combobox_loaitaikhoan.get()
            result = self.model.sua_tai_khoan(tendangnhap, matkhau, loaitaikhoan)
            self.display_result("Sửa tài khoản thành công")
            self.update_treeview()
        else:
            self.display_result("Hãy chọn bản ghi cần sửa")
            
    def xoa_tai_khoan(self):
        selected_item = self.get_selected_item()
        if selected_item:
            tendangnhap = self.viewQuanLyTaiKhoan.entry_tendangnhap.get()
            result = self.model.xoa_tai_khoan(tendangnhap)
            self.display_result("Xóa tài khoản thành công")
            self.update_treeview()
            self.clear()
        else:
            self.display_result("Hãy chọn bản ghi cần xóa")

    def tim_kiem_tai_khoan(self,event):
        search_text = self.viewQuanLyTaiKhoan.entry_timkiem.get()
        for item in self.viewQuanLyTaiKhoan.tree.get_children():
            self.viewQuanLyTaiKhoan.tree.delete(item)
        if search_text:
            for item in self.model.tim_kiem_tai_khoan(search_text):
                self.viewQuanLyTaiKhoan.tree.insert("", 0, values=(item[0], item[2]))
        else:
            self.update_treeview()

    def clear(self):
        self.viewQuanLyTaiKhoan.entry_tendangnhap.config(state="normal")
        self.viewQuanLyTaiKhoan.entry_tendangnhap.delete(0, END)
        self.viewQuanLyTaiKhoan.entry_matkhau.delete(0, END)
        self.viewQuanLyTaiKhoan.entry_timkiem.delete(0, END)

    def on_select(self, event):
        selected_items = self.viewQuanLyTaiKhoan.tree.selection()
        if selected_items:
            self.clear()
            selected_item = selected_items[0]
            values = self.viewQuanLyTaiKhoan.tree.item(selected_item)['values']
            if isinstance(values[0],str):
                tendangnhap = values[0].rstrip()
            else:
                tendangnhap = values[0]
            self.viewQuanLyTaiKhoan.entry_tendangnhap.insert(0, tendangnhap)
            self.viewQuanLyTaiKhoan.entry_tendangnhap.config(state="readonly")
            self.viewQuanLyTaiKhoan.combobox_loaitaikhoan.set(values[1])


    def dang_xuat(self):
        confirm = messagebox.askyesno(title="Xác nhận", message="Bạn có chắc chắn muốn đăng xuất không?")
        if confirm:
            self.viewQuanLyTaiKhoan.destroy()
            self.viewLogin = View_Login()
            self.viewLogin.create_controller(self)
            self.viewLogin.create_view()

