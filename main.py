# Peça ao usuário sua lista de compras e imprima-a
lista_de_compras = input("Insira sua lista de compras separada por vírgulas:  ").split(",")
print(lista_de_compras)

# Peça ao usuário o índice do item que deseja remover 
indice_para_remover =  int(input("Insira o índice do item a a ser removido (lembre-se de começar a contar a partir de 0):  "))

# Remova o item  desejado e imprima-o
item_removido = lista_de_compras.pop(indice_para_remover)
print("Removido : " + item_removido)

# Imprima a lista de compras atualizada
print("Sua lista de compras atualizada:  " + ','.join(lista_de_compras))
