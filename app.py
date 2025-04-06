from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']
        mensaje = request.form['mensaje']
        print(f"Nombre: {nombre}, Teléfono: {telefono}, Email: {email}, Mensaje: {mensaje}")
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
