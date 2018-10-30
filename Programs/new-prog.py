#!/usr/bin/env python

class Solution:

	def __new__(self, n, m, movies):
		

		i = 0
		arr = []
		for x in range(n):
			arr.append(x)

			# x = x + 1
			# watch = []
			# if len(watch) == m:
			# 	return watch 
			# for j in movies:
			# 	print(str(j)+"+"+str(x))
			# 	if j == x:
			# 		watch.append(j)


		return arr






if __name__ == '__main__':
        string_to_morse = Solution(5,3,[4,4,5])
        print(string_to_morse)



#         Input
# 3
# 3
# [3,1,1]


# Output
# "2,1,0"


# EXAMPLE 2
# Input
# 5 
# 3
# [4,4,5]


# Output
# "3,0,4"