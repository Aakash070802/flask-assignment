from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')

    return jsonify({
        "status": "success",
        "name": name,
        "email": email
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
