from flask import Flask, render_template_string

app = Flask(__name__)

menu = [
    {"n": "Gelato #33", "p": 35, "t": "1g"},
    {"n": "Tropical", "p": 45, "t": "1g"},
    {"n": "Pinaple Expres", "p": 30, "t": "1g"},
    {"n": "Cítrica", "p": 40, "t": "1g"},
    {"n": "Horlandesa", "p": 25, "t": "1g"},
    {"n": "Regular Kush", "p": 35, "t": "1g"},
    {"n": "Kali OG", "p": 80, "t": "1g"},
    {"n": "Cristal", "p": 120, "t": "Entero"}
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background: #121212; color: white; font-family: sans-serif; text-align: center; padding: 20px; }
        .card { background: #1e1e1e; margin: 10px auto; padding: 15px; border-radius: 12px; border-left: 5px solid #4CAF50; max-width: 350px; box-shadow: 0 4px 10px rgba(0,0,0,0.5); }
        h1 { color: #4CAF50; }
        .precio { font-weight: bold; color: #fff; font-size: 1.1em; }
        .btn { background: #25D366; color: white; padding: 12px; border-radius: 8px; text-decoration: none; display: inline-block; margin-top: 10px; font-weight: bold; }
        .promo { color: #ffca28; font-size: 0.9em; margin-bottom: 20px; }
    </style>
</head>
<body>
    <h1>🌿 Menú ANS</h1>
    <p class="promo">💎 Tarjeta de Lealtad: Compra 5 y la 6ta es regalo</p>
    {% for i in menu %}
    <div class="card">
        <h3>{{ i.n }}</h3>
        <p class="precio">{{ i.t }} — ${{ i.p }}</p>
        <a href="https://wa.me/tu_numero" class="btn">Pedir por WhatsApp</a>
    </div>
    {% endfor %}
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, menu=menu)

if __name__ == '__main__':
    app.run()
