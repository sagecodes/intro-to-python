import random

number = random.randint(1, 10)
guess_count = 1
guesses = 5

print("Guess the random number between 1 & 10. you have {} guesses!".format(guesses))

while True:
	guess = input()

	try:
		guess = int(guess)
	except:
		print("Thats not a whole number! Your guess must be a single digit between 1 & 10.")
        


	if guess == number:
		print("You got it! Great job!")
		break

	elif guess < number:
		print("Try something higher... you have {} guesses remaining!".format(guesses - guess_count))
		guess_count = guess_count + 1

	elif guess > number:
		print("Try something lower... you have {} guesses remaining!".format(guesses - guess_count))
		guess_count = guess_count + 1

	elif guess_count == guesses:
		print("Bummer! You are out of guesses... The number was {}".format(number))
		break