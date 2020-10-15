#defining the main function of the program
def main():

	i = 0               #setting integer to 0
	x = 119.0           #declaring the x float

	for i in range(120):    #loop i from 0 to 119, inclusive
		if((i%2)==0):       #if i is even
			x += 3.         # add 3 to x
		else:               #if i is odd
			x -=5.          #subtract 5 from x

	s = "%3.2e" % x         #make a string containing x with
							#sci. notation w/ 2 decimal places

	print(s)				#prints s to the screen

#rest of program continues
if __name__== "__main__": #if the main() function exists, run it
	main()
