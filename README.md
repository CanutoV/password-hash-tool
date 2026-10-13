<div id="top">

<div align="center">

# 🔐 Password Hash Tool

<em>Validador de complexidade de senhas e gerador de hashes criptográficos via linha de comando.</em>

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Cybersecurity-Auth%20%26%20Hashes-red?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

</div>

---

## 📋 Sumário

- [Visão Geral](#-visão-geral)
- [Funcionalidades](#-funcionalidades)
- [Pré-requisitos e Instalação](#-pré-requisitos-e-instalação)
- [Como Usar](#-como-usar)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Conceitos de Cibersegurança](#-conceitos-de-cibersegurança)

---

## 🛠️ Visão Geral

O **Password Hash Tool** é uma ferramenta interativa em Python desenvolvida para análise e auditoria rápida de segurança de credenciais. A aplicação avalia a força de uma senha fornecida em tempo real com base em critérios de entropia e complexidade, gerando simultaneamente suas representações em algoritmos de hash amplamente utilizados no mercado.

---

## ✨ Funcionalidades

- **Entrada Segura:** Utiliza a biblioteca nativa `getpass` para ocultar os caracteres digitados no terminal, evitando a exposição visual da senha (*shoulder surfing*).
- **Análise de Complexidade:** Pontua a senha com base em:
  - Comprimento mínimo (8 a 12+ caracteres).
  - Presença de letras maiúsculas e minúsculas.
  - Presença de números e caracteres especiais (`!@#$%^&*`).
- **Geração Multialgorítmica de Hashes:** Computa em tempo real os hashes da senha em:
  - `MD5` *(Inseguro / Apenas para fins demonstrativos)*
  - `SHA-256`
  - `SHA-512`

---

## 🚀 Pré-requisitos e Instalação

A aplicação utiliza **apenas a biblioteca padrão do Python** (`hashlib`, `re`, `getpass`), não exigindo a instalação de nenhuma dependência externa via `pip`.

1. **Clone o repositório:**
   ```bash
   git clone git@github.com:canutov/password-hash-tool.git