def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            result = chr((ord(char) - start + shift_amount) % 26 + start)
            encrypted_text += result
        else:
            encrypted_text += char
    return encrypted_text

original_text = (input("Masukkan String : "))
shift_amount = int(input("Makkan berapa langkah : "))
encrypted_text = caesar_cipher(original_text, shift_amount)
print("String asli:", original_text)
print("Setelah dienkripsi:", encrypted_text)
