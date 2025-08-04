from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import os
from dotenv import load_dotenv
load_dotenv()


print (os.getenv("AGENT_IDid"))
print(os.getenv("TENANT_ID"))
chat_model = LiteLlm(
    model="openai/gpt-4o",
    api_base= os.getenv("LITELLM_URL"),
    api_key="slkk",
    headers={"agent": "sagent007t",
                        "appid": os.getenv("AGENT_ID"),
                        "userid": "user_123_456",
                        "tenantid": os.getenv("TENANT_ID"),
                        "sessionid": "session_123_456",
                        "teamid": "team_123_456"})

print (os.getenv("AGENT_IDid"))
print(os.getenv("TENANT_ID"))

root_agent = Agent(
    name="user_query_agent",
    description=(
        "A helpful and friendly AI assistant that answers user questions clearly, "
        "politely, and with relevant details. "
        "Designed to provide accurate information while keeping responses easy to understand."
    ),
    model= chat_model,
    instruction=(
        "When answering, always use a warm and approachable tone, but remain factual and concise. "
        "If you are confident in the answer, provide it with clear reasoning or steps. "
        "If you do not know the answer, explicitly say: "
        "'I do not have knowledge about that.' — do not guess or make up facts. "
        "If needed, suggest possible next steps for the user to find accurate information. "
        "Avoid technical jargon unless the user requests it, and tailor explanations to the user's skill level."
    )
)
