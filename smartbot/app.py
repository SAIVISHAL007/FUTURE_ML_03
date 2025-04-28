from flask import Flask, request, jsonify, render_template
import brain
import traceback

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({'response': 'Please enter a message.'}), 400

        # Print for debugging
        print(f"Received message: '{user_message}'")
        
        intent = brain.find_intent(user_message)
        print(f"Found intent: '{intent}'")
        
        response = brain.get_response(intent)
        print(f"Generated response: '{response}'")
        
        return jsonify({'response': response})
    except Exception as e:
        print(f"Error in chat route: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'response': 'Sorry, something went wrong. Please try again later.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
