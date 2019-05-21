name = input()

if name[::-1] == name[0:]:
    print(name, " is a palindrome")

else:
    print(name, " is not a palindrome")
