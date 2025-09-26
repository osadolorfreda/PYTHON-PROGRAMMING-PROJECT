from Flask import Flask, request, jsonify# type: ignore
from blockchain import FinanceApp # type: ignore
from import predict_stock_price# type: ignore
from _sqlite3 import insert_transaction, get_transactions

app = Flask(__name__)

# Create instance of smart contract
finance_app = FinanceApp()

# Predict stock price endpoint
@app.route('/predict_stock_price', methods=['POST'])
def predict_stock_price_endpoint():
    data = request.get_json()
    stock_symbol = data['stock_symbol']
    prediction = predict_stock_price(stock_symbol)
    return jsonify({'prediction': prediction})

# Make transaction endpoint
@app.route('/make_transaction', methods=['POST'])
def make_transaction_endpoint():
    data = request.get_json()
    user_id = data['user_id']
    amount = data['amount']
    type = data['type']
    timestamp = data['timestamp']
    insert_transaction(user_id, amount, type, timestamp)
    return jsonify({'message': 'Transaction successful'})

# Get transactions endpoint
@app.route('/get_transactions', methods=['POST'])
def get_transactions_endpoint():
    data = request.get_json()
    user_id = data['user_id']
    transactions = get_transactions(user_id)
    return jsonify({'transactions': transactions})

if __name__ == '__main__':
    app.run(debug=True)

