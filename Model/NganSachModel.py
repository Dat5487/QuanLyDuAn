import os
import pyodbc
import openpyxl
from tkinter import messagebox


class NganSachModel:
    maduan = None
    def __init__(self,):
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
    
    def get_data_from_database(self,maduan):
        data = []
        for row in self.cursor.execute(f"SELECT * FROM NganSach WHERE maduan={maduan}"):
            data.append(row)
        return data
    
    def cap_nhat_ngan_sach(self,maduan, ngansachmoi, noidung, thoigiancapnhat):
        self.cursor.execute(f"INSERT INTO NganSach (maduan, ngansachmoi, noidung, thoigiancapnhat) VALUES ({maduan}, {ngansachmoi}, N'{noidung}', N'{thoigiancapnhat}')")
        
        self.conn.commit()
        self.cursor.execute(f"UPDATE HoSo SET tongngansach={ngansachmoi} WHERE maduan='{maduan}'")
        self.conn.commit()
        return True
    
    def get_ngan_sach_hien_tai(self,maduan):
        result =  self.cursor.execute(f"SELECT TOP 1 * FROM NganSach WHERE maduan = {maduan} ORDER BY mangansach DESC;")
        return result.fetchone()

    

