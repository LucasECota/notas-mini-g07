# Arredondamento da nota: arredondar_nota(nota)

**Arquivos:** `notas/arredondar.py` (função) e `tests/test_arredondar.py` (testes).

**Regra (inventada para a prática):** arredonda para uma casa decimal; a metade vai para cima (7,25 vira 7,3).

**Casos de teste (um teste para cada linha):**

| nota | resultado |
|---|---|
| 7.25 | 7.3 |
| 7.24 | 7.2 |
| 6.35 | 6.4 |
| 0.05 | 0.1 |
| 10.0 | 10.0 |

**Atenção:** `round(nota, 1)` parece resolver, mas erra alguns casos da tabela por causa da forma como o computador guarda números com vírgula. Se quiser ver o teste pegar esse defeito, implemente primeiro com `round` e veja o pipeline ficar vermelho. A implementação que passa em todos os casos:

```python
from decimal import Decimal, ROUND_HALF_UP


def arredondar_nota(nota):
    return float(Decimal(str(nota)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
```

**Começo do arquivo de teste:**

```python
import unittest

from notas.arredondar import arredondar_nota


class TestArredondar(unittest.TestCase):

    def test_metade_vai_para_cima(self):
        self.assertEqual(arredondar_nota(7.25), 7.3)

    # escreva um teste para cada linha da tabela
```

**Passos:** os da Parte B do roteiro (PDF da tarefa no Moodle; resumo em `PRATICA.md`): testes primeiro, pull request, pipeline vermelho, implementação, pipeline verde, revisão e merge.

**Pronto quando:** o pull request foi revisado, o pipeline está verde e o merge foi feito.
