# app.py
import os
from flask import Flask, render_template
# importo la classe mock che simula il database
import mock as db

# costruisco il percorso alla cartella "static" 
# basandomi sul path dell'applicazione corrente
static_file_dir = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "static")

# creo la app passando il percorso della cartella con le risorse statiche
app = Flask(__name__, static_url_path="/static", static_folder=static_file_dir)
 
# carico la pagina
def get_page(id):
    page = db.get(id)
    if page == None:
        # se non trovo la pagina errore 404
        return page_not_found(None)
    # recupero il menu
    menu = db.menu()
    # faccio il render
    return render_template("page.html", menu=menu, page=page) 

# definisco la prima route, home, caricherà la pagina con id=0
@app.route("/")
def main():
    return get_page(0)
  
# la route per caricare le pagine nella forma /pagina/<id>
@app.route("/pagina/<int:id>")
def pagina(id):
    return get_page(id)
  
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404
      
# verifica se è il programma principale
# e manda in esecuzione il web server su http://localhost:5000
# in questo caso in debug, ovvero si riavvia ad ogni cambiamento dei file
if __name__ == "__main__":
    app.run(debug=True, port=5000)
