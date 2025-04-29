# def main() -> None:
#     print("Hello from openai-sdk!")



from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
from dotenv import load_dotenv
load_dotenv()
set_tracing_disabled(disabled=True)

MODEL = "gemini/gemini-2.0-flash"
GEMINI_API_KEY =os.getenv("GEMINI_API_KEY")
def main():
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=LitellmModel(model=MODEL, api_key=GEMINI_API_KEY),
    )

    result = Runner.run_sync(agent, "What's the python?")
    print(result.final_output)