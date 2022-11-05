
# APABILA YG DICARI KETEMU, AKAN MENGAMBILIKAN INDEX DATA
# JIKA TIDAK AKAN MENGEMBALIKAN -1
def binary_search(arr, item):
    lower_part = 0
    higher_part = len(arr) - 1
    middle_part = 0
    while lower_part <= higher_part:
        middle_part = (higher_part + lower_part) // 2
        # Apabila item lebih besar, maka ambil sisi kanan
        if arr[middle_part] < x:
            lower_part = middle_part + 1
        # kalau item lebih kecil, maka ambil sisi kiri
        elif arr[middle_part] > x:
            higher_part = middle_part - 1
        # kalau sama berarti middle_part adalah item itu sendiri
        else:
            return middle_part
    # Kalau item tidak ada kembalikan -1
    return -1

arr = ['abc', 'apa', 'cinta', 'dia', 'ketika', 'menjadi', 'pergi', 'saya', 'tentu', 'tidak']
x = 'abc'
# Function call
result = binary_search(arr, x)

if result != -1:
    print(f"Elemen berada di index {result}")
else:
    print("Elemen tidak ditemukan")