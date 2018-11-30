import random

number = random.randint(1, 10)
guess_count = 0
guesses = 5

print("Guess the random number between 1 & 10. you have {} guesses!".format(guesses))

while guess_count <= guesses:
	guess = int(input())

	if guess == number:
		print("You got it! Great job!")
		break

	elif guess < number:
	    guess_count = guess_count + 1
        print("Try something higher... you have {} guesses remaining!".format(guesses - guess_count))
		

	elif guess > number:
		guess_count = guess_count + 1
        print("Try something lower... you have {} guesses remaining!".format(guesses - guess_count))