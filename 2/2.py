#!/usr/bin/env python3

#https://adventofcode.com/2020/day/2/

#Get input to iterable format
def input():
	f = open("input.txt", "r")
	pw = []
	for x in f:
		pw.append(x.split(' '))
	return pw

#Finds values from input and checks if pw is valid according to given values
def countValids(pw):
	q1Amount = 0
	q2Amount = 0
	for x in pw:
		minimum = int(x[0].split('-')[0])
		maximum = int(x[0].split('-')[1])
		letter = x[1][0]

		#Check according to question 1
		if minimum <= x[2].count(letter) <= maximum:
			q1Amount += 1

		#Check according to question 2
		if (x[2][minimum-1] == letter) is not (x[2][maximum-1] == letter):
			q2Amount += 1

	return q1Amount, q2Amount

answer1, answer2 = countValids(input())
print(answer1, answer2)

