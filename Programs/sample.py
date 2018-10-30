# x = 10
# y = 15

# x = x + y
# y = x - y
# x = x - y

# # print(x)
# print(y)

# x = sum(n/2 for n in range(2, 6, 2))

# # print(x)

# i = 0

# while i<3:
# 	print(++i)
# 	i += 1
# 	print(i+1)


# print(list("hello"))

# bool1 = True
# bool2 = False
# bool3 = False

# if bool1 or bool2 and bool3:
# 	print(bool1)
# else:
# 	print(bool2)
# 	

# number = [ 1,2,3,4,5,1,2,3,4,5,0,1]

# print(len(set(number))/2)

# l = (1,2,5,6,4,3)
# print(l[int(-1/2):int(7/2)])

import random
import string

def gen_pass(length):  


    word_list = list(string.ascii_lowercase) 
    word_list.extend(string.digits)
    word_list.extend(string.punctuation)

    generatepassword = "".join([random.choice(word_list) for i in range(length)]) 
    print(word_list)
    print(generatepassword)
    print("The passwords consists of: {} Characters\n".format(length)) 

if __name__ == '__main__':

	gen_pass(8)