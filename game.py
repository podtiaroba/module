"""Main executable file where the game starts"""
import exceptions
import models


def play():
    """Beginning of the game"""
    start = input("To start the game enter 'start': ")
    if start != 'start':
        print('You entered incorrect data!')
        play()
    else:
        print("Enter your name, please: ")
        name = input()
        player = models.Player(name)
        level = 1
        enemy = models.Enemy(level)
        while True:
            try:
                player.attack(enemy)
                player.defense(enemy)
            except exceptions.EnemyDown:
                level += 1
                player.score += 5
                print("The enemy is defeated, increase the level to: ", level)
                enemy = models.Enemy(level)


def main():
    """Output Results"""
    try:
        play()
    except exceptions.GameOver:
        print("Game over.")
    finally:
        print("Good bye!")


if __name__ == "__main__":
    main()
