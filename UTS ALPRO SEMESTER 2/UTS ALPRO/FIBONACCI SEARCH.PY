def output(z):
    print("Nama             : ", z["nama"])
    print("Umur             : ", z["umur"])
    print("NIK              : ", z["nik"])
    print("Tanggal Masuk RS : ", z["tgl"])

def partition(array, low, high, value):
    pivot = array[low]
    x = low + 1
    y = high
    while True:
        while x <= y and array[y][value] >= pivot[value]:
            y = y - 1
        while x <= y and array[x][value] <= pivot[value]:
            x = x + 1
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

arr = [
    {"nama" : "Saban", "umur" : "22", "nik" : "6472040210200005", "tgl" : "24-05-2020"},
    {"nama" : "Liu", "umur" : "18", "nik" : "6309061905030006", "tgl" : "23-06-2021"},
    {"nama" : "Alfi", "umur" : "12", "nik" : "6489010202100002", "tgl" : "23-01-2022"}
]

quick_sort(arr, 0, len(arr)-1, "nama")
for x in arr:
    output(x)
    print("")
input("Tekan Enter untuk lanjut")