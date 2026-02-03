class Tamagotchi:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.vida_maxima = 100
        self.vida_atual = self.vida_maxima
        self.energia_maxima = 100
        self.energia_atual = self.energia_maxima
        self.status_acordado = True

    def brincar(self):
      if self.status_acordado:
        if self.energia_atual - 10 >= 0:
            self.energia_atual -= 10
            return f"O {self.nome} brincou"
        else:
            return "Não é possível brincar, energia insuficiente"
      else:
        return f"Não é possível brincar por que o {self.nome} ta dormindo"

    def dormir(self):
      if self.status_acordado:
        self.status_acordado = False
        if self.energia_atual + 25 < self.energia_maxima:
            self.energia_atual += 25
            return f"O {self.nome} dormiu"
        else:
            self.energia_atual = self.energia_maxima
            return f"O {self.nome} dormiu"
      else:
        return f"Não é possível dormir, por que o {self.nome} já está dormindo"
    
    def acordar(self):
      if not self.status_acordado:
        self.status_acordado = True
        return f"O {self.nome} acordou"
      else:
        return f"Não é possível acordar, pois o {self.nome} já está acordado"

    def lutar(self):
      if self.status_acordado:
        if self.vida_atual - 25 > 0:
          if self.energia_atual - 20 > 0:
            self.vida_atual -= 25
            self.energia_atual -= 20
            return f"O {self.nome} lutou"
          else:
            return f"Não é possível lutar por que o {self.nome} está muito cansado e precisa de mais energia"
        else:
            return f"Não é possível lutar por que o {self.nome} está muito machucado e precisa de mais vida"
      else:
        return f"Não é possível lutar por que o {self.nome} está dormindo"

    def comer(self):
      if self.status_acordado:
        if self.vida_atual + 30 < self.vida_maxima:
          if self.energia_atual + 10 < self.energia_maxima:
            self.vida_atual += 30
            self.energia_atual += 10
          else:
            self.energia_atual = self.energia_maxima
            return f"O {self.nome} comeu e está com a energia no máximo"
        else:
          self.vida_atual = self.vida_maxima
          if self.energia_atual + 10 < self.energia_maxima:
            self.energia_atual += 10
            return f"O {self.nome} comeu e está com a vida no máximo e encheu energia."
          else:
            self.energia_atual = self.energia_maxima
            return f"O {self.nome} comeu e está com a vida no máximo e com a energia no máximo."
      else:
        return f'Não é possível comer pois o {self.nome} está dormindo'


bixim = Tamagotchi(nome="Spike", tipo="Reptil")

print(bixim.brincar())
print(bixim.energia_atual)
print(bixim.brincar())
print(bixim.energia_atual)
print(bixim.brincar())
print(bixim.energia_atual)
print(bixim.dormir())
print(bixim.energia_atual)
print(bixim.dormir())
print(bixim.energia_atual)
print(bixim.brincar())
print(bixim.energia_atual)
print(bixim.acordar())
print(bixim.brincar())
print(bixim.energia_atual)