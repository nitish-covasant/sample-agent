from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


chat_model = LiteLlm(
    model="openai/gpt-4o",
    api_base= "https://aifabric-litellm.dev.gcp.covasant.io/v2",
    api_key="slkk",
    headers={"agent": "sagent007t",
                        "appid": "3b0a205d-45dd-43a6-b17f-1d4b8911ce78",
                        "userid": "user_123_456",
                        "tenantid": "115bc9db-4017-4f69-9816-6ca32660f6e5",
                        "sessionid": "session_123_456",
                        "teamid": "team_123_456"})



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
