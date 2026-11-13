import unittest
from notas.situacao import situacao


class TestSituacao(unittest.TestCase):
    def test_media_alta_e_frequencia_boa(self):
        self.assertEqual(situacao(8.0, 90), "aprovado")

    def test_media_seis_e_frequencia_no_limite(self):
        self.assertEqual(situacao(6.0, 75), "aprovado")

    def test_media_abaixo_de_seis_vai_para_exame(self):
        self.assertEqual(situacao(5.9, 100), "exame")

    def test_media_quatro_vai_para_exame(self):
        self.assertEqual(situacao(4.0, 80), "exame")

    def test_media_abaixo_de_quatro_reprova(self):
        self.assertEqual(situacao(3.9, 80), "reprovado")

    def test_frequencia_abaixo_de_75_reprova(self):
        self.assertEqual(situacao(9.0, 74), "reprovado")


if __name__ == "__main__":
    unittest.main()
