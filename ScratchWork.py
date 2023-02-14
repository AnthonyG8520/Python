def disem_vowel(input):
    check_str = input.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_str = ""
    for c in check_str:
        if c in vowels:
            new_str += c
    return new_str


print(disem_vowel("Hello"))







