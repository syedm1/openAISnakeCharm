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

    # Extract the messages from the data
    messages = data['messages']

    # Prepare the conversation history for OpenAI API
    conversation = []
    for message in messages:
        role = message['role']
        content = message['content']
        conversation.append({'role': role, 'content': content})

    try:
        # Make the request to OpenAI API
        response = openai.Completion.create(
            engine= OPEN_AI_ENGINE,
            messages=conversation,
            max_tokens=MAX_TOKENS,
            temperature=0.6,
            n=1,
            stop=None
        )

        # Return the generated text as a response
        return jsonify({'data': response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
