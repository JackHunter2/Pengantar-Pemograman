class Calculator:
    def __init__(self):
        pass

    def calculate_factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.calculate_factorial(n-1)

    def count_case(self, s):
        uppercase = 0
        lowercase = 0
        for c in s:
            if c.isupper():
                uppercase += 1
            elif c.islower():
                lowercase += 1
        return uppercase, lowercase

    def generate_squares(self, number):
        squares = {}
        for i in range(1, number + 1):
            squares[i] = i * i
        return squares

    def multiply_values(self, d):
        return {k: v * v for k, v in d.items()}

def main():
    calculator = Calculator()

    while True:
        print("\nMenu:")
        print("1. Faktorial")
        print("2. Upper dan Lower case")
        print("3. Pascal")
        print("4. Pengkalian angka")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            num = int(input("Enter a number: "))
            print(f"Factorial of {num} is {calculator.calculate_factorial(num)}")
        elif choice == "2":
            s = input("Enter a string: ")
            uppercase, lowercase = calculator.count_case(s)
            print(f"Uppercase characters: {uppercase}")
            print(f"Lowercase characters: {lowercase}")
        elif choice == "3":
            number = int(input("Enter a number: "))
            print(calculator.generate_squares(number))
        elif choice == "4":
            d = eval(input("Enter a dictionary: "))
            print(calculator.multiply_values(d))
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
