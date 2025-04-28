import pandas as pd
import preprocess

# Load chatbot intents with correct parser settings
try:
    # Skip the first line which contains a comment
    data = pd.read_csv('intents.csv', 
                      comment='//', 
                      engine='python',
                      quotechar='"',
                      escapechar='\\',
                      on_bad_lines='skip')
    print(f"Successfully loaded {len(data)} intents")
except Exception as e:
    print(f"Error loading intents.csv: {str(e)}")
    # Create an empty DataFrame with required columns as fallback
    data = pd.DataFrame(columns=['Intent', 'Patterns', 'Responses'])
    # Add a default greeting intent
    data = data.append({
        'Intent': 'greeting',
        'Patterns': 'hello|hi|hey',
        'Responses': 'Hello! How can I help you today?'
    }, ignore_index=True)

def find_intent(user_message):
    """
    Find intent based on keyword matching.
    """
    try:
        user_message = preprocess.clean_text(user_message)
        
        for index, row in data.iterrows():
            patterns = row['Patterns'].split('|')
            for pattern in patterns:
                if preprocess.clean_text(pattern) in user_message:
                    return row['Intent']
        return None
    except Exception as e:
        print(f"Error in find_intent: {str(e)}")
        return None

def get_response(intent):
    """
    Get response based on intent.
    """
    try:
        if intent:
            matches = data[data['Intent'] == intent]
            if not matches.empty:
                row = matches.iloc[0]
                return row['Responses']
        return "I'm sorry, I didn't understand. Could you please rephrase?"
    except Exception as e:
        print(f"Error in get_response: {str(e)}")
        return "I'm sorry, I couldn't generate a response."
