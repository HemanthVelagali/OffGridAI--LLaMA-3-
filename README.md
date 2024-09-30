
# OffGridAI (LLaMA 3)

**OffGridAI (LLaMA 3)** is a privacy-focused, locally hosted chatbot built upon the powerful LLaMA 3 model from Meta. Designed for entirely offline operation, it prioritizes data security and confidentiality by eliminating reliance on external servers and APIs. This project empowers users who value control, customization, and privacy in their AI interactions.

## Key Features

* **Local AI Processing:** All computations occur on your device, maximizing privacy and reducing potential security risks.
* **LLaMA 3 Powered:** Leverages the advanced language understanding and generation capabilities of Meta's LLaMA 3 model.
* **No Cloud Dependency:** Operates entirely offline, freeing you from internet connections and third-party APIs.
* **Speech-to-Text Functionality:** Accepts voice input and transcription for a natural interaction experience.
* **PDF Interaction:** Allows uploading and engaging with PDF content through the chatbot interface.
* **Customizable Architecture:** Offers flexibility to add or swap features and models, tailoring the assistant to your specific needs.

## Installation

**Prerequisites**

1. **Download and install Python 3.x:** [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt 

3.  **To install Ollama, run the command:**
    
     ```bash
     pip install -r requirements.tx
   
    
4.  **Download the LLaMA 3 model:** (Important Note: Refer to Meta's official guidelines for LLaMA 3 distribution and potential access requirements.)
    
    ```bash
    pip install ollama

## Running the Application

1.  Ensure Ollama is running and the LLaMA 3 model is loaded successfully.
    
2.  Start the application:
    
	   ```bash
	  python app.py 
     
    
3.  Access the chatbot: Open **[http://localhost:5000](http://localhost:5000)** in your web browser.
    

## Usage

After launching the server, you can interact with your AI assistant locally:

-   **Text Input:** Type questions or commands to receive responses powered by LLaMA 3.
-   **Voice Input:** Utilize the microphone icon (if available) for voice-based interaction.
-   **PDF Upload:** Upload PDFs for the chatbot to reference while answering inquiries.

## Contributing

We welcome contributions! If you'd like to enhance this project or address issues, feel free to fork the repository and send a pull request.

## License

This project is licensed under the MIT License (see the LICENSE file for details).

## Acknowledgments

-   **LLaMA 3:** Developed by Meta.
-   **Ollama:** Facilitates local integration of large language models
