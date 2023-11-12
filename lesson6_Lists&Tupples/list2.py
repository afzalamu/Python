nums = [4, 42, 78, 1, 5]

nums.reverse()  # reverse an array list
print(nums)

# -----------------------------------------
nums.sort()  # sort in ascending order
print(nums)

# ------------------------------------------
# nums.sort(reverse=True)  # sort in descending ordre
# print(nums)

# ---------------------------------------------
# Note: they modify the lists
# what if original list is not modified

# global sorted function

print(sorted(nums, reverse=True))  # this appproach doent modify the original lists
print(nums)


# anotehr appproach is to amke the copy and sort the copy
# ways to make a copy
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(nums)
print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)


# ---------------------------------------------?
# check the type of list
print(type(nums))

mylist = list(["afzal", "1"])
print(mylist)
