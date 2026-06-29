
from dotenv import load_dotenv,find_dotenv,dotenv_values
from config import Model
from prompts.translation import TRANSLATION_PROMPT
from examples import CUSTOMER_EMAIL, STYLE
from util import get_completion


def main():
    prompt = TRANSLATION_PROMPT.format(
        style=STYLE,
        customer_email=CUSTOMER_EMAIL,
    )

    result = get_completion(prompt, model=Model.GPT_5_NANO)
    result = get_completion(prompt, model=Model.GPT_4_1_MINI)


    print(result)


if __name__ == "__main__":
    main()
