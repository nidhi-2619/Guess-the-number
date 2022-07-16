from quiz_brain import QuizBrain
from data import question_data
from question_model import Question

question_bank = []
# we are converting all the question data into object
for question in question_data:
    ques_text = question["text"]
    ques_answer = question["answer"]
    new_question = Question(ques_text, ques_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_have_question():
    quiz.next_question()
print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")