# 📘 Atividade: Depuração e Testes em Python

## 🎯 Objetivo

Aprenda a identificar erros, criar testes simples com `assert` e corrigir funções Python usando exemplos claros de entrada e saída esperadas.

## 📝 Tarefas

### 🛠️ Identificar o Comportamento Incorreto

#### Descrição
Abra o arquivo `starter-code.py` e execute as funções existentes com os exemplos da seção de requisitos. Compare o resultado recebido com o resultado esperado e registre o problema encontrado em comentários no código.

#### Requisitos
O programa concluído deve:

- Executar `average([10, 20, 30])` e mostrar o problema na função `average`.
- Executar `is_adult(17)` e `is_adult(18)` e verificar a idade mínima.
- Executar `to_fahrenheit(0)` e `to_fahrenheit(100)` e comparar com os valores esperados.
- Adicionar comentários explicando o que está incorreto em cada função.

### 🛠️ Escrever Casos de Teste

#### Descrição
Crie testes simples usando `assert` para representar os resultados corretos das três funções. Inclua pelo menos um caso comum e um caso limite para cada função.

#### Requisitos
O programa concluído deve:

- Usar `assert` para testar `average` com uma lista comum e uma lista vazia.
- Usar `assert` para testar `is_adult` com idades abaixo, igual a e acima de 18.
- Usar `assert` para testar `to_fahrenheit` com 0, 100 e um valor negativo.
- Fazer com que a execução de `starter-code.py` falhe imediatamente quando algum resultado estiver incorreto.
- Exemplo de testes:
  ```python
  assert average([10, 20, 30]) == 20
  assert is_adult(18) is True
  assert to_fahrenheit(0) == 32
  ```

### 🛠️ Corrigir as Funções

#### Descrição
Corrija as implementações sem alterar os nomes das funções nem o objetivo de cada função. Depois execute novamente todos os testes.

#### Requisitos
O programa concluído deve:

- Calcular a média dos números sem usar uma solução fixa para um exemplo específico.
- Retornar `0` quando `average` receber uma lista vazia.
- Retornar `True` em `is_adult` apenas para idades maiores ou iguais a 18.
- Converter Celsius para Fahrenheit usando a fórmula `(celsius * 9/5) + 32`.
- Passar em todos os testes definidos na tarefa anterior.
