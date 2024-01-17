#!/usr/bin/python3

def uppercase(s):
    for char in s:
        uppercase_char = char
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(uppercase_char), end='')
            print()

            if __name__ == "__main__":
                uppercase("best")
                uppercase("Best School 98 Battery street")
