minha_lista = ["Pedro", "Carla", "Isaac", "Samuel", "Paulo"]
nome = "Carla"

print("Primeiro nome:", minha_lista[0])
print("Terceiro nome:", minha_lista[-3])
print("Ultimo nome:", minha_lista[-1])
print("  ")

if nome in minha_lista:
    print(f"{nome} está na lista!")
        
else:
    print("Carla não foi encontrada na lista.")



