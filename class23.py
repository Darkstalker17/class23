'''Get rid of the duplicates
Outline:
First, create a dictionary that consists of - id, name, class and subject integration of students.
Then, write a program to retrieve unique entries and eliminate the rest.'''
'''myDictionary = {"name" : "John", "age" : 7, "class" : 2}
print(myDictionary["name"])
myDictionary["gender"] = "boy"
print(myDictionary.items())
studentData = {"id1" : {"name" : "Sarah", "class" : 9, "Subject" : ["English, Math, Science"]},
               "id2" : {"name" : "Michael", "class" : 6, "Subject" : ["English, Coding, Science"]},
               "id3" : {"name" : "Roger", "class" : 8, "Subject" : ["English, French, Science"]},
               "id4" : {"name" : "Lily", "class" : 9, "Subject" : ["English, Math, Science"]},
               "id5" : {"name" : "Sarah", "class" : 9, "Subject" : ["English, Math, Science"]}}

result = {}
for key, value in studentData.items():
    if value not in result.values():
        result[key] = value
print(result)'''

'''Check the frequency
Outline:
Write a program to check the frequency of a value in a dictionary
{'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}.
'''
newDictionary = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print(newDictionary)
k = 1
result = 0
for j in newDictionary:
    if newDictionary[j] == k:
        result = result+1
print("Frequency of K is" ,result)

'''
Get the country code
Outline:
Write a program to return the country code for various countries. Here’s
a dictionary of different country codes
{'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}.
'''
cc = {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}
print(cc.get("India", "Country Not found"))
print(len(cc))