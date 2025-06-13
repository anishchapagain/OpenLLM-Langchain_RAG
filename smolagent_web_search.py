from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel

model = InferenceClientModel( # HfApiModel
    max_tokens=2096,
    temperature=0.5,
    model_id='Qwen/Qwen2.5-Coder-32B-Instruct',# it is possible that this model may be overloaded
    custom_role_conversions=None,
    api_key="ADD_HF_API_KEY"
)

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()], 
    model=model
    )

response = agent.run("Provide world top football playing nations who have won world cup at least once")

print(response)