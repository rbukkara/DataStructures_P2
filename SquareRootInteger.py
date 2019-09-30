def sqrt(number):

    if number != (number//1):
        print("not an integer")

    if number == 0 or number == 1:
        return number

    min = 1
    max = number
    result = number

    while max-min > 1:
        #print("result is {0}".format(result))
        product = result * result
        if product == number:
            #print("product match result is {0}".format(result))
            return result
        if product > number:
            max = result
            result = result//2
        else:
            min = result
            result = (max+min)//2

    return min


print("Pass" if(3 == sqrt(9)) else "Fail")
print("Pass" if(0 == sqrt(0)) else "Fail")
print("Pass" if(4 == sqrt(16)) else "Fail")
print("Pass" if(1 == sqrt(1)) else "Fail")
print("Pass" if(5 == sqrt(27)) else "Fail")
print("Pass" if(6 == sqrt(37)) else "Fail")
print("Pass" if(7 == sqrt(60)) else "Fail")
print("Pass" if(20 == sqrt(401)) else "Fail")
print("Pass" if(25 == sqrt(651)) else "Fail")
print("Pass" if(24 == sqrt(623)) else "Fail")







