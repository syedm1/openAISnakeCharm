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
        response1 = openai.Completion.create(
            model= OPEN_AI_ENGINE,
            messages=conversation,
        )

        print(response1)
        response= openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": "Who won the world series in 2020?"},
                        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                        {"role": "user", "content": "Where was it played?"}
                    ]
                )
        # Return the generated text as a response
        return jsonify({'data': response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
