 # WhatsApp Chatbot
WhatsApp Chatbot is a simple chabot which responds to predefined messages . The chatbot is capable of receiving messages from WhatsApp, processing them, and sending responses back to the user using Gupshup as a API.
## Features
* Automated Responses: Chatbots can automatically respond to customer inquiries 24/7, ensuring that customer engagement is maintained even outside of business hours.

* Natural Language Processing (NLP): Many sophisticated WhatsApp chatbots are equipped with NLP capabilities, allowing them to understand and process user queries in a natural, conversational manner.

* Interactive Messaging: Chatbots can use rich media and interactive elements like buttons, quick replies, and carousels to provide a more engaging and intuitive user experience.

* Personalization: With access to user data and conversation history, chatbots can deliver personalized experiences, addressing users by name and tailoring responses to their specific needs and preferences.

## Prerequisities
Before you begin, ensure you have met the following requirements:

* Python 3.6 or higher installed on your machine
* A Gupshup account for WhatsApp API access
* Ngrok (for local development and testing)

## Installing

A step-step series of examples that tell you how to get a development environment running:


#### 1. Clone the repo:

git clone 

`https://github.com/your-username/whatsapp-chatbot-flask-gupshup.git`

#### 2. Navigate to the project directory:

cd whatsapp-chatbot-flask-gupshup

#### 3. Create and Activate Virtual Environent :
For Unix/Linux Systems:

`python3 -m venv env
source env/bin/activate`

For Windows:

`python -m venv env
.\env\Scripts\activate`

#### 4. Install Dependencies:
pip install -r requirements.txt

#### 5. Setup Gupshup
* Log in to your Gupshup account and create a new WhatsApp bot.
* Note down the API key and WhatsApp bot name provided by Gupshup.

#### 6. Environment Variables
Create a `.env` file in the root directory of the project and add the following:

`GUPSHUP_API_KEY=your_gupshup_api_key`
`GUPSHUP_BOT_NAME=your_gupshup_bot_name`
`FLASK_APP=app.py`

Replace `your_gupshup_api_key` and `your_gupshup_bot_name` with the actual API key and bot name provided by Gupshup.

#### 7. Run the Flask Application

`flask run`

#### 8. Expose Local Server using Ngrok

To allow WhatsApp to send messages to your local server, use Ngrok to expose your local server to the internet.

`ngrok http 5000`

Copy the HTTPS forwarding address provided by Ngrok (e.g., `https://12345.ngrok.io`) and use it in the webhook configuration in your Gupshup dashboard.

## Usage
Once everything is set up, your WhatsApp chatbot should be able to receive messages sent to your WhatsApp number connected through Gupshup and respond based on the logic you've implemented in `app.py`.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.














