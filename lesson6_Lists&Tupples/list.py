users = ["afzal", "malik", "ilma"]
data = ["afzal", "42", True]
emptylist = []

# print(emptylist)
# print(data)
# print(users)
# print("afzal" in users)
# print("afzal" in data)
# print("afzal" in emptylist)

# list start with zero inedex
# print(users[0])
# print(users[-1])  # to know the last value
# print(users[-2])


# to know the position
# print(users.index("ilma"))  # returns the index value
# print(users[0:2])  # printing range of values
# print(users[0:])
# print(users[-3:-1])

# length of the list
# print(len(users))
# print(len(data))

users.append("nagma")
print(users)

# users += ["akeel"] #make sure brackets otherwise?
# print(users)

# another method

users.extend(["akeel", "ahmad"])
print(users)

# users.extend(data)
# print(users)

# --------------------------------------------
users.insert(0, "Bob")
print(users)

users[2:2] = ["eddy", "alex"]
print(users)
# --------------------------------------------
# to replace values

users[1:3] = ["eddy", "alex"]
print(users)


# ----------------------------------------------
# remove methods in list

users.remove("Bob")
print(users)
users.remove("ahmad")
print(users)
print(len(users))

print(users.pop())  # remove and retutrn the last vale in list
print(users)

del users[0]  # deleet from specific positions
print(users)

# del data # to delete an entire list
# print(data)

data.clear()  # empty the list but doesnt delete it
print(data)  # emety data list is returned


users[1:2] = ["dave"]
users.sort()  # sort the list alphabetically
print(users)

users.sort(key=str.lower)
print(users)

# ----------------------------------------------
