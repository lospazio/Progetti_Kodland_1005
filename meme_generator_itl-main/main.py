# Import
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Form results
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # ottenere l'immagine selezionata
        selected_image = request.form.get('image-selector')

        # Consegna #2. Ricevere il testo
        testo_sopra = request.form.get('textTop')
        testo_sotto = request.form.get('textBottom')

        # Consegna #3. Ricezione del posizionamento del testo
        testo_sopra_y = request.form.get('textTop_Y')
        testo_sotto_y = request.form.get('textBottom_Y')

        # Consegna #3. Ricezione del colore del testo
        colore_selezionato = request.form.get('color-selector')

        return render_template('index.html', 
                               # Visualizzazione dell'immagine selezionata
                               selected_image=selected_image, 

                               # Consegna #2. Visualizzazione del testo
                               testo_sopra=testo_sopra,
                               testo_sotto=testo_sotto,

                               # Consegna #3. Visualizzazione del posizionamento del testo
                               testo_sopra_y=testo_sopra_y,
                               testo_sotto_y=testo_sotto_y,

                               # Consegna #3. Visualizzazione del colore 
                               colore_selezionato=colore_selezionato
                               )
    else:
        # Visualizzazione predefinita della prima immagine
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
