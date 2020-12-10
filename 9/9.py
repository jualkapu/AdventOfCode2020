#!/usr/bin/env python3

#https://adventofcode.com/2020/day/9/

def getData():
	f = open("input.txt", "r")
	numbers = []
	for x in f:
		numbers.append(int(x))
	return numbers

def findInvalid(data):
	for i in range(25,len(data)):
		prevNums = data[i-25:i]
		if not any(data[i] == x+y for x in prevNums for y in prevNums if x != y):
			invalid = data[i]
			break
	return invalid

def findNums(data, invalid):
	count = 0
	numbers = []
	for x in range(0, len(data)):
		for y in range(x, len(data)):
			count += data[y]
			numbers.append(data[y])
			if count == invalid:
				return numbers
			elif count >= invalid:
				break
		count = 0
		numbers = []

data = getData()
answer1 = findInvalid(data)
answer2list = findNums(data, answer1)
answer2 = min(answer2list)+max(answer2list)
print(answer1, answer2)