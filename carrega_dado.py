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



def yyy (backoffica_data, contratos_data, direitos_data):
    pass
    



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
    test(carrega_dados, backoffice_data_autores_01, (
        (100.0, 180.0, (('PAULO LEANDRO FERNANDES SOARES', 180.0),('APARECIDO DE TOLEDO, VALTENIR', 180.0), ('MALI', 360.0)))
        ))