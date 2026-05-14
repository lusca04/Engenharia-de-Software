# 📚 Portfólio – Engenharia de Software | FIAP 2026

## Sobre este repositório

**Aluno:** Lucas Santos Rodrigues — RM 556891

Este repositório reúne os exercícios das aulas do curso de Engenharia de Software. Cada pasta contém o código referente à aula, imagens de diagramação e imagens de execução quando disponíveis.

---

## Como executar os exercícios

1. Abra o terminal no diretório do exercício desejado.
2. Execute o script Python correspondente:

```bash
python aula-03-requisitos/gymtrack_validador.py
python aula-04-srs/srs_marketplace.py
python aula-05-casos-de-uso/biblioteca_digital.py
python aula-06-atividades/cadastro_usuario.py
python aula-07-sequencia/transferencia_nubank.py
python aula-08-classes/streaming_netflix.py
```

## Pré-requisitos

- Python 3.10 ou superior instalado
- Editor de texto ou IDE (VS Code recomendado)

## Instalação

```bash
git clone https://github.com/lusca04/Engenharia-de-Software.git
cd Checkpoint-3---Engenharia-de-Software
```

---

## Exercícios por Aula

### Aula 03 – Requisitos Funcionais vs. Não-Funcionais

- Código: [`aula-03-requisitos/gymtrack_validador.py`](aula-03-requisitos/gymtrack_validador.py)
- Saída: [`aula-03-requisitos/aula03-output.png`](aula-03-requisitos/aula03-output.png)

Validação de dados de treino em um sistema GymTrack, verificando nome, peso, repetições e tipo de exercício com mensagens de erro específicas para cada campo inválido.

---

### Aula 04 – Documento SRS

- Código: [`aula-04-srs/srs_marketplace.py`](aula-04-srs/srs_marketplace.py)
- Saída: [`aula-04-srs/aula04-output.png`](aula-04-srs/aula04-output.png)

Implementação de um **Software Requirements Specification (SRS)** para o FIAP Marketplace usando dataclasses e enums. Inclui:
- 4 Requisitos Funcionais: Cadastro de Produto, Busca por Categoria, Checkout e Pagamento, Avaliação do Vendedor
- 3 Requisitos Não-Funcionais: Disponibilidade 99,9%, Desempenho da busca (< 2s / 5k usuários), Conformidade com LGPD
- Função `validar_requisito()` que verifica descrição adequada, pré-condição definida e critério mensurável
- Função `exportar_markdown()` que gera o SRS completo em formato Markdown para Confluence/Notion

---

### Aula 05 – UML e Casos de Uso

- Diagrama: [`aula-05-casos-de-uso/diagrama-casos-de-uso.png`](aula-05-casos-de-uso/diagrama-casos-de-uso.png)
- Código: [`aula-05-casos-de-uso/biblioteca_digital.py`](aula-05-casos-de-uso/biblioteca_digital.py)
- Saída: [`aula-05-casos-de-uso/aula05-output.png`](aula-05-casos-de-uso/aula05-output.png)

Sistema de biblioteca digital implementado em duas versões — **procedural** e **OOP** — mapeando diretamente os casos de uso do diagrama UML:

| Caso de Uso | Implementação |
|---|---|
| UC-01 Listar Catálogo | `biblioteca.listar()` |
| UC-02 Buscar Livro | busca case-insensitive com list comprehension |
| UC-03 Emprestar Livro | `biblioteca.emprestar()` com `<<include>>` verificar disponibilidade |
| UC-04 Devolver Livro | `biblioteca.devolver()` com `<<extend>>` aplicar multa |

---

### Aula 06 – Diagramas de Atividades

- Diagrama: [`aula-06-atividades/diagrama-atividades.png`](aula-06-atividades/diagrama-atividades.png)
- Código: [`aula-06-atividades/cadastro_usuario.py`](aula-06-atividades/cadastro_usuario.py)
- Saída: [`aula-06-atividades/aula06-output.png`](aula-06-atividades/aula06-output.png)

Função `cadastro_usuario()` implementada seguindo o fluxo do diagrama de atividades (estilo iFood), com guard clauses que espelham cada losango de decisão:

