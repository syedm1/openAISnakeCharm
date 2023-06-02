from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set up your OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Define a route for the API endpoint
@app.route('/messages', methods=['POST'])
def openai_request():
    # Get the data from the request
    data = request.json

    # Extract the messages from the data
    messages = data['messages']

    return jsonify({'completion': messages})
    # Prepare the conversation history for OpenAI API
    conversation = []
    for message in messages:
        role = message['role']
        content = message['content']
        conversation.append({'role': role, 'content': content})

    try:
        # Make the request to OpenAI API
        response = openai.Completion.create(
            engine='davinci',
            messages=conversation,
            max_tokens=100,
            temperature=0.6,
            n=1,
            stop=None
        )

        # Get the generated completion text from the response
        completion_text = response.choices[0].message['content']

        # Return the generated text as a response
        return jsonify({'completion': completion_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
