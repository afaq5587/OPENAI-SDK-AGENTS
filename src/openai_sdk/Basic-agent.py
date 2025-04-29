from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
# from agents.extensions.models.litellm_model import LitellmModel
from openai import AsyncOpenAI

import os
from dotenv import load_dotenv
load_dotenv()
set_tracing_disabled(disabled=True)

MODEL = "gemini/gemini-2.0-flash"
GEMINI_API_KEY =os.environ.get("GEMINI_API_KEY")

base_url="https://generativelanguage.googleapis.com/v1beta/openai/"

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=base_url
)
def main():
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
    )

    result = Runner.run_sync(agent, "What's the python?")
    print(result.final_output)

main()