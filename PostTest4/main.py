import datetime

# MENU
x = datetime.datetime.now()
print("___________________________________________________")
print("                    CHIM's CAFE                    ")
print("          Jln. My Story, Kota Imagination          ")
print("            ", (x), )
print("___________________________________________________")
print("___________________________________________________")
print("""               
                1. Login Sebagai Admin  
                2. Login sebagai Customer
___________________________________________________""")
login = int(input("Anda Ingin Login Sebagai Apa? "))
menu_makanan = [["1.", "Chicken Wings", "              ", 25000],
                ["2.", "Pasta Carbonara", "            ", 35000],
                ["3.", "Oregano French Fries", "       ", 20000],
                ["4.", "Spicy Tortilla Chicken Roll", "", 35000],
                ["5.", "Spicy Fried Beancurd", "       ", 30000],
                ["6.", "Beef Steak", "                 ", 45000],
                ["7.", "Omlet", "                      ", 15000],
                ["8.", "Fettucini", "                  ", 27000],
                ["9.", "Chicken Sup", "                ", 20000],
                ["10.", "Beef Burger", "               ", 25000], ]
menu_minuman = [["1.", "Latte", "        ", 25000],
                ["2.", "Macchiato", "    ", 35000],
                ["3.", "Ice Blend", "    ", 20000],
                ["4.", "Ice Drinks", "   ", 35000],
                ["5.", "Milk Shake", "   ", 30000],
                ["6.", "Americano", "    ", 30000],
                ["7.", "Flavourd Tea", " ", 25000],
                ["8.", "Hot Chocolate", "", 30000],
                ["9.", "Mocktail", "     ", 40000],
                ["10.", "Mojito", "      ", 20000], ]
