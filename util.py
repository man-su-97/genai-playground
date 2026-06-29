from client import client
from config import MAX_OUTPUT_TOKENS, Model

def get_completion(input_text: str, model: Model ) -> str:
    """
    Get a Text Response from The OpenAI API using the specified model and input text.
    """
    response = client.responses.create(
      model=model,
      input=input_text,
      max_output_tokens=MAX_OUTPUT_TOKENS,
    )

    return response.output_text