from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_API_KEY')

OPEN_AI_ENGINE = 'gpt-3.5-turbo'
MAX_TOKENS = 2000

# Define a route for the API endpoint
@app.route('/messages', methods=['POST'])
def openai_request():
    # Get the data from the request
    data = request.json

    print(data)
    # Extract the messages from the data
    conversation = data['messages']

    print(conversation)

    try:

        response= openai.ChatCompletion.create(
                model=OPEN_AI_ENGINE,
                messages=conversation,
                max_tokens=MAX_TOKENS,
                temperature=0.9,
                )
        # Return the generated text as a response
        return jsonify({'data': response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
