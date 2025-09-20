### 1.Eligible or not:
l1 = ["sravan", "harish", "aravind", "akhil"]
l2 = [24, 17, 20, 18]

for i in range(len(l1)):
    if l2[i] >= 18:
        print(l1[i], "-", l2[i], "- Eligible")
    else:
        print(l1[i], "-", l2[i], "- Not Eligible")


### 2. Sum of digits:
n = 123
s = 0
while n > 0:
    d = n % 10
    s += d
    n = n // 10
print("Sum of digits:", s)


### 3. Highest digit in an integer:
n = 123498
max_digit = 0

while n > 0:
    d = n % 10
    if d > max_digit:
        max_digit = d
    n = n // 10

print("Highest digit:", max_digit)




### 4 .Chocolate wrapper distribution:

amount = 21
chocs = amount   # chocolates bought directly
wrappers = amount

while wrappers >= 3:
    new_chocs = wrappers // 3
    chocs += new_chocs
    wrappers = wrappers % 3 + new_chocs

print("Total chocolates:", chocs)
