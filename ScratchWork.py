def disem_vowel(input):
    check_str = input.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_str = ""
    for c in check_str:
        if c in vowels:
            new_str += c
    return new_str


def filter_out_strings(lis):
    int_list = [num for num in lis if isinstance(num, int)]
    return int_list


def fizz_buzz(num):
    i = 1
    while i <= num:
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
        i += 1


print(disem_vowel("Hello"))

print(filter_out_strings([1, 2, 'a', 'b']))

fizz_buzz(100)




