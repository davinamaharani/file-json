# Program utama

from json_ku import JsonKu

def main():
    # Tentukan file path untuk file JSON
    file_path = 'data_json'

    # Inisialisasi objek JsonKu
    json_ku = JsonKu(file_path)

    # Data yang akan ditulis ke file
    data_json = {
        "nama": "Davina",
        "umur": 17,
        "alamat": "Jalan Lesanpuro 2b Malang",
        "status": "pelajar"
    }

    # Tulis data ke file
    print(json_ku.tulis(data_json))

    # Baca data dari file
    print("Data awal:", json_ku.baca())

    # Update data
    print(json_ku.update("umur", 17))

    # Baca data setelah update
    print("Data setelah update:", json_ku.baca())

    # Delete data
    print(json_ku.delete("status"))

    # Baca data setelah delete
    print("Data setelah delete:", json_ku.baca())

if __name__ == "__main__":
    main()