def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count += 1
    return count
def main():
    text = input("enter neme: ")
    print("vowels count:",count_vowels(text))
main()