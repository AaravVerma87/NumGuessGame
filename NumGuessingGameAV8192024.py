import random, math

lower = int(input("Enter the lower limit of the range: "))
upper = int(input("Enter the upper limit of the range: "))

x = random.randint(lower, upper)
total_chances = math.ceil(math.log(upper - lower + 1, 2))
print("\n\tYou've only", total_chances, "chances to guess the integer!\n")

count = 0
flag = False

while count < total_chances:
	count += 1

	guess = int(input("Guess a number: "))

	if x == guess:
		print("Congratulations you did it in", count, "tries!")
		flag = True
		break
	
	elif x > guess:
		print("You guessed too small!")
		
	elif x < guess:
		print("You guessed too high!")


if not flag:
	print("\nThe number is %d" % x)
	print("\tBetter luck next time!")
