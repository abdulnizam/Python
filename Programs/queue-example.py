#!/bin/python

from collections import deque



queue_list = deque(["abc", "bcd", "cde"]);
queue_list.append("def");
# full list
print("Full List : " + str(queue_list))
# pop left
print("Popped Value Left : " + queue_list.popleft()) # popped value
# after pop left
print("After Pop Left (list.popleft()): " + str(queue_list))
# pop right
print("Popped Value Right : " + queue_list.pop()) # popped value
# after pop right
print("After Pop Right (list.pop()): " + str(queue_list))
