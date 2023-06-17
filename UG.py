import random

characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", ".", "_"]

def generate_name(amount):
    random_chars = random.sample(characters, amount)
    return ''.join(random_chars)

def main():
    amount = int(input("How many characters do you want in your name? "))
    print("Press Enter to generate a new name. Press Ctrl+C to exit.")
    while True:
        input()
        result = generate_name(amount)
        print(result)

if __name__ == "__main__":
    main()
