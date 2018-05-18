def swap (array, firstIndex, secondIndex):
	x = array[firstIndex] 
	array[firstIndex] = array[secondIndex]
	array[secondIndex] = x

def checkSort (array):
	for idx, val in enumerate(array):
		if idx == len(array)-1:
			print ("The sort answer:", array)
			return True
		elif val > array[idx+1]:
			return False
		
def adjacentSort (array):
	while checkSort(array) != True:
		for idx, val in enumerate(array):
			if idx == len(array)-1:
				break
			elif val > array[idx + 1]:
				print(array)
				swap(array, idx, idx+1)
				

array = [22, 11, 99, 88, 9]

adjacentSort(array)
