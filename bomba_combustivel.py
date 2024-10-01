class BombaCombustivel:
    def __init__(self, valor_litro, quantidade_disponivel):
        self.__valor_litro = valor_litro
        self.__quantidade_disponivel = quantidade_disponivel

    def get_valor_litro(self):
        return self.__valor_litro
    
    def get_quantidade_disponivel(self):
        return self.__quantidade_disponivel

    # Para aluno implementar
    def retirar_litros(self, litros):
        pass

    def abastecer_por_valor(self, valor):
        litros = valor / self.valor_litro
        if litros > self.quantidade_disponivel:
            return -1
        self.quantidade_disponivel -= litros
        return litros

    def abastecer_por_litro(self, litros):
        if litros > self.quantidade_disponivel:
            return -1
        valor = litros * self.valor_litro
        self.quantidade_disponivel -= litros
        return valor
