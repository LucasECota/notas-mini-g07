# Conceito da nota: nota_para_conceito(nota)

**Arquivos:** `notas/conceito.py` (função) e `tests/test_conceito.py` (testes).

**Regra (inventada para a prática):** a nota vai de 0 a 10.
- de 9,0 para cima: `"A"`; de 8,0: `"B"`; de 7,0: `"C"`; de 6,0: `"D"`; de 4,0: `"E"`; abaixo de 4,0: `"F"`;
- nota menor que 0 ou maior que 10: a função levanta `ValueError`.

**Casos de teste (um teste para cada linha):**

| nota | resultado |
|---|---|
| 10.0 | `"A"` |
| 9.0 | `"A"` |
| 8.9 | `"B"` |
| 7.0 | `"C"` |
| 6.0 | `"D"` |
| 5.9 | `"E"` |
| 3.9 | `"F"` |
| 10.5 | `ValueError` |

**Começo do arquivo de teste:**

```python
import unittest

from notas.conceito import nota_para_conceito


class TestConceito(unittest.TestCase):

    def test_dez_e_a(self):
        self.assertEqual(nota_para_conceito(10.0), "A")

    def test_nota_acima_de_dez_da_erro(self):
        with self.assertRaises(ValueError):
            nota_para_conceito(10.5)

    # escreva um teste para cada linha da tabela
```

**Passos:** os da Parte B do roteiro (PDF da tarefa no Moodle; resumo em `PRATICA.md`): testes primeiro, pull request, pipeline vermelho, implementação, pipeline verde, revisão e merge.

**Pronto quando:** o pull request foi revisado, o pipeline está verde e o merge foi feito.
