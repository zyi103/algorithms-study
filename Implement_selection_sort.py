def swap (array, firstIndex, secondIndex):
	x = array[firstIndex] 
	array[firstIndex] = array[secondIndex]
	array[secondIndex] = x
	
def indexOfMin (array, startIndex):
	minValue = array[startIndex]
	minIndex = startIndex
	
	for i in array[startIndex:]:
		if i < minValue:
			minIndex = array.index(i)
			minValue = i
				
	return minIndex
	
def selectionSort (array):
	for idx, val in enumerate(array):
		print (array)
		swap(array, idx, indexOfMin(array, idx))

	
array = [22, 11, 99, 88, 9, 7, 42]
selectionSort(array)

print("Array after sorting:  ", array)
		