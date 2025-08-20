# Local CLI Chatbot — SmolLM-360M-Instruct

A lightweight command-line chatbot built with **Hugging Face’s SmolLM-360M-Instruct** model.  
It maintains a sliding memory buffer to deliver coherent multi-turn conversations in a minimal setup.

---

## Features

- Runs entirely **locally** using a small instruction-tuned model  
- **Context-aware** responses with sliding window memory (last 3 turns)  
- **Simple CLI interface** for continuous chatting  
- Graceful shutdown using `/exit` command  
- **Modular codebase** for easy extension and maintenance  

---

## Installation

### Requirements
- Python **3.8+**
- `torch`
- `transformers`

### Steps
1. Clone or download this repository.  
2. Install dependencies:
   ```bash
   pip install transformers torch
   ```
3. On first run, the model (~360M) will be downloaded automatically from Hugging Face Hub.

---

## Usage

Navigate to the project folder and run:

```bash
python interface.py
```

- Start typing messages to chat with the bot.  
- To exit:
```bash
/exit
```

---

## Example Conversation

```
Bot: Hello! How can I help you today?
User: What is the capital of France?
Bot: Paris
User: And the capital of Italy?
Bot: Rome
User: Who is the president of the United States?
Bot: The president of the United States is Joe Biden.
User: /exit
Exiting chatbot. Goodbye!
```

---

## Project Structure

```
├── model_loader.py    # Loads model & tokenizer with Hugging Face pipeline
├── chat_memory.py     # Sliding window buffer (last 3 exchanges)
├── interface.py       # Main CLI loop, handles prompts & responses
```

---

## Technical Notes

- **Memory**: Sliding window of last 3 exchanges for contextual answers  
- **Output cleaning**: Removes redundant trailing content for smooth responses  
- **Model parameters**:  
  - `max_new_tokens=120`  
  - `temperature=0.7`  
  - `top_p=0.9`  

- **Hardware**: Runs on CPU by default  

---


## License

This project relies on **publicly available models and libraries** under their respective licenses.  
