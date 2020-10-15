import numpy as np      #we use numpy for lots of things

def main():
	i = 0				#integers can declared with a number
	n = 10				#here is another integer
	x = 119.0			#floating point nums are declared with a "."

	#we can use numpy to declare arrays quickly

	y = np.zeros(n,dtype=float) #declares 10 zeros as floats using np

	# we can use for loops to iterate a vairable

	for i in range(n):			#i in range [0, n-1]
		y[i] = 2.0 * float(i) + 1.   #set y = 2i+1 as floats

	# we can alos simply iterate through a vairable
	for y_element in y:
		print(y_element)

#excute the main function
if __name__ == "__main__":
	main()