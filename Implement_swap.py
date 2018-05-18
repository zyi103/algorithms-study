def swap(array, firstIndex, secondIndex):
	x = array[firstIndex] 
	array[firstIndex] = array[secondIndex]
	array[secondIndex] = x

array = [7,9,4]
swap(array,0,1)
swap(array,0,2)

print (array)