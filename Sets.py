fruits = {'apple', 'orange', 'banana'}
# print(fruits)

fruits_1 = set(['apple', 'orange', 'banana'])

# print(len(fruits))
# print(fruits)

# for item in fruits:
#     print(item)

fruits.add('mango')
# print(fruits)

fruits.update(['mango', 'pineapple'])
# print(fruits)

fruits.remove('apple')
print(fruits)

fruits.remove('mango')
print(fruits)

fruits.add('mango')
print(fruits)

fruits.discard('mango')
print(fruits)

fruits.pop()
print(fruits)

