#import modules
import random
import math

# taking Inputs
lower = int(input("Enter Lower number limit:- "))
upper = int(input("Enter Upper number limit:- "))

# generating random number between
# the lower number and upper number limit

x = random.randint(lower, upper)
print("\n\tYou've only ",
	round(math.log(upper - lower + 1, 10 )),
	" chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

while count < math.log(upper - lower + 1, 2):
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	# Condition testing
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		# to break the loop
		break
	elif x > guess:
		print("Guess more than", guess)
	elif x < guess:
		print("Guess less than", guess )


if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")

