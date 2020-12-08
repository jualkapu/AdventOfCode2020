#!/usr/bin/env python3

#https://adventofcode.com/2020/day/8/

#Swaps instructions for of single entry.
def swap(instructions):
	if instructions[0] == 'jmp':
		instructions[0] = 'nop'
		return ' '.join(instructions)
	if instructions[0] == 'nop':
		instructions[0] = 'jmp'
	return ' '.join(instructions)

#Gets input data to iterable list
def getData():
	with open('input.txt') as f:
		return f.read().splitlines()

#Finds when we loop trough same item second time and returns position of that item and current value of acc
def q1(data):
	acc = 0
	i = 0
	while i < len(data):
		if data[i] == 'x':
			break
		instructions = data[i].split(' ')
		if instructions[0] == 'acc':
			acc += int(instructions[1])
			data[i] = 'x'
		if instructions[0] == 'jmp':
			data[i] = 'x'
			i += int(instructions[1])			
		else:
			i += 1
	return [acc, i]

#Brute force solution. On every occurence of "jmp" or "nop". Changes the values and tries with that input.
#Returns position of first item that loops to the end of the input list. Gets fresh input from input file after every loop.
def q2():
	data = getData()
	answers = []
	for i in range(len(data)):
		instructions = data[i].split(' ')
		data[i] = swap(instructions)
		answers = q1(data)
		if(answers[1]>= len(data)):
			break
		else:
			data[i] = swap(instructions)
		data = getData()
	return answers

data = getData()
answer1 = q1(data)
answer2 = q2()
print(answer1, answer2)