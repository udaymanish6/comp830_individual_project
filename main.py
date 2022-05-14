import context
from context import *


class Game:
    def __init__(self, que) -> None:
        self.que = que

    def startGame(self):
        current_question = list(self.que)[0]
        return current_question

    def restartGame(self):
        a = input().lower()
        if a != "yes":
            self.endGame()
        else:
            return self.startGame()

    def endGame(self):
        sys.exit()

    def answerYes(self, current_question):
        current_question = self.que[current_question][0]

        return current_question

    def answerNo(self, current_question):
        current_question = self.que[current_question][1]

        return current_question


question = Question(Game(question_dict), Game(question_dict))

while True:
    question.showQuestion()




