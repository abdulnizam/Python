#!/bin/python

from collections import deque



queue_list = deque(["abc", "bcd", "cde"]);
queue_list.append("def");
# full list
print("Full List : " + str(queue_list))
# pop left
queue_list.popleft()
# after pop left
print("After Pop Left (list.popleft()): " + str(queue_list))
# pop right
queue_list.pop()
# after pop right
print("After Pop Right (list.pop()): " + str(queue_list))
