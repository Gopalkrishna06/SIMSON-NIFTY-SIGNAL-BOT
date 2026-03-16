from flask import Flask, request
from twilio.rest import Client
import os

app = Flask(_name_)

# Twilio credentials from environment variables
TWILIO_SID = os.environ.get('TWILIO_SID')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
TWILIO_WHATSAPP = os.environ.get('TWILIO_WHATSAPP')
YOUR_WHATSAPP = os.environ.get('YOUR_WHATSAPP')

@app.route('/')
def home():
    return 'Simson Nifty Signal Bot is Running! 🚀'

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        
        # Extract signal data from TradingView
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

        # Build WhatsApp message
        message = f"""
🚨 SIMSON SIGNAL BOT 🚨
━━━━━━━━━━━━━━━━
📊 Index: {symbol}
💰 Price: {price}
📈 Signal: {signal}
━━━━━━━━━━━━━━━━
🎯 Action: {action}
⚡ Strike: {strike}
🛑 Stop Loss: {sl}
✅ Target 1: {target1}
✅ Target 2: {target2}
━━━━━━━━━━━━━━━━
📉 RSI: {rsi}
🔮 Trend: {trend}
━━━━━━━━━━━━━━━━
⚠️ Trade at your own risk!
        """

        # Send WhatsApp message
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        client.messages.create(
            body=message,
            from_=f'whatsapp:{TWILIO_WHATSAPP}',
            to=f'whatsapp:{YOUR_WHATSAPP}'
        )

        return {'status': 'success', 'message': 'Signal sent!'}, 200

    except Exception as e:
        return {'status': 'error', 'message': str(e)}, 500

if _name_ == '_main_':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
