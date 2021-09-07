"""
Write a Python Program that prints the reversed version of a string.
The program must preserve uppercase and lowercase letters.
If the string is empty, print it intact.
"""
if __name__== "__main__":
    # cách 1:
    s = "Hello"
    print("cách 1: {}".format(s[::-1]))
    # Cách 1 dùng s[start:stop:step]
    # cách 2:
    reverse_str = "".join(reversed(s))
    print("cách 2: {}".format(reverse_str))
    # Cách 2 dùng hàm reversed()
    # reversed(s) hàm này tạo ra list đảo ngược =>> ['o','l','l','e','H']
    # tiếp đó dùng hàm join() join list thành chuỗi tạo ra chuỗi mới 0lleH