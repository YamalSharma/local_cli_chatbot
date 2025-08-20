echo "# Local CLI Chatbot — SmolLM-360M-Instruct

This project is a simple, lightweight command-line chatbot built with Hugging Face’s SmolLM-360M-Instruct model. It maintains conversation context using a sliding window memory buffer to deliver coherent multi-turn conversations.

---

## Features

- Loads and runs the small SmolLM-360M-Instruct language model locally
- Maintains short-term conversation history (last 3 turns) for context
- Robust CLI interface accepting continuous user input
- Gracefully terminates on /exit command
- Modular Python codebase for easy maintenance and extension

---

## Setup Instructions

1. Ensure you have **Python 3.8+** installed on your system.

2. Clone or download this project folder.

3. Install required dependencies via pip:

   \`\`\`
   pip install -r requirements.txt
   \`\`\`

   The main dependencies are:
   - transformers (Hugging Face Transformers library)
   - torch (PyTorch)

4. The first run will download the SmolLM-360M-Instruct model (~small size) from Hugging Face Hub, so ensure an internet connection on the initial launch.

---

## How to Run

Navigate to the project folder in your terminal or command prompt and run:

\`\`\`
python interface.py
\`\`\`

You will see the chatbot greeting prompt. Start typing your messages and press Enter to get the bot's response.

To exit the chatbot at any time, type:

\`\`\`
/exit
\`\`\`

---

## Sample Interaction

\`\`\`
Bot: Hello! How can I help you today?
User: What is the capital of France?
Bot: Paris
User: And the capital of Italy?
Bot: Rome
User: Who is the president of the United States?
Bot: The president of the United States is Joe Biden.
User: /exit
Exiting chatbot. Goodbye!
\`\`\`

---

## Project Structure

- model_loader.py  
  Loads the SmolLM-360M-Instruct model and tokenizer with Hugging Face pipeline for text generation.

- chat_memory.py  
  Implements a sliding window buffer maintaining the last 3 user-bot exchanges to supply context for multi-turn conversations.

- interface.py  
  Main command-line interface script. Manages the input-output loop, constructs prompts, handles model inference, applies output cleaning, and maintains chat memory.

- requirements.txt  
  Lists Python dependencies: transformers and torch.

---

## Notes

- The chatbot uses a sliding window of the last 3 conversation turns to maintain coherence.
- Output cleaning in interface.py removes unwanted trailing content (e.g., repeated prompts, tutorial steps) for smoother conversation.
- Model parameters like max_new_tokens=120, temperature=0.7, and top_p=0.9 are set to balance coherence and creativity.
- The project runs on CPU by default but can leverage GPUs if available.

---

## Optional Improvements

- Fine-tune the model or switch to instruction-tuned variants for better conversational accuracy.
- Enhance prompt formatting and add a system prompt for more specific responses.
- Build a richer interface (e.g., GUI, web app) or add logging and analytics.
- Experiment with memory window size in chat_memory.py.

---

Feel free to explore and customize this project to build your ideal chatbot!

---

# License

This project uses publicly available models and libraries under their respective licenses.
" > README.md
