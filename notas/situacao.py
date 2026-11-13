def situacao(media, frequencia):
    """Retorna 'aprovado', 'exame' ou 'reprovado'."""
    if frequencia < 75:
        return "reprovado"
    if media >= 6.0:
        return "aprovado"
    if media >= 4.0:
        return "exame"
    return "reprovado"
