from modelos.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo

    def __str__(self):
        return f'{self._marca} | {self._marca} | {self._ligado} | {self._tipo}'