def rem(string):
    st = ""
    for i in range(len(string)):
        if i%2==0:
            if string[i].isalpha():
                st+=string[i]
        else:
            st+=string[i]
    return st

new = input("Enter a String : ")
print(rem(new))
