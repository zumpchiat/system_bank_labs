# System Bank in Python 

Projeto  de um sistema bancário desenvolvido em Python durante .
O repositório explora diferentes paradigmas e técnicas de programação.

---

## 📂 Estrutura do Projeto


## 🔄 Versão 1: Programação Funcional Modularizada

Primeira evolução do sistema com **modularização através de funções**, **cadastro de usuários** com validação e **sistema de contas correntes**.

### Funcionalidades

| Função              | Descrição                                                           |
|---------------------|---------------------------------------------------------------------|
| `depositar()`       | Realiza depósitos apenas com argumentos posicionais                 |
| `sacar()`           | Realiza saques com argumentos nomeados (keyword only)               |
| `exibir_extrato()`  | Exibe extrato com combinação de argumentos posicionais e nomeados   |
| `create_usuario()`   | Cadastra novos clientes com validação de CPF                        |
| `create_conta()`     | Cria contas vinculadas a um usuário existente (agência fixa 0001)   |
| `listar_contas()`   | Lista todas as contas cadastradas                                   |

### Regras de Negócio

#### Depósitos e Saques

- **Depósito**: Somente valores positivos
- **Saque**:
  - Máximo de **3 saques por dia**
  - Limite de saque: **R$ 500 por operação**
  - Impede saque com saldo insuficiente

#### Usuários

| Campo     | Formato                                    |
|-----------|--------------------------------------------|
| Nome      | Texto livre                                |
| CPF       | Somente números (validado)                 |
| Nascimento| `dd-mm-aaaa`                               |
| Endereço  | `logradouro, nro - bairro - cidade/UF`     |

⚠️ **Não é permitido cadastrar dois usuários com o mesmo CPF.**

#### Contas

| Campo           | Valor                      |
|-----------------|----------------------------|
| Agência         | `0001` (fixa)              |
| Número da Conta | Sequencial (1, 2, 3, ...)  |
| Usuário         | Associado pelo CPF         |

✔ Um usuário pode possuir **várias contas**, mas **cada conta pertence a apenas um usuário**.

---


---

## 🚀 Como Executar

### Versão  (Funcional)
```bash
python system_bank_funcional.py
```

---

## 📋 Menu de Operações (Versão 2)

```
================ MENU ================
[1]    Depositar
[2]    Sacar
[3]    Extrato
[4]    Nova conta
[5]    Listar contas
[6]    Novo usuário
[0]    Sair
```

### Fluxo de Uso Recomendado

1. **[6]** Criar novo usuário
   - Informe CPF (somente números)
   - Nome completo
   - Data de nascimento (`dd-mm-aaaa`)
   - Endereço completo

2. **[4]** Criar conta para o usuário
   - Informe o CPF do usuário cadastrado

3. **[1]** Fazer depósito
   - Informe CPF e valor

4. **[2]** Realizar saque
   - Informe CPF e valor (limite R$ 500, máx 3 saques)

5. **[3]** Consultar extrato
   - Informe CPF para ver histórico completo



## 🎓 Conceitos Aplicados

### Versão 1
- ✅ Funções com argumentos posicionais e nomeados
- ✅ Modularização de código
- ✅ Validação de dados de entrada
- ✅ Estruturas de dados (listas e dicionários)





## 🔧 Tecnologias Utilizadas

- **Python 3.x**
- 
---



