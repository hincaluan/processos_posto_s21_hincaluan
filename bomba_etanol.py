# Classe base
class BombaCombustivel:
    def __init__(self, tipo_combustivel, preco_por_litro, quantidade_litros):
        self.__tipo_combustivel = tipo_combustivel
        self.__preco_por_litro = preco_por_litro
        self.__quantidade_litros = quantidade_litros

    def abastecer_por_litro(self, litros):
        if litros <= self.__quantidade_litros:
            valor_total = litros * self.__preco_por_litro
            self.__quantidade_litros -= litros
            return valor_total
        else:
            raise ValueError("Quantidade de litros insuficiente.")

    def abastecer_por_valor(self, valor):
        litros = valor / self.__preco_por_litro
        if litros <= self.__quantidade_litros:
            self.__quantidade_litros -= litros
            return litros
        else:
            raise ValueError("Quantidade de litros insuficiente.")

    def get_quantidade_litros(self):
        return self.__quantidade_litros

# Classe para Bomba de Etanol
class BombaEtanol(BombaCombustivel):
    def __init__(self, quantidade_litros):
        super().__init__("Etanol", 4.50, quantidade_litros)  # Preço do etanol como exemplo

# Classe para Bomba de Gasolina
class BombaGasolina(BombaCombustivel):
    def __init__(self, quantidade_litros):
        super().__init__("Gasolina", 5.50, quantidade_litros)  # Preço da gasolina como exemplo

    def abastecer_por_valor_com_aditivo(self, valor):
        preco_aditivo = self.__preco_por_litro * 1.05  # Aumento de 5% para gasolina com aditivo
        litros = valor / preco_aditivo
        if litros <= self.get_quantidade_litros():
            self._BombaCombustivel__quantidade_litros -= litros  # Acesso ao atributo protegido
            return litros
        else:
            raise ValueError("Quantidade de litros insuficiente.")

# Exemplo de uso
et = BombaEtanol(100)
gs = BombaGasolina(100)

# Abastecer por litro
print("Abastecendo Etanol por litro:", et.abastecer_por_litro(20))  # Valor total

# Abastecer por valor
print("Abastecendo Gasolina por valor:", gs.abastecer_por_valor(20))

# Abastecer Gasolina com aditivo
print("Abastecendo Gasolina com aditivo por valor:", gs.abastecer_por_valor_com_aditivo(20))
