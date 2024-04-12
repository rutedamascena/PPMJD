from flask import Flask, render_template, url_for, request
from raspador import dados_html 
from raspador import enviar_email_com_html

app = Flask(__name__, template_folder='templates')


@app.route('/dinamica')
def dinamica():
    return render_template('dinamica.html',dados_html=dados_html)

@app.route('/processar_busca', methods=['POST'])
def processar_busca():
    destinatario_email = request.form['destinatario_email']
    print(destinatario_email)
    enviar_email_com_html(dados_html, destinatario_email)
    return render_template('dinamica.html', dados_html=dados_html)


@app.route('/destinatarios', methods=['POST'])
def enviar_email():
    destinatario_email = request.form['destinatario_email']
    enviar_email_com_html(dados_html)
    return render_template('dinamica.html', destinatario_email,dados_html=dados_html)