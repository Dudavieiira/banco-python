class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): # self: referencia a instancia atual da classe
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self): #para definir um metodo coloca a apalavra reservada def da um nome ao metodo e dentro dele define pelo menos um argumento (self)
        print("Plim Plim..")
    
    def parar(self): #self é uma convençao, mas poderia ser qualquer nome, mas é uma convenção usar self
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Correndo...")
        print("Bicicleta em movimento!")

    # def get_cor(self):
    #     return self.cor

    # def __str__(self):
    #     return f"Bicicleta(cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor})"
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f' {chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        # # __str__ é um método especial que define como a instância da classe deve ser representada como string.
        # # __class__.__name__ retorna o nome da classe da instância atual.
        # # self.__dict__ é um dicionário que contém os atributos da instância.
        # # items() retorna uma lista de tuplas (chave, valor) para cada atributo.
        # # join() junta todos os elementos da lista em uma string, separados por ", ".

b1 = Bicicleta("vermelho", "caloi", 2022, 600)
b1.buzinar()
b1.correr() 
b1.parar()

b2 = Bicicleta("vermelho", "caloi", 2022, 600)
print (b2)
b2.correr()