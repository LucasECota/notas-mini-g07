"""Média ponderada (exemplo pronto, feito pelo professor)."""


def media_ponderada(notas, pesos):
    """Devolve a média das notas, cada uma com o seu peso.

    Exemplos:
        media_ponderada([5, 7], [1, 1])  ->  6.0
        media_ponderada([10, 0], [3, 1]) ->  7.5
    """
    if len(notas) != len(pesos):
        raise ValueError("notas e pesos precisam ter o mesmo tamanho")
    soma_dos_pesos = sum(pesos)
    if soma_dos_pesos <= 0:
        raise ValueError("a soma dos pesos precisa ser maior que zero")
    return sum(n * p for n, p in zip(notas, pesos)) / soma_dos_pesos
