from time import time
import hashlib
import json

class Blockchain:
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        # self.nodes = set()

        # Cria o bloco de gênese
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Cria um novo bloco na blockchain

        :param proof: <int> A prova dada pelo algoritmo de prova de trabalho
        :param previous_hash: <string> Hash do último bloco
        :return: <dict> Novo bloco
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reseta a atual lista de transações
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Cria uma nova transação para ir no próximo bloco minerado

        :param sender: <string> Endereço do pagador
        :param recipient: <string> Endereço do recebedor
        :param amount: <float> Valor
        :return: <int> O índice do bloco que guardará esta transação
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Cria um hash SHA-256 de um bloco

        :param block: <dict> Bloco
        :return: <string> Hash
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """
        Retorna o último bloco na cadeia

        :return: <dict> Último bloco
        """
        return self.chain[-1]
    
    def proof_of_work(self, last_block):
        """
        Algoritmo SHA-256 de mineração do bitcoin:
        - Encontra um número p' tal que o hash(pp') começa com 4 zeros, onde p é o p' anterior
        - p é a prova anterior, e p' é a nova prova
        
        :param last_block: <dict> Último bloco
        :return: <int> Prova
        """
        last_proof = last_block['proof']
        last_hash = self.hash(last_block)

        proof = 0
        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1

        return proof
    
    @staticmethod
    def valid_proof(last_proof, proof, last_hash):
        """
        Valida a prova

        :param last_proof: <int> Prova anterior
        :param proof: <int> Prova atual
        :param last_hash: <str> O hash do bloco anterior
        :return: <bool> True se correto, False se não.
        """
        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
