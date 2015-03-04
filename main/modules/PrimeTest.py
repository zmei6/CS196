class Prime(object):
	def checkPrime(self, num):
		b = (int)(num**(0.5)+1)
		alist = range(2,b)
		isPrime = True
		for a in alist:
			if (num%a==0):
				isPrime=False
				break
		if(isPrime==True):
			return ("%d is a prime number." %num)
		else:
			return ("%d is not a prime number." %num)

if __name__ == '__main__':
	test = Prime()
	print test.checkPrime(49)
#		num = int(raw_input("Enter a Number: "))
#	alist = range(2, num)
#	isPrime = True
#	for a in alist:
#		if (num%a)==0:
#			isPrime=False
#			break
#	if (isPrime==True):
#		print ("%d is a prime number." %num)
#	else:
#		print ("%d is not a prime number." %num)