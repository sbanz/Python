Nama_Karyawan = str(input("Nama Karyawan : "))
Jumlah_Coklat = int(input("Jumlah Bungkus Rasa Coklat : "))
Jumlah_Strawberry = int(input("Jumlah Bungkus Rasa Strawberry : "))
Jumlah_Kacang = int(input("Jumlah Bungkus Rasa Kacang : "))
if Jumlah_Coklat >= 3000 and Jumlah_Strawberry >= 3000:
    Jumlah_Strawberry = 6000 - Jumlah_Coklat
    Jumlah_Kacang = 0
elif Jumlah_Coklat >= 3000 and Jumlah_Kacang >= 3000:
    Jumlah_Kacang = 6000 - Jumlah_Coklat
    Jumlah_Strawberry = 0
elif Jumlah_Strawberry >= 3000 and Jumlah_Kacang >= 3000:
    Jumlah_Kacang = 6000 - Jumlah_Strawberry
    Jumlah_Coklat = 0

    Level_Karyawan = str(input("Level Karyawan ((A/b)/(B/b)/(C/c)) : "))
    if Level_Karyawan == 'A' or Level_Karyawan == 'a':
        Gaji_Pokok = 7000
        # Rasa Coklat
        if Jumlah_Coklat >= 5001 and Jumlah_Coklat <= 6000:
            Bonus_1 = Gaji_Pokok * 35 / 100
        elif Jumlah_Coklat >= 4000 and Jumlah_Coklat <= 5000:
            Bonus_1 = Gaji_Pokok * 30 / 100
        elif Jumlah_Coklat >= 3000 and Jumlah_Coklat <= 3999:
            Bonus_1 = Gaji_Pokok * 25 / 100
        else:
            Bonus_1 = 0
        # Rasa Strawberry
        if Jumlah_Strawberry >= 5001 and Jumlah_Strawberry <= 6000:
            Bonus_2 = Gaji_Pokok * 40 / 100
        elif Jumlah_Strawberry >= 4000 and Jumlah_Strawberry <= 5000:
            Bonus_2 = Gaji_Pokok * 30 / 100
        elif Jumlah_Strawberry >= 3000 and Jumlah_Strawberry <= 3999:
            Bonus_2 = Gaji_Pokok * 15 / 100
        else:
            Bonus_2 = 0
        # Rasa Kacang
        if Jumlah_Kacang >= 5001 and Jumlah_Kacang <= 6000:
            Bonus_3 = Gaji_Pokok * 40 / 100
        elif Jumlah_Kacang >= 4000 and Jumlah_Kacang <= 5000:
            Bonus_3 = Gaji_Pokok * 30 / 100
        elif Jumlah_Kacang >= 3000 and Jumlah_Kacang <= 3999:
            Bonus_3 = Gaji_Pokok * 15 / 100
        else:
            Bonus_3 = 0

        Seluruh_Bonus = Bonus_1 + Bonus_2 + Bonus_3
        Total_Gaji = Gaji_Pokok + Seluruh_Bonus

        print("\n\n-------------------------------------")
        print("PERSAHAAN PERMEN")
        print("PERHITUNGAN GAJI KARYAWAN")
        print("Nama Karyawan : ", Nama_Karyawan)
        print("Level Karyawan : ", Level_Karyawan)
        print("Gaji Pokok : Rp.", Gaji_Pokok)
        print("PERMEN YANG KARYAWAN BUNGKUS")
        print("Rasa Coklat : ", Jumlah_Coklat)
        print("Rasa Strawberry : ", Jumlah_Strawberry)
        print("Rasa Kacang : ", Jumlah_Kacang)
        print("BONUS YANG KARYAWAN DAPATKAN")
        print("Bonus Membungkus Permen Rasa Coklat : Rp. ", Bonus_1)
        print("Bonus Membungkus Permen Rasa Strawberry : Rp. ", Bonus_2)
        print("Bonus Membungkus Permen Rasa Kacang : Rp. ", Bonus_3)
        print("------------------------------------------------+")
        print("                       Total_Bonus : Rp. ", Seluruh_Bonus)
        print("Total Gaji : Rp. ", Total_Gaji)
    choose = str(input("Apakah Ingn Menghitung Lagi? y/n "))
    print("-----------------------------------------------------")

if 3000 <= coklat:
    qty_coklat = coklat
    if 3000 <= straw:
        qty_straw = 6000 - qty_coklat

        if qty_total <= 6000:
            kacang = 6000 - qty_total
            qty_kacang = kacang
        else:

    else:
        qty_straw = straw
        qty_kacang = 6000 - qty_coklat
        qty_total = qty_coklat + qty_kacang
elif 0 <= coklat:
    qty_coklat = coklat
    qty_straw = straw
    if 3000 <= kacang:
        kacang = 6000 - qty_straw
        qty_kacang = kacang
        qty_total = qty_straw + qty_kacang
    else:
        print("asdasa")