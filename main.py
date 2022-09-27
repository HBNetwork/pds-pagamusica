" 1 - O que foi feito: Somar os valores os valores por música"
" 2 - O que foi feito: criar uma função que é o núcleo do problema. O cálculo que divide o valor da música entre os envolvidos"
" 2 - Próximo passo: capturar os dados para função core."
" N - Próximo passo: Separar os autores de cada música"
" TODO: Alterar input para Decimal"
# INPUTS
# parser_backoffice_data
backoffice_data_default = (
    ('BO_SONGCODE', 'SONG_TITLE', 'SONG_OWNERS', 'ROYALTIES_TO_BR_PAID_$'),
    (4836078, 'UTOPIA',
     'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI',
     800),
    (4836078, 'UTOPIA',
     'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI',
     200),
)
backoffice_data_01_musica = (
    ('BO_SONGCODE', 'SONG_TITLE', 'SONG_OWNERS', 'ROYALTIES_TO_BR_PAID_$'),
    (4836078, 'UTOPIA',
     'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI',
     800),
)
backoffice_data_02_musicas = (
    ('BO_SONGCODE', 'SONG_TITLE', 'SONG_OWNERS', 'ROYALTIES_TO_BR_PAID_$'),
    (4836078, 'UTOPIA',
     'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI',
     800),
    (4836079, 'PIA',
     'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI',
     200),
)
backoffice_data_02_musicas_autor_diferente = (
    ('BO_SONGCODE', 'SONG_TITLE', 'SONG_OWNERS', 'ROYALTIES_TO_BR_PAID_$'),
    (4836078, 'UTOPIA',
     'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI',
     800),
    (4836080, 'PIA_02', 'JOÃO DÓRIA / APARECIDO DE TOLEDO, VALTENIR / MALIBU',
     200),
)
backoffice_data_04_musicas_autor_diferente = (
    ('BO_SONGCODE', 'SONG_TITLE', 'SONG_OWNERS', 'ROYALTIES_TO_BR_PAID_$'),
    (4836078, 'UTOPIA',
     'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI',
     800),
    (4836078, 'UTOPIA',
     'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI',
     200),
    (4836080, 'PIA_02', 'JOÃO DÓRIA / APARECIDO DE TOLEDO, VALTENIR / MALIBU',
     200),
    (4836080, 'PIA_02', 'JOÃO DÓRIA / APARECIDO DE TOLEDO, VALTENIR / MALIBU',
     800),
)
# ---

direitos = (
    ('Representante', 'Código Música', 'Título Música', 'Autor', 'Percentual'),
    ('Editora A', 4836078, 'UTOPIA', 'PAULO LEANDRO FERNANDES SOARES', 25),
    ('Editora A', 4836078, 'UTOPIA', 'APARECIDO DE TOLEDO, VALTENIR', 25),
    ('Editora A', 4836078, 'UTOPIA', 'MALI', 50),
)
"""
def parser_backoffice_data_01(backoffice_data: tuple):
    resp = dict()
    for musica in backoffice_data[1:]:
        try:
            resp[musica[0:3]] += musica[3]
        except KeyError:
            resp[musica[0:3]] = musica[3]
    return resp
"""


def parser_backoffice_data(backoffice_data: tuple):
    from collections import defaultdict
    resp = defaultdict(int)  # = zero, 0
    for musica in backoffice_data[1:]:
        resp[musica[:3]] += musica[3]
    return resp


def test(f, in_, expected):
    """
    Executa tuple a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'\n# --> e o correto é \n{expected!r}'

    print(f'\n{sign} {f.__name__}({in_!r}) \n # --> retornou\n{out!r} {info}')


if __name__ == '__main__':
    test(parser_backoffice_data, (backoffice_data_default, ), ({
        (4836078, 'UTOPIA', 'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI'):
        1000
    }))
    test(parser_backoffice_data, (backoffice_data_01_musica, ), ({
        (4836078, 'UTOPIA', 'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI'):
        800
    }))
    test(parser_backoffice_data, (backoffice_data_02_musicas, ), ({
        (4836078, 'UTOPIA', 'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI'):
        800,
        (4836079, 'PIA', 'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI'):
        200
    }))
    test(parser_backoffice_data, (
        backoffice_data_02_musicas_autor_diferente,
    ), ({
        (4836078, 'UTOPIA', 'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI'):
        800,
        (4836080, 'PIA_02', 'JOÃO DÓRIA / APARECIDO DE TOLEDO, VALTENIR / MALIBU'):
        200
    }))
    test(parser_backoffice_data, (
        backoffice_data_04_musicas_autor_diferente,
    ), ({
        (4836078, 'UTOPIA', 'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI'):
        1000,
        (4836080, 'PIA_02', 'JOÃO DÓRIA / APARECIDO DE TOLEDO, VALTENIR / MALIBU'):
        1000
    }))

relatorio_esperado = (
    ('Representante', 'Autor', 'Total', 'Tx Contrato', 'TT Editora',
     'Tx Editora', 'R$ Autor'),
    ('Editora A', 'PAULO LEANDRO FERNANDES SOARES', 250, 25, 225, 45, 180),
    ('Editora A', 'APARECIDO DE TOLEDO, VALTENIR', 250, 25, 225, 45, 180),
    ('Editora A', 'MALI', 500, 50, 450, 90, 360),
)
"""
admin: 10
editora: 20
autores: (('Samuel', 30), ('Igor', 70))
Valor total: 1000
------------
admin: 100,00
editora: 180,00
PAULO LEANDRO FERNANDES SOARES: 216
APARECIDO DE TOLEDO, VALTENIR: 432
MALI: 72

admin_perc=10, editora_perc=20, autores_perc=((('PAULO LEANDRO FERNANDES SOARES', 30), ('APARECIDO DE TOLEDO, VALTENIR', 60), ('MALI', 10))), total=1000

'PAULO LEANDRO FERNANDES SOARES','APARECIDO DE TOLEDO, VALTENIR','MALI'
"""

backoffice_data = (
    ('BO_SONGCODE', 'SONG_TITLE', 'SONG_OWNERS', 'ROYALTIES_TO_BR_PAID_$'),
    (4836078, 'UTOPIA',
     'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI',
     800),
    (4836078, 'UTOPIA',
     'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI',
     200),
    (4836079, 'PIA',
     'JOAO FERNANDES SOARES / ANTONIO DE TOLEDO, VALTENIR / PEDRO', 200),
    (4836077, 'PIANO', 'MALI / PEDRO', 500),
)

contratos = (
    ('Clientes', 'Taxa Contrato', 'Taxa Cliente'),
    ('Editora A', 10, 20),
)

_direitos = (
    ('Representante', 'Código Música', 'Título Música', 'Autor', 'Percentual'),
    ('Editora A', 4836078, 'UTOPIA', 'PAULO LEANDRO FERNANDES SOARES', 25),
    ('Editora A', 4836078, 'UTOPIA', 'APARECIDO DE TOLEDO, VALTENIR', 25),
    ('Editora A', 4836078, 'UTOPIA', 'MALI', 50),
)

direitos = {
    4836078: {
        'nome':
        'UTOPIA',
        'representante':
        'Aditora A',
        'autores': (
            ('PAULO LEANDRO FERNANDES SOARES', 25),
            ('APARECIDO DE TOLEDO, VALTENIR', 25),
            ('MALI', 50),
        )
    }
}
