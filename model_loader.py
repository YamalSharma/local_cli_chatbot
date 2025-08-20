from transformers import pipeline

def load_model():
    """
    Loads the SmolLM-360M-Instruct model and tokenizer.
    Returns a Hugging Face pipeline for text-generation.
    """
    model_name = "HuggingFaceTB/SmolLM-360M-Instruct"
    generator = pipeline(
        "text-generation",
        model=model_name,
        tokenizer=model_name,
        max_length=256,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
    )
    return generator
