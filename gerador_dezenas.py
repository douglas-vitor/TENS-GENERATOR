#Script V1.0
#script de geracao de conjuntos de dezenas randomicos

from random import randrange

def Casa():
    num = randrange(1, 60)
    return num

dezenas = set()

#abaixo insita as dezenas recentes que deseja remover no fomrmato:
#'set([14, 16, 19, 21, 33, 55])'
try:
    dezenas_remove = {'set([14, 16, 19, 21, 33, 55])',
                      'set([10, 21, 32, 34, 48, 57])',
                      'set([1, 6, 14, 22, 30, 56])',
                      'set([12, 20, 24, 28, 33, 57])',
                      'set([8, 33, 40, 52, 55, 59])',
                      'set([4, 6, 39, 44, 52, 60])',
                      'set([4, 8, 10, 21, 45, 54])'}
except Exception as erro:
    print('Algo de errado com a lista de dezenas a remover. Erro code: ', erro)

while (len(dezenas) < 1):
    #define seis casas de numeros ramdomicos
    a = Casa()
    b = Casa()
    c = Casa()
    d = Casa()
    e = Casa()
    f = Casa()

    #abaixo o metodo que cuidara de gerar a combinacao e adicionar no set
    sequencia = {a, b, c, d, e, f}
    sequencia_string = str(sequencia)
    dezenas.add(sequencia_string)

try:
    #agora vou discartar os resultados da lista remove se tiver ele remove, se nao tiver
    #ele nao faz nada
    dezenas.discard(dezenas_remove)
except Exception as erro:
    print('erro ao remover dezenas. Erro Code: ', erro)

#abaixo faz o for para exibicao dos resultados do meu set
i = 0
for dezena in dezenas:
    i += 1
    print 'dezena numero:' + str(i) + ' ' + dezena