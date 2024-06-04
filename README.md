# langchain_chatbot
LLM chatbot with LangChain


# easy_chatbot.py

## Description:
The `easy_chatbot.py` file contains a chatbot constructed by Langchain using the OpenAI API. This chatbot is designed to facilitate conversations with users by leveraging the capabilities of the OpenAI API. In order to use this chatbot, users will need to configure a `secret.json` file in the same folder after cloning the repository.

## Usage:
To use the chatbot:
1. Clone the repository containing the `easy_chatbot.py` file.
2. Configure a `secret.json` file in the same folder with the necessary API credentials.
```json
{
    "key":"{YOUR-LLM-API-KEY}",
    "langchian_api" : "{YOUR-LANGSMITH_API_KEY}"
}
```
3. Run the `easy_chatbot.py` file to interact with the chatbot.

# testopenai.py

## Description:
The `testopenai.py` file is a program designed to test the connection to the OpenAI API. This program serves as a validation tool to ensure that the connection to the OpenAI API is correctly established and functional.

## Usage:
To test the connection to the OpenAI API:
1. Ensure that the necessary API credentials are correctly configured.
2. Run the `testopenai.py` file to verify the connection status.

# File: trace_langsmith.py

## Description:
The `trace_langsmith.py` file is used to set up an auto-trace function for the Langsmith platform. This file contains the necessary code to enable automated tracing functionality within the Langsmith platform, enhancing its capabilities and performance.

## Usage:
To set up the auto-trace function for the Langsmith platform:
1. Include the `trace_langsmith.py` file in the Langsmith platform project.
2. Configure the auto-trace settings as needed within the file.
3. Execute the `trace_langsmith.py` file to activate the auto-trace feature.

These files provide essential functionalities for interacting with the Langchain chatbot, testing the OpenAI API connection, and enabling auto-trace functionality within the Langsmith platform.