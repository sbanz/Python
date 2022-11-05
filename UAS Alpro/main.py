print("================================================")
print("          Penghitungan Gaji Karyawan")
print("================================================")
print()

#INPUT DATA KARYAWAN
nama = str(input("Masukkan Nama Karyawan : "))
level = str.upper(input("Masukkan Level Karyawan (A/B/C) : "))
print("================================================")
print()

#INPUT BUNGKUS
coklat = int(input("Masukkan berapa banyak bungkus Coklat : "))
straw = int(input("Masukkan berapa banyak bungkus Strawberry : "))
kacang = int(input("Masukkan berapa banyak Kacang : "))

#Prioritas
qty_coklat = coklat
qty_straw = straw
qty_kacang = kacang
qty_max = 0
if qty_coklat == 6000:
    qty_coklat = coklat
    qty_straw = 0
    qty_kacang = 0
elif qty_coklat > 6000:
    more = coklat - 6000
    qty_coklat = coklat - more
    qty_straw = 0
    qty_kacang = 0
elif 1 <= qty_coklat < 6000:
    qty_coklat = coklat
    qty_straw = 6000 - qty_coklat
    if qty_straw >= straw:
        qty_straw = straw
    qty_max = qty_coklat + qty_straw
    if qty_max == 6000:
        qty_kacang = 0
    elif qty_max < 6000:
        qty_kacang = 6000 - qty_coklat
        qty_kacang = qty_kacang - qty_straw
        if qty_kacang >= kacang:
            qty_kacang = kacang
elif qty_coklat == 0:
    qty_coklat = coklat
    qty_kacang = 6000 - qty_straw

# Bonus Gaji
if level == "A":
    gaji = 7000
    if 5001 <= qty_coklat <= 6000:
        bonusC = gaji * 35/100
    elif 4000 <= qty_coklat <= 5000:
        bonusC = gaji * 30/100
    elif 3000 <= qty_coklat <= 3999:
        bonusC = gaji * 25/100
    else:
        bonusC = 0

    if 5001 <= qty_straw <= 6000:
        bonusS = gaji * 40 / 100
    elif 4000 <= qty_straw <= 5000:
        bonusS = gaji * 30 / 100
    elif 3000 <= qty_straw <= 3999:
        bonusS = gaji * 15 / 100
    else:
        bonusS = 0

    if 5001 <= qty_kacang <= 6000:
        bonusK = gaji * 40/100
    elif 4000 <= qty_kacang <= 5000:
        bonusK = gaji * 30/100
    elif 3000 <= qty_kacang <= 3999:
        bonusK = gaji * 15/100
    else:
        bonusK = 0
elif level == "B":
    gaji = 5000
    if 5001 <= qty_coklat <= 6000:
        bonusC = gaji * 25 / 100
    elif 4000 <= qty_coklat <= 5000:
        bonusC = gaji * 20 / 100
    elif 3000 <= qty_coklat <= 3999:
        bonusC = gaji * 15 / 100
    else:
        bonusC = 0

    if 5001 <= qty_straw <= 6000:
        bonusS = gaji * 30 / 100
    elif 4000 <= qty_straw <= 5000:
        bonusS = gaji * 20 / 100
    elif 3000 <= qty_straw <= 3999:
        bonusS = gaji * 7 / 100
    else:
        bonusS = 0

    if 5001 <= qty_kacang <= 6000:
        bonusK = gaji * 30 / 100
    elif 4000 <= qty_kacang <= 5000:
        bonusK = gaji * 20 / 100
    elif 3000 <= qty_kacang <= 3999:
        bonusK = gaji * 7 / 100
    else:
        bonusK = 0
elif level == "C":
    gaji = 3000
    if 5001 <= qty_coklat <= 6000:
        bonusC = gaji * 15 / 100
    elif 4000 <= qty_coklat <= 5000:
        bonusC = gaji * 10 / 100
    elif 3000 <= qty_coklat <= 3999:
        bonusC = gaji * 5 / 100
    else:
        bonusC = 0

    if 5001 <= qty_straw <= 6000:
        bonusS = gaji * 20 / 100
    elif 4000 <= qty_straw <= 5000:
        bonusS = gaji * 10 / 100
    elif 3000 <= qty_straw <= 3999:
        bonusS = gaji * 5 / 100
    else:
        bonusS = 0

    if 5001 <= qty_kacang <= 6000:
        bonusK = gaji * 20 / 100
    elif 4000 <= qty_kacang <= 5000:
        bonusK = gaji * 10 / 100
    elif 3000 <= qty_kacang <= 3999:
        bonusK = gaji * 5 / 100
    else:
        bonusK = 0

bonus = bonusC + bonusS + bonusK
gaji_akhir = gaji + bonus

print()
print("================================================")
print()

#OUTPUT
print(f"""
================================================
                   SLIP GAJI
================================================

NAMA                : {nama}
LEVEL KARYAWAN      : {level}

JUMLAH BUNGKUSAN :
Coklat      : {coklat}
Strawberry  : {straw}
Kacang      : {kacang}

TAMBAHAN GAJI :
Coklat      : Rp. {bonusC}
Strawberry  : Rp. {bonusS}
Kacang      : Rp. {bonusK}

TOTAL GAJI : Rp. {gaji_akhir}

================================================""")