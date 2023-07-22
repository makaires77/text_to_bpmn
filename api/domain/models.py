# paradigms/domain/models.py

class Entrevista:
    def __init__(self, id, especialista, data, respostas):
        self.id = id
        self.especialista = especialista
        self.data = data
        self.respostas = respostas

class Resposta:
    def __init__(self, pergunta, resposta):
        self.pergunta = pergunta
        self.resposta = resposta
