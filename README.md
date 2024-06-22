
# Local LLM Deployment and Interaction

###  Youtube tutorial - https://www.youtube.com/watch?v=79mzhwnaW1s
------------------------------------
## Overview

This repository demonstrates how to deploy and interact with large language models (LLMs) locally using different platforms and tools. It provides instructions and examples for setting up and interacting with models using Ollama and GPT4ALL.

## Table of Contents

- [Ollama](#ollama)
  - [Setting up Ollama](#setting-up-ollama)
  - [Model 1: Llama3](#model-1-llama3)
    - [Interaction with the Model](#interaction-with-the-model)
    - [Interaction using curl command](#interaction-using-curl-command)
  - [Model 2: Phi3](#model-2-phi3)
    - [Interaction with the Model](#interaction-with-the-model-1)
    - [Interaction using curl command](#interaction-using-curl-command-1)
- [GPT4ALL](#gpt4all)
  - [Setting up GPT4ALL](#setting-up-gpt4all)
  - [Model 3: Phi3 Mini Using GPT4ALL Chat Client](#model-3-phi3-mini-using-gpt4all-chat-client)
    - [Interaction with the Model](#interaction-with-the-model-2)
  - [Model 4: orca-mini-3b Using GPT4ALL Python Client](#model-4-orca-mini-3b-using-gpt4all-python-client)
    - [Interaction using curl command](#interaction-using-curl-command-2)



## Ollama

Ollama is a platform offering customizable generative AI models for various applications. This section covers setting up Ollama and interacting with two models: Llama3 and Phi3.

### Setting up Ollama

1. **Download Ollama**: Visit the [Ollama GitHub page](https://github.com/Ollama/llama3) and download the installer for your OS.
2. **Install Ollama**: Run the downloaded `OllamaSetup.exe` and follow the prompts to install **(Here i have installed for Windows)**.
3. **Check Installation**: Ensure Ollama is installed in your Programs folder in `C:\Users`.

### Model 1: Llama3

#### Interaction with the Model:

1. **Run Model**: Open a command prompt and execute:
   ```sh
   ollama run llama3
   ```
1. **Ask a question**: Start interacting by typing questions in the prompt.

#### Interaction using curl command: 

1. **Serve Model**: Open a  command prompt and execute:
   ```sh
   ollama serve
   ```
2. **Check Server**: Verify by running:
   ```sh
   curl http://127.0.0.1:11434/
   ```
3. **Generate Completion**: Open a new command prompt and execute:
* Streaming:
   ```sh
   curl -X POST http://127.0.0.1:11434/api/generate -H "Content-Type: application/json" -d "{\"model\": \"llama3\", \"prompt\": \"Why is the sky blue?\"}"
   ```
* No Streaming:
  ```sh
  curl -X POST http://localhost:11434/api/generate -H "Content-Type: application/json" -d "{\"model\": \"llama3\", \"prompt\": \"What is the largest planet in our solar system?\", \"stream\": false}"
  ```
### Model 2: Phi3

#### Interaction with the Model:

1. **Run Model**: Open a command prompt and execute:
   ```sh
   ollama run phi3
   ```
1. **Ask a question**: Start interacting by typing questions in the prompt.

#### Interaction using curl command:

1. **Serve Model**: Open a command prompt and execute:
   ```sh
   ollama serve
   ```
2. **Check Server**: Verify by running:
   ```sh
   curl http://127.0.0.1:11434/
   ```
3. **Generate Completion**: Open a new command prompt and execute:
* Streaming:
   ```sh
   curl -X POST http://127.0.0.1:11434/api/generate -H "Content-Type: application/json" -d "{\"model\": \"phi3\", \"prompt\": \"Why is the sky blue?\"}"
   ```
* No Streaming:
  ```sh
  curl -X POST http://localhost:11434/api/generate -H "Content-Type: application/json" -d "{\"model\": \"phi3\", \"prompt\": \"What is the largest planet in our solar system?\", \"stream\": false}"
  ```
## GPT4ALL

GPT4ALL provides accessible and privacy-friendly LLMs that can be run locally without extensive cloud infrastructure. This section covers setting up GPT4ALL and interacting with models using both the Chat Client and Python Client.

### Setting up GPT4ALL

1. **Choose Client**: Decide whether to use the Chat Client or Python Client.
2. **Download**: Obtain the installer or package from the [GPT4ALL website](https://gpt4all.com/).
3. **Install**: Follow the installation instructions specific to your chosen client.

### Model 3: Phi3 Mini Using GPT4ALL Chat Client
#### Interaction with the Model
1. **Install**: Download and install the Chat Client from the [GPT4ALL website](https://gpt4all.com/).
2. **Run**: After installation, search for and open the GPT4ALL application.
3. **Chat**: Select the `Phi3 Mini` model and start interacting.

### Model 4: orca-mini-3b Using GPT4ALL Python Client
1. **Setup Virtual Environment**:
    ```sh
    python -m venv gpt4all-venv
    ```
2. **Activate Environment**:
    ```sh
    gpt4all-venv\Scripts\activate
    ```
3. **Install GPT4ALL**:
    ```sh
    pip install gpt4all
    ```
4. **Install Flask**:
    ```sh
    pip install flask
    ```
5. **Create a script to start server**: Create a Python script named `gpt4all_server.py` with the following content to start the server: 

   ```python
   from gpt4all import GPT4All
   from flask import Flask, request, jsonify
   
   app = Flask(__name__)
   model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
   
   @app.route('/api/generate', methods=['POST'])
   def generate():
    try:
        data = request.json
        prompt = data.get('prompt')
        response = model.generate(prompt)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500   

    if __name__ == '__main__':
    app.run(port=5000)
    ```
6.  **Now, run the server**:
    ```sh
    python gpt4all_server.py
    ```
    And then our server will be running on http://127.0.0.1:5000
#### Interaction using curl command: 
Open a new command prompt and execute:
```sh
curl -X POST http://localhost:5000/api/generate -H "Content-Type: application/json" -d "{\"prompt\": \"Write a Python function to calculate the factorial of a number.\", \"max_tokens\": 50}"
```

```sh
curl -X POST http://localhost:5000/api/generate -H "Content-Type: application/json" -d "{\"prompt\": \"Tell me how to cook pasta?\", \"max_tokens\": 50}"
```

