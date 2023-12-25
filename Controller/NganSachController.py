from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from datetime import date
from Model.KhoanChiModel import KhoanChiModel
from View.View_QuanLyNganSach import View_QuanLyNganSach
import re

class NganSachController:
    maduan = None
    def __init__(self, model, viewCapNhatNganSach, maduan, loaitaikhoan):
        self.maduan = maduan
        self.model = model
        self.loaitaikhoan = loaitaikhoan
        global globalLoaitaikhoan 
        globalLoaitaikhoan = loaitaikhoan
        self.KhoanChiModel = KhoanChiModel()
        self.viewCapNhatNganSach = viewCapNhatNganSach
        self.viewCapNhatNganSach.create_controller(self)
        values = self.model.get_ngan_sach_hien_tai(maduan)
        self.viewCapNhatNganSach.create_view(values)
        self.thong_tin_ngan_sach()
        
        

    def display_result(self, result):
        messagebox.showinfo("Thông báo", result)

    def get_entry_value(self):
        ngansachmoi = self.viewCapNhatNganSach.entry_sotien.get()
        noidung = self.viewCapNhatNganSach.textarea_noidung.get("1.0",'end-1c')
        if ngansachmoi == "":
            self.display_result("Ngân sách mới không hợp lệ")
            return False
        elif noidung == "":
            self.display_result("Nội dung không hợp lệ")
            return False
        thoigiancapnhat  = date.today()
        return [ngansachmoi, noidung, thoigiancapnhat]
    
    def update_treeview(self):
        for item in self.viewCapNhatNganSach.tree.get_children():
            self.viewCapNhatNganSach.tree.delete(item)

        data = self.model.get_data_from_database(self.maduan)
        for item in data:
            self.viewCapNhatNganSach.tree.insert("", 0,values=(item[0],item[1],self.format_currency(item[2]),item[3],item[4]))

    def on_select(self, event):
        selected_items = self.viewCapNhatNganSach.tree.selection()
        if selected_items:
            selected_item = selected_items[0]
            values = self.viewCapNhatNganSach.tree.item(selected_item)['values']
            self.clear()
            self.mangansach = values[0]
            self.viewCapNhatNganSach.entry_sotien.insert(0, values[2].replace(" VND", ""))
            self.viewCapNhatNganSach.textarea_noidung.insert("1.0", values[3])
            

    def cap_nhat_ngan_sach(self):
        confirm = messagebox.askyesno(title="Xác nhận", message="Bạn có chắc chắn muốn cập nhật không?")
        if confirm:
            input_values = self.get_entry_value()
            if input_values:
                ngansachmoi, noidung, thoigiancapnhat = input_values
                ngansachmoi = ngansachmoi.replace(".", "")
                if int(ngansachmoi) < self.KhoanChiModel.get_ngan_sach_da_chi(self.maduan):
                    self.display_result("Ngân sách mới nhỏ hơn ngân sách đã chi")
                else:
                    self.model.cap_nhat_ngan_sach(self.maduan, ngansachmoi, noidung, thoigiancapnhat)
                    self.display_result("Cập nhật ngân sách thành công")
                    self.update_treeview()

    def quay_lai_khoan_chi(self):
        from Controller.KhoanChiController import KhoanChiController
        self.viewCapNhatNganSach.destroy()
        view = View_QuanLyNganSach()
        model = KhoanChiModel()
        KhoanChiController(model,view,self.maduan,self.loaitaikhoan)

    def clear(self):
        self.viewCapNhatNganSach.entry_sotien.delete(0, END)
        self.viewCapNhatNganSach.textarea_noidung.delete('1.0', END)

    def thong_tin_ngan_sach(self):
        self.tong_ngan_sach = self.KhoanChiModel.get_tong_ngan_sach(self.maduan)
        self.ngan_sach_da_chi = self.KhoanChiModel.get_ngan_sach_da_chi(self.maduan)
        self.ngan_sach_hien_tai = self.tong_ngan_sach - self.ngan_sach_da_chi
        
    def format_currency(self,number):
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
        
        return formatted_number + " VND"