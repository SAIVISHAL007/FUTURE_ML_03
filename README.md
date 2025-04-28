# FUTURE_ML_03


## Customer Support Chatbot:

## Project Overview
This project is a rule-based customer support chatbot designed to streamline common support interactions. It leverages simple Natural Language Processing techniques to interpret user queries and generate context-aware responses using a CSV-based dataset of predefined intents, patterns, and responses.

## Skills Gained
- **Natural Language Processing (NLP)**: Building foundational techniques in text preprocessing and keyword-based intent recognition.
- **Chatbot Development**: Creating a modular and maintainable solution for handling customer queries.
- **Data Preprocessing**: Utilizing regular expressions to normalize and clean user inputs.
- **Web Development**: Integrating a Flask-based web interface with HTML, CSS, and JavaScript for a real-time interactive experience.
- **Error Handling**: Implementing robust mechanisms to gracefully handle unexpected inputs or system errors.

## Tools & Libraries Used
- **Python**: Core programming language.
- **Flask**: For building the web server and API endpoints.
- **Pandas**: To manage and parse the CSV dataset of intents.
- **Regular Expressions (re)**: For efficient text cleaning and normalization.
- **HTML, CSS, JavaScript**: For building and styling the interactive chat interface.

## Dataset
The chatbot's responses are driven by an `intents.csv` file, which contains:
- **Intent**: The category of the support query (e.g., technical_issue, refund_request, greeting).
- **Patterns**: Sample user phrases separated by a pipe (`|`) used to recognize the intent.
- **Responses**: Predefined messages that are returned based on the identified intent.

## Architecture & Implementation
- **Preprocessing**: Every user input is cleaned by the `preprocess.py` module (lowercasing and removing special characters) to ensure consistent pattern matching.
- **Intent Recognition**: The core logic in `brain.py` iterates through the CSV dataset to match cleaned inputs against known patterns.
- **Response Generation**: Once an intent is identified, the corresponding response is retrieved and sent back to the user.
- **Dual Interface**:  
  - A **web interface** served by Flask provides a dynamic and modern chat UI.
  - A **command-line interface (CLI)** allows for quick testing and development.

## Future Enhancements
- Integrate advanced NLP models to support multi-turn dialog and contextual conversations.
- Expand and refine the dataset with more comprehensive customer queries.
- Implement sentiment analysis to dynamically adjust responses based on user mood.
- Enhance the web interface with additional interactive and visual elements.

