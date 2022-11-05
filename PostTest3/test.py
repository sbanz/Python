import time
import sys
import json
import os
from tabulate import tabulate

# List Inventory

# Start Main Menu
def reset():
    os.system('cls' if os.name == 'nt' else 'clear')


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
                    menu_login()

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
                    menu_login()
        break


def login_user():
    while True:
        print("""
              SILAHKAN LOGIN
              """)
        int_attempt_counter = 0
        while True:
            global login_username
            login_username = input("Username : ")
            login_username = login_username.lower()
            if login_username in list_user[0]:
                index_username = list_user[0].index(login_username)
                int_attempt_counter = 0
                break
            else:
                print("Username Tidak Terdaftar\n")
                int_attempt_counter += 1
                print("Anda Telah Salah Memasukkan Username : ", int_attempt_counter, "Kali")
                if int_attempt_counter > 2:
                    print("\nAnda Salah Memasukan username sebanyak 3 Kali Aplikasi Akan Keluar")
                    menu_login()

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
                    menu_login()
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
            with open("user.json", 'w') as f:
                json.dump(list_user, f)
            break
        else:
            print("\nKonfirmasi Password Tidak Sesuai")

    print("Akun Anda Berhasil Didaftar Silahkan Login")


# End Main Menu

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
        try:
            inventory_input = input("Masukkan Nama Item : ")
            inventory_name = inventory_input.upper()
            if inventory_name in inventory_list[0]:
                print("Item Sudah Ada Silahkan ke Menu Update Jika Ingin Mengubah")
                retry = input("Apakah Ingin Memasukkan Item Lain ? (y/n) : ")
                if retry == "n":
                    break
            else:
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
        except:
            print("Mohon Masukkan Sesuai Tipe Data")


def update_inventory():
    if len(inventory_list[0]) > 0:
        while True:
            length = len(inventory_list[0]) + 1
            print(tabulate({'Nama': inventory_list[0], 'Stock': inventory_list[1], 'Harga Beli': inventory_list[2],
                            'Harga Jual': inventory_list[3]}, headers="keys", tablefmt='fancy_grid',
                           showindex=range(1, length)))
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
                    length = len(inventory_list[0]) + 1
                    print(tabulate(
                        {'Nama': inventory_list[0], 'Stock': inventory_list[1], 'Harga Beli': inventory_list[2],
                         'Harga Jual': inventory_list[3]}, headers="keys", tablefmt='fancy_grid',
                        showindex=range(1, length)))
                    try:
                        index_item = int(input("Silahkan Masukkan Nomor Item Yang Ingin Di Hapus : "))
                        if index_item > len(inventory_list[0]):
                            print("Nomor Item Tidak Ada Dalam Inventory")
                            break
                        elif index_item < 0:
                            print("Silahkan Masukkan Nomor Item Positif")
                        else:
                            index_item = index_item - 1
                            confirm = input("\nApakah Anda Yakin Ingin Menghapus ? (y/n) : ")
                            if confirm == "y":
                                del inventory_list[0][index_item]
                                del inventory_list[1][index_item]
                                del inventory_list[2][index_item]
                                del inventory_list[3][index_item]
                                print("Inventory Berhasil Dihapus")
                                retry = input("Apakah Anda Ingin Menghapus Lagi ? (y/n) : ")
                                if retry == "n":
                                    break
                            else:
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
    if len(inventory_list[0]) > 0:
        length = len(inventory_list[0]) + 1
        print(tabulate({'Nama': inventory_list[0], 'Stock': inventory_list[1], 'Harga Beli': inventory_list[2],
                        'Harga Jual': inventory_list[3]}, headers="keys", tablefmt='fancy_grid',
                       showindex=range(1, length)))
        input("Pencet Enter Untuk Kembali")
    else:
        print("Data Inventory Kosong Silahkan Mengisi Inventory Terlebih Dahulu")


