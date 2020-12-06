#!/usr/bin/env python3

#https://adventofcode.com/2020/day/6/

answer1, answer2 = 0, 0
for x in open("input.txt").read().split('\n\n'):
	#For answer1: Counts occurences of different chars withi multiple lines
	letters = set(x.replace('\n', ''))
	answer1 += len(letters)

	#For answer2: Counts characters that appear on every line within single group
	passengers = len(x.split('\n'))
	for y in letters:
		if x.count(y) == passengers:
			answer2 += 1

print(answer1, answer2)