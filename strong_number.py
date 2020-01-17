
#Script: Strong Number 
#Written By: knowledgeless


#find multiple strong numbers from a range
def multiplestrong():
	try:
		start = int(input("Enter starting number: "))
		end = int(input("Enter end number: "))
		print("-"*50)
		for k in range(start, end+1): #getting range from user
			user = k
			sum = 0
			for i in range(len(str(k))):
				result = 1
				reminder = k%10
				k = int(k/10)
				for j in range(1,reminder+1):
					result=result*j		#calculating factorial result of the reminder value
				sum = sum+result	#adding all factorial 
			if sum == user:		#checking strong number
				print("\t",user, "is a Strong Number")
			else:
				print("\t",user, "is not a Strong Number")
		print("-"*50)
	except ValueError:		#Error handling
		print("ValueError: Enter integer number only!")

#check a number is strong or not		
def checkstrong():
	try:
		user = int(input("\tEnter your value: "))
		check = user
		sum = 0
		for i in range(len(str(user))):
			result = 1
			reminder = user%10		#Getting reminder 
			user = int(user/10)
			for j in range(1,reminder+1):
				result*=j		#calculating factorial result of the reminder value
			sum += result		#adding all factorial
		if sum == check:		#checking strong number
			print("\n\t",check, "is a strong number\n")
		else:
			print("\n\t",check, "is not a strong number\n")
	except ValueError:		#Error handling
		print("ValueError: Enter integer number!")

# Showing option to use function separately
print('''
	\t  ---Choose an option---
	1 => Find multiple strong number in a range
	2 => Check your value is a strong number or not
	''')

try:
	value = int(input("\tSelect option: "))	#asking user to select an option
	if value ==1:
		multiplestrong()	#calling multiplestrong function
	elif value ==2:
		checkstrong()		#calling checkstrong function
	else:
		print("Choose between option 1 & 2")
except ValueError:		#Error handling
	print("ValueError: Choose an option using integer number!")