def report():
    while True:
        if len(report_list[0]) < 1:
            print("Penjualan Belum Pernah Dilakukan")
            break
        else:
            print("""
Pilih Proses 
1. Melihat Laporan Penjualan
2. Mereset Laporan Penjualan
        """)
            choice = input("Masukkan Nomor Pilihan : ")
            if choice == "1":
                print("""
                ==================================
                        LAPORAN PENJUALAN
                ==================================""")
                length = len(report_list[0]) + 1
                print(tabulate({'Nama': report_list[0], 'Stock Terjual': report_list[1], 'Harga Beli': report_list[4],
                                'Harga Jual': report_list[5]}, headers="keys", tablefmt='fancy_grid',
                               showindex=range(1, length)))
                if sum(report_list[4]) > sum(report_list[5]):
                    print("Anda Mengalami Rugi Sebesar Rp", sum(report_list[4]) - sum(report_list[5]))
                elif sum(report_list[5]) > sum(report_list[4]):
                    print("Anda Mendapatkan Untung Sebesar Rp", sum(report_list[5]) - sum(report_list[4]))
                input("Tekan Enter Untuk Kembali")
                break
            elif choice == "2":
                report_list[0].clear()
                report_list[1].clear()
                report_list[2].clear()
                report_list[3].clear()
                report_list[4].clear()
                report_list[5].clear()
                break
            else:
                print("Mohon Masukkan Nomor Proses Sesuai Yang Tertera")


def second_menu():
    while True:
        with open("inventory.json", 'w') as f:
            json.dump(inventory_list, f)
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
            report()
        elif choice == "6":
            break
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
    while True:
        try:
            length = len(inventory_list[0]) + 1
            print(tabulate({'Nama': inventory_list[0], 'Stock': inventory_list[1], 'Harga': inventory_list[3]},
                           headers="keys", tablefmt='fancy_grid', showindex=range(1, length)))
            index_menu = int(input("Masukkan Nomor Item Yang Anda Inginkan : "))
            if index_menu > len(inventory_list[0]):
                print("Nomor Item Tidak Ada")
            else:
                qty_order = int(input("Masukkan Banyak Stock Yang Anda Inginkan : "))
                index_menu = index_menu - 1
                if qty_order > inventory_list[1][index_menu]:
                    print("Stock Tidak Cukup")
                elif qty_order < 0:
                    print("Quantity Harus Positif")
                else:
                    if inventory_list[0][index_menu] not in order_list[0]:
                        order_list[0].append(inventory_list[0][index_menu])
                        order_list[1].append(qty_order)
                        inventory_list[1][index_menu] = (inventory_list[1][index_menu]) - (qty_order)
                        order_list[2].append(inventory_list[3][index_menu])
                        order_list[3].append((inventory_list[3][index_menu] * qty_order))
                        if inventory_list[0][index_menu] not in report_list[0]:
                            report_list[0].append(inventory_list[0][index_menu])
                            report_list[1].append(qty_order)
                            report_list[2].append(inventory_list[2][index_menu])
                            report_list[3].append(inventory_list[3][index_menu])
                            report_list[4].append((inventory_list[2][index_menu] * qty_order))
                            report_list[5].append((inventory_list[3][index_menu] * qty_order))
                        else:
                            index_report = report_list[0].index(inventory_list[0][index_menu])
                            report_list[1][index_report] = report_list[1][index_report] + qty_order
                            report_list[4][index_report] = (report_list[4][index_report]) + (
                                        inventory_list[2][index_menu] * qty_order)
                            report_list[5][index_report] = (report_list[5][index_report]) + (
                                        inventory_list[3][index_menu] * qty_order)

                        repeat = input("Apakah Ingin Memesan Lagi? (y/n) : ")
                        with open("inventory.json", 'w') as f:
                            json.dump(inventory_list, f)
                        with open("order.json", 'w') as f:
                            json.dump(order_list, f)
                        with open("report.json", 'w') as f:
                            json.dump(report_list, f)
                        if repeat == "y":
                            continue
                        else:
                            break
                    else:
                        index_order = order_list[0].index(inventory_list[0][index_menu])
                        order_list[1][index_order] = order_list[1][index_order] + qty_order
                        inventory_list[1][index_menu] = (inventory_list[1][index_menu]) - (qty_order)
                        order_list[3][index_order] = (order_list[3][index_order]) + (
                                    inventory_list[3][index_menu] * qty_order)
                        if inventory_list[0][index_menu] not in report_list[0]:
                            report_list[0].append(inventory_list[0][index_menu])
                            report_list[1].append(qty_order)
                            report_list[2].append(inventory_list[2][index_menu])
                            report_list[3].append(inventory_list[3][index_menu])
                            report_list[4].append((inventory_list[2][index_menu] * qty_order))
                            report_list[5].append((inventory_list[3][index_menu] * qty_order))
                        else:
                            index_report = report_list[0].index(inventory_list[0][index_menu])
                            report_list[1][index_report] = report_list[1][index_report] + qty_order
                            report_list[4][index_report] = (report_list[4][index_report]) + (
                                        inventory_list[2][index_menu] * qty_order)
                            report_list[5][index_report] = (report_list[5][index_report]) + (
                                        inventory_list[3][index_menu] * qty_order)

                        with open("inventory.json", 'w') as f:
                            json.dump(inventory_list, f)
                        with open("order.json", 'w') as f:
                            json.dump(order_list, f)
                        with open("report.json", 'w') as f:
                            json.dump(report_list, f)
                        repeat = input("Apakah Ingin Memesan Lagi? (y/n) : ")
                        if repeat == "y":
                            continue
                        else:
                            break
        except:
            print("Mohon Masukkan Sesuai Dengan Tipe Data")


