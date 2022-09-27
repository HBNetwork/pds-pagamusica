from collections import defaultdict
from pprint import pprint

# region dados
backoffice_data = (
    ('BO_SONGCODE', 'SONG_TITLE', 'SONG_OWNERS',                                              'ROYALTIES_TO_BR_PAID_$'),
    (4836078,       'UTOPIA',     'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI', 800),
    (4836078,       'UTOPIA',     'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI', 200),
    #(4836078,       'UTOPIA',     'PAULO LEANDRO FERNANDES SOARES / APARECIDO DE TOLEDO, VALTENIR / MALI', 1000),
    (4836079,          'PIA',     'JOAO FERNANDES SOARES / ANTONIO DE TOLEDO, VALTENIR / PEDRO', 200),
    (4836077, 'PIANO', 'MALI / PEDRO', 500),
)

contratos = (
    ('Clientes', 'Taxa Contrato', 'Taxa Cliente'),
    ('Editora A',             10,             20),
)


direitos = (
    ('Representante', 'Código Música', 'Título Música', 'Autor', 'Percentual'),
    ('Editora A', 4836078, 'UTOPIA', 'PAULO LEANDRO FERNANDES SOARES', 10),
    ('Editora A', 4836078, 'UTOPIA', 'APARECIDO DE TOLEDO, VALTENIR', 30),
    (''         , 4836078, 'UTOPIA', 'MALI', 60),
    #('Editora A', 4836077, 'PIANO', 'MALI', 50),
    #('Editora A', 4836077, 'PIANO', 'PEDRO', 50),
)
# endregion

relatorio_esperado = (
    ('Representante', 'Autor',                         'Total', 'Tx Contrato', 'TT Editora', 'Tx Editora', 'R$ Autor'),
    ('Editora A'    , 'PAULO LEANDRO FERNANDES SOARES', 250,               25,          225,           45,       180),
    ('Editora A'    , 'APARECIDO DE TOLEDO, VALTENIR',  250,               25,          225,           45,       180),
    ('Editora A'    , 'MALI',                           500,               50,          450,           90,       360),
)


def calcula_total_por_musica(data):
    total = defaultdict(int)

    for pagamento in data[1:]:
        total[pagamento[:3]] += pagamento[3]

    #pprint(total)
    return total




def calcula_direitos_por_representante_musica_artista(total_por_musica, direitos):

    resp_ok = defaultdict(float)
    musicas_faltam_cadastro = []

    dict_direitos = defaultdict(list)

    for direito in direitos[1:]:
        dict_direitos[direito[1]] += (direito,)

    #pprint(dict_direitos)

    for musica, total in total_por_musica.items():
        if direitos := dict_direitos[musica[0]]:
            for direito in dict_direitos[musica[0]]:
                resp_ok[direito[0], direito[3]] += total * direito[4] / 100


        else:
            musicas_faltam_cadastro.append((musica, total))

    #pprint(resp)

    print("miscas que faltam cadastro")
    pprint(musicas_faltam_cadastro)
    return resp_ok, musicas_faltam_cadastro


def gera_relatorio(direitos_bruto, contratos):

    resp = []
    contratos_dict = {
        contrato[0]: (contrato[1], contrato[2]) for contrato in contratos[1:]
    }


    for (representante, autor), valor_tt in direitos_bruto.items():
        pct_contrato, pct_editora = contratos_dict[representante]
        tx_contrato = valor_tt * pct_contrato /100
        tt_editora = valor_tt - tx_contrato
        tx_editora = tt_editora * pct_editora / 100
        vlr_autor = tt_editora - tx_editora

        resp += ((representante, autor, valor_tt, tx_contrato, tt_editora, tx_editora, vlr_autor),)


    print("\n\n Relatorio")
    pprint(resp)

    return resp


total_recebido_por_musica = calcula_total_por_musica(backoffice_data)
direitos_bruto, musicas_faltam_cadastro = calcula_direitos_por_representante_musica_artista(total_recebido_por_musica, direitos)

relatorio = gera_relatorio(direitos_bruto, contratos)
