#!/usr/bin/env python3

#https://adventofcode.com/2020/day/5/

#Finds the highest seatID from input rows. Also returns a lsit of seatIDs for question 2
def highestSeatID(input, trans):
	highestSeatID = 0
	listOfSeatIDs = []
	for x in input:
		row = int(x[:-3].translate(trans), 2)
		column = int(x[-3:].translate(trans), 2)
		seatID = row*8+column
		listOfSeatIDs.append(seatID)
		if (seatID) > highestSeatID:
			highestSeatID = seatID
	return highestSeatID, listOfSeatIDs

#Sorts list and returns the missing number (seatID). Checks if item in list is equal to item before it + 1. 
def findMissingSeat(listOfSeatIDs):
	listOfSeatIDs.sort()
	for x in range(1, len(listOfSeatIDs)):
		if listOfSeatIDs[x]!=listOfSeatIDs[x-1]+1:
			return listOfSeatIDs[x]-1

input = open("input.txt", "r").read().splitlines()
trans = str.maketrans('FBLR', '0101')
answer1, listOfSeatIDs = highestSeatID(input, trans)
answer2 = findMissingSeat(listOfSeatIDs)
print(answer1, answer2)

