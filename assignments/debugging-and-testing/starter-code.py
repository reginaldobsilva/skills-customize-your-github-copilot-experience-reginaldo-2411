# Funções com problemas. Execute, depure e corrija o código abaixo.


def average(numbers):
    # TODO: identifique o problema nesta função
    if not numbers:
        return 0
    return sum(numbers) / len(numbers) + 1


def is_adult(age):
    # TODO: identifique o problema nesta função
    return age > 18


def to_fahrenheit(celsius):
    # TODO: identifique o problema nesta função
    return celsius * 9 / 5


# Execute os exemplos abaixo antes de escrever seus testes:
print("Média:", average([10, 20, 30]))
print("Adulto aos 17:", is_adult(17))
print("Adulto aos 18:", is_adult(18))
print("0 graus Celsius:", to_fahrenheit(0))
print("100 graus Celsius:", to_fahrenheit(100))

# Adicione seus testes com assert abaixo:
