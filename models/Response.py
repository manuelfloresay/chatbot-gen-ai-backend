class Response:
    def __init__(self, answer):
        self.answer = answer

    @property
    def answer(self):
        return self.answer
    
    @answer.setter
    def answer(self, value):
        self.answer = value