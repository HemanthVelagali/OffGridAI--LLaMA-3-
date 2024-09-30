# **OffGridAI-(LLaMA 3)**

**OffGridAI-(LLaMA 3)** is a locally hosted, privacy-first chatbot powered by the LLaMA 3 model. It runs entirely offline on your machine, ensuring data security and confidentiality by eliminating the need for internet connections or third-party APIs. This project is designed for users who value control, customization, and privacy in their AI interactions.

## **Key Features**

- **Local AI Processing**: All computations are done locally, ensuring maximum privacy.
- **Powered by LLaMA 3**: Built on Meta’s LLaMA 3 model for high-quality language understanding and generation.
- **No Cloud Dependency**: No need for APIs or internet access—everything runs on your hardware.
- **Speech-to-Text**: Integrated support for voice input and audio transcription.
- **PDF Reading**: Interact with AI based on the content of uploaded PDF files.
- **Customizable**: Easily add new features or swap models to tailor the assistant for your needs.

## **Installation**

### **Prerequisites**

1. Install [Python 3.x](https://www.python.org/downloads/).
2. Install necessary dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
## **Installation**

1. **Install Ollama** to load and run the LLaMA 3 model locally.

2. **Download the LLaMA 3 model** using the `ollama` command:

   ```bash
   ollama pull llama3  pyhton app.py
3.Ensure that Ollama is running and the LLaMA 3 model is loaded.

###**Running the Application**
1.Start the application:
      ```bash
   ollama pull llama3  pyhton app.py```

Interact with the chatbot by accessing###**[Running the Application](http://localhost:5000)** in your browser.

   
Usage
Once the server is running, you can interact with the AI assistant locally. Features include:

Text Input: Type questions or commands and receive responses powered by LLaMA 3.
Voice Input: Use the integrated microphone button to input commands by voice.
PDF Upload: Upload a PDF file, and the chatbot will use its content to answer questions.
Contributing
We welcome contributions! If you'd like to improve the project or fix issues, please fork the repository and submit a pull request.

License
This project is licensed under the MIT License. See the section below on how to create a license file.

Acknowledgments
LLaMA 3 by Meta
Ollama for enabling local LLM integration.
