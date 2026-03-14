import random

# 20 Sep 2025
# guessing the number between 1-100 with 3 hints

class Game:
	def __init__(self):
		self.answer = random.randint(1,100)
		self.guessing = 0

	def game_logic(self):

		while True:

			try:
				print(self.answer)
				num_guess = input("Enter your guessing number: ") # input statement return string
				num_guess = int(num_guess)
			
				if num_guess > self.answer:
					print(f"Your guessing is over. Guess again!")
					
				if num_guess < self.answer:
					print(f"Your guessing is less than the answer. Guess again!")
				self.guessing += 1

				print(f"guessing count {self.guessing}!!!")
				print()

				if num_guess == self.answer:
					print("Congradtulations You won!!")
					break

				if self.guessing == 3:
					print("You lose!!!")
					break

			except TypeError:
				print("input number only")
			except ValueError:
				print("input number only")

game = Game()

if __name__ == "__main__":
	game.game_logic()