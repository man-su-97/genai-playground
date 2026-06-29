from enum import StrEnum

class Role(StrEnum):
    USER = "user"
    ASSISTANT = "assistant"
    DEVELOPER = "developer"
    SYSTEM = "system"


class Model(StrEnum):
    GPT_5_NANO = "gpt-5-nano"
    GPT_5_5 = "gpt-5.5"
    GPT_4_1_MINI = "gpt-4.1-mini"
    GPT_4O = "gpt-4o"

DEFAULT_MODEL = Model.GPT_5_NANO

TEMPERATURE = 0.0
MAX_OUTPUT_TOKENS = 300