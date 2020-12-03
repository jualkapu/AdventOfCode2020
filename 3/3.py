#!/usr/bin/env python3

#https://adventofcode.com/2020/day/3/

#Get input to list and remove linebreaks 
def input():
	f = open("input.txt", "r")
	lines = []
	for x in f:
		lines.append(x.rstrip("\n"))
	return lines

#Checks if there is a '#' in the current position. a = steps horizontally, b = steps vertically
def countTrees(lines, a, b):
	amount = 0
	posX = 0
	posY = 0

	#If not at the end of input or end of line; check if there is a tree in position.
	#Then adjust coordinates according to given pattern
	while posY < len(lines):
		if posX >= len(lines[0]):
			posX = posX - len(lines[0])
		if lines[posY][posX] == '#':
			amount += 1

		posX+=a
		posY+=b

	return amount

#Given movement patterns.
patterns = ((1,1),(3,1),(5,1),(7,1),(1,2))
lines = input()

answer = 1
for x in patterns:
	answer *= countTrees(lines,x[0],x[1])

print(answer)

