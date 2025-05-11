from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms import LlamaCpp

# https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q5_K_M.gguf?download=true

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# model_path="models/qwen2.5-coder-7b-instruct-q5_k_m.gguf",


# net issue
llm = LlamaCpp(
    model_path="models/llama-2-7b-chat.Q3_K_M.gguf",
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
    callback_manager=callback_manager,
    verbose=True,
)

system_prompt = "Balen lives in Rio.; Peter in Guyana.; Peter is currently living in St Louis." # test
user_prompt = "Where does Peter live?"

prompt_naive = f"{system_prompt}\n{user_prompt}"

llm(prompt_naive)

llama_prompt = f"<s>[INST]<<SYS>>\n{system_prompt}<</SYS>>\n{user_prompt}[/INST]"

pprint(llama_prompt)

llm(llama_prompt)
