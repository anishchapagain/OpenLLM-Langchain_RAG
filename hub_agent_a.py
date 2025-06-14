from smolagents import LiteLLMModel

# Code Agent Example: Retrieve Weather Information
def get_weather(city):
    import requests
    api_url = f"https://api.weather.com/v1/location/{city}?apiKey=YOUR_API_KEY"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data.get("weather", "No weather information available")
    else:
        return "Error: Unable to fetch weather data."

def main():
    print("Hello from huggingface-agents!")
    model = LiteLLMModel(
        model_id="ollama_chat/gemma3:latest",  # Or try other Ollama-supported models 
        api_base="http://127.0.0.1:11434",  # Default Ollama local server
        num_ctx=8192, # plan ctx
    )
    print(model)
    print(dir(model))

    # Execute the function and prepare the final answer
    result = get_weather("New York")
    final_answer = f"The current weather in New York is: {result}"
    print(final_answer)

if __name__ == "__main__":
    main()