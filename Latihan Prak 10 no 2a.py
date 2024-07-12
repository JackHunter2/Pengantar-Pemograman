#a
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Masukkan angka :"))
result = factorial(num)

print(f"Faktorial dari {num} adalah {result}")

#b
def count_case(s):
    uppercase = 0
    lowercase = 0
    for c in s:
        if c.isupper():
            uppercase += 1
        elif c.islower():
            lowercase += 1
    return uppercase, lowercase

s = input("\nString Original :")
uppercase, lowercase = count_case(s)

print(f"Jumlah karakter uppercase pada string :{uppercase}")
print(f"Jumlah karakter lowercase pada string :{lowercase}")

#c
squares = {}

number = int(input("\nMasukkan angka: "))

for i in range(1, number + 1):
    squares[i] = i * i

print(squares)

#d
def multiply_values(d):
    return {k: v * v for k, v in d.items()}

d1 = {"a": 1, "b": 2, "e": 3, "d": 4}
d2 = {"b": 2, "e": 3, "d": 4}

print("\n",multiply_values(d1))
print(multiply_values(d2))
