def show_menu():
    print("Selamat datang di Warteg Ibu Kantin.")
    print("Menu pilihan tersedia di bawah, silahkan di lihat terlebih dahulu.")
    print()
    print("Menu Pilihan, anda:")
    print("BU: Bakso Urat, Rp.15000")
    print("MA: Mie Ayam, Rp.12000")
    print("NG: Nasi Goreng, Rp.12000")
    print("ET: Es Teh Manis, Rp.3000")
    print("AG: Ayam Goreng, Rp.10000")
    print("AGK: Ayam Geprek Kriuk, Rp.15000")
    print("L: Lapor")
    print("X: Selesai memesan")
    print()

def get_price(menu_code):
    prices = {
        "BU": 15000,
        "MA": 12000,
        "NG": 12000,
        "ET": 3000,
        "AG": 10000,
        "AGK": 15000
    }
    return prices.get(menu_code, 0)

def main():
    orders = {}
    show_menu()
    while True:
        menu_code = input("Silahkan pilih menu: ").upper()
        if menu_code == "X":
            break
        elif menu_code == "L":
            print_report(orders)
        else:
            if menu_code in ["BU", "MA", "NG", "ET", "AG", "AGK"]:
                qty = int(input(f"Berapa banyak {menu_code} yang dipesan: "))
                if menu_code in orders:
                    orders[menu_code] += qty
                else:
                    orders[menu_code] = qty
            else:
                print("Menu tidak tersedia.")
    
    total, total_with_tax, change = generate_bill(orders)
    print(f"Total Pembelian: Rp. {total}")
    print(f"Total Pajak: Rp. {total * 0.1}")
    print(f"Total seluruh: Rp. {total_with_tax}")
    
    amount_paid = float(input("Jumlah uang konsumen: Rp. "))
    while amount_paid < total_with_tax:
        print(f"Uang tidak cukup. Silahkan masukkan kembali uang yang cukup: Rp{total_with_tax}")
        amount_paid = float(input("Jumlah uang konsumen: Rp. "))
    
    change = amount_paid - total_with_tax
    print(f"Kembaliannya: Rp {change}")
    print("Keluar Program")

def print_report(orders):
    print("Laporan pembelian:")
    print("Item\t\tQuantity\tSales")
    for item, qty in orders.items():
        price = get_price(item)
        print(f"{item}\t\t{qty}\t\tRp{qty * price}")
    print()

def generate_bill(orders):
    total = 0
    for item, qty in orders.items():
        price = get_price(item)
        total += qty * price
    total_with_tax = total + (total * 0.1)
    return total, total_with_tax, 0

if __name__ == "__main__":
    main()
