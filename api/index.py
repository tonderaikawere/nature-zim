from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Nature Zimbabwe - Test</h1>
    <p>If you see this, the Flask app is working on Vercel!</p>
    <p>Created by Tonde for nature education.</p>
    '''

@app.route('/api')
def api():
    return {'message': 'API is working', 'status': 'success'}

if __name__ == '__main__':
    app.run(debug=True)
