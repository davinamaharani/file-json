import json

class JsonKu:
    def __init__(self, filepath):
        self.filepath = filepath

    def baca(self):
        #Membaca data dari file JSON
        try:
            with open(self.filepath, 'r') as file:
                data= json.load(file)
                return data
        except FileNotFoundError:
            return "File tidak ditemukan!"
        except json.JSONDecodeError:
            return "File tidak berisi JSON yang valid!"
        
    def tulis(self, data):
        #Menulis data ke file JSON
        with open(self.filepath, 'w') as file:
            json.dump(data, file, indent=4)
            return "Data berhasil ditulis!"
        
    def update(self, key, value):
        #Mengupdate data pada file JSON berdasarkan kunci
        data =  self.baca()
        if isinstance(data, dict):
            data[key] = value
            self.tulis(data)
            return f"Data dengan kunci '{key} berhasil diupdate!"
        return "Gagal mengupdate data!"
    
    def delete(self, key):
        #Menghapus data dari file JSON berdasarkan kunci
        data = self.baca()
        if isinstance(data, dict):
            if key in data:
                del data[key]
                self.tulis(data)
                return f"Data dengan kunci '{key}' berhasil dihapus!"
            else:
                return f"Kunci '{key}' tidak ditemukan dalam data!"
            return "Gagal menghapus data!"