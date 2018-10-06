#!/usr/bin/env python

import re 



class Solution:

	def __new__(self, p):
		nr_counts, nr_consonants, replaced = self.count_vowels_consonants(self, p)
		inversed = ''.join(c.lower() if c.isupper() else c.upper() for c in p)
		replaced_by_ = p.replace(' ' ,'-')
		combined_queries = str(nr_counts) + ' ' + str(nr_consonants) + '::' 
		combined_queries += str(self.reverse_words(inversed)) + '::' 
		combined_queries += str(replaced_by_ )+ '::' + str(replaced)
		return combined_queries

	def count_vowels_consonants(self, text):
		vowels_list = ['A', 'E', 'I', 'O', 'U']
		consonants = 0
		vowels = 0
		string = ''
		for character in text:
		  if character.isalpha():
		  	if character.upper() in vowels_list:
			  	vowels += 1
			  	string += 'pv'
		  	else:
		  		consonants += 1
		  string += character
		return (vowels, consonants, string)

	def reverse_words(word):
		list_string = word.split(' ')
		list_string.reverse()
		string = ' '.join(list_string) 
		return string	

if __name__ == '__main__':
	solutions = Solution('The iterator is just clutter')
	# solutions = Solution('The')
	print(solutions)