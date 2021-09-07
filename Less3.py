"""
Write a Python Program that prints the reversed version of a string.
The program must preserve uppercase and lowercase letters.
If the string is empty, print it intact.
"""
# cách 1
s = "Wo"
print("cách 1: {}".format(s[::-1]))
# s[start:stop:step]

# cách 2:
reverse_str = "".join(reversed(s))
print("cách 2: {}".format(reverse_str))

# reversed(s) =>> tạo ra 1 list ['o', 'W'] list này đã đảo ngược
# tiếp theo dùng hàm join() nó sẽ tạo ra string mới đã đảo ngược