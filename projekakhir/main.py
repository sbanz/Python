import time
import sys

# List User Dan Admin
list_admin = [["admin"], ["admin"]]
list_user = [["admin"], ["admin"]]
# List Inventory
inventory_list = [["AYAM", "SAPI"], [200, 300], [10000, 20000], [15000, 35000]]


# Start First Menu
def menu_login():
    print("""
==================================
  SELAMAT DATANG DI APLIKASI POS
==================================
    1. Login sebagai admin
    2. Login sebagai user
    3. Register sebagai user
    4. Keluar
""")


def login_admin():
    while True:
        print("""
              SILAHKAN LOGIN
              """)
        int_attempt_counter = 0
        while True:
            login_admin = input("Username : ")
            login_admin = login_admin.lower()
            if login_admin in list_admin[0]:
                index_username = list_admin[0].index(login_admin)
                int_attempt_counter = 0
                break
            else:
                print("Username Tidak Terdaftar\n")
                int_attempt_counter += 1
                print("Anda Telah Salah Memasukkan Username : ", int_attempt_counter, "Kali")
                if int_attempt_counter > 2:
                    print("\nAnda Salah Memasukan username sebanyak 3 Kali Aplikasi Akan Keluar")
                    first_menu()

                    # Login Password
        while True:
            login_password_admin = input("Password : ")
            if login_password_admin == list_admin[1][index_username]:
                int_attempt_counter = 0
                print(
                    """
                ==================================
                Selamat Datang Anda Berhasil Login
                ==================================
                    """)
                break

            else:
                print("Password salah")
                int_attempt_counter += 1
                print("Anda Telah Salah Memasukkan password : ", int_attempt_counter, "Kali")
                if int_attempt_counter > 2:
                    print("\nAnda Salah Memasukan Password sebanyak  3 Kali Aplikasi")
                    print("Anda akan dikembalikan ke menu awal!")
                    first_menu()
        break


def login_user():
    while True:
        print("""
              SILAHKAN LOGIN
              """)
        int_attempt_counter = 0
        while True:
            login_user = input("Username : ")
            login_user = login_user.lower()
            if login_user in list_user[0]:
                index_username = list_user[0].index(login_user)
                int_attempt_counter = 0
                break
            else:
                print("Username Tidak Terdaftar\n")
                int_attempt_counter += 1
                print("Anda Telah Salah Memasukkan Username : ", int_attempt_counter, "Kali")
                if int_attempt_counter > 2:
                    print("\nAnda Salah Memasukan username sebanyak 3 Kali Aplikasi Akan Keluar")
                    first_menu()

                    # Login Password
        while True:
            login_password_user = input("Password : ")
            if login_password_user == list_user[1][index_username]:
                int_attempt_counter = 0
                print(
                    """
                ==================================
                Selamat Datang Anda Berhasil Login
                ==================================
                    """)
                break

            else:
                print("\nPassword salah")
                int_attempt_counter += 1
                print("Anda Telah Salah Memasukkan password : ", int_attempt_counter, "Kali")
                if int_attempt_counter > 2:
                    print("\nAnda Salah Memasukan Password sebanyak  3 Kali ")
                    print("Anda akan dikembalikan ke menu awal!")
                    first_menu()
        break


def create_user():
    print(
        """
        ==================================
                  REGISTER MENU
        ==================================
        """)
    while True:
        register_username = input("Masukkan Username : ")
        register_username = register_username.lower()
        if register_username not in list_user[0]:
            break
        else:
            print("Username", register_username, "Sudah Ada, Gunakan Username Lain\n")

    register_password = input("Masukkan Password : ")

    while True:
        konfirmasi_password = input("Konfirmasi Password : ")
        if register_password == konfirmasi_password:
            list_user[0].append(register_username)
            list_user[1].append(register_password)
            break
        else:
            print("\nKonfirmasi Password Tidak Sesuai")

    print("Akun Anda Berhasil Didaftar Silahkan Login")


def first_menu():
    while True:
        menu_login()
        choice = input("Masukkan Nomor Pilihan : ")
        if choice == "1":
            login_admin()
            second_menu()
        elif choice == "2":
            login_user()
        elif choice == "3":
            create_user()
        elif choice == "4":
            count = int(3)
            for i in range(count):
                print("Program Akan Keluar Dalam", (int(count) - i), "Detik")
                time.sleep(1)
            print("Selamat Tinggal")
            sys.exit()
        else:
            print("Mohon Masukkan Nomor Sesuai Yang Diatas!!")


