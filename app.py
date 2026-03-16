from flask import Flask, request
from twilio.rest import Client
import os

app = Flask(__name__)

TWILIO_SID = os.environ.get('TWILIO_SID')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
TWILIO_WHATSAPP = os.environ.get('TWILIO_WHATSAPP')
YOUR_WHATSAPP = os.environ.get('YOUR_WHATSAPP')

@app.route('/')
def home():
    return 'Simson Nifty Signal Bot is Running!'

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        symbol = data.get('symbol', 'NIFTY')
        signal = data.get('signal', '')
        price = data.get('price', '')
        rsi = data.get('rsi', '')
        trend = data.get('trend', '')
        strike = data.get('strike', '')
        action = data.get('action', '')
        sl = data.get('sl', '')
        target1 = data.get('target1', '')
        target2 = data.get('target2', '')

        message = (
            "SIMSON SIGNAL BOT\n"
            "Index: " + symbol + "\n"
            "Price: " + price + "\n"
            "Signal: " + signal + "\n"
            "Action: " + action + "\n"
            "Strike: " + strike + "\n"
            "Stop Loss: " + sl + "\n"
            "Target 1: " + target1 + "\n"
            "Target 2: " + target2 + "\n"
            "RSI: " + rsi + "\n"
            "Trend: " + trend + "\n"
            "Trade at your own risk!"
        )

        client = Client(TWILIO_SID, TWILIO_TOKEN)
        client.messages.create(
            body=message,
            from_="whatsapp:" + TWILIO_WHATSAPP,
            to="whatsapp:" + YOUR_WHATSAPP
        )

        return {"status": "success"}, 200

    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
