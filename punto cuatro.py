#En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18:9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.
añoA: float = 25e6
añoB: float = 18.9e6
año: int
año = 2022

while añoA >= añoB:
    añoA = añoA*(1 + 0.02)
    añoB = añoB*(1 + 0.03)
    año = año + 1
print("En el año " + str(año) + " la población del país B superará a la de A")
print("Fin")