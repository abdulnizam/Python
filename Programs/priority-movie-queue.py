#!/usr/bin/env python


class Solution:

	def __new__(self, nr_movies, priorities, start_times):
	
		movies_list_hour = ""
		priorities_time_list = {}
		
		start_times_list = start_times
		
		for i in range(nr_movies):
			priorities_time_list[start_times[i]] = priorities[i]
		
		start_times_list.sort()
		filtered = []
		unfiltered = []
		previous_val = 0;

		for x in range(0, nr_movies):
			current_val = start_times_list[x]
			if current_val != previous_val:
				# future_val = start_times_list[x+(0 if x+1 == nr_movies else 1)]
				future_val = start_times_list[x+[1, 0][x+1 == nr_movies]]
				diff = current_val - previous_val
				future_diff = current_val - future_val
				if diff >= 2:
					if previous_val in filtered or future_diff >= 2:
						filtered.append(current_val)
						previous_val = current_val
					else:
						if priorities_time_list[current_val] > priorities_time_list[future_val]:
							if priorities_time_list[current_val] == priorities_time_list[future_val]:
								filtered.append(future_val)
							else:
								filtered.append(current_val)
						else:
							filtered.append(future_val)
							previous_val = future_val
			
		return filtered

if __name__ == '__main__':

	solutions = Solution(10,[9,2,10,4,5,1,9,3,6,7],[8,10,11,13,14,15,17,19,20,21])
	# solutions = Solution(6,[6,2,3,5,2,7],[18,10,12,11,17,13])

	print(solutions)


#input 

# 10, [9,2,10,4,5,1,9,3,6,7],[8,10,11,13,14,15,17,19,20,21]

# Expected Result:
# 8,11,13,15,17,19,21

# Input:
# 6,[6,2,3,5,2,7],[18,10,12,11,17,13]

# Expected Result:
# 11,13,18
