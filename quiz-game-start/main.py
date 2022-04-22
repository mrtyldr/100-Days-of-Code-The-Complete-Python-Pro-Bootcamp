from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in range(0,(len(question_data["results"]))):
    question_bank.append(Question(question_data["results"][q]["question"], question_data["results"][q]["correct_answer"]))

q = QuizBrain(question_bank)
while q.still_has_questions():
    q.next_question()
