
def prime_number(number):
    num=number//2
    a=2
    is_prime=True
    for a in range (2,num):
        if number%a==0:
            is_prime=False
    if is_prime:
        print("this number is prime")
    else:
        print("this number is not prime")

user_input= int(input("Check this number : "))
prime_number(number = user_input)
