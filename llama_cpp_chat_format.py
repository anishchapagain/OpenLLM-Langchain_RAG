from llama_cpp import Llama

llm = Llama(
    model_path="qwen2.5-coder-7b-instruct-q4_k_m.gguf",
    chat_format="chatml",  # Make sure this matches your model
    n_ctx=4096,
)

messages = [
    {
        "role": "system",
        "content": "You are a Python expert who writes pandas code only. Use the DataFrame `df`. Do not explain — only return valid Python code."
    },
    {
        "role": "user",
        "content": "Show average account balance by customer industry."
    }
]

response = llm.create_chat_completion(messages)
print(response["choices"][0]["message"]["content"])
