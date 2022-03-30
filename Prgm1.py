# Create test cases using pytest for the following programs and generate the testcase reports in either HTML / JSON / XML files . For each test cases you have to use the concepts of Parameterizing Tests, Xfail, skip tests , stop test cases after N Test Failures .
#
# 1.  Python program to check if the number is an Armstrong number or not
# 2. Python program to check if the number is divisible by 8 or not
# 3. Python program to find the smallest number among 3 numbers
# 4. Python program to check if the number is even number or odd
# 5. python program to check whether a string is palindrome or not

def armstrong(number):
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if number == sum:
        return True
    else:
        return False
def divisible_8(number):
    if number%8 == 0:
        return True
    else:
        return False
def smallest_3numbers(number1, number2, number3):
    if (number1<number2) and (number1<number3):
        return "number1"
    elif(number2<number1) and (number2<number3):
        return "number2"
    else:
        return "number3"
def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
def is_palindrome(string):
    reverse = (string[::-1])
    if string == reverse:
        return True
    else:
        return False

if __name__ == "__main__":
    print(" Check Armstrong or not")
    number = int(input("Enter a number:"))
    Armstrong = armstrong(number)
    print(Armstrong)

    print("Check divisible by 8 or not")
    number = int(input("Enter a number:"))
    Divisible_8 = divisible_8(number)
    print(Divisible_8)

    print("check smallest among 3 numbers:")
    number1 = int(input("Enter a number1:"))
    number2 = int(input("Enter a number2:"))
    number3 = int(input("Enter a number3:"))
    Smallest = smallest_3numbers(number1, number2, number3)
    print(Smallest)

    print("check even or odd:")
    number = int(input("Enter a number:"))
    Even_or_odd = even_or_odd(number)
    print(Even_or_odd)

    print("Check palindrome or not")
    string = (input("Enter a word:"))
    Is_palindrome = is_palindrome(string)
    print(Is_palindrome)
