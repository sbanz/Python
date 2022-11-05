import sys
import os
def clear():
    os.system("cls" if os.name=="nt" else "clear")

arr = [
    {"nama" : "Saban", "umur" : "25", "nik" : "6472040210970005", "tgl" : "24-05-2020"},
    {"nama" : "Liu", "umur" : "18", "nik" : "6309061905030006", "tgl" : "23-06-2021"},
    {"nama" : "Alfi", "umur" : "12", "nik" : "6489010202100002", "tgl" : "23-01-2022"}
]

def show():
    for y, x in enumerate(arr):
        x.update({"nomor" : int(y)+1})
        print("Nomor Pasien     : ",x["nomor"])
        output(x)
        print("")
    input("Tekan Enter untuk lanjut")
    print("")

def change():
    show()
    while True:
        try:
            nomor = int(input("Masukkan Nomor Pasien    : "))
            break
        except:
            print("Input anda salah !!!")
    clear()
    for data in arr:
        if data["nomor"] == nomor:
            while True:
                try:
                    nama = str(input("Masukkan Nama                 : "))
                    umur = str(input("Masukkan Umur                 : "))
                    nik =  str(input("Masukkan NIK                  : "))
                    tgl =  str(input("Tanggal Masuk RS (dd-mm-yyyy) : "))
                    data["nama"] = nama
                    data["umur"] = umur
                    data["nik"] = nik
                    data["tgl"] = tgl
                    break
                except:
                    print("Input anda salah !!!")

def input_data():
    data = {}
    while True:
        try:
            data["nama"] = str(input("Masukkan Nama                 : "))
            data["umur"] = str(input("Masukkan Umur                 : "))
            data["nik"] =  str(input("Masukkan NIK                  : "))
            data["tgl"] =  str(input("Tanggal Masuk RS (dd-mm-yyyy) : "))
            arr.append(data)
            print("")
            print("Data berhasil ditambahkan")
            break
        except:
            print("Masukkan Input yang benar")
    clear()

def deleting():
    show()
    while True:
        try:
            dele = int(input("Data Nomor Pasien berapa yang ingin dihapus : "))
            break
        except:
            print("Input anda salah !!!")
    clear()
    for data in arr:
        if data["nomor"] == dele:
            print("Nomor Pasien     : ", data["nomor"])
            output(data)
            confirm = str(input("Anda yakin ingin menghapus data ini (y/n) : "))
            if confirm == "y":
                for index in range(len(arr)):
                    if arr[index]["nomor"] == dele:
                        del arr[index]
                        break
            print("Data telah dihapus")
    clear()

def output(z):
    print("Nama             : ", z["nama"])
    print("Umur             : ", z["umur"])
    print("NIK              : ", z["nik"])
    print("Tanggal Masuk RS : ", z["tgl"])

def manage_menu():
    clear()
    print("""
    ========MANAGEMENT MENU========
    1. Lihat data
    2. Ubah data
    3. Tambah data
    4. Hapus data
    5. Kembali""")
    while True:
        try:
            print("")
            pilihan = int(input("Pilih : "))
            break
        except:
            print("Input sesuai dengan menu !!!")
    if pilihan == 1:
        show()
        manage_menu()
    elif pilihan == 2:
        change()
        manage_menu()
    elif pilihan == 3:
        input_data()
        manage_menu()
    elif pilihan == 4:
        deleting()
        manage_menu()
    elif pilihan == 5:
        main_menu()
    clear()

def partition(array, low, high, value):
    pivot = array[low]
    x = low + 1
    y = high
    while True:
        while x <= y and array[x][value] <= pivot[value]:
            x = x + 1
        while x <= y and array[y][value] >= pivot[value]:
            y = y - 1
        if x <= y:
            array[x], array[y] = array[y], array[x]
        else:
            break
    array[low], array[y] = array[y], array[low]
    return y
def quick_sort(array, low, high, value):
   if low >= high:
      return
   p = partition(array, low, high, value)
   quick_sort(array, low, p - 1, value)
   quick_sort(array, p + 1, high, value)

def sort_menu():
    clear()
    print("""
    ========SORT MENU========
    1. Urutkan berdasarkan Nama
    2. Urutkan berdasarkan Umur
    3. Urutkan berdasarkan NIK
    4. Urutkan berdasarkan Tanggal Masuk RS
    5. Kembali""")
    while True:
        try:
            print("")
            pilih = int(input("Pilih : "))
            break
        except:
            print("Input sesuai dengan menu !!!")
    if pilih == 1:
        quick_sort(arr, 0, len(arr)-1, "nama")
        for x in arr:
            output(x)
            print("")
        input("Tekan Enter untuk lanjut")
        sort_menu()
    elif pilih == 2:
        quick_sort(arr, 0, len(arr)-1, "umur")
        for x in arr:
            output(x)
            print("")
        input("Enter Untuk melanjutkan")
        sort_menu()
    elif pilih == 3:
        quick_sort(arr, 0, len(arr)-1, "nik")
        for x in arr:
            output(x)
            print("")
        input("Enter Untuk melanjutkan")
        sort_menu()
    elif pilih == 4:
        quick_sort(arr, 0, len(arr)-1, "tgl")
        for x in arr:
            output(x)
            print("")
        input("Tekan Enter untuk lanjut")
        sort_menu()
    elif pilih == 5:
        clear()
        main_menu()

def lin_search(arr, find):
    founded = []
    for element in arr:
        for nilai in element.items():
            if find.lower() in str(nilai).lower():
                founded.append(element)
    return founded

def search_menu():
    clear()
    print("""
    ========SEARCH MENU========
    1. Cari Nama
    2. Cari Umur
    3. Cari NIK
    4. Cari Tanggal Masuk RS
    5. Kembali""")
    while True:
        try:
            print("")
            pilihh = int(input("Pilih : "))
            break
        except:
            print("Input sesuai dengan menu !!!")       
    if pilihh == 1:
        print("")
        carikan = str(input("Masukkan Nama yang dicari : "))
        print("")
        find = lin_search(arr, carikan)
        if find != []:
            for x in find:
                output(x)
                print("")
                break
        else:
            print("Data tidak ditemukan")
        input("Tekan Enter untuk lanjut")
        search_menu()
    elif pilihh == 2:
        print("")
        carikan = str(input("Masukkan Umur yang dicari : "))
        print("")
        find = lin_search(arr, carikan)
        if find != []:
            for x in find:
                output(x)
                print("")
        else:
            print("Data tidak ditemukan")
        input("Tekan Enter untuk lanjut")
        search_menu()
    elif pilihh == 3:
        print("")
        carikan = str(input("Masukkan NIK yang dicari : "))
        print("")
        find = lin_search(arr, carikan)
        if find != []:
            for x in find:
                output(x)
                print("")
        else:
            print("Data tidak ditemukan")
        input("Tekan Enter untuk lanjut")
        search_menu()
    elif pilihh == 4:
        print("")
        carikan = str(input("Tanggal masuk RS (dd-mm-yyyy) : "))
        print("")
        find = lin_search(arr, carikan)
        if find != []:
            for x in find:
                output(x)
                print("")
        else:
            print("Data tidak ditemukan")
        input("Tekan Enter untuk lanjut")
        search_menu()
    elif pilihh == 5:
        clear()
        main_menu() 

def main_menu():
    print("""
    ========MAIN MENU========
    1. MANAGE MENU
    2. SORT MENU
    3. SEARCH MENU
    4. exit""")

    loop = True
    while loop == True:
        print("")
        pilih = int(input("Pilih : "))
        if pilih == 1:
            clear()
            manage_menu()
        elif pilih == 2:
            clear()
            sort_menu()
        elif pilih == 3:
            clear()
            search_menu()
        elif pilih == 4:
            clear()
            loop = False
            sys.exit()
        else:
            print("Input sesuai dengan menu !!!") 
    
main_menu()