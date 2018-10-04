#!/usr/bin/env python


class Solution:

	def __new__(self, nr_movies, priorities, start_times):
		#
		# Some work here; return type and arguments should be according to the problem's requirements
		#
		movies_list_hour = ""
		priorities_time_list = {}
		
		start_times_list = start_times
		
		for i in range(nr_movies):
			priorities_time_list[start_times[i]] = priorities[i]
		
		start_times_list.sort()

		sorted_list = [ ]

		# for key in sorted(priorities_time_list.iterkeys()):
  #   		# print "%s: %s" % (key, mydict[key]) 
  #   		sorted_list[priorities_time_list[key]] = priorities_time_list[key]


		# priorities.sort()

		# return priorities
		


		for x in range(0, nr_movies):

			previous_val = '';

			sorted_list.append(start_times_list[x])

			current_val = start_times_list[x]

			# future_val = start_times_list[x+(0 if x+1 == nr_movies else 1)]

			future_val = start_times_list[x+[1, 0][x+1 == nr_movies]]

			diff = future_val - current_val

			if diff >= 2:
				print(current_val)

			# print(str(current_val)+'cc')
			# print(str(future_val)+'ff')


			previous_val = current_val

			
			# add = 1
			# if x == nr_movies:
			# 	return movies_list_hour
			
			# if x+1 == nr_movies:
			# 	add = 0 

			# if x != 0:
			# 	movies_list_hour += ','

			# val = start_times_list[x+add] - start_times_list[x] 

			# if val <= 0:
			# 	movies_list_hour += str(start_times_list[x] )

			# if priorities_time_list[start_times_list[x]] >


			
			# if start_times_list[x]+2 > start_times_list[x+add]:
			# 	# list_set.append( start_time_list[x] )
			# 	movies_list_hour += str(start_times_list[x] )

			# movies_list_hour += str(x)




			
		return sorted_list



if __name__ == '__main__':

	solutions = Solution(10,[9,2,10,4,5,1,9,3,6,7],[8,10,11,13,14,15,17,19,20,21])

	print(solutions)


#input 

# 10, [9,2,10,4,5,1,9,3,6,7],[8,10,11,13,14,15,17,19,20,21]

# Expected Result:
# 8,11,13,15,17,19,21

# Input:
# 6,[6,2,3,5,2,7],[18,10,12,11,17,13]

# Expected Result:
# 11,13,18
