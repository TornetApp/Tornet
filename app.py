from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hoş Geldin Tornet!</h1><p>Bu Tornet'in anasayfası.</p>"

if __name__ == "__main__":
    app.run()
