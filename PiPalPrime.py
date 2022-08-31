import requests
import mmap


def isPalindrome(s):
    return s == s[::-1]


def is_prime(num):
    if num == 2:
        return True
    if not num & 1:
        return False
    return pow(2, num-1, num) == 1


digits = 11
length = digits
j = 0
with open("C:\TEMP\Pi - Dec.txt", 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        i = 0
        while i < len(m):

            checkPalindromo = str(m[i:length+i]).replace(".",
                                                         "").replace("b", "").replace("'", "")
            num = int(checkPalindromo)
            if (isPalindrome(checkPalindromo) & is_prime(num)):
                print(f"O número {num} é palíndromo e primo")
            # memory-map the file, size 0 means whole file
            i += 1


# print(is_prime(507946030086901688309))
