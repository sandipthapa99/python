
#checking if a number is a prime number or not
num = int(input("Enter a number:"))


if num>1: #prime numbers are always greater than 1
    for i in range(2,num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else: #this works specifically for number "2"
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")