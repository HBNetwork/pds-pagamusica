from collections import namedtuple
from tempfile import NamedTemporaryFile
from unicodedata import name
from core import calculos_comissoes
from money import Money as M
from percent import Percent as P


Participacao = namedtuple("Participacao", "tx_adm tx_repre txs_artistas valor_total")
TaxaArtista = namedtuple("TaxaArtista", "nome taxa")
Distribuicao = namedtuple("Distribuicao", "vl_adm vl_repre vls_arti")
DistribuicaoArtista = namedtuple("DistribuicaoArtista", "nome valor")


def test_calcula_comissoes_1000():
    
    entrada = Participacao(
        P("10"), 
        P("20"), 
        (TaxaArtista('PAULO LEANDRO FERNANDES SOARES', P("25")), 
         TaxaArtista('APARECIDO DE TOLEDO, VALTENIR', P("25")),
         TaxaArtista('MALI', P("50"))),
        M("1000")
    )
    
    saida = Distribuicao(
        M("100.0"), 
        M("180.0"), 
        (DistribuicaoArtista('PAULO LEANDRO FERNANDES SOARES', M("180.0")),
         DistribuicaoArtista('APARECIDO DE TOLEDO, VALTENIR', M("180.0")), 
         DistribuicaoArtista('MALI', M("360.0"))),
    )    
    
    assert calculos_comissoes(*entrada) == saida

def test_calcula_comisoes_2():
    entrada = Participacao(
        P("10"), 
        P("20"), 
        (TaxaArtista('PAULO LEANDRO FERNANDES SOARES', P("100")),),
        M("1000")
    )
    
    saida = Distribuicao(
        M("100.0"), 
        M("180.0"), 
        (DistribuicaoArtista('PAULO LEANDRO FERNANDES SOARES', M("720.0")),),
    )    
    
    assert calculos_comissoes(*entrada) == saida


def test_calcula_comissoes_3():
    entrada = Participacao(
        P("10"), 
        P("20"), 
        (TaxaArtista('PAULO LEANDRO FERNANDES SOARES', P("33.33")), 
         TaxaArtista('APARECIDO DE TOLEDO, VALTENIR', P("33.33")),
         TaxaArtista('MALI', P("33.34"))),
        M("1000")
    )
    
    saida = Distribuicao(
        M("100.0"), 
        M("179.99"), 
        (DistribuicaoArtista('PAULO LEANDRO FERNANDES SOARES', M("239.98")),
         DistribuicaoArtista('APARECIDO DE TOLEDO, VALTENIR', M("239.98")), 
         DistribuicaoArtista('MALI', M("240.05")))
    )    
    
    assert calculos_comissoes(*entrada) == saida
    
    