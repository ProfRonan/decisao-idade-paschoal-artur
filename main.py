#Recebendo idade do usuário
age = int(input("Digite sua idade: \n"))

#Definindo condições
if age < 0 :
    print("impossível!")
    print("não precisa se alistar.")
elif age < 18 :
    print("Não precisa se alistar")
if age > 18 and age < 65 :
    print("Não esqueça de votar na próxima eleição.")
elif age > 65 :
    print("Vá descansar.")