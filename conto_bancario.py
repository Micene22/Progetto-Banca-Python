# File: conto.py

class ContoBancario:
    def __init__(self, nome_titolare, id_conto):
        self.nome = nome_titolare
        self.id= id_conto
        self.saldo = 0.0

    # In futuro qui aggiungeremo:
    # def deposita(self, importo): ...
    # def ritira(self, importo): ...