choice = 'y'
while choice == 'y':
    if login == 1:
        print()
        print("           ANDA TELAH LOGIN SEBAGAI ADMIN          ")
        while choice == 'y' or choice == 'Y':
            print("\nBerikut Adalah Daftar Menu Dari Cafe Anda : ")
            print("FOOD MENU")
            for menu in menu_makanan:
                print(menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
            print("                     DRINKS MENU")
            for menu in menu_minuman:
                print("                    ", menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
            print("""
                   Menu List Changes :
                  1. Menambahkan Menu dari Belakang
                  2. Menambahakan Menu dari Indeks Tertentu
                  3. Menghapus Menu Metode 1
                  4. Menghapus Menu Metode 2
                  5. Mengubah Nama & Harga Menu""")
            change = int(input("Apa Yang Ingin Anda Lakukan Terhadap Chim's cafe? "))
            while choice == 'y' or choice == 'Y':
                if change == 1:
                    add_menu = str(input("Menu Apa yang Ingin Anda Tambahkan? F/f=Food & D/d=Drink : "))
                    if add_menu == 'f' or add_menu == 'F':
                        add_food_menu = []
                        add_food_menu.append(str(input("Silahkan Isi Daftar Nomornya? ")))
                        add_menu1 = str(input("Silahkan Isi Nama Menu Makanan Yang Ingin Ditambahkan? "))
                        add_food_menu.append(add_menu1)
                        add_food_menu.append("     ")
                        add_food_menu.append(int(input(f"Silahkan Isi Harga {add_menu1}? ")))
                        menu_makanan.append(add_food_menu)
                        print("NEW FOOD MENU")
                        for menu in menu_makanan:
                            print(menu[0:11][0], menu[0:11][1], menu[0:11][2], "RP.", menu[0:11][3])
                        print("\nMenu", add_menu1, "berhasil Ditambahkan")
                    elif add_menu == 'd' or add_menu == 'D':
                        add_drink_menu = []
                        add_drink_menu.append(str(input("Silahkan Isi Daftar Nomornya? ")))
                        add_menu1 = str(input("Silahkan Isi Nama Menu Minuman Yang Ingin Ditambahkan? "))
                        add_drink_menu.append(add_menu1)
                        add_drink_menu.append("     ")
                        add_drink_menu.append(int(input(f"Silahkan Isi Harga {add_menu1}? ")))
                        menu_minuman.append(add_drink_menu)
                        print("NEW DRINK MENU")
                        for menu in menu_minuman:
                            print(menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
                        print("\nMenu", add_menu1, "berhasil Ditambahkan")
                    else:
                        print("Silahkan Input Kode Yang Benar")
                    choice = str(input("Apakah Anda Ingin Menambahkan Menu Baru Lagi? "))
                    print("SEMOGA CHIM's CAFE SELALU SUKSES")
                elif change == 2:
                    while choice == 'y' or choice == 'Y':
                        add_menu = str(input("Menu Apa yang Ingin Anda Tambahkan? F/f=Food & D/d=Drink : "))
                        if add_menu == 'f' or add_menu == 'F':
                            add_food_menu = []

                            add_food_menu.insert(0, str(input("Silahkan Isi Daftar Nomornya? ")))
                            add_menu1 = str(input("Silahkan Isi Nama Menu Makanan Yang Ingin Ditambahkan? "))
                            add_food_menu.insert(1, add_menu1)
                            add_food_menu.insert(3, "                ")
                            add_food_menu.insert(4, int(input(f"Silahkan Isi Harga {add_menu1}? ")))
                            indeks = int(input("Anda Ingin Menambahkan di Indeks Ke Berapa? "))
                            menu_makanan.insert(indeks, add_food_menu)
                            print("NEW FOOD MENU")
                            for menu in menu_makanan:
                                print(menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
                        elif add_menu == 'd' or add_menu == 'D':
                            add_drink_menu = []

                            add_drink_menu.insert(0, str(input("Silahkan Isi Daftar Nomornya? ")))
                            add_nama_menu = str(input("Silahkan Isi Nama Menu Minuman Yang Ingin Ditambahkan? "))
                            add_drink_menu.insert(1, add_nama_menu)
                            add_drink_menu.insert(3, "                ")
                            add_drink_menu.insert(4, int(input(f"Silahkan Isi Harga {add_nama_menu}? ")))
                            indeks = int(input("Anda Ingin Menambahkan di Indeks Ke Berapa? "))
                            menu_minuman.insert(indeks, add_drink_menu)
                            print("NEW DRINK MENU")
                            for menu in menu_minuman:
                                print(menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
                        else:
                            print("Silahkan Input Kode Yang Benar")
                        choice = str(input("Apakah Anda Ingin Menambahkan Menu Baru Lagi? "))
                        print("SEMOGA CHIM's CAFE SELALU SUKSES")
                elif change == 3:
                    while choice == 'y' or choice == 'Y':
                        delete_menu = str(input("Menu Apa yang Ingin Anda Hapus? F/f=Food & D/d=Drink : "))
                        if delete_menu == 'f' or delete_menu == 'F':
                            print("FOOD MENU")
                            for menu in menu_makanan:
                                print(menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
                            delete_menu_makanan = int(
                                input("Silahkan Pilih Menu Makanan Yang Ingin Di Hapus, cth. 1, 2, 3 : "))
                            delete = delete_menu_makanan - 1
                            del menu_makanan[delete]
                            print("\n       Daftar Menu", delete_menu_makanan, " berhasil Dihapus")
                            print("FOOD MENU")
                            for menu in menu_makanan:
                                print(menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
                        elif delete_menu == 'd' or delete_menu == 'D':
                            print("DRINKS MENU")
                            for menu in menu_minuman:
                                print(menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
                            delete_menu_minuman = int(
                                input("Silahkan Pilih Menu Minuman Yang Ingin Di Hapus, cth. 1, 2, 3 : "))
                            delete = delete_menu_minuman - 1
                            del menu_minuman[delete]
                            print("\n       Daftar Menu", delete_menu_minuman, " berhasil Dihapus")
                            print("DRINKS MENU")
                            for menu in menu_minuman:
                                print(menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
                        else:
                            print("Silahkan Input Kode Yang Benar")
                        choice = str(input("Apakah Anda Ingin Menghapus Menu Lagi? "))
                        print("SEMOGA CHIM's CAFE SELALU SUKSES")
                elif change == 4:
                    while choice == 'y' or choice == 'Y':
                        remove_menu = str(input("Menu Apa yang Ingin Anda Hapus? F/f=Food & D/d=Drink : "))
                        if remove_menu == 'f' or remove_menu == 'F':
                            print("FOOD MENU")
                            for menu in menu_makanan:
                                print(menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
                            remove_menu_makanan = int(
                                input("Silahkan Pilih Menu Makanan Yang Ingin Di Hapus, cth. 1, 2, 3 : "))
                            remove = remove_menu_makanan - 1
                            menu_makanan.remove(menu_makanan[remove])
                            print("\n       Daftar Menu", remove_menu_makanan, " berhasil Dihapus")
                            print("FOOD MENU")
                            for menu in menu_makanan:
                                print(menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
                        elif remove_menu == 'd' or remove_menu == 'D':
                            print("DRINKS MENU")
                            for menu in menu_minuman:
                                print(menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
                            remove_menu_minuman = int(
                                input("Silahkan Pilih Menu Minuman Yang Ingin Di Hapus, cth. 1, 2, 3 : "))
                            remove = remove_menu_minuman - 1
                            menu_minuman.remove(menu_minuman[remove])
                            print("\n       Daftar Menu", remove_menu_minuman, " berhasil Dihapus")
                            print("DRINKS MENU")
                            for menu in menu_minuman:
                                print(menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
                        else:
                            print("Silahkan Input Kode Yang Benar")
                        choice = str(input("Apakah Anda Ingin Menghapus menu Lagi? "))
                        print("SEMOGA CHIM's CAFE SELALU SUKSES")
                elif change == 5:
                    while choice == 'y' or choice == 'Y':
                        ubah_menu = str(input("Menu Apa yang Ingin Anda Ubah? F/f=Food & D/d=Drink : "))
                        if ubah_menu == 'f' or ubah_menu == 'F':
                            print("NEW FOOD MENU")
                            for menu in menu_makanan:
                                print(menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
                            ubah_menu_makanan = int(
                                input("Silahkan Pilih Menu Makanan Yang Ingin Di Ubah, cth. 1, 2, 3 : "))
                            ubah_nama = input("Silahkan Masukkan Menu Baru : ")
                            ubah_harga = input("Silahkan Masukkan Harga Menu Baru : ")
                            spasi = "     "
                            ubah = ubah_menu_makanan - 1
                            menu_makanan[ubah] = ubah_menu_makanan, ubah_nama, spasi, ubah_harga
                            for menu in menu_makanan:
                                print(menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
                        elif ubah_menu == 'd' or ubah_menu == 'D':
                            print("NEW DRINKS MENU")
                            for menu in menu_minuman:
                                print(menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
                            ubah_menu_minuman = int(
                                input("Silahkan Pilih Menu minuman Yang Ingin Di Ubah, cth. 1, 2, 3 : "))
                            ubah_nama = input("Silahkan Masukkan Menu Baru : ")
                            ubah_harga = input("Silahkan Masukkan Harga Menu Baru : ")
                            spasi = "     "
                            ubah = ubah_menu_minuman - 1
                            menu_minuman[ubah] = ubah_menu_minuman, ubah_nama, spasi, ubah_harga
                            for menu in menu_minuman:
                                print(menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
                        else:
                            print("Silahkan Input Kode Yang Benar")
                        choice = str(input("Apakah Anda Ingin Mengubah Menu Lagi? "))
                else:
                    print("Daftar Tersebut Tidak Ada Dalam Menu List Changes")
            choice = str(input("Apakah Ingin Kembali Ke Menu Awal? "))
    elif login == 2:
        import datetime

        # MENU
        x = datetime.datetime.now()
        print("___________________________________________________")
        print("                    CHIM's CAFE                    ")
        print("                   Jln. My Story                   ")
        print("           ", (x), )
        print("___________________________________________________")
        for menu in menu_makanan:
            print(menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
        print("                     DRINKS MENU")
        for menu in menu_minuman:
            print("                    ", menu[0:10][0], menu[0:10][1], menu[0:10][2], "RP.", menu[0:10][3])
        print("*perhatikan kode menu jika ingin memesan F/D")
        print("___________________________________________________")

        # List of Dictionary Menu

        menu_makanan = [
            {"no_f": "1", "food": "Chicken Wings", "food_price": 25000},
            {"no_f": "2", "food": "Pasta Carbonara", "food_price": 35000},
            {"no_f": "3", "food": "Oregano French Fries", "food_price": 20000},
            {"no_f": "4", "food": "Spicy Tortilla Chicken Roll", "food_price": 35000},
            {"no_f": "5", "food": "Spicy Fried Beancurd", "food_price": 30000},
            {"no_f": "6", "food": "Beef Steak", "food_price": 45000},
            {"no_f": "7", "food": "Omlet ", "food_price": 15000},
            {"no_f": "8", "food": "Fettucini", "food_price": 27000},
            {"no_f": "9", "food": "Chicken Sup", "food_price": 20000},
            {"no_f": "10", "food": "Beef Burger", "food_price": 25000},
        ]
        menu_minuman = [
            {"no_d": "1", "drink": "Latte", "drink_price": 30000},
            {"no_d": "2", "drink": "macchiato", "drink_price": 30000},
            {"no_d": "3", "drink": "Ice Blend", "drink_price": 20000},
            {"no_d": "4", "drink": "Ice Drinks", "drink_price": 20000},
            {"no_d": "5", "drink": "Milk Shake", "drink_price": 25000},
            {"no_d": "6", "drink": "Americano", "drink_price": 30000},
            {"no_d": "7", "drink": "Falvoured Tea", "drink_price": 25000},
            {"no_d": "8", "drink": "Hot Chocolate", "drink_price": 30000},
            {"no_d": "9", "drink": "Mocktail", "drink_price": 40000},
            {"no_d": "10", "drink": "Mojito", "drink_price": 20000},
        ]
        print("______________________WELCOME______________________")

        # Proses

        list_ordered_makanan = []
        list_ordered_minuman = []
        greet1 = str(input("Hello, Apakah Anda Ingin Memesan Sesuatu? "))

        # Jika Belum Ingin Memesan

        if greet1 == 'n' or greet1 == 'N':
            greet2 = input("Apakah Ingin Menunggu Seseorang? ")
            if greet2:
                print("""
                      a. 15 menit
                      b. 25. menit
                      c. 45 menit""")
                minute = [{"kode": "a", "min": "15 Menit"},
                          {"kode": "b", "min": "25 Menit"},
                          {"kode": "c", "min": "30 menit"}, ]
                greet3 = str(input("Baik, Berapa Lama? "))
                kode = greet3
                if kode:
                    print("Baik, Ditunggu")
                    waiting = next((sub for sub in minute if sub['kode'] == greet3), None)
                    print(f"________Menunggu {waiting['min']} Sebelum Pemesanan________")
                greet1 = str(input("Apakah Anda Sudah Siap Memesan? "))

        # Jika Ingin Memesan

        while greet1 == 'y' or greet1 == 'Y':
            print("_____________________Pemesanan______________________")
            order = str(input("Apa Yang Ingin Anda Pesan? F/f=Food & D/d=Drink : "))
            if order == 'f' or order == 'F':
                order_food = input("Silahkan Pilih Menu Makanan Anda : ")
                ordered = next((sub for sub in menu_makanan if sub['no_f'] == order_food), None)
                total_food = int(input(f"Berapa porsi {ordered['food']}, yang ingin anda pesan? "))
                ordered['total_food'] = int(total_food)
                ordered['payment'] = ordered['total_food'] * ordered['food_price']
                list_ordered_makanan.append(ordered)
                greet1 = str(input("Apa Ada Tambahan Lagi? "))
            elif order == 'd' or order == 'D':
                order_drink = input("Silahkan Pilih Menu Minuman Anda : ")
                ordered = next((sub for sub in menu_minuman if sub['no_d'] == order_drink), None)
                total_drink = int(input(f"Berapa porsi {ordered['drink']}, yang ingin anda pesan? "))
                ordered['total_drink'] = int(total_drink)
                ordered['payment'] = ordered['total_drink'] * ordered['drink_price']
                list_ordered_minuman.append(ordered)
                greet1 = str(input("Apa Ada Tambahan Lagi? "))
            else:
                print("Mohon Maaf, Menu Tersebut Tidak Ada Dalam Daftar")
        print("___________________________________________________")

        # Proses Penjumlahan Pesanan

        total_food = 0
        total_drinks = 0
        for list_order in list_ordered_makanan:
            total_food += list_order['total_food']
        for list_order in list_ordered_minuman:
            total_drinks += list_order['total_drink']

        # Potongan Harga Yang Di Dapatkan

        if total_food >= 2:
            food_discount = 5
        else:
            food_discount = 0
        if total_drinks >= 3:
            drink_discount = 10
        else:
            drink_discount = 0
        menu_discount = food_discount + drink_discount
        if datetime.datetime.today().weekday() < 5:
            day_discount = 10
        else:
            day_discount = 5
        payment = str(input("Apakah Ingin Melakukan Pembayaran Melalu E-Money? "))
        if payment == 'y' or payment == 'Y':
            emoney_discount = 5
        else:
            emoney_discount = 0

        # Proses Perhitungan Keseluruhan

        print("___________________________________________________")
        print()
        print("                     PEMBAYARAN                 ")
        print("                     ----------                 ")
        for list_order in list_ordered_makanan:
            print(list_order['food'])
            print(list_order['food_price'], "x", list_order['total_food'], "= RP.", list_order['payment'])
        for list_order in list_ordered_minuman:
            print(f"{list_order['drink']}")
            print(f"{list_order['drink_price']} x {list_order['total_drink']} = RP. {(list_order['payment'])}")
        print("---------------------------------------------------+")
        total_discount = menu_discount + day_discount + emoney_discount
        list_all_ordered = list_ordered_makanan + list_ordered_minuman
        total_price = sum(list_order['payment'] for list_order in list_all_ordered)
        cut_discount = total_price * total_discount / 100
        total_payment = total_price - cut_discount
        print("                                         RP.", total_price)
        print("----------------------------------------------------")
        print("Diskon Makanan :  ", food_discount, "%")
        print("Diskon Minuman :  ", drink_discount, "%")
        print("Diskon Hari    :  ", day_discount, "%")
        print("Diskon E_Money :  ", emoney_discount, "%")
        print("---------------------------------------------------+")
        print("            RP.", total_price, "Diskon Sebesar", total_discount, "%")
        print("---------------------------------------------------=")
        print("                                Total : RP.", total_payment)
        print("____________________________________________________")
    else:
        print()
    choice = str(input("Apakah Anda Ingin Login Lagi? "))
    if choice == 'y' or choice == 'Y':
        print("___________________________________________________")
        print("""               
                1. Login Sebagai Admin  
                2. Login sebagai Customer
___________________________________________________""")

        login = int(input("Anda Ingin Login Sebagai Apa? "))
print("\n    TERIMA KASIH TELAH BERKUNJUNG KE CHIM's CAFE     ")
print("          Jln. My Story, Kota Imagination          ")