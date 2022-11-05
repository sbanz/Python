import string
import random


def generate_id(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


menus = [
    [generate_id(), "Es Teh", 7000, "drink"],
    [generate_id(), "Soda Gembira", 8000, "drink"],
    [generate_id(), "One-Shot Espresso", 9000, "drink"],
    [generate_id(), "Nasi Kucing", 5000, "food"],
    [generate_id(), "Mie Ayam", 8000, "food"],
    [generate_id(), "Nasi Goreng", 6000, "food"],
    [generate_id(), "Sate", 10000, "food"],
]


def print_options():
    print("""
MENU
========
1. Lihat Daftar Menu
2. Tambah Menu
3. Ubah Menu
4. Hapus Menu
5. Keluar
  """)


# PRINT
def print_menu():
    foods = []
    drinks = []
    for menu in menus:
        if menu[3] == "food":
            foods.append(menu)
        else:
            drinks.append(menu)
    print("""
DAFTAR MENU
===============""")
    print("""
MAKANAN
==============""")
    for index, food in enumerate(foods):
        print(f"{index + 1}. [{food[0]}] {food[1]} - Rp. {food[2]}")
    print("""
\nMINUMAN
==============""")
    for index, drink in enumerate(drinks):
        print(f"{index + 1}. [{drink[0]}] {drink[1]} - Rp. {drink[2]}")
    input()


# UTILS
def find_menu(items, id):
    return next((item for item in items if item[0] == id), None)


def store_menu(items, data, is_append=True):
    if is_append:
        items.append(data)
    else:
        midpoint = len(items) // 2
        items.insert(midpoint, data)
    return items


def destroy_menu(items, id):
    menu = find_menu(items, id)
    if menu != None:
        if menu[3] == "food":
            del menu
        else:
            items.remove(menu)


def get_is_food(message):
    print(f"""
{message}
1. Makanan
2. Minuman
  """)
    choice = input("Masukkan pilihan : ")
    return choice == "1"


# MAIN
choice = "0"
while choice != "5":
    print_options()
    choice = input("Apa yang ingin anda lakukan: ")
    if choice == "1":
        print_menu()
    elif choice == "2":
        is_food = get_is_food("Menu apa yang ingin anda tambahkan?")
        menu_type = "food" if is_food else "drink"
        menu_id = generate_id()
        name = input("\nMasukkan nama menu : ")
        price = input("Masukkan harga menu : ")
        menu = [menu_id, name, int(price), menu_type]
        is_append = input("Apa anda ingin menambahkan menu di tengah (y/n) : ") == "n"
        store_menu(menus, menu, is_append)
        print("Menu berhasil ditambahkan")
        input()

    elif choice == "3":
        id = input("Masukkan ID menu : ")
        menu = find_menu(menus, id)
        if menu != None:
            print(f"""
ID Menu: {menu[0]}
Nama Menu: {menu[1]}
Harga: Rp. {menu[2]}\n""")
            menu[1] = input("Masukkan nama baru menu : ")
            menu[2] = input("Masukkan harga baru menu : ")
            print("Menu berhasil diubah")
        else:
            print("Menu tidak ditemukan")
        input()

    elif choice == "4":
        id = input("Masukkan ID menu : ")
        menu = find_menu(menus, id)
        if menu != None:
            print(f"""
ID Menu: {menu[0]}
Nama Menu: {menu[1]}
Harga: Rp. {menu[2]}\n""")
            is_confirmed = input("Apakah anda yakin ingin menghapus menu (y/n) : ") == "y"
            if is_confirmed:
                destroy_menu(menus, id)
                print("Menu berhasil dihapus")
        else:
            print("Menu tidak ditemukan")
        input()
    else:
        print("Terima kasih")
        exit()