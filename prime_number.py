num=int(input('Enter the number to check '))
#primenumber greater than one
if num>1:
    for i in range(2, num):
        if (num%i)==0:
            print (num, ' is not a prime number')
            print (i, ' times ', num//i, ' is ', num)
            break
        else:
            print(num, ' is a prime number')

#if input is less than or equal to 1, it is not a prie number

else:
    print(num, ' is not a prime number')