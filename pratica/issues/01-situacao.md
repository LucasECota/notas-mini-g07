# Situação do aluno: situacao(media, frequencia)

**Arquivos:** `notas/situacao.py` (função) e `tests/test_situacao.py` (testes).

**Regra (inventada para a prática):**
- frequência (em %) abaixo de 75: `"reprovado"`, qualquer que seja a média;
- senão, média de 6,0 para cima: `"aprovado"`;
- senão, média de 4,0 para cima: `"exame"`;
- senão: `"reprovado"`.

**Casos de teste (um teste para cada linha):**

| media | frequencia | resultado |
|---|---|---|
| 8.0 | 90 | `"aprovado"` |
| 6.0 | 75 | `"aprovado"` |
| 5.9 | 100 | `"exame"` |
| 4.0 | 80 | `"exame"` |
| 3.9 | 80 | `"reprovado"` |
| 9.0 | 74 | `"reprovado"` |

**Começo do arquivo de teste:**

```python
import unittest

from notas.situacao import situacao


class TestSituacao(unittest.TestCase):

    def test_media_alta_e_frequencia_boa(self):
        self.assertEqual(situacao(8.0, 90), "aprovado")

    # escreva um teste para cada linha da tabela
```

**Passos:** os da Parte B do roteiro (PDF da tarefa no Moodle; resumo em `PRATICA.md`): testes primeiro, pull request, pipeline vermelho, implementação, pipeline verde, revisão e merge.

**Pronto quando:** o pull request foi revisado, o pipeline está verde e o merge foi feito.
