import requests

# Cria novas transações e as envia para o servidor
for x in range(15):
    new_transaction = {
        'sender': 'Bob',
        'recipient': 'Eva',
        'amount': 1,
    }
    response = requests.post('http://localhost:5000/transactions/new', json=new_transaction)
    print(response.json())
