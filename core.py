

def calculos_comissoes(admin_perc, editora_perc, autores_perc, total):
    
    comissao_admin = total * admin_perc
    valor_total_editora = total - comissao_admin
    comissao_editora = valor_total_editora * editora_perc
    valor_autores = valor_total_editora - comissao_editora
    comissao_autores = []
    total_autores = 0 
    for autor, autor_perc in autores_perc:
        comissao_autor = round(valor_autores * autor_perc, 2)

        comissao_autores.append((autor, comissao_autor))
        total_autores += comissao_autor

    comissao_editora = total - comissao_admin - total_autores 
        
    return comissao_admin, comissao_editora, tuple(comissao_autores)
    
