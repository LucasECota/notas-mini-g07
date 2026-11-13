# notas-mini

Projeto da **prática de DevOps** de CSI410 — Engenharia de Software II (UFOP, 2026/2).

Funções pequenas sobre as notas de uma disciplina, cada uma com os seus testes. O código é simples de propósito: o objetivo da prática é o caminho do código até a `main` — issue, branch, commit, pull request, pipeline, revisão e merge. O roteiro completo é o PDF da tarefa da prática no Moodle; a lista de passos está em [PRATICA.md](PRATICA.md).

> As regras de notas deste projeto são inventadas para a prática. Não são as da UFOP nem as da ES2.

## Estrutura

```
notas/                     código (uma função por arquivo)
  media.py                 media_ponderada: exemplo pronto
tests/                     testes automatizados (unittest, da biblioteca padrão do Python)
  test_media.py            modelo para os seus testes
.github/workflows/ci.yml   pipeline: roda os testes a cada push na main e a cada pull request
pratica/issues/            texto das issues da prática
```

## Como rodar os testes

- **No GitHub (não precisa instalar nada):** os testes rodam sozinhos no pipeline (aba Actions) a cada pull request.
- **No computador, com Python 3.6 ou mais novo:** na pasta do repositório, `python -m unittest -v` (no Windows, às vezes `py -m unittest -v`).
- **Num compilador online de Python:** veja o Apêndice B do roteiro.

## Integrantes e issues

Cada integrante acrescenta uma linha no fim da tabela, no próprio pull request.

| Integrante | Issue | Função |
|---|---|---|
| Professor (exemplo) | — | `media_ponderada` |
