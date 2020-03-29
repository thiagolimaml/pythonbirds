class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__=='__main__':
    renzo = Pessoa(nome='Renzo')
    lima = Pessoa(renzo, nome='Lima')
    print(Pessoa.cumprimentar(lima))
    print(id(lima))
    print(lima.cumprimentar())
    print(lima.nome)
    print(lima.idade)
    for filho in lima.filhos:
        print(filho.nome)
