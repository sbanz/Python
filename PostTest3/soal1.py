import datetime

makan = {
    "Nasi Goreng": 12000,
    "Nasi Mawut": 12000,
}
minum = {
    "Es/Hangat Teh": 4000,
    "Es/Hangat Jeruk": 5000,
    "Es/Hangat Kopi": 5000,
}

def print_menu():
    print("""Menu : 
1.  Nasi Goreng             Harga : Rp. 12000
2.  Nasi Mawut              Harga : Rp. 12000
3.  Es/Hangat Teh           Harga : Rp. 4000
4.  Es/Hangat Jeruk         Harga : Rp. 5000
5.  Es/Hangat Kopi          Harga : Rp. 5000
    """)

beli = True
total_makan = []
total_minum = []
while beli:
    print_menu()
    pilih_menu = input("Pilih menu 1-5 = ")
    banyak_menu = input("Berapa Banyak = ")

    if pilih_menu == "1":
        print("Anda memesan Nasi Goreng, Sebanyak", banyak_menu, "Porsi")
        harga = int(banyak_menu) * makan["Nasi Goreng"]
        total_makan.append(harga)
        beli = input("Ingin memesan lagi? y/n = ") == "y"
    elif pilih_menu == "2":
        print("Anda memesan Nasi Mawut, Sebanyak", banyak_menu, "Porsi")
        harga = int(banyak_menu) * makan["Nasi Mawut"]
        total_makan.append(harga)
        beli = input("Ingin memesan lagi? y/n = ") == "y"
    elif pilih_menu == "3":
        print("Anda memesan Es/Hangat Teh, Sebanyak", banyak_menu, "Gelas")
        harga = int(banyak_menu) * minum["Es/Hangat Teh"]
        total_minum.append(harga)
        beli = input("Ingin memesan lagi? y/n = ") == "y"
    elif pilih_menu == "4":
        print("Anda memesan Es/Hangat Jeruk, Sebanyak", banyak_menu, "Gelas")
        harga = int(banyak_menu) * minum["Es/Hangat Jeruk"]
        total_minum.append(harga)
        beli = input("Ingin memesan lagi? y/n = ") == "y"
    elif pilih_menu == "5":
        print("Anda memesan Es/Hangat Kopi, Sebanyak", banyak_menu, "Gelas")
        harga = int(banyak_menu) * minum["Es/Hangat Kopi"]
        total_minum.append(harga)

        beli = input("Ingin memesan lagi? y/n = ") == "y"
    else:
        print("PILIH MENU YANG ADA !!!")
print("=================================")
print()
print("Total Makanan = Rp. ", total_makan)
print("Total Minuman = Rp. ", total_minum)
print()
print("=================================")
print()

metode_bayar = input("Ingin membayar dengan E-Money? y/n = ")
print()
print("=================================")
print()
if metode_bayar == "y":
    diskon_metode = 5
    print("Anda mendapatkan diskon E-money sebesar 5 %")
else:
    diskon_metode = 0


if sum(total_makan) >= 24000:
    diskon_makan = 5
    print("Anda mendapatkan diskon Makanan sebesar 5 %")
else:
    diskon_makan = 0


if sum(total_minum) >= 8000:
    diskon_minum = 10
    print("Anda mendapatkan diskon Minuman sebesar 10 %")
else:
    diskon_minum = 0


if datetime.datetime.today().weekday() < 5:
    diskon_hari = 10
    print("Anda mendapatkan diskon weekdays sebesar 10 %")
else:
    diskon_hari = 5
    print("Anda mendapatkan diskon weekend sebesar 5 %")


diskon_total = diskon_makan + diskon_minum + diskon_hari + diskon_metode
total_bayar = sum(total_makan) + sum(total_minum)

if diskon_total == 0:
    potongan = 0
else:
    potongan = total_bayar * diskon_total / 100

bayar = total_bayar - potongan
print()
print("=================================")
print()
print("Total yang harus dibayar sebesar = Rp. ", bayar)
print("Terima Kasih telah Memesan")

