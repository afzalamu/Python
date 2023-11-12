mytuple = tuple(("Dave", "42", True))
yourtuple = ("1", "4", "21", "afzal")
print(mytuple)
print(yourtuple)

print(type(yourtuple))
print(type(mytuple))

# ------------------------------------

# Tuple cannot be changed
# but we can copy it to do something creative

newlist = list(mytuple)  # changed it to a list

print(newlist)
print(type(newlist))
# now value can be addded or removed
newlist.append("Neil")
print(newlist)

newtuple = tuple(newlist)
# casted a list into tuple
print(newtuple)
print(type(newtuple))


# ---------------------------------------
# unpacking a tuple
(one, two, *hey) = yourtuple
print(one)
print(two)
print(*hey)

(one, *two, hey) = yourtuple
print(one)
print(*two)
print(hey)
print(yourtuple.count(2))
