def palindrom(x):
    a = x[::-1]
    if x == a:
        return True
    else:
        return False
print(palindrom(input('enter the text')))
