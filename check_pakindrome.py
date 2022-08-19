def palindrome(str):
    is_palindrome=True
    s= str[::-1]
    if s!=str:
        is_palindrome=False
    return is_palindrome

print(palindrome("121"))

# def swap(a,b):
#     return b,a
# a,b =10,30
# print (f"before swap a : {a}")
# print (f"before swap b : {b}")
# a1,b1 = swap(a,b)
# print (f"after swap a : {a1} ")
# print (f"after swap b : {b1}")

