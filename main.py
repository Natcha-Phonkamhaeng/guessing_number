import random

# guessing the number between 1-100 with 3 hints

answer = random.randint(1,100) # generate random number between 1 to 100 (inclusive)
print(answer)
guessing = 0 # guessing the correct number limit 3 times

while True:

	num_guess = input("Enter your guessing number: ") # input statement return string
	num_guess = int(num_guess)

	if num_guess > answer:
		print(f"Your guessing is over. Guess again!")
		
	if num_guess < answer:
		print(f"Your guessing is less than the answer. Guess again!")
	guessing += 1

	print(f"guessing count {guessing}!!!")
	print()

	if num_guess == answer:
		print("Congradtulations You won!!")
		break

	if guessing == 3:
		print("You lose!!!")
		break
