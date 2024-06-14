def game():
    choices = ["Gunting", "Batu", "Kertas"]

    user1 = input("Pemain 1: Silahkan anda pilih : Gunting, Batu, Kertas -> ").capitalize()
    user2 = input("Pemain 2: Silahkan anda pilih : Gunting, Batu, Kertas -> ").capitalize()
    while user1 not in choices:
        user1 = input("Pilihan pemain 1 tidak ada, silahkan pilih : Gunting, Batu, Kertas : ").capitalize()
    while user2 not in choices:
        user2 = input("Pilihan pemain 2 tidak ada, silahkan pilih : Gunting, Batu, Kertas : ").capitalize()

    if user1 == user2:
        print("Seri!")
    elif (user1 == "Gunting" and user2 == "Kertas") or (user1 == "Batu" and user2 == "Gunting") or (user1 == "Kertas" and user2 == "Batu"):
        print("Permain 1 menang!")
    else:
        print("Pemain 2 menang!")

while True:
    game()
    play_again = input("Apakah Anda ingin bermain lagi? (y/n): ").lower()
    if play_again == "y":
        print("Permainan baru akan dimulai")
    elif play_again == "n":
        print("GAME OVER")
        break
    else:
        print("Pilihan tidak tersedia, silah pilih y/n -> ")
        
