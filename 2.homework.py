def palindrome():
    num = eval(input("Enter a number: "))
    if str(num) == str(num)[::-1]:
        print(f"{num} is a palindrome")
    else:
        print(f"{num} is not a palindrome")
palindrome()


''' -----------------------------------------------------------
OUTPUT :
Enter a number: 12321
12321 is a palindrome

Enter a number: 123
123 is not a palindrome
--------------------------------------------------------------'''

def reverse():
    num = eval(input("Enter a number: "))
    reversed_num = str(num)[::-1]
    print(f"Reversed number: {reversed_num}")
reverse()

''' -----------------------------------------------------------
OUTPUT :
Enter a number: 12345
Reversed number: 54321

Enter a number: 987654321
Reversed number: 123456789
--------------------------------------------------------------'''

def even_odd():
    num = eval(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")
even_odd()

''' -----------------------------------------------------------
OUTPUT :            
Enter a number: 10
10 is an even number

Enter a number: 51
51 is an odd number
-------------------------------------------------------------- '''

def square_list(l):
    result = []
    for i in l:
        result.append(i * i)
    return result
numbers = [1, 2, 3, 4, 5,6,7,8,9,10]
print(square_list(numbers))
''' -----------------------------------------------------------
OUTPUT :
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
-------------------------------------------------------------- '''