# End First Menu

# Start Admin Menu
def admin_menu():
    print("""
==================================
         SELAMAT DATANG
==================================
    1. Tambah Inventory
    2. Update Inventory
    3. Hapus Inventory
    4. Lihat Inventory
    5. Lihat Laporan Penjualan
    6. Keluar
""")


def create_inventory():
    while True:
        inventory_input = input("Masukkan Nama Item : ")
        inventory_name = inventory_input.upper()
        if inventory_name not in inventory_list[0]:
            inventory_stock = int(input("Masukkan Banyak Stock : "))
            if inventory_stock < 0:
                print("Mohon Masukkan Banyak Stock Dengan Angka Positif")
            else:
                inventory_buy_price = int(input("Masukkan Harga Beli : "))
                if inventory_buy_price < 0:
                    print("Mohon Masukkan Harga Beli Dengan Angka Positif")
                else:
                    inventory_sell_price = int(input("Masukkan Harga Jual : "))
                    if inventory_sell_price < 0:
                        print("Mohon Masukkan Harga Jual Dengan Angka Positif")
                    else:
                        inventory_list[0].append(inventory_name)
                        inventory_list[1].append(inventory_stock)
                        inventory_list[2].append(inventory_buy_price)
                        inventory_list[3].append(inventory_sell_price)
                        print("Anda Berhasil Memasukkan", inventory_input, "Ke Dalam Inventory")
                        retry = input("Apakah Ingin Memasukkan Item Lain ? (y/n) : ")
                        if retry == "n":
                            break
        else:
            print("Item Sudah Ada Silahkan ke Menu Update Jika Ingin Mengubah")
            retry = input("Apakah Ingin Memasukkan Item Lain ? (y/n) : ")
            if retry == "n":
                break


def update_inventory():
    from itertools import count
    if len(inventory_list[0]) > 0:
        while True:
            print("""
                    =======================================        
                                INVENTORY 
                    ====================================== """)
            for index, nama_item, stock_item, buy_price, sell_price in zip(count(), inventory_list[0],
                                                                           inventory_list[1], inventory_list[2],
                                                                           inventory_list[3]):
                print("|", index + 1, ".", "|", "{}".format(nama_item), "\t\t -Rp ", "{}".format(buy_price),
                      "\t\t -Rp ", "{}".format(sell_price), "|", stock_item)
            try:
                index_item = int(input("Silahkan Masukkan Nomor Item Yang Ingin Di Update : "))
                if index_item > len(inventory_list[0]):
                    print("Nomor Item Tidak Ada Dalam Inventory")
                else:
                    index_item = index_item - 1
                    print("""
Pilih Proses Yang Ingin Anda Lakukan
    1. Mengubah Stock Barang
    2. Mengubah Harga Beli
    3. Mengubah Harga Jual""")
                choice = input("Masukkan Pilihan Anda Disini : ")
                if choice == "1":
                    update_stock = int(input("Masukkan Banyak Stock Baru : "))
                    if update_stock < 0:
                        print("Mohon Masukkan Angka Positif")
                    else:
                        inventory_list[1][index_item] = update_stock
                        retry = input("Apakah Ingin Mengupdate Lagi ? (y/n) : ")
                        if retry == "n":
                            break
                elif choice == "2":
                    update_buy_price = int(input("Masukkan Harga Beli Baru : "))
                    if update_buy_price < 0:
                        print("Mohon Masukkan Angka Positif")
                    else:
                        inventory_list[2][index_item] = update_buy_price
                        retry = input("Apakah Ingin Mengupdate Lagi ? (y/n) : ")
                        if retry == "n":
                            break
                elif choice == "3":
                    update_sell_price = int(input("Masukkan Harga Jual Baru : "))
                    if update_sell_price < 0:
                        print("Mohon Masukkan Angka Positif")
                    else:
                        inventory_list[3][index_item] = update_sell_price
                        retry = input("Apakah Ingin Mengupdate Lagi ? (y/n) : ")
                        if retry == "n":
                            break
                else:
                    print("Mohon Masukkan Nomor Proses Sesuai Yang Tertera")
            except:
                print("Mohon Masukkan Nomor Item Dengan Benar")
    else:
        print("Data Inventory Anda Kosong Silahkan Mengisi Inventory Terlebih Dahulu")