| Nó do Diagrama | Código |
|---|---|
| Validar formato do e-mail | regex `r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"` |
| E-mail já cadastrado? | `if email_ja_existe` |
| Confirmação recebida? | `if not confirmou_email` → cadastro expirado |
| Fluxo principal | `return "✅ Cadastro concluído!"` |

---

### Aula 07 – Diagramas de Sequência

- Diagrama: [`aula-07-sequencia/diagrama-sequencia.png`](aula-07-sequencia/diagrama-sequencia.png)
- Código: [`aula-07-sequencia/transferencia_nubank.py`](aula-07-sequencia/transferencia_nubank.py)
- Saída: [`aula-07-sequencia/aula07-output.png`](aula-07-sequencia/aula07-output.png)

Simulação de transferência bancária com três classes que representam as lifelines do diagrama de sequência — `AppNubank → ServidorNubank → BancoDeDados` — e o fragmento `[alt]` para aprovação ou recusa de pagamento por saldo insuficiente.

---

### Aula 08 – Diagramas de Classes

- Diagrama: [`aula-08-classes/diagrama-classes.png`](aula-08-classes/diagrama-classes.png)
- Código: [`aula-08-classes/streaming_netflix.py`](aula-08-classes/streaming_netflix.py)
- Saída: [`aula-08-classes/aula08-output.png`](aula-08-classes/aula08-output.png)

Implementação de dois sistemas a partir do diagrama UML de classes, demonstrando os três tipos de relacionamento:

| Relacionamento | Símbolo | Exemplo no código |
|---|---|---|
| Composição | ◆ | `Pedido` cria `Item` internamente |
| Agregação | ◇ | `Catalogo` recebe `Filme` por parâmetro |
| Associação | → | `Usuario` referencia `Avaliacao` |

Sistema 1 — **iFood**: `Cliente`, `Pedido`, `Item`, `Restaurante` com `confirmar()` e `calcularTotal()`.  
Sistema 2 — **Netflix**: `Plataforma`, `Catalogo`, `Filme`, `Usuario`, `Avaliacao` com `listar_filmes()` e `ver_avaliacoes()`.

---

### Aula 09 – Arquitetura MVC

- Diagrama: [`aula-09-mvc/diagrama-mvc.png`](aula-09-mvc/diagrama-mvc.png)

*(em desenvolvimento)*

---

## Links

| Recurso | Link |
|---|---|
| 🐙 GitHub | [Engenharia-de-Software](https://github.com/lusca04/Engenharia-de-Software.git) |
| 📌 Checkpoint 3 | [Whimsical](https://whimsical.com/checkpoint-3-engenharia-de-software-Mhe3fp7DXwvVaNtN1FZiyi) |
| Aula 03 | [Whimsical](https://whimsical.com/aula-es-03-requisitos-funcionais-vs-nao-funcionais-VeRe2FAFiQkj7bRSeUU7km) |
| Aula 04 | [Whimsical](https://whimsical.com/aula-es-04-documento-de-especificacao-de-requisitos-de-software--YChfpWcG8f9w7qx2uC2wLH) |
| Aula 05 | [Whimsical](https://whimsical.com/aula-es-05-introducao-a-uml-e-diagramas-de-casos-de-uso-2xASW5FbDUd4n7R1hPMdbZ) |
| Aula 06 | [Whimsical](https://whimsical.com/aula-es-06-diagramas-de-atividades-para-processos-de-negocio-TGccPNXDmV16wG3EFemG1M) |
| Aula 07 | [Whimsical](https://whimsical.com/aula-es-07-diagramas-de-sequencia-interacao-entre-objetos-Q6mdtrvJoAevsCs3LQnYER) |
| Aula 08 | [Whimsical](https://whimsical.com/aula-es-08-diagramas-de-classes-estrutura-relacionamentos-atribu-Fq8bUxi9VTtzjAiBQxxypK) |
| Aula 09 | [Whimsical](https://whimsical.com/aula-es-09-arquitetura-de-software-introducao-a-camadas-e-mvc-KgpgBBV8RN7ZJiaDgqo48N) |
| Aula 10 | [Whimsical](https://whimsical.com/aula-es-10-de-requisitos-a-wireframes-baixa-fidelidade-Wgh814XebntrEdtFjSxMii) |
| Aula 11 | [Whimsical](https://whimsical.com/aula-es-11-design-system-industrial-e-ui-components-7D1P5w19nv5TgQ51C7ozKt) |