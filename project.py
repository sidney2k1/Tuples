def multipletuples(nums):
    temp=list(nums)
    product=1
    for x in temp:
        product*=x
    return product
nums=(4,3,2,2,-1,18)
print("Original list:")
print(nums)
print("Multiplying all the numbers of the tuple:",multipletuples(nums))
nums=(2,4,8,8,3,2,9)
print("Original tuple")
print(nums)
print("Multiplying all the numbers in the tuple",multipletuples(nums))