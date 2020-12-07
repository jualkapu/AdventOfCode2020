#!/usr/bin/env python3

#https://adventofcode.com/2020/day/7/

bagDict = {}

def contains(bagColor, amount):
	total = 0
	for value in bagDict[bagColor]:
		if 'other' in value:
			return amount
		next_bag = value[2:]
		total += contains(next_bag, int(value[0]))
	return(total * amount) + amount

with open('input.txt') as f:
	data = f.read().splitlines()
	bagDict = {}

	for x in data:
		y = x.split(' bags contain ')
		y[1] = y[1].strip('.').replace(' bags', '').replace(' bag', '').split(', ')
		bagDict[y[0]] = y[1]

	#Checks which bags are parents of "shiny gold". Then finds parents of those bags and so on.
	colors = ['shiny gold']
	for i in colors:
		for x in bagDict:
			for y in bagDict[x]:
				if i in y:	
					colors.append(x)

	answer1 = len(set(colors))-1
	answer2 = contains("shiny gold", 1) -1
	print(answer1, answer2)






