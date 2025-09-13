from flask import Flask
from threading import Thread
from dotenv import load_dotenv
import webbrowser

load_dotenv()

app = Flask('')

@app.route('/')
def home():
    return '''
    <html>
        <head><title>Discord Server</title></head>
        <body>
            <h1>Welcome to My Discord</h1>
            <h2>Click the Link to Open Discord Server:</h2>
            <a href="https://discord.gg/GT7xnps9" target="_blank">Join My Discord Server</a>
        </body>
    </html>
    '''

def run():
    app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
    webbrowser.open("http://127.0.0.1:8080")
