# Progrma que não recebe entrada, apenas tem como saída
# uma tabela de preços

tupla = (("Lápis", 1.75), ("Borracha", 2.00), ("Caderno", 15.90), ("Estojo", 25.00), ("Transferidor", 4.20),
         ("Compasso", 9.99), ("Mochila", 120.32), ("Canetas", 22.30), ("Livro", 34.90))

print("-" * 50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("-" * 50)

for produto in tupla:
    print("%s%-35s%s%-2s%10.2f%s" % ("|", produto[0], "|", "R$", produto[1], "|"))

print("-" * 50)