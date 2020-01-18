"""
Main module with game mechanics
"""
import random
import exceptions
import settings


class Player:
    """Main class"""

    def __init__(self, name):
        self.name = name
        self.lives = settings.LIVES
        self.score = 0

    @staticmethod
    def fight(attack, defense):
        """Round result return"""
        if attack == defense:
            return 0

        if settings.ATTACK.get(attack) == defense:
            return 1

        return -1

    def attack(self, enemy_obj):
        """
        Player attacks
        :param enemy_obj: Enemy
        """
        print(self.name + " attacks: ")
        # We ask the user to enter from 1 to 3
        while True:
            print("If you selected ROBBER - enter 1, if WARRIOR - enter 2, if WIZARD - enter 3.")
            your_attack = int(input())
            if your_attack in [settings.ROBBER, settings.WARRIOR, settings.WIZARD]:
                break

        enemy_attack = Enemy.select_attack()
        print(f"The enemy - {enemy_attack}")

        result = Player.fight(your_attack, enemy_attack)
        # Get the result of the battle
        if result == 0:
            print("It's a draw!")
        elif result == 1:
            enemy_obj.decrease_lives()
            print("You attacked successfully!")
            print(f"The enemy has - {enemy_obj.lives} lives.")
        elif result == -1:
            self.decrease_lives()
            print("You missed!")
            print(f"{self.name} has - {self.lives} lives.")

    def defense(self, enemy_obj):
        """
        Player defenses
        :param enemy_obj: Enemy
        """
        print(f"{self.name} defends herself: ")
        # We ask the user to enter from 1 to 3
        while True:
            print("If you selected ROBBER - enter 1, if WARRIOR - enter 2, if WIZARD - enter 3.")
            your_attack = int(input())
            if (your_attack in [settings.ROBBER, settings.WARRIOR, settings.WIZARD]):
                break

        enemy_attack = Enemy.select_attack()
        print(f"The enemy - {enemy_attack}")

        result = Player.fight(enemy_attack, your_attack)
        # Get the result of the battle
        if result == 0:
            print("It's a draw!")
        elif result == 1:
            self.decrease_lives()
            print("You lose.")
            print(f"{self.name} has - {self.lives} lives.")
        elif result == -1:
            enemy_obj.decrease_lives()
            print("You won!")
            print(f"The enemy has - {enemy_obj.lives} lives.")

    def decrease_lives(self):
        """
        If player lost battle then reduce his lives
        :return: int Player's lives
        """
        # Raises a GameOver exception
        self.lives -= 1
        if self.lives == 0:
            print('Your Game is Over')
            print('Your total score is ', self.score)
            exceptions.GameOver.save_result(self.name, self.score)
            raise exceptions.GameOver()
        return self.lives


class Enemy:
    """class Enemy"""

    def __init__(self, level):
        self.lives = self.level = level

    @staticmethod
    def select_attack():
        """
        Returns a random number from 1 to 3
        :return: int
        """
        return random.choice([settings.ROBBER, settings.WARRIOR, settings.WIZARD])

    def decrease_lives(self):
        """
        If Enemy lost battle then reduce his lives
        :return: int Enemy's lives
        """
        # Reduces the number of lives.
        self.lives -= 1
        if self.lives == 0:
            raise exceptions.EnemyDown()
