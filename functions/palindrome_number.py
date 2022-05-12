def palindrome_number(x):
    temp = x
    reverse = 0
    while(x>0):
        dig = x%10
        reverse = reverse*10 + dig
        x = x//10

    if temp == reverse:
        return True
    else:
        return False
