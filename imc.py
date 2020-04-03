altura = float(input("Insira sua altura: "))
peso = float(input("Insira seu peso: "))
imc = peso/(altura**2)

print("Seu índice de massa corporal é:\n", imc)
if imc < 17:
	print("Você está muito abaixo do peso!")
elif imc >= 17 and imc < 18.5:
	print("Você está abaixo do peso")
elif imc >= 18.5 and imc < 25:
	print("Seu peso está ideal")
elif imc >= 25 and imc < 30:
	print("Você está acima do peso")
elif imc >= 30 and imc < 35:
	print("Você possui obesidade I")
elif imc >= 35 and imc < 40:
	print("Você possui obesidade II (severa)")
elif imc >= 40:
	print("Você pussui obesidade II (mórbida)")
