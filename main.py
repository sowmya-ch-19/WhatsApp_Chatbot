from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace these with your Gupshup details
GUPSHUP_API_KEY = 'YOUR_GUPSHUP_API_KEY'
WHATSAPP_SANDBOX_NUMBER = 'YOUR_WHATSAPP_SANDBOX_NUMBER'  # This is the number provided by Gupshup for testing
YOUR_NUMBER = 'YOUR_NUMBER'  # The number you've verified with Gupshup for testing

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received data:", data)  # Log data for debugging

    # Extract message details
    incoming_msg = data['payload']['payload']['text']
    sender = data['payload']['sender']['phone']

    # Simple auto-reply logic
    if 'hi' in incoming_msg.lower():
        reply = "Hello! How can I assist you?"
        send_message(sender, reply)

    return jsonify(success=True), 200

def send_message(to, message):
    url = f"https://api.gupshup.io/sm/api/v1/msg"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'apikey': GUPSHUP_API_KEY,
    }
    data = {
        'channel': 'whatsapp',
        'source': WHATSAPP_SANDBOX_NUMBER,
        'destination': to,
        'message': message,
        'src.name': 'YOUR_GUPSHUP_APP_NAME'  # Replace with your Gupshup app name
    }
    response = requests.post(url, headers=headers, data=data)
    print("Sent message response:", response.json())

if __name__ == '__main__':
    app.run(port=5000, debug=True)
