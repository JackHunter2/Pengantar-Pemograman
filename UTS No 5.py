class ATM:
    def __init__(self, pin=1234, balance=0):
        self.pin = pin
        self.balance = balance

    def check_pin(self, input_pin):
        if input_pin == self.pin:
            return True
        else:
            return False

    def show_menu(self):
        print("\n1. Informasi saldo")
        print("2. Penarikan uang")
        print("3. Tabung uang")
        print("4. Keluar")

    def check_balance(self):
        print(f"\nSaldo anda : Rp {self.balance:,}")

    def withdraw_cash(self):
        amount = int(input("\nBerapa yang ingin anda tarik : "))
        if amount > self.balance:
            print("Tidak bisa menarik saldo, karena saldo anda kurang!")
        else:
            self.balance -= amount
            print(f"Rp {amount:,} Telah berhasil di tarik. Saldo anda sekarang adalah : Rp {self.balance:,}")
                
    def deposit_cash(self):
        amount = int(input("\nBerapa yang ingin anda tabung : "))
        self.balance += amount
        print(f"Rp {amount:,} Telah berhasil di tabung. Saldo anda sekarang : Rp {self.balance:,}")

def main():
    print("Selamat datang di program ATM, Bank AMAN")
    atm = ATM()
    
    while True:
        pin = int(input("\nSilahkan masukkan pin anda : "))
        if atm.check_pin(pin):
            while True:
                atm.show_menu()
                choice = input("\nSilahkan pilih menu yang anda inginkan : ")
                if choice == "1":
                    atm.check_balance()
                    choice = input("\nApakah anda ingin ke menu awal (y/n) : ")
                    if choice.lower() == "y":
                        continue
                    elif choice.lower() == "n":
                        print("========================================================")
                        print("Kartu anda akan keluar dari mesin ATM...")
                        print("\nTerima kasih telah menggunakan layanan Bank AMAN")
                        break
                elif choice == "2":
                    atm.withdraw_cash()
                    choice = input("\nApakah anda ingin ke menu awal (y/n) : ")
                    if choice.lower() == "y":
                        continue
                    elif choice.lower() == "n":
                        print("========================================================")
                        print("Kartu anda akan keluar dari mesin ATM...")
                        print("\nTerima kasih telah menggunakan layanan Bank AMAN")
                        break
                elif choice == "3":
                    atm.deposit_cash()
                    choice = input("\nApakah anda ingin ke menu awal (y/n) : ")
                    if choice.lower() == "y":
                        continue
                    elif choice.lower() == "n":
                        print("========================================================")
                        print("Kartu anda akan keluar dari mesin ATM...")
                        print("\nTerima kasih telah menggunakan layanan Bank AMAN")
                        break
                elif choice == "4":
                    print("========================================================")
                    print("Kartu anda akan keluar dari mesin ATM...")
                    print("\nTerima kasih telah menggunakan layanan Bank AMAN")
                    break
                else:
                    print("Pilihan tidak ada, Silahkan pilih kembali.")
        else:
            print("\nPin salah, Silahkan coba lagi.")
            if input("\nApakah anda ingin mencoba lagi (y/n) : ").lower() != "y":
                print("========================================================")
                print("Kartu anda akan keluar dari mesin ATM...")
                print("\nTerima kasih telah menggunakan layanan Bank AMAN")  

if __name__ == "__main__":
    main()
