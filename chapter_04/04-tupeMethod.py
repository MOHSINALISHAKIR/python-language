# Different ways to create tuples
t1 = (1, 2, 3)
t2 = ("apple", "banana", "cherry")
t3 = (1, "hello", 3.5, True)

# Single-element tuple (must have a comma!)
t4 = (5,)
print(type(t4))   # <class 'tuple'>
t = (10, 20, 30, 40)

print(t[0])    # 10
print(t[-1])   # 40
print(t[1:3])  # (20, 30)

numbers = (5, 2, 9, 1)

print(len(numbers))   # 4
print(max(numbers))   # 9
print(min(numbers))   # 1
print(sum(numbers))   # 17
print(sorted(numbers))  # [1, 2, 5, 9]
