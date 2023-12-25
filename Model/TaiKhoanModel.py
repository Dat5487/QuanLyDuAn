import os
import pyodbc
import openpyxl
from tkinter import messagebox


class TaiKhoanModel:
    def __init__(self):
        self.conn_str = (
            "Driver={SQL Server};"
            "Server=DESKTOP-IS4BEN5\SQLEXPRESS;"
            "Database=QuanLyDuAn;"
            "Trusted_Connection=yes"
        )
        try:
            self.conn = pyodbc.connect(self.conn_str)
            self.cursor = self.conn.cursor()
        except pyodbc.Error as e:
            self.exception("Lỗi Kết nối", f"Không thể kết nối đến cơ sở dữ liệu:\n{str(e)}")
            exit()

    def DangNhap(self, tendangnhap, matkhau):
        data = []
        for row in self.cursor.execute(f"SELECT * FROM TaiKhoan WHERE tendangnhap='{tendangnhap}' AND matkhau='{matkhau}'"):
            data.append(row)
        
        if data == []:
            return False
        else:
            return data[0]
        
    def check_ten_dang_nhap(self, tendangnhap):
        data = []
        for row in self.cursor.execute(f"SELECT * FROM TaiKhoan WHERE tendangnhap='{tendangnhap}'"):
            data.append(row)
        if data == []:
            return True
        else:
            return False
        
    def get_data_from_database(self):
        data = []
        for row in self.cursor.execute("SELECT * FROM TaiKhoan"):
            data.append(row)
        return data

    def them_tai_khoan(self, tendangnhap, matkhau, loaitaikhoan):
        self.cursor.execute(f"SELECT * FROM TaiKhoan WHERE tendangnhap='{tendangnhap}'")
        result = self.cursor.fetchone()
        if result is not None:
            return False
        self.cursor.execute(f"INSERT INTO TaiKhoan (tendangnhap, matkhau, loaitaikhoan) VALUES ('{tendangnhap}', '{matkhau}', N'{loaitaikhoan}')")
        self.conn.commit()
        return True

    def sua_tai_khoan(self, tendangnhap, matkhau, loaitaikhoan):
        if matkhau=="":
            self.cursor.execute(f"UPDATE TaiKhoan SET loaitaikhoan=N'{loaitaikhoan}' WHERE tendangnhap='{tendangnhap}'")
        else:
            self.cursor.execute(f"UPDATE TaiKhoan SET matkhau='{matkhau}', loaitaikhoan=N'{loaitaikhoan}' WHERE tendangnhap='{tendangnhap}'")
        self.conn.commit()
        return True

    def xoa_tai_khoan(self,tendangnhap):
        confirm = messagebox.askyesno(title="Xác nhận", message="Bạn có chắc chắn muốn xóa không?")
        if confirm:
            self.cursor.execute(f"DELETE FROM TaiKhoan WHERE tendangnhap='{tendangnhap}'")
            self.conn.commit()
            return True
        else:
            return False

    def tim_kiem_tai_khoan(self, search_text):
        try:
            data = []
            for item in self.cursor.execute(f"SELECT * FROM TaiKhoan WHERE tendangnhap LIKE '%{search_text}%'"):
                data.append(item)
            return data
        except pyodbc.Error as e:
            self.exception("Lỗi Truy vấn", f"Lỗi khi truy vấn cơ sở dữ liệu:\n{str(e)}")

    


