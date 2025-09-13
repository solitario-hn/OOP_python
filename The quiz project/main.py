from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)  # this will save new questions as new objects(instances) every time looping happens into the list.

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print(f"Congratulation you've completed the quiz\nYour final Score:{quiz.score}/{quiz.question_number}")



