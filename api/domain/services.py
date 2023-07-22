# paradigms/domain/services.py

class GerenciadorEntrevistas:
    def criar_entrevista(self, especialista, data, respostas):
        # Lógica para criar uma nova entrevista
        entrevista = Entrevista(None, especialista, data, respostas)
        # Outras operações de negócio...
        return entrevista

    def obter_entrevista_por_id(self, entrevista_id):
        # Lógica para obter uma entrevista pelo ID
        entrevista = # Consultar o banco de dados ou outra fonte de dados
        # Outras operações de negócio...
        return entrevista

    def atualizar_entrevista(self, entrevista, respostas):
        # Lógica para atualizar uma entrevista existente
        entrevista.respostas = respostas
        # Outras operações de negócio...
        return entrevista

    def excluir_entrevista(self, entrevista):
        # Lógica para excluir uma entrevista
        # Outras operações de negócio...
        return
