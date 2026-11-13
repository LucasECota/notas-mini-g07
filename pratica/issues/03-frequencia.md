# Frequência mínima: frequencia_ok(presencas, aulas)

**Arquivos:** `notas/frequencia.py` (função) e `tests/test_frequencia.py` (testes).

**Regra (inventada para a prática):**
- devolve `True` se o aluno esteve em pelo menos 75% das aulas, e `False` se não;
- se o número de aulas for 0 (ou negativo), a função levanta `ValueError`.

Dica: dá para comparar sem divisão: `4 * presencas >= 3 * aulas`.

**Casos de teste (um teste para cada linha):**

| presencas | aulas | resultado |
|---|---|---|
| 24 | 32 | `True` |
| 23 | 32 | `False` |
| 32 | 32 | `True` |
| 0 | 32 | `False` |
| 5 | 0 | `ValueError` |

**Começo do arquivo de teste:**

```python
import unittest

from notas.frequencia import frequencia_ok


class TestFrequencia(unittest.TestCase):

    def test_exatamente_75_por_cento(self):
        self.assertTrue(frequencia_ok(24, 32))

    def test_sem_aulas_da_erro(self):
        with self.assertRaises(ValueError):
            frequencia_ok(5, 0)

    # escreva um teste para cada linha da tabela
```

**Passos:** os da Parte B do roteiro (PDF da tarefa no Moodle; resumo em `PRATICA.md`): testes primeiro, pull request, pipeline vermelho, implementação, pipeline verde, revisão e merge.

**Pronto quando:** o pull request foi revisado, o pipeline está verde e o merge foi feito.
