class Calculadora:
    def __init__(self, n1: int, n2: int) -> None:
        self.n1 = n1
        self.n2 = n2
        
    def sumar(self) -> int:
        return self.n1 + self.n2
    
    def restar(self) -> int:
        return self.n1 - self.n2
    
    def multiplicar(self) -> int:
        return self.n1 * self.n2
    
    def dividir(self) -> float:
        return self.n1 / self.n2
    

calc1 = Calculadora(5, 10)
print(calc1.sumar())
print(calc1.restar())
print(calc1.multiplicar())
print(calc1.dividir())