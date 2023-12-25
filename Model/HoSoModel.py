import os
import pyodbc
import openpyxl
from tkinter import messagebox


class HoSoModel:
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
  
    def get_data_from_database(self):
        data = []
        for row in self.cursor.execute("SELECT * FROM HoSo"):
            data.append(row)
        return data
    
    def get_data_from_maduan(self,maduan):
        data = []
        for row in  self.cursor.execute(f"SELECT * FROM HoSo WHERE maduan='{maduan}'"):
            data.append(row)
        return data
    
    def them_ho_so(self, tenduan, vitri, ngaybatdau, dukienhoanthanh, mota, tailieu):
        self.cursor.execute(f"INSERT INTO HoSo (tenduan, vitri, ngaybatdau, dukienhoanthanh, mota, tailieu) VALUES (N'{tenduan}', N'{vitri}', N'{ngaybatdau}', N'{dukienhoanthanh}', N'{mota}', N'{tailieu}')")
        self.conn.commit()
        return True

    def sua_ho_so(self, maduan, tenduan, vitri, ngaybatdau, dukienhoanthanh, mota, tailieu):
        self.cursor.execute(f"UPDATE HoSo SET tenduan=N'{tenduan}', vitri=N'{vitri}', ngaybatdau=N'{ngaybatdau}', dukienhoanthanh=N'{dukienhoanthanh}', mota=N'{mota}', tailieu=N'{tailieu}' WHERE maduan='{maduan}'")
        self.conn.commit()
        return True

    def xoa_ho_so(self,maduan):
        confirm = messagebox.askyesno(title="Xác nhận", message="Bạn có chắc chắn muốn xóa không?")
        if confirm:
            self.cursor.execute(f"DELETE FROM HoSo WHERE maduan='{maduan}'")
            self.conn.commit()
            return True
        else:
            return False

    def tim_kiem_ho_so(self, search_text):
        try:
            data = []
            for item in self.cursor.execute(f"SELECT * FROM HoSo WHERE tenduan LIKE '%{search_text}%'"):
                data.append(item)
            return data
        except pyodbc.Error as e:
            self.exception("Lỗi Truy vấn", f"Lỗi khi truy vấn cơ sở dữ liệu:\n{str(e)}")

    

