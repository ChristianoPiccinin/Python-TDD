




for lance in leilao.lances:
    print(f'o usuario {lance.usuario.nome} deu um lance de {lance.valor}')


avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')