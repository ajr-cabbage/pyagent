# Chatbot with Gemini API

This project is a chatbot that utilizes the Gemini API with function calling capabilities. It allows for interactive conversations and can execute specific functions based on user prompts.

## Features

- **Gemini API Integration**: Leverages the power of the Gemini API for natural language understanding and generation.
- **Function Calling**: Capable of identifying and executing predefined functions based on the context of the conversation.
- **Configurable**: Uses `.env` for API key management and `system_prompt.py` for defining system instructions.
- **Verbose Output**: Supports a verbose mode for detailed logging of prompt and response tokens, as well as function call results.

## Setup

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    (Assuming a `requirements.txt` file exists, or equivalent if using `pyproject.toml` and a lock file like `uv.lock`)

3.  **Set up environment variables**:
    Create a `.env` file in the root directory and add your Gemini API key:
    ```
    GEMINI_API_KEY=YOUR_GEMINI_API_KEY
    ```

## Usage

Run the chatbot from the command line:

```bash
python main.py "Your prompt here"
```

For verbose output, use the `--verbose` flag:

```bash
python main.py "What is the weather like?" --verbose
```

## Project Structure

-   `main.py`: The main script to run the chatbot.
-   `functions/`: Directory containing available functions that the chatbot can call.
-   `system_prompt.py`: Defines the system instructions for the Gemini model.
-   `.env`: Environment variables, including the Gemini API key.
-   `README.md`: This file.
