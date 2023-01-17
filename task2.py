def mystery(n):
	# Return mystery result
	return ((10**(n+1))*(9 * n - 1)+10)/(9**3)-n*(n + 1)/18

if __name__=='__main__':
    print('Please input a number')
    n = int(input())
    mystery(n)
    print(mystery(n))