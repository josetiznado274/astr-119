import numpy as np 
import sys

#define a function that returns value
def expo(x):
	return np.exp(x)		#return the np e^x function

#define a subroutine that does not return
def show_expo(n):
	for i in range (n):
		print(expo(float(i)))	#call the expo function

#define a mian function
def main():
	n = 10 #provide a defualt function for n

	#check if there is a command line arguement provided
	if(len(sys.argv)>1):
		n = int(sys.argv[1])	#if an arguement was provided, use it for n

	show_expo(n)		#call the show_expo subroutine

#run the main function
if __name__ == "__main__":
	main()