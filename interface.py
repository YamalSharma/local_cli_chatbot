from model_loader import load_model
from chat_memory import ChatMemory

def main():
    print("Local Chatbot (SmolLM-360M-Instruct)")
    print("Type /exit to quit.\n")

    memory = ChatMemory(window_size=3)
    generator = load_model()

    print("Bot: Hello! How can I help you today?")

    while True:
        user_input = input("User: ").strip()
        if user_input.lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        
        prompt = memory.get_context() + f"User: {user_input}\nBot:"

        response = generator(
            prompt,
            max_new_tokens=120,
            pad_token_id=generator.tokenizer.eos_token_id
        )[0]["generated_text"]

        answer = response[len(prompt):].strip()

        stop_words = [
            "User:",
            "Step",
            "* Menu",
            "**Step",
            "**",      
            "###",      
            "Example",  
            "Instructions",
        ]
        for stop_word in stop_words:
            if stop_word in answer:
                answer = answer.split(stop_word)[0].strip()

        if answer:
            print(f"Bot: {answer}")
        else:
            print("Bot: (no valid response generated)")

        memory.add_turn(user_input, answer)

if __name__ == "__main__":
    main()
