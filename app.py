from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample user data (replace with a database)
users = [{'username': 'user1', 'password': 'password1'}]


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    for user in users:
        if user['username'] == username and user['password'] == password:
            return jsonify({'message': 'Login successful'})
    
    return jsonify({'message': 'Invalid credentials'}), 401


if __name__ == '__main__':
    app.run(debug=True)
