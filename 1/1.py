#!/usr/bin/env python3

#https://adventofcode.com/2020/day/1/

def input():
	f = open("input.txt", "r")
	numbers = []
	for x in f:
		numbers.append(int(x))
	return numbers

def find2(numbers):
	num = 2020-numbers[0]
	if num in numbers:
		return num, numbers[0]
	else:
		numbers.pop(0)
		return find2(numbers)

def find3(numbers):
	for x in numbers:
		for y in numbers:
			if 2020-(x+y) in numbers:
				return x, y, 2020-(x+y)



#find TWO entries that sum to 2020 and then multiply those two numbers together.
x, y = find2(input())
answer = x*y
print(answer)


#find THREE entries that sum to 2020 and then multiply those two numbers together.
x, y, z = find3(input())
answer = x*y*z
print(answer)



