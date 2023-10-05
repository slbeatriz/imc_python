altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso/(altura*altura)

print (f"IMC: {imc:.1f}")

if imc >= 18.5:
    print ("Magreza")

elif imc >= 18.5 and imc < 24.9:
    print ("Normal")

elif imc >= 25 and imc < 29.9:
    print ("Sobrepeso")

elif imc >= 30 and imc < 39.9:
    print ("Obesidade")
else:
    print ("Obesidade grave")