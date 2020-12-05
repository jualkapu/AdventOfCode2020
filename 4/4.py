#!/usr/bin/env python3

#Gets input to iterable list. Every entry in input is separated by empty line. This is not the best way to do this and should be fixed
def input():
    f = open("input.txt", "r")
    passports =''
    for line in f:
        if len(line)>1:
            passports += line.strip()+' '
        else:
            passports+=line
    return passports.split('\n')

#Counts passports that have all posiible fields OR all except 'cid'-field
def countPart1(passports):
    amount = 0
    for passPort in passports:
        fields = passPort.split()
        #True if there are 8 fields in passport data OR if there is 7 fields and none of them is 'cid'
        if (len(fields)==8) or (len(fields)==7 and all('cid' not in field for field in fields)):
            amount += 1
    return amount

#Returns a list of passports where fields and values are stored in dictionary
def fieldsToDict(passports):
    passportsAsDict = []
    for passport in passports:
        temp = {}
        fields = passport.split()
        for field in fields:
            value = field.split(':')
            temp[value[0]] = value[1]
        passportsAsDict.append(temp)
    return passportsAsDict

#Checks if passport fields are in given range of values. Counts passports that have all correct values
def countPart2(passports):
    amount = 0
    for fields in passports:
        tests = 0
        if len(fields)==8 or (len(fields)==7 and all('cid' not in i for i in fields)):
            if 1920<=int(fields['byr'])<=2002:
                tests+=1
            if 2010<=int(fields['iyr'])<=2020:
                tests+=1
            if 2020<=int(fields['eyr'])<=2030:
                tests+=1
            if 'hgt' in fields:
                if 'cm' in fields['hgt'] and 150 <= int(fields['hgt'][:-2]) <=193:
                    tests+=1
                if 'in' in fields['hgt'] and 59 <= int(fields['hgt'][:-2]) <=76:
                    tests+=1
            if len(fields['hcl'])==7 and all(i in '#abcdef1234567890' for i in fields['hcl']):
                tests+=1
            if fields['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                tests+=1
            if len(fields['pid']) == 9 and all(i.isdigit() for i in fields['pid']):
                tests+=1
            if tests==7:
                amount+=1
    return amount


answer1 = countPart1(input())
answer2 = countPart2(fieldsToDict(input()))

print(answer1, answer2)