# Programa que recebe um ano como entrada, devolvendo
# como saída se ele é ou não bissexto

from datetime import date

ano = int(input("Que ano quer analisar? Para analisar o ano atual digite 0: "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano} É BISSEXTO ")
else:
    print(f"O ano de {ano} NÃO É BISSEXTO ")