def delete_order():
    while True:
        try:
            if len(order_list[0]) > 0:
                length = len(order_list[0]) + 1
                print(tabulate({'Nama Item': order_list[0], 'Quantity': order_list[1], 'Harga': order_list[2],
                                'Total': order_list[3]}, headers="keys", tablefmt='fancy_grid',
                               showindex=range(1, length)))
                index_hapus = int(input("Masukkan Nomor Pesanan Yang Ingin Dihapus : "))
                if index_hapus > len(order_list[0]):
                    print("Nomor Pesanan Tidak Ada")
                elif index_hapus < 0:
                    print("Nomor Pesanan TIdak Ada")
                else:
                    index_hapus = index_hapus - 1
                    qty_return = inventory_list[0].index(order_list[0][index_hapus])
                    confirm = input("Apakah Anda Yakin Ingin Menghapus? (y/n) : ")
                    if confirm == "y":
                        index_report = report_list[0].index(order_list[0][index_hapus])
                        if report_list[1][index_report] == order_list[1][index_hapus]:
                            del report_list[0][index_report]
                            del report_list[1][index_report]
                            del report_list[2][index_report]
                            del report_list[3][index_report]
                            del report_list[4][index_report]
                            del report_list[5][index_report]
                        else:
                            report_list[1][index_report] = report_list[1][index_report] - order_list[1][index_hapus]
                            report_list[4][index_report] = report_list[4][index_report] - (
                                        order_list[1][index_hapus] * inventory_list[2][qty_return])
                            report_list[5][index_report] = report_list[5][index_report] - (
                                        order_list[1][index_hapus] * inventory_list[3][qty_return])

                        inventory_list[1][qty_return] = inventory_list[1][qty_return] + order_list[1][index_hapus]
                        del order_list[0][index_hapus]
                        del order_list[1][index_hapus]
                        del order_list[2][index_hapus]
                        del order_list[3][index_hapus]
                        with open("order.json", 'w') as f:
                            json.dump(order_list, f)
                        with open("inventory.json", 'w') as f:
                            json.dump(inventory_list, f)
                        with open("report.json", "w") as f:
                            json.dump(report_list, f)
                        break
                    else:
                        print("Anda Akan Kembali Ke Menu Sebelumnya")
                        break
            else:
                print("Pesanan Belum Ada Silahkan Membuat Pesanan Terlebih Dahulu")
                break
        except:
            print("Mohon Masukkan Sesuai Tipe Data")


def read_order():
    if len(order_list[0]) > 0:
        length = len(order_list[0]) + 1
        print(tabulate(
            {'Nama Item': order_list[0], 'Quantity': order_list[1], 'Harga': order_list[2], 'Total': order_list[3]},
            headers="keys", tablefmt='fancy_grid', showindex=range(1, length)))
        input("Pencet Enter Untuk Kembali")
    else:
        print("Pesanan Belum Ada Silahkan Membuat Pesanan Terlebih Dahulu")


def pay_order():
    while True:
        try:
            pay = input("Apakah Anda Ingin Membayar ? (y/n) : ")
            if pay == "y":
                if len(order_list[0]) > 0:
                    import datetime
                    date = datetime.datetime.now()
                    harga_total = sum(order_list[3])
                    print("\n=========================================================")
                    print("|                   S T R U K  B E L I                  |")
                    print("=========================================================")
                    print("Tanggal :", date.strftime("%x"))
                    print("Nama Pelayan :", login_username, "\n")
                    length = len(order_list[0]) + 1
                    print(tabulate({'Nama Item': order_list[0], 'Quantity': order_list[1], 'Harga': order_list[2],
                                    'Total': order_list[3]}, headers="keys", tablefmt='fancy_grid',
                                   showindex=range(1, length)))
                    print("=========================================================")
                    print(" Total Harga                                  :", "Rp", harga_total)
                    print("=========================================================")
                    order_list[0].clear()
                    order_list[1].clear()
                    order_list[2].clear()
                    order_list[3].clear()
                    input("\nTekan Enter Untuk Membuat Pesanan Baru")
                    break
                else:
                    print("Pesanan Belum Ada Silahkan Membuat Pesanan Terlebih Dahulu")
                    break
            elif pay == "n":
                break
            else:
                continue
        except:
            print("Pesanan Belum Ada Silahkan Pesan Terlebih Dahulu")


def third_menu():
    while True:
        user_menu()
        choice = input("Masukkan Nomor Pilihan : ")
        if choice == "1":
            create_order()
        elif choice == "2":
            delete_order()
        elif choice == "3":
            read_order()
        elif choice == "4":
            pay_order()
        elif choice == "5":
            break
        else:
            print("Mohon Masukkan Nomor Sesuai Yang Diatas!!")


# Load Data
while True:
    try:
        with open("inventory.json", 'r') as f:
            inventory_list = json.load(f)
        with open("admin.json", 'r') as f:
            list_admin = json.load(f)
        with open("user.json", 'r') as f:
            list_user = json.load(f)
        with open("order.json", 'r') as f:
            order_list = json.load(f)
        with open("report.json", 'r') as f:
            report_list = json.load(f)

        break
    except:
        inventory_list = [[], [], [], []]
        list_admin = [[], []]
        list_user = [[], []]
        order_list = [[], [], [], []]
        report_list = [[], [], [], [], [], []]

        print("""
        ==================================
                SELAMAT DATANG
        ==================================
    Silahkan Untuk Membuat Akun Admin Terlebih Dahulu""")

        admin_name = (input("\nMasukkan Nama Admin Terlebih Dahulu : ")).lower()
        admin_password = input("Masukkan Password Untuk Admin : ")
        print("Akun Anda Dapat Mengakses Sebagai User Maupun Admin")
        list_admin[0].append(admin_name)
        list_admin[1].append(admin_password)
        list_user[0].append(admin_name)
        list_user[1].append(admin_password)
        with open("inventory.json", 'w') as f:
            json.dump(inventory_list, f)
        with open("admin.json", 'w') as f:
            json.dump(list_admin, f)
        with open("user.json", 'w') as f:
            json.dump(list_user, f)
        with open("order.json", 'w') as f:
            json.dump(order_list, f)
        with open("report.json", 'w') as f:
            json.dump(report_list, f)

# Menu Awal
while True:
    menu_login()
    choice = input("Masukkan Nomor Pilihan : ")
    if choice == "1":
        login_admin()
        second_menu()
    elif choice == "2":
        login_user()
        third_menu()
    elif choice == "3":
        create_user()
    elif choice == "4":
        count = int(3)
        for i in range(count):
            print("program akan keluar dalam", (int(count) - i), "detik")
            time.sleep(1)
        print("Selamat Tinggal")
        sys.exit()
    else:
        print("Mohon Masukkan Nomor Sesuai Yang Diatas!!")