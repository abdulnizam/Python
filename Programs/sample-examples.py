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