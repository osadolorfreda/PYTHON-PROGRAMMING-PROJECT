class Question:
    def __init__(self, question_text, answers):
        self.question_text = question_text
        self.answers = answers
        self.prompt = prompt

Question=[
    Question("How many people are there?", [1, 2, 3, 4, 5]),
    Question("how many programming language do we have?",)
    Question("which language is used for web development?",
             ["Python", "Java"])
    Question("which language is used for andriod development?",)
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.question_text)
        print(question.answers)
    