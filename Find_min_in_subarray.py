def indexOfMin (array, startIndex):
	minValue = array[startIndex]
	minIndex = startIndex
	
	for i in array[startIndex:]:
		print(i,array.index(i))
		if i < minValue:
			minIndex = array.index(i)
			minValue = i
				
	return minIndex

array = [18, 6, 66, 44, 9, 22, 14]
index = indexOfMin(array,2)

print ("The index of the minimum value of the subarray starting at index 2 is ", index, "."  )