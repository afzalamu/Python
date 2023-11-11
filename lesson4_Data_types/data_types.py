import math

# String_Data_Type

# Literal assignment

first = "Afzal"
last = "Malik"

print(type(first))  # to check the type of first
print(type(first) == str)  # another way to check
print(isinstance(first, str))  # another way to check
# ----------------------------------------------------------


# Constructor Function

Pizza = str("Pepporoni")  # another way to assign data
print(type(Pizza))  # to check the type
print(type(Pizza) == str)  # another way to check
print(isinstance(Pizza, str))  # another way to check

# ----------------------------------------------

# Concatination

fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string

decade = str(1980)
print(type(decade))
print(decade)

statement = " I like story of the" + " " + decade + " " + "and it is nice "
print(statement)

# ----------------------------------------------------------
# Multiple lines

multiline = """
Hey, How are you?

I was just checking in,
                                All good?

"""
print(multiline)

# -----------------------------------------------------------
# Escaping special cahracters

sentence = "I'm back at work ! \t Hey \n\n Where this at \\ located?"
print(sentence)
# -----------------------------------------------

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)
print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)
# ------------------------------------------------------------------

# whitespaces

print(len(multiline))
multiline += "                   "
multiline = "                " + multiline
print(len(multiline))

print(len(multiline.strip()))  # remove whitespace
print(len(multiline.lstrip()))  # remove whitespace from left side
print(len(multiline.rstrip()))  # remove whitespace from right sides

# ------------------------------------------------------------------
print(" ")
print(" ")
print(" ")
title = "menu".upper()
print(title.center(20, "="))
print("coffee".ljust(16, ".") + "$1".rjust(4))
print("MUffin".ljust(16, ".") + "$2".rjust(4))
print("cuttle".ljust(16, ".") + "$5".rjust(4))
# --------------------------------------------------------------------

# string index value
print(first[-1])  # give last value
print(first[1])
print(first[0])  # index start at 0
print(first[0:-1])  # doesnot give last index value
print(first[0:])  # this gives last value too


# --------------------------------
# somemethods return boolean data

print(first.startswith("A"))
print(first.endswith("k"))


# -------------------------------
#  Boolen dat type

# true and false  make proper True and False

# -------------------------------------------

# Numeric data types

# integers

price = 100
best_price = int(100)
print(type(price))
print(isinstance(best_price, int))


# float type

Gpa = 3.28
y = float(1.14)
print(type(Gpa))
print(isinstance(y, float))

# complex value

comp_value = 5 + 3j
print(type(comp_value))
print(comp_value)
print(comp_value.real)
print(comp_value.imag)

# Built in function
print(abs(Gpa))  # check absolute value
print(abs(Gpa * -1))
print(round(Gpa))  # roundoff ton nearest intgere value
print(round(Gpa, 1))  # roundoff to mentioned decimal place value


print(math.pi)
print(math.sqrt(64))
print(math.ceil(Gpa))
print(math.floor(Gpa))


# casting string to a number

zipcode = "262121"
zip_value = int(zipcode)
print(type(zip_value))


#  Error if you attempt to cast incorrect data
# zip_value = int("New York")
