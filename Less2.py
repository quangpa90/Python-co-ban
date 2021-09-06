'''
 bài 2: yêu cầu viết chương trình khi nhập 1 index trong string s in ra ký tự tại vị trí đã nhập
    nếu string rỗng in ra màn hình "Empty string"
    nếu index ngoài string đã cho thì in ra "i is out of range"*//
'''

s = "Hello"
n = int(input("Nhập vị trí cần lấy trong chuỗi"))
if s == "":
    print("Empty string")
elif n >= len(s):
    print("i is out of range")
else:
    print("ký tự tại index {} là:{}".format(n,s[n]))
