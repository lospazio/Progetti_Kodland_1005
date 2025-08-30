from flask import Flask
import random

app = Flask(__name__)

lista_fatti = [
    "Gli elefanti sono gli unici animali che non possono saltare.",
    "Le api comunicano tra loro attraverso una danza chiamata 'danza delle api'.",
    "Il cuore di una balena blu è così grande che un essere umano potrebbe nuotare attraverso le sue arterie.",
    "Le giraffe hanno la lingua lunga circa 45 centimetri.",
    "I polpi hanno tre cuori e il loro sangue è di colore blu.",
    "Le farfalle assaggiano con i piedi.",
    "Il miele non si deteriora mai e può durare per migliaia di anni.",
    "Le stelle marine possono rigenerare i loro bracci se li perdono.",
    "I camaleonti possono muovere i loro occhi in direzioni diverse contemporaneamente.",
    "Le tartarughe possono respirare attraverso il loro sedere."
]

# ACCUANTO PARE SERVE PER LA BARRA DI NAVIGAZIONE
def navbar():
    return '''
    <nav>
        <a href="/">Home</a> |
        <a href="/fatto_casuale">Fatto Casuale</a> |
        <a href="/about">About</a> |
        <a href="/contact">Contact</a> |
        <a href="/help">Help</a> |
        <a href="/services">Services</a> |
        <a href="/products">Products</a> |
        <a href="/blog">Blog</a> |
        <a href="/faq">FAQ</a> |
        <a href="/terms">Terms</a> |
        <a href="/privacy">Privacy</a> |
        <a href="/sitemap">Sitemap</a> |
        <a href="/login">Login</a> |
        <a href="/register">Register</a>
    </nav>
    <hr>
    '''

@app.route("/")
def ciao_mondo():
    return f'''
    {navbar()}
    <p>Benvenuto! <a href="/fatto_casuale">Scopri un fatto casuale!</a></p>
    '''

@app.route("/fatto_casuale")
def fatto_casuale():
    return f'''
    {navbar()}
    <p>{random.choice(lista_fatti)}</p>
    '''

@app.route("/about")
def about():
    return f'''
    {navbar()}
    <p>Questa è una semplice applicazione Flask che mostra fatti casuali sugli animali.</p>
    '''

@app.route("/contact")
def contact():
    return f'''
    {navbar()}
    <p>Contattami a: NUMERO DI TELEFONO</p>
    '''

@app.route("/help")
def help():
    return f'''
    {navbar()}
    <p>Per assistenza, invia un'email a: EMAIL</p>
    '''

@app.route("/services")
def services():
    return f'''
    {navbar()}
    <p>Offriamo servizi di consulenza sugli animali.</p>
    '''

@app.route("/products")
def products():
    return f'''
    {navbar()}
    <p>Vendiamo libri e giocattoli sugli animali.</p>
    '''

@app.route("/blog")
def blog():
    return f'''
    {navbar()}
    <p>Leggi il nostro blog per articoli interessanti sugli animali.</p>
    '''

@app.route("/faq")
def faq():
    return f'''
    {navbar()}
    <p>Domande frequenti sugli animali.</p>
    '''

@app.route("/terms")
def terms():
    return f'''
    {navbar()}
    <p>Termini e condizioni del nostro sito.</p>
    '''

@app.route("/privacy")
def privacy():
    return f'''
    {navbar()}
    <p>Informativa sulla privacy del nostro sito.</p>
    '''

@app.route("/sitemap")
def sitemap():
    return f'''
    {navbar()}
    <p>Mappa del sito.</p>
    '''

@app.route("/login")
def login():
    return f'''
    {navbar()}
    <p>Pagina di login.</p>
    '''

@app.route("/register")
def register():
    return f'''
    {navbar()}
    <p>Pagina di registrazione.</p>
    '''

if __name__ == "__main__":
    app.run(debug=True)
