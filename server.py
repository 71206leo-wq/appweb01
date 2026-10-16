from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('index.html', titulo="Home", mensaje="Bienvenido a mi sitio web")


@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

def contacto():
    return render_template('contacto.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

if __name__ == '__main__':
    app.run(debug=True, port=5050)
    
