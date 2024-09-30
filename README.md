# OffGridAI (LLaMA 3)

**OffGridAI (LLaMA 3)** is a privacy-focused, locally hosted chatbot powered by the LLaMA 3 model. Designed to operate entirely offline, it ensures data security and confidentiality by eliminating reliance on internet connections or third-party APIs. This project is ideal for users who prioritize control, customization, and privacy in their AI interactions.

## Key Features

- **Local AI Processing**: All computations occur on your machine, providing maximum privacy.
- **LLaMA 3 Powered**: Utilizes Meta’s LLaMA 3 model for superior language understanding and generation capabilities.
- **No Cloud Dependency**: Operates without the need for APIs or internet access—everything runs locally.
- **Speech-to-Text Functionality**: Supports voice input and transcription for seamless interaction.
- **PDF Interaction**: Allows users to upload PDF files and engage with the content through the chatbot.
- **Customizable Architecture**: Easily add or swap features and models to tailor the assistant to your specific needs.

## Installation

### Prerequisites

1. Download and install [Python 3.x](https://www.python.org/downloads/).
2. Install the required dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
Install Ollama to load and run the LLaMA 3 model locally.

Download the LLaMA 3 model with the following command:

bash
Copy code
ollama pull llama3
Running the Application
Make sure Ollama is running and the LLaMA 3 model is properly loaded.

Start the application using the command:

bash
Copy code
python app.py
Access the chatbot by navigating to http://localhost:5000 in your web browser.

Usage
After starting the server, you can interact with your AI assistant locally. Features include:

Text Input: Enter questions or commands to receive responses from LLaMA 3.
Voice Input: Utilize the integrated microphone button to input commands via speech.
PDF Upload: Upload a PDF file for the chatbot to reference when answering questions.
Contributing
Contributions are welcome! If you'd like to enhance the project or address issues, please fork the repository and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more information.

Acknowledgments
LLaMA 3: Developed by Meta.
Ollama: For facilitating local integration of large language models.
