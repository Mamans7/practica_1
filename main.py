from flask import Flask, request, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/quienes')
def quienes():
  return render_template('quienes.html')

@app.route('/servicios')
def servicios():
  return render_template('servicios.html')

# @app.noticias('/noticias')
# def noticias():
#   return render_template('noticias.html')

@app.route('/contactos')
def contactos():
  return render_template('contactos.html')



if __name__ == '__main__':
  app.run(debug=True)