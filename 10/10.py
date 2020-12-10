#!/usr/bin/env python3

#https://adventofcode.com/2020/day/10/

def getData():
	numbers = [int(x) for x in open("input.txt", "r").read().splitlines()]
	numbers.append(max(numbers)+3) #end
	numbers.append(0) #start
	numbers.sort()
	return numbers

def q1(data):
	ones = 0
	threes = 0
	for x in range(0, len(data)-1):
		if data[x]+1 == data[x+1]:
			ones += 1
		if data[x]+3 == data[x+1]:
			threes += 1
	return ones*threes

data = getData()
answer1 = q1(data)
print(answer1)