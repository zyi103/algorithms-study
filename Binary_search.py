primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
		41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
lookupnum = int(input("Give me a Prime!"))
		

def doSearch(ilist,i):
	min = 0
	max = len(primes) - 1
	guess = 0
	while primes[guess] != lookupnum:
		guess = int((max+min)/2)
		print(guess,primes[guess])
		if max < min:
			print("your input number is not a PRIME!")
			break
		elif primes[guess] < lookupnum:
			print("guess is too small.","Min:",min,"Max:",max,"guess:",guess)
			min = guess + 1
		elif primes[guess] > lookupnum:
			print("guess is too big.","Min:",min,"Max:",max,"guess:",guess)
			max = guess - 1
		else:
			print("you got it! It's",primes[guess])
			break
	return -1
	
doSearch(primes,lookupnum)
