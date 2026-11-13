# (Reserva) Nota necessária no exame: nota_necessaria_no_exame(media)

Para o grupo com mais integrantes, ou para quem terminar a sua issue antes.

**Arquivos:** `notas/exame.py` (função) e `tests/test_exame.py` (testes).

**Regra (inventada para a prática):**
- quem fica de exame tem média de 4,0 até menos de 6,0;
- a nota final é a média entre a média do semestre e a nota do exame, e aprova com 6,0;
- então a nota necessária no exame é `12 - media`;
- se a média estiver fora da faixa do exame (menor que 4,0 ou de 6,0 para cima), a função levanta `ValueError`.

**Casos de teste (um teste para cada linha):**

| media | resultado |
|---|---|
| 5.0 | 7.0 |
| 4.0 | 8.0 |
| 5.5 | 6.5 |
| 6.0 | `ValueError` |
| 3.9 | `ValueError` |

Compare números com vírgula usando `assertAlmostEqual`, como em `tests/test_media.py`.

**Começo do arquivo de teste:**

```python
import unittest

from notas.exame import nota_necessaria_no_exame


class TestExame(unittest.TestCase):

    def test_media_cinco(self):
        self.assertAlmostEqual(nota_necessaria_no_exame(5.0), 7.0)

    def test_media_seis_nao_faz_exame(self):
        with self.assertRaises(ValueError):
            nota_necessaria_no_exame(6.0)

    # escreva um teste para cada linha da tabela
```

**Passos:** os da Parte B do roteiro (PDF da tarefa no Moodle; resumo em `PRATICA.md`): testes primeiro, pull request, pipeline vermelho, implementação, pipeline verde, revisão e merge.

**Pronto quando:** o pull request foi revisado, o pipeline está verde e o merge foi feito.
