import tkinter
from tkinter.messagebox import showinfo
import sys

win = tkinter.Tk()
win.title("HCF and LCM Finder")
win.config(bg="beige")

global new_divisor
global num1, num2


def orHCF():
    global new_divisor
    num1: int = entry1.get()
    num2: int = entry2.get()
    dividend = max(num1, num2)
    divisor = min(num1, num2)
    if num1 == num2:
        dividend = max(num1, num2)
        divisor = min(num1, num2)
    while dividend > divisor:
        quotient = int(dividend) / int(divisor)
        remainder = int(dividend) % int(divisor)
        while remainder != 0:
            new_dividend = divisor
            new_divisor = remainder
            new_quotient = int(new_dividend) / int(new_divisor)
            remainder = int(new_dividend) % int(new_divisor)
        else:
            break


def newHCF():
    num1: int = entry1.get()
    num2: int = entry2.get()
    global new_divisor
    if num1 == "" and num2 == "":
        return showinfo("RESULTS", "There are no numbers")
    else:
        showinfo("RESULTS", "Your numbers are \n{0} and \n{1}".format(str(num1), str(num2)))
    if num1 == num2:
        return showinfo("RESULTS", "Your numbers are the same")
    dividend = max(num1, num2)  # Naming Dividend
    divisor = min(num1, num2)  # Naming Divisor
    while dividend > divisor:  # Here, it identifies which number is the highest and lowest and prints 0 <= r < b
        quotient = int(dividend) / int(divisor)  # Naming the quotient
        remainder = int(dividend) % int(divisor)  # Naming the remainder
        while remainder != 0:
            new_dividend = divisor  # Renaming the earlier divisor to new dividend
            new_divisor = remainder  # Renaming the earlier remainder to new divisor
            new_quotient = int(new_dividend) / int(new_divisor)  # Naming the new quotient
            remainder = int(new_dividend) % int(new_divisor)
            # it is the new remainder that is produced when the new dividend and new divisor divide each other
            # showinfo("RESULTS","{0} = {1} * {2} + {3}\n".format(str(new_dividend), str(new_divisor), str(int(new_quotient)),str(remainder)))
            # Prints in the form of a = bq + r
        else:
            showinfo("RESULTS", "\nThe HCF of {0} and {1} is {2}".format(str(num1), str(num2), str(new_divisor)))
            # HCF is printed
            break  # Break the loop when remainder is 0


def LCM():
    global new_divisor
    global entry1, entry2
    num1: int = entry1.get()
    num2: int = entry2.get()
    orHCF()
    showinfo("RESULTS", "The LCM of your numbers is: " + str((int(num1) * int(num2)) / int(new_divisor)))


label1 = tkinter.Label(win, text="Enter a positive number :  ", font=("agency fb", 20, "bold"))
label1.grid(row=0, column=0)
label1.config(fg="maroon", bg="beige")

label2 = tkinter.Label(win, text="Enter a positive number :  ", font=("agency fb", 20, "bold"))
label2.grid(row=1, column=0)
label2.config(fg="maroon", bg="beige")

entry1 = tkinter.Entry(win, width=25)
entry1.grid(row=0, column=1, pady=10)
entry1.config(fg="cyan4", bg="wheat2")

entry2 = tkinter.Entry(win, width=25)
entry2.grid(row=1, column=1, pady=10)
entry2.config(fg="cyan4", bg="wheat2")

button1 = tkinter.Button(win, text=" LCM ", font=("futura", 30, "underline", "bold"), command=LCM)
button1.grid(row=2, column=0, columnspan=1, pady=10)
button1.config(fg="royalblue4", bg="lightgoldenrod1")

button2 = tkinter.Button(win, text=" HCF", font=("futura", 30, "underline", "bold"), command=newHCF)
button2.grid(row=2, column=1, columnspan=2, pady=10)
button2.config(fg="royalblue4", bg="lightgoldenrod1")

button3 = tkinter.Button(win, text="<|         EXIT         |>", font=("berlin sans fb", 30, "italic"), command=sys.exit)
button3.grid(row=3, column=0, columnspan=2, pady=20)
button3.config(fg="royalblue4", bg="lightgoldenrod1")

win.mainloop()
