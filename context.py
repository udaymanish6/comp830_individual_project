import sys

question_dict = {
    "Welcome to the Game!Think of a design pattern and answer these following yes/no questions: Ready? ":
        ["Does it provide the object creation mechanism that enhance the flexibilities of the existing code? "],
    "Does it provide the object creation mechanism that enhance the flexibilities of the existing code? ":
        ["Does it ensure you have at most one instance of a class in your application? ",
         "Is it responsible for how one class communicates with others? "],
    "Does it ensure you have at most one instance of a class in your application? ":
        ["Is it singleton pattern? ", "Is it builder Pattern? "],
    "Is it responsible for how one class communicates with others? ":
        ["Does it provide a mechanism to the context to change its behavior? ",
         "Does it explain how to assemble objects and classes into a larger structure and simplifies a structure by "
         "identifying the relationships? "],
    "Does it provide a mechanism to the context to change its behavior? ": ["Is changing behavior built into its scheme?",
                            "Does it allow a group of objects to be notified when some state changes? "],
    "Is changing behavior built into its scheme? ": ["Is it state pattern? ", "Is it strategy pattern? "],
    "Does it allow a group of objects to be notified when some state changes? ": ["Is it observer pattern? ",
                                                                                  "Is it command pattern? "],
    "Does it explain how to assemble objects and classes into a larger structure and simplifies a structure by "
    "identifying the relationships? ": ["Does it attach additional behavior to an object dynamically at run-time? ", "end"],
    "Does it attach additional behavior to an object dynamically at run-time? ": ["Is it decorator pattern? ",
                                                                                  "Is it adapter pattern? "]
}
questions_restart = [
    "Wohooo! I guessed it! Try again?",
"Ooops! Something went wront! Try again?"
]




class Question:
    def __init__(self, game, answer) -> None:
        self.game = game
        self.answer = answer

        self.current_question = self.game.startGame()

    def showQuestion(self):
        answer = input(self.current_question).lower()

        while answer != "yes" and answer != "no":
            answer = input(self.current_question).lower()

        try:
            if question_dict[self.current_question][1] == "end" and answer == "no":
                print(questions_restart[1])
                return self.game.restartGame()
        except:
            pass

        if self.current_question == list(question_dict)[0] and answer == "no":
            self.game.endGame()
        elif self.checkLast():
            if answer == "yes":
                print(questions_restart[0])
            else:
                print(questions_restart[1])
            self.current_question = self.game.restartGame()
        else:
            if answer == "yes":
                self.current_question = self.answer.answerYes(self.current_question)
            else:
                self.current_question = self.answer.answerNo(self.current_question)

    def checkLast(self) -> bool:
        if "is it" in self.current_question.lower() and "pattern" in self.current_question.lower():
            return True
        return False