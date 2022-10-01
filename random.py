import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if two_ls(s) + max_min(s) + last(s) + first_num(s) + no_per(s) + numer(s) == 6:
        return True
    else:
        return False


def two_ls(s):
    if s[0:2].isalpha():
        return 1
    else:
        return 0


def max_min(s):
    if 2 <= len(s) <= 6:
        return 1
    else:
        return 0


def last(s):
    d = re.findall(r'\d+', s)
    if bool(d):
        if s[-1].isnumeric():
            return 1
        else:
            return 0
    else:
        return 1


def first_num(s):
    d = re.findall(r'\d+', s)
    if bool(d):
        f = (d[0])
        a = (f[0])
        if int(a) != 0:
            return 1
        else:
            return 0
    else:
        return 1


def no_per(s):
    if s.isalnum():
        return 1
    else:
        return 0


def numer(s):
    d = re.findall(r'\d+', s)
    if bool(d):
        for i, c in enumerate(s):
            if c.isdigit():
                a = i
                break
        if s[a:-1].isdigit():
            return 1
        else:
            return 0
    else:
        return 1


main()
