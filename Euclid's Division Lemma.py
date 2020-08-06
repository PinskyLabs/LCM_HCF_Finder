num1 = input("Enter a positive number: ")
num2 = input("Enter a positive number: ")


# noinspection PyGlobalUndefined
def HCF_euclid(num1, num2):
    global new_divisor
    print("\nYour numbers are {0} and {1}\n".format(str(num1), str(num2)))
    if num1 == num2:
        return print("Your numbers are the same")
    dividend = max(num1, num2)  # Naming Dividend
    divisor = min(num1, num2)  # Naming Divisor
    while dividend > divisor:  # Here, it identifies which number is the highest and lowest and prints 0 <= r < b
        quotient = int(dividend) / int(divisor)  # Naming the quotient
        remainder = int(dividend) % int(divisor)  # Naming the remainder
        if remainder == 0:
            return print("\nThe HCF of {0} and {1} is {2}".format(str(num1), str(num2), str(int(quotient))))
            # If the remainder is zero, then print this and stop it that instant
        while remainder != 0:
            new_dividend = divisor  # Renaming the earlier divisor to new dividend
            new_divisor = remainder  # Renaming the earlier remainder to new divisor
            new_quotient = int(new_dividend) / int(new_divisor)  # Naming the new quotient
            remainder = int(new_dividend) % int(new_divisor)
            # it is the new remainder that is produced when the new dividend and new divisor divide each other
            print("{0} = {1} * {2} + {3}".format(str(new_dividend), str(new_divisor), str(int(new_quotient)),
                                                 str(remainder)))  # Prints in the form of a = bq + r
        else:
            print("\nThe HCF of {0} and {1} is {2}".format(str(num1), str(num2), str(new_divisor)))  # HCF is printed
            break  # Break the loop when remainder is 0

    def HCF():
        print(new_divisor)


HCF_euclid(num1, num2)

project_credit = "\nTHIS PROJECT IS MADE BY PINAK PARATE!!!"
project_method = "\nFINDING HCF BY USING EUCLID'S DIVISION LEMMA"

print("{0}\n{1}".format(project_method, len(project_method) * "-"))
print("{0}\n{1}".format(project_credit, len(project_credit) * "-"))
