class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        answer = input(f" Q.{self.question_number + 1} {self.question_list[self.question_number].text} True/False:")
        if self.check_answer(answer):
            self.score +=1
            print(f"{self.score}/{self.question_number + 1}")
        else:
            print(f"{self.score}/{self.question_number + 1}")
        self.question_number += 1

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, answer):
        return self.question_list[self.question_number].answer.lower() == answer.lower()
