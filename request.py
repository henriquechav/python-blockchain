import requests

# Create a new transaction and send it to the server
for x in range(10):
    new_transaction = {
        'sender': 'Bob',
        'recipient': 'Alice',
        'amount': 4,
    }
    response = requests.post('http://localhost:5000/transactions/new', json=new_transaction)
    print(response.json())

    new_transaction = {
        'sender': 'Eva',
        'recipient': 'Eva',
        'amount': 10,
    }
    response = requests.post('http://localhost:5000/transactions/new', json=new_transaction)
    print(response.json())

    new_transaction = {
        'sender': 'Bob',
        'recipient': 'Eva',
        'amount': 3,
    }
    response = requests.post('http://localhost:5000/transactions/new', json=new_transaction)
    print(response.json())

# # Mine a block
# response = requests.get('http://localhost:5000/mine')
# print(response.json())

# # Get the full chain (better visualization at the browser)
# response = requests.get('http://localhost:5000/chain')
# print(response.json())
