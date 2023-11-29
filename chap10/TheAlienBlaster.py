class Player:
	def blast(self, enemy):
		print("The player blast an enrmy.")
		enemy.die()
	
class Alien:
	def die(self):
		print("Good-bye, cruel universe.")

	
hero = Player()
invader = Alien()
hero.blast(invader)

