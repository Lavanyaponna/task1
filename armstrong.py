num = int(input("Enter a number: "))

digits = str(num)
power = len(digits)
total = sum(int(digit) ** power for digit in digits)
if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
