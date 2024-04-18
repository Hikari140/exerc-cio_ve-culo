# Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. 
# No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.

from modelos.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas

    def __str__(self):
        return f'{self._marca} | {self._marca} | {self._ligado} | {self._portas}'