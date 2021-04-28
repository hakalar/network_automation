nums = [1,2,3,4,5]

for num in nums:
    if num ==3:
        print('Found')
        # break
        continue
    print(num)

nums = [1,2,3,4,5]

for num in nums:
    for letter in 'abc':
        print(num, letter)

# prints 0 - 9
for i in range(10):
    print(i)

# prints 1 - 10
for i in range(1, 11):
    print(i)


x = 0

while True:
    if x == 1000:
        break
    print(x)
    x += 1