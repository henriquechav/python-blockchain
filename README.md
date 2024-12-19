# Blockchain em Python

Esta blockchain foi implementada para realizar o projeto da disciplina de Segurança de Redes na UFABC. Além do código fonte, ela conta com uma simples API, feita usando Flask, permitindo a interação com o usuário. A referência para sua construção está neste [link](https://bimoputro.medium.com/build-your-own-blockchain-in-python-a-practical-guide-f9620327ed03).

## Detalhes

A proposta do trabalho foi testar três diferentes funções de prova de trabalho em uma blockchain simples. As funções testadas foram: hashcash, primecoin e scrypt. Nos arquivos `blockchain.py` e `api.py` estão as três funções. Para usar uma em específico, basta descomentá-la e por as demais como comentários.

No repositório também está o relatório dos testes e os slides usados na apresentação final da disciplina.

## Como usar

Para interagir com a blockchain, recomendo criar um ambiente virtual (virtual environment) do Python no diretório do código fonte. Isso pode ser feito usando o comando `python -m venv meu_ambiente_virtual` no terminal.

Depois, para ativá-lo, digite `meu_ambiente_virtual\Scripts\activate` caso esteja usando Windows, ou `source meu_ambiente_virtual/bin/activate` caso esteja usando MacOS ou Linux.

Para instalar as dependências do projeto digite `pip install -r requirements.txt`.

Por fim, execute o arquivo `api.py` e teste a blockchain.
