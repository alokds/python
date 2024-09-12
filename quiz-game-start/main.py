from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# for i in range(len(question_data)):
#     new_q = Question(question_data[i]['text'], question_data[i]['answer'])
#     question_bank.append(new_q)
# print(question_bank)

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print(f"You have completed the quiz!\n Your Final Score was: {quiz.score}/{quiz.question_number}")
