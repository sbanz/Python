makan = [
    ["Nasi Goreng", 12000],
    ["Nasi Mawut", 12000]
]
minum = [
    ["Es/Hangat Teh", 4000],
    ["Es/Hangat Jeruk", 5000],
    ["Es/Hangat Kopi", 5000]
]

def print_menumakan():
    print("="*20, " MENU MAKANAN ", "="*20)
    for index in range (len(makan)):
        print(makan[index][0], "Rp. ", makan[index][1])
def print_menuminum():
    print("="*20, " MENU MINUMAN ", "="*20)
    for index in range (len(minum)):
        print(minum[index][0], "Rp. ", minum[index][1])

def tambah_makan():
    addfood = str(input("Masukkan Nama Makanan : "))
    makan[0][1].append(addfood)

def tambah_minum():
    adddrink = input("Masukkan Nama Minuman : ")
    minum.append(adddrink)

tambah_makan()
print_menumakan()