choice = "0"

student = {
    "name": "",
    "nim": "",
    "age": 0,
    "program": "",
    "ipk": 0,
}

def choices():
    print("""
DATA MAHASISWA
Pilih menu di bawah ini:
1. Lihat Data
2. Ubah Data
3. Keluar
  """)
    choice = input("Pilih menu : ")
    return choice


while choice != "3":
    choice = choices()
    if choice == "1":
        print(f"""
DATA MAHASISWA
Nama: {student["name"]}
NIM: {student["nim"]}
Umur: {student["age"]}
Prodi: {student["program"]}
IPK Terakhir: {float(student["ipk"])}
  """)

    elif choice == "2":

        student["name"] = input("Masukkan Nama: ")
        student["nim"] = input("Masukkan NIM: ")
        student["age"] = input("Masukkan Umur: ")
        student["program"] = input("Masukkan Prodi: ")
        student["ipk"] = input("Masukkan IPK: ")

        print("Data anda sudah tersimpan!")

print("Terima kasih!")