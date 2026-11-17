import requests
import html


class Question:
    def __init__(self, text, answer):
        self.question_text = text
        self.answer = answer

    def __str__(self):
        return self.question_text + ' [" + self.answer + "]'


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def load_quiz(self):
        response = requests.get(
            'https://opentdb.com/api.php?amount=5&type=boolean')
        data = response.json()
        results = data['results']
        for result in results:
            escaped_text = html.unescape(result['question'])
            q = Question(escaped_text, result['correct_answer'])
            self.questions.append(q)
            print(q)

    def run(self):
        for q in self.questions:
            print(q.question_text, end=' ')
            answer = input('T/F')
            if answer == 'T' and q.answer == 'True':
                self.score += 1
            elif answer == 'F' and q.answer == 'False':
                self.score += 1
            print(f"SCORE: {self.score}/5")


quiz = Quiz()
quiz.load_quiz()
quiz.run()
