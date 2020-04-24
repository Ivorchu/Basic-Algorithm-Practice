'''
MIT License

Copyright (c) 2020 Ivor Chu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

LST = [5,7,2,3,4,9,8,1,6] #Unsorted List Given
LST2 = [1,2,3,4,5,6,7,8,9] #Sorted List Given
results = ""
score = 0

#Modify the functions below

#Sequential Search
#Find the index of the number 9 in the list
def Sequential_Search(lst):

	for i in lst:
		if i == 9:
			return lst.index(i)


#Binary Search
#Find the index of the given number(not shown) in a sorted list
def Binary_Search(lst, num):

	while True:
		
	return


#Breadth First Search
#Sort the given list from small to large
def Breadth_First_Search(lst):

	return


#Depth First Search
#Sort the given list from small to large
def Depth_First_Search(lst):

	return


#Euclidean algorithm
#Find the GCD of the given number(not shown)
def Euclidean_Algorithm(num1, num2):

	return


#Bubble Sort
#Sort the given list from small to large
def Bubble_Sort(lst):

	return


#Insertion Sort
#Sort the given list from small to large
def Insertion_Sort(lst):

	return


#Selection Sort
#Sort the given list from small to large
def Selection_Sort(lst):

	return


#Merge Sort
#Sort the given list from small to large
def Merge_Sort(lst):

	return


#End of functions
#Run to see the results
#Try not to peak below

class Wrong_Answer(Exception):
	def __init__(self, *args):
		if args:
			self.message = args[0]
		else:
			self.message = None

	def __str__(self):
		if self.message:
			return "Wrong_Answer, {0} ".format(self.message)
		else:
			return "Wrong_Answer"

try:
	if Sequential_Search(LST) != 5:
		raise Wrong_Answer
	else:
		print("Sequential_Search:\ncorrect\n")
		results += "Sequential_Search: Pass\n"
		score += 1

except Exception as e:
	print("Sequential_Search:")
	print(e)
	print()
	results += "Sequential_Search: Fail\n"

try:
	if Sequential_Search(LST2) != 4:
		raise Wrong_Answer
	else:
		print("Binary_Search:\ncorrect\n")
		results += "Binary_Search: Pass\n"
		score += 1

except Exception as e:
	print("Binary_Search:")
	print(e)
	print()
	results += "Binary_Search: Fail\n"

try:
	if Breadth_First_Search(LST) != [1,2,3,4,5,6,7,8,9]:
		raise Wrong_Answer
	else:
		print("Breadth_First_Search:\ncorrect\n")
		results += "Breadth_First_Search: Pass\n"
		score += 1

except Exception as e:
	print("Breadth_First_Search:")
	print(e)
	print()
	results += "Breadth_First_Search: Fail\n"

try:
	if Depth_First_Search(LST) != [1,2,3,4,5,6,7,8,9]:
		raise Wrong_Answer
	else:
		print("Depth_First_Search:\ncorrect\n")
		results += "Depth_First_Search: Pass\n"
		score += 1
	
except Exception as e:
	print("Depth_First_Search:")
	print(e)
	print()
	results += "Depth_First_Search: Fail\n"
	
try:
	if Euclidean_Algorithm(165, 297) != 33:
		raise Wrong_Answer
	else:
		print("Euclidean_Algorithm:\ncorrect\n")
		results += "Euclidean_Algorithm: Pass\n"
		score += 1
	
except Exception as e:
	print("Euclidean_Algorithm:")
	print(e)
	print()
	results += "Euclidean_Algorithm: Fail\n"
	
try:
	if Bubble_Sort(LST) != [1,2,3,4,5,6,7,8,9]:
		raise Wrong_Answer
	else:
		print("Bubble_Sort:\ncorrect\n")
		results += "Bubble_Sort: Pass\n"
		score += 1
	
except Exception as e:
	print("Bubble_Sort:")
	print(e)
	print()
	results += "Bubble_Sort: Fail\n"
	
try:
	if Insertion_Sort(LST) != [1,2,3,4,5,6,7,8,9]:
		raise Wrong_Answer
	else:
		print("Insertion_Sort:\ncorrect\n")
		results += "Insertion_Sort: Pass\n"
		score += 1
	
except Exception as e:
	print("Insertion_Sort:")
	print(e)
	print()
	results += "Insertion_Sort: Fail\n"

try:
	if Selection_Sort(LST) != [1,2,3,4,5,6,7,8,9]:
		raise Wrong_Answer
	else:
		print("Selection_Sort:\ncorrect\n")
		results += "Selection_Sort: Pass\n"
		score += 1
	
except Exception as e:
	print("Selection_Sort:")
	print(e)
	print()
	results += "Selection_Sort: Fail\n"

try:
	if Merge_Sort(LST) != [1,2,3,4,5,6,7,8,9]:
		raise Wrong_Answer
	else:
		print("Merge_Sort:\ncorrect\n")
		results += "Merge_Sort: Pass\n"
		score += 1

except Exception as e:
	print("Merge_Sort:")
	print(e)
	print()
	results += "Merge_Sort: Fail\n"

print()
print("Results:\n" + results)
print("Score: " + str(score) + "/8")