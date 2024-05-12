class Request:
    def __init__(self, question):
        self.question = question

    @property
    def question(self):
        return self.question
    
    @question.setter
    def question(self, value):
        self.question = value
