pilihan = "0"
Menus = [
  ["1.","Nasi Goreng","",15000, "Makanan"],
  ["2.","Mie Goreng", " ",10000, "Makanan"],
  ["3.","Mie Mawut", "  ",13000, "Makanan"],
  ["4.","Es Teh", "     ",5000, "Minuman"],
  ["5.","Teh Hangat", " ",6000, "Minuman"],
  ["6.","Es Jeruk", "   ",5000, "Minuman"]
  ]

def Menuz():
  print("===========Menu==========")
  for index in range (len(Menus)) :
            print(Menus[index][0], Menus[index][1], Menus[index][2], "RP.", Menus[index][3])
  print("========================")

def main():
	print("\n=============== Promo Super Gila! ==============")
	print("PEMBELIAN 3 MINUMAN DISKON SEBESAR 10%")
	print("PEMBELIAN 2 MAKANAN DISKON SEBESAR 5%")
	print("PEMBELIAN MENGGUNAKAN E-money DISKON SEBESAR 5%")
	print("DISKON SEBESAR 5% SAAT WEEKEND")
	print("DISKON SEBESAR 10% SAAT WEEKDAYS")
	print()
	print("Menu yang Tersedia :")
	print("1. Nasi Goreng = Rp.15.000")
	print("2. Mie Goreng = Rp.10.000")
	print("3. Mie Mawut = Rp.13.000")
	print("4. Es Teh = Rp.5.000")
	print("5. Teh Hangat = Rp.6.000")
	print("6. Es Jeruk = Rp.5.000")
	print("================================================")


def pilihanku():
  print("""
=====HOME=====
\nPilih menu di bawah ini :
1. Tampikan Menu
2. Tambahkan Menu
3. Ubah Menu
4. Hapus Menu
5. Keluar
  """)
  pilihan = input("Pilih menu : ")
  return pilihan

def add():
  for Menu in Menus:
    Menu.append("Nasi_Padang, Rp.14000")
    print(Menu)

def tambah():
    y="y"
    while y=="y":
        Menuz()
        Menu=["7.", str(input("Masukkan menu: "))," ", int(input("Masukkan harga: "))]
        letak=str(input("Ingin meletakan ditengah? y/n "))
        if letak=="y":
            urutan=(len(Menus))//2
            Menus.insert(urutan,Menu)
        else:
            Menus.append(Menu)
        print("Menu berhasil ditambahkan")
        y=str(input("Ingin menambahkan menu lagi? y/n "))


def delete():
  Menuz()
  urutan=int(input("Menu berapa yang ingin dihapus? "))
  del Menus[urutan-1][1][2][3]

def chance():
  Menuz()
  urutan=int(input("Tuliskan nomor menu yang ingin diubah: "))
  Menus[urutan-1][1]=str(input("Menu baru: "))
  print("==========Menu Sudah Terubah==========")


loop = True
while loop :
    print(40*"=")
    print(15*"*", "Menu", 15*"*")
    print(40*"=")
    print("[1] Tampikan Menu \n[2] Tambahkan Menu \n[3] Ubah Menu \n[4] Hapus Menu \n[0] Keluar ")
    pilihan = int(input("Masukkan Pilihan = "))
    if pilihan == 1:
        main()
        Menuz()
        print()
    elif pilihan == 2:
        tambah()
        print()
    elif pilihan == 3:
        chance()
    elif pilihan == 4:
        delete()
    elif pilihan == 0:
        print("Terima Kasih! Selamat Tinggal")
        loop = False
    else:
      print("Input Salah,Silahkan Masukkan input Dengan Benar")