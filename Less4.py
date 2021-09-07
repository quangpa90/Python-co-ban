'''
Write a Python program that prints the first and last three characters of the string s as a single string.
If the string has less than six characters, print an empty string (blank output).
'''
if __name__ == "__main__":
    s = "Amazing"
    if len(s) < 6:
        print("")
    else:
        out_str = s[:3] + s[len(s)-3:]
        print(out_str)
