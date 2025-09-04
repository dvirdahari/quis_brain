from data import question_data
from model import Question
from quiz_brain import QuizBrain

q_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    q_bank.append(new_question)

quiz = QuizBrain(q_bank)

while quiz.still_has_question():
    quiz.next_question()


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


#TODO &quot FIX THE BUG