def delete_inventory():
    from itertools import count
    while True:
        if len(inventory_list[0]) > 0:
            print("""
Pilih Proses Yang Ingin Anda Lakukan
    1. Menghapus Seluruh Data Inventory
    2. Menghapus 1 Data Item Inventory
""")
            choice = input("Masukkan Nomor Proses : ")
            if choice == "1":
                confirm = input("Apakah Anda Yakin Ingin Menghapus Semua Inventory ? (y/n) : ")
                if confirm == "y":
                    inventory_list[0].clear()
                    inventory_list[1].clear()
                    inventory_list[2].clear()
                    inventory_list[3].clear()
                    break
                if confirm == "n":
                    break

            elif choice == "2":
                while True:
                    print("""
                    =======================================        
                                INVENTORY 
                    ====================================== """)
                    for index, nama_item, stock_item, buy_price, sell_price in zip(count(), inventory_list[0],
                                                                                   inventory_list[1], inventory_list[2],
                                                                                   inventory_list[3]):
                        print("|", index + 1, ".", "|", "{}".format(nama_item), "\t\t -Rp ", "{}".format(buy_price),
                              "\t\t -Rp ", "{}".format(sell_price), "|", stock_item)
                    try:
                        index_item = int(input("Silahkan Masukkan Nomor Item Yang Ingin Di Hapus : "))
                        if index_item > len(inventory_list[0]):
                            print("Nomor Item Tidak Ada Dalam Inventory")
                            break
                        else:
                            index_item = index_item - 1
                            confirm = input("Apakah Anda Yakin Ingin Menghapus ? (y/n) : ")
                            if confirm == "y":
                                del inventory_list[0][index_item]
                                del inventory_list[1][index_item]
                                del inventory_list[2][index_item]
                                del inventory_list[3][index_item]
                                retry = input("Apakah Anda Ingin Menghapus Lagi ? (y/n) : ")
                                if retry == "n":
                                    break
                    except:
                        print("Mohon Masukkan Nomor Item Dengan Benar")
            else:
                print("Mohon Masukkan Nomor Proses Sesuai Yang Tertera")

        else:
            print("Data Inventory Anda Kosong Silahkan Mengisi Inventory Terlebih Dahulu")
            break
        break


def read_inventory():
    from itertools import count
    print("""
                    =======================================        
                                INVENTORY 
                    ====================================== """)
    for index, nama_item, stock_item, buy_price, sell_price in zip(count(), inventory_list[0], inventory_list[1],
                                                                   inventory_list[2], inventory_list[3]):
        print("|", index + 1, ".", "|", "{}".format(nama_item), "\t\t -Rp ", "{}".format(buy_price), "\t\t -Rp ",
              "{}".format(sell_price), "|", stock_item)
    input("Pencet Enter Untuk Kembali")


def second_menu():
    while True:
        admin_menu()
        choice = input("Masukkan Nomor Proses : ")
        if choice == "1":
            create_inventory()
        elif choice == "2":
            update_inventory()
        elif choice == "3":
            delete_inventory()
        elif choice == "4":
            read_inventory()
        elif choice == "5":
            print("Belum Ada")
        elif choice == "6":
            first_menu()
        else:
            print("Mohon Masukkan Nomor Proses Sesuai Yang Tertera")


# End Admin Menu

# Start User Menu
def user_menu():
    print("""
==================================
         SELAMAT DATANG
==================================
    1. Tambah Pesanan
    2. Hapus Pesanan
    3. Lihat Pesanan
    4. Bayar Pesanan
    5. Keluar
""")


def create_order():
    from itertools import count
    print("""
            =======================================        
                        INVENTORY 
            ======================================= """)
    for index, nama_item, stock_item, sell_price in zip(count(), inventory_list[0], inventory_list[1],
                                                        inventory_list[3]):
        print("|", index + 1, ".", "|", "{}".format(nama_item), "\t\t\t\t -Rp ", "{}".format(sell_price), "|",
              stock_item)


# MAIN
create_order()