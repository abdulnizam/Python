#!usr/bin/python

# Mapping Example
seq = range(8)
def add(x, y): return x+y
map_list = map(add, seq, seq)
print("Mapping List : " + str(tuple(map_list)))
# for x in map_list:
# 	print(x)

# squares X**2
squares = [x**2 for x in range(10)]
# squares = (x**2 for x in range(10))  then str(tuple(squares))
print("Squares (x_value**2): " + str(squares))

a = lambda x : x**2
squares_lambda = [ a(x) for x in range(10)]

squares_map = list(map(a, range(10)))
print(squares_map)
# squares = (x**2 for x in range(10))  then str(tuple(squares))
print("Squares (x_value**2): " + str(squares_lambda))


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
  	pass
  print(x)


dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
  
print(list(map(lambda x : x['name'], dict_a)))

ab = [1, 2, 3, 4, 5, 6]
res = filter(lambda x : x % 2 == 0, ab)
print(list(res))