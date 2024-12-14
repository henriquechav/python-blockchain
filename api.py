from blockchain import Blockchain
from flask import Flask, jsonify, request
from uuid import uuid4
import time

app = Flask(__name__)

# Gera um endereço globalmente único para este nó 
node_identifier = str(uuid4()).replace('-', '')

# Instancia a blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    # Executamos o algoritmo de prova de trabalho para pegar a próxima prova...
    # e contamos o tempo decorrido
    last_block = blockchain.last_block
    
    start = time.time()

    ### CASO HASHCASH OU SCRYPT ###
    proof = blockchain.proof_of_work(last_block)

    ### CASO PRIMECOIN ###
    # proof = blockchain.proof_of_work()
    
    end = time.time()
    elapsed = end - start

    # Devemos receber uma recompensa por encontrar a prova.
    # O pagador é "0" para indicar que este nó minerou uma nova moeda.
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    # Forja um novo bloco e o adiciona na cadeia
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "Novo bloco forjado",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
        'time': f"Levou {elapsed} segundos para minerar este bloco.",
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    # Checa se os campos requeridos estão nos dados enviados
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400
    
    # Cria uma nova transação
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'A transação será adicionada ao bloco {index}'}
    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
