# Projeto Gerenciamento de Caminhões – React + Python

## Visão Geral

O **Projeto Gerenciamento de Caminhões** é uma aplicação web desenvolvida para realizar o **cadastro, listagem e gerenciamento de caminhões**, integrando um **front-end em React** com um **back-end em Python utilizando Django**. O sistema foi construído com foco em organização, validações de dados e boas práticas de desenvolvimento, servindo também como um projeto de aprendizado e consolidação de conceitos.

---

## Arquitetura do Projeto

O projeto está dividido em duas camadas principais:

* **Front-end:** Responsável pela interface com o usuário
* **Back-end:** Responsável pelas regras de negócio, persistência de dados e integração com serviços externos

---

## Front-end

### Tecnologias utilizadas

* **React**
* **JavaScript
* **CSS** para estilização

### Funcionalidades

* Tela de **listagem de caminhões** em formato de tabela
* Tela de **cadastro de caminhões** com formulário dedicado
* **Validação de campos** no formulário
* **Tratamento e exibição de mensagens de erro** retornadas pelo back-end
* Separação de responsabilidades entre componentes e serviços

---

## Back-end

### Tecnologias utilizadas

* **Python**
* **Django**
* **Django ORM**
* **Pytest** para testes automatizados
* **Requests** para integração com API externa

### Estrutura

O back-end segue a **estrutura padrão do Django**, criada a partir do comando:

```bash
django-admin startproject agroe_api
```

Por se tratar do primeiro projeto utilizando Django, foi adotada a organização nativa do framework, priorizando clareza e entendimento do fluxo da aplicação.

Foi configurado um **ambiente virtual (.env)** para isolamento das dependências do projeto.

---

### Regras de Negócio (Services)

As regras de negócio foram centralizadas em **classes de serviço**, promovendo:

* Melhor organização do código
* Facilidade de manutenção
* Testabilidade
* Separação entre lógica de negócio e camada de apresentação

---

## 🧪 Testes Automatizados

Foram implementados **testes automatizados com pytest**, focados nas **classes de serviço**, garantindo:

* Validação das regras de negócio
* Maior confiabilidade e segurança na evolução do código

---

## Integrações

* **API da Tabela FIPE** para validação de modelos de caminhões

---

## Objetivos do Projeto

* Aplicar conceitos de **desenvolvimento full stack**
* Praticar **React no front-end** e **Django no back-end**
* Implementar **boas práticas**, como services e testes automatizados


