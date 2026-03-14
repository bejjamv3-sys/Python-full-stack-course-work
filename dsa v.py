def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for vhar in vowels:
        count += 1
    return count
def main():
    text = input("enter neme: ")
    print("vowels count:",count_vowels(text))
main()