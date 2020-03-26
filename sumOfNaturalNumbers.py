#Sum of square of first n natural numbers


num=int(input("Enter a number:"))

def sum(num):
    result=0
    if num < 0:
        print(num, "is not a natural number!")
    else:
        for i in range(1,num+1):
            result=result + (i*i)
        return result

print("The sum of square of first", num, "natural number is:", sum(num))
# One logical error here is, last print statement is being executed for if condition as well
#where can i place print statement so as to get same result as below for negative numbers?????? 





# ***Second way****

num=int(input("Enter a number:"))


result=0
if num < 0:
    print(num, "is not a natural number!")
else:
    for i in range(1,num+1):
        result=result + (i*i)
    print("The sum of square of first", num, "natural number is:",result)