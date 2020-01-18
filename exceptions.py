"""
Module for exeptions
"""


class GameOver(Exception):
    """
    class GameOver
    """

    @staticmethod
    def save_result(name, score):
        """
        Save result into file
        :param name: str User name
        :param score: int User score
        :return: True if writing in file is ok
        """
        with open('scores.txt', 'a') as file:
            file.write(f"Name: {name}, Score: {score} \n")
            file.close()
        return True


# This function has no docstring, so it needs a `pass` statement.
class EnemyDown(Exception):
    pass
