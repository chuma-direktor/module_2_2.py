first = 1455
print(first)
second = 785
print(second)
third = 1933
print(third)

if first == second and second == third and first == third:
        print("3")
elif first == second or second == third or third == first:
        print(" 2 ")
else:
        print("0")