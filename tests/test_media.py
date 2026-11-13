"""Testes da média ponderada: use este arquivo como modelo para os seus."""

import unittest

from notas.media import media_ponderada


class TestMediaPonderada(unittest.TestCase):

    def test_pesos_iguais(self):
        self.assertAlmostEqual(media_ponderada([5, 7], [1, 1]), 6.0)

    def test_pesos_diferentes(self):
        self.assertAlmostEqual(media_ponderada([10, 0], [3, 1]), 7.5)

    def test_uma_nota_so(self):
        self.assertAlmostEqual(media_ponderada([8], [2]), 8.0)

    def test_tamanhos_diferentes_da_erro(self):
        with self.assertRaises(ValueError):
            media_ponderada([5, 7], [1])

    def test_pesos_somando_zero_da_erro(self):
        with self.assertRaises(ValueError):
            media_ponderada([5, 7], [0, 0])


if __name__ == "__main__":
    unittest.main()
