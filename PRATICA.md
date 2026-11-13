# Prática de DevOps — resumo do roteiro
 
CSI410 — Engenharia de Software II · 2026/2 · **atividade assíncrona, até 11/11/2026 (qua), 23h59**, por grupo do projeto, com entrega individual no Moodle (Atividades/Participação).
 
**O roteiro completo, com as explicações (conceitos, o pipeline, como escrever os testes, problemas comuns), é o PDF da tarefa da prática no Moodle.** Este arquivo é só a lista de passos, com a mesma numeração do roteiro.
 
## Parte A — o dono prepara o repositório (cerca de 15 min)
 
- [ ] **A1.** No modelo, <https://github.com/ufopleds/notas-mini>, **Use this template** › **Create a new repository**: nome `notas-mini-gNN` (número do grupo), **Public**.
- [ ] **A2.** **Settings** › **Collaborators** › **Add people**: os colegas do grupo.
- [ ] **A3.** Aba **Actions**: o **CI** está verde? Se não houver execução: **CI** › **Run workflow**.
- [ ] **A4.** Aba **Actions** › **Criar issues da prática** › **Run workflow** (uma vez só).
- [ ] **A5.** **Settings** › **Rules** › **Rulesets** › **New branch ruleset**: *Enforcement status* **Active** (o padrão é *Disabled*); alvo *default branch*; **Require a pull request before merging** com 1 aprovação; **Require status checks to pass before merging** com a verificação `testes`; **Create**.
- [ ] **A6.** Confira a proteção sem gravar nada: em **Settings** › **Rules** › **Rulesets**, a regra `main` está **Active** (não *Disabled*); e, ao editar um arquivo da `main` pelo lápis, a janela de **Commit changes…** não deixa gravar direto na `main`, só criar uma branch (clique em **Cancel**). Se deixar gravar, veja *A `main` aceitou um commit direto* nos problemas comuns do roteiro. Depois, mande o link do repositório no grupo.
## Parte B — cada integrante resolve uma issue (cerca de 1h)
 
- [ ] **B1.** Aceite o convite.
- [ ] **B2.** Pegue uma issue livre (*assign yourself*).
- [ ] **B3.** Na issue: **Development** › **Create a branch** (nome curto, por exemplo `3-frequencia`).
- [ ] **B4.** Na sua branch, crie `tests/test_xxx.py` com um teste para cada linha da tabela da issue.
- [ ] **B5.** Abra o pull request (`Closes #N` na descrição): o pipeline fica **vermelho**. Guarde o link da execução.
- [ ] **B6.** Na sua branch, crie `notas/xxx.py` com a função: o pipeline fica **verde**. Guarde o link.
- [ ] **B7.** Acrescente o seu nome na tabela do `README.md` (na sua branch).
- [ ] **B8.** Peça a revisão de um colega e revise o pull request de outro.
- [ ] **B9.** Com verde e aprovação: **Merge pull request** › **Delete branch**.
- [ ] **B10.** Conflito no README? **Resolve conflicts**, deixe as duas linhas, apague as marcas.
## Parte C — fechamento (cerca de 10 min)
 
- [ ] **C1.** A última execução do CI na `main` está verde.
- [ ] **C2.** O dono cria a release `v0.1.0` (depois dos merges).
- [ ] **C3.** Entrega no Moodle: os 5 links (repositório, seu pull request, execução vermelha, execução verde, release) e a reflexão de 3 a 5 linhas.
- [ ] **C4.** Em computador compartilhado, saia da sua conta do GitHub.
