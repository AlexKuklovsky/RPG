from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/Dungeon_Master')
def dungeon_master():
    return render_template('Dungeon_Master.html')

@app.route('/cesta1')
def cesta1():
    return render_template('cesta1.html')

if __name__ == '__main__':
    app.run(debug=True)