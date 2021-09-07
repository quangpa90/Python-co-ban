'''
         Write a Python program that prints the character at index i in the string s.
        If the index is out of range, the program should print "i is out of range"
        If the string is empty, the program should print ""
'''
if __name__ == "__main__":
    s = "Pizza"
    i = int(input("Nhap vao index:"))
    if s == "":
        print("Empty String")
    elif i >= len(s):
        print("i is out of range")
    else:
        print("ky tu tai index i la: {}".format(s[i]))

