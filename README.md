
---

# 🧪 Atividade – Testes Unitários e Mock com Unittest

Este repositório contém o código desenvolvido como **atividade acadêmica da disciplina de *Testes e Automações***, do curso de **Análise e Desenvolvimento de Sistemas (ADS)** da **Faculdade Impacta**.

O objetivo desta atividade foi **implementar testes automatizados com `unittest` e uso de mock** (`unittest.mock.MagicMock`), aplicando conceitos de isolamento de dependências e verificação de comportamento de funções.

---

## 🎯 **Objetivos da Atividade**

1. Implementar funções para **classificação de nadadores** com base em faixas etárias.
2. Criar **testes unitários** cobrindo todos os cenários possíveis de classificação.
3. Aplicar **mocking** para simular dependências externas (como um serviço de busca de idade).
4. Executar os testes com `unittest` e validar o funcionamento completo da solução.

---

## ⚙️ **Descrição do Código**

### 🧩 **Função `obter_categoria()`**

Classifica nadadores conforme a idade fornecida.

```python
def obter_categoria(idade):
    if idade >= 5 and idade <= 7:
        categoria = 'Infantil A'
    elif idade >= 8 and idade <= 10:
        categoria = 'Infantil B'
    elif idade >= 11 and idade <= 13:
        categoria = 'Juvenil A'
    elif idade >= 14 and idade <= 17:
        categoria = 'Juvenil B'
    elif idade >= 18:
        categoria = 'Sênior'
    else:
        categoria = 'Idade fora das categorias'
    return categoria
```

### 🧠 **Função `classificar_nadador()`**

Depende de um **serviço externo** que retorna a idade do nadador.
Essa dependência é **simulada com um Mock**, para permitir testes sem precisar de um serviço real.

```python
def classificar_nadador(servico_idade, id_nadador):
    idade = servico_idade.buscar_idade(id_nadador)
    return obter_categoria(idade)
```

---

## 🧪 **Testes Automatizados**

Os testes foram criados utilizando o módulo `unittest` do Python, em dois blocos principais:

---

### ✅ **Testes de Unidade – `TestObterCategoria`**

Validam a lógica de classificação por idade diretamente.

```python
class TestObterCategoria(unittest.TestCase):
    def test_infantil_a(self):
        self.assertEqual(obter_categoria(5), "Infantil A")
        self.assertEqual(obter_categoria(7), "Infantil A")

    def test_juvenil_b(self):
        self.assertEqual(obter_categoria(14), "Juvenil B")
        self.assertEqual(obter_categoria(17), "Juvenil B")
```

Esses testes garantem que a função retorne corretamente a categoria esperada para cada faixa etária.

---

### 🧩 **Testes com Mock – `TestClassificacaoComMock`**

Utilizam o `MagicMock` para simular o retorno da idade a partir de um “serviço externo”.

```python
from unittest.mock import MagicMock

class TestClassificacaoComMock(unittest.TestCase):
    def test_classificar_nadador_com_mock(self):
        mock_servico_idade = MagicMock()
        mock_servico_idade.buscar_idade.return_value = 15
        resultado = classificar_nadador(mock_servico_idade, id_nadador=123)
        self.assertEqual(resultado, "Juvenil B")
        mock_servico_idade.buscar_idade.assert_called_with(123)
```

Esse teste garante:

* Que a função chama corretamente o método do mock (`buscar_idade`)
* Que o valor retornado é classificado conforme esperado
* Que a interação com o mock ocorre com os parâmetros corretos

---

## ⚡ **Execução dos Testes**

Para executar os testes no terminal:

```bash
python -m unittest nome_do_arquivo.py -v
```

### 💻 **Exemplo de saída esperada**

```
test_classificar_nadador_com_mock (TestClassificacaoComMock) ... ok
test_idade_fora_da_categoria (TestObterCategoria) ... ok
test_infantil_a (TestObterCategoria) ... ok
test_infantil_b (TestObterCategoria) ... ok
test_juvenil_a (TestObterCategoria) ... ok
test_juvenil_b (TestObterCategoria) ... ok
test_senior (TestObterCategoria) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.001s
OK
```

---

## 🎓 **Informações Acadêmicas**

* **Disciplina:** Testes e Automações
* **Curso:** Análise e Desenvolvimento de Sistemas (ADS)
* **Período:** 5º Semestre
* **Instituição:** Faculdade Impacta de Tecnologia
* **Linguagem:** Python
* **Framework de Teste:** Unittest

---

## 🧠 **Resumo do Aprendizado**

Esta atividade reforçou os conceitos de:

* **Testes unitários** com `unittest`
* **Cobertura de casos de borda e validação de lógica condicional**
* Uso de **mocking** para isolar dependências externas
* Boas práticas de **testes automatizados e verificações de comportamento**

---

**📌 Autor:**Felipe Souza Panichi
**🏫 Faculdade Impacta – 5º Semestre de ADS**

---
