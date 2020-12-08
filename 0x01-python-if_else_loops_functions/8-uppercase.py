#!/usr/bin/python3


def uppercase(str):
    newString = ""
    for i in range(len(str)):
        if(ord(str[i]) >= 97 and ord(str[i]) <= 122):
            newString += chr((ord(str[i]) - 32))
        else:
            newString += str[i]

    print(newString)
