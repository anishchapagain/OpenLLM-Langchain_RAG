from llama_cpp import Llama

llm = Llama(
    model_path="qwen2.5-coder-7b-instruct-q5_k_m.gguf", # q4_k_m Star Coder
    chat_format="chatml",  # Required for Qwen
    n_ctx=4096,
    temperature=0.2,
    top_p=0.9
)

# SYSTEM prompt with schema
system_prompt = """
You are a Python pandas expert who writes only executable Python code using a DataFrame named `df`.

Here is the schema of the DataFrame:

Columns:
- `customer_id` (str): Unique customer identifier.
- `customer_name` (str): Name of the customer.
- `account_balance` (float): Current balance of the customer account.
- `customer_industry` (str): Industry of the customer.
- `account_open_date` (datetime): The date when the account was opened.

Here are 3 sample rows from the DataFrame `df`:

  customer_id    customer_name    account_balance    customer_industry    account_open_date
  C001          Alice Smith       10345.55           Manufacturing         2020-01-15
  C002          Bob Johnson       5678.30            IT Services           2019-05-10
  C003          Charlie Brown     8230.00            Retail                2021-07-25

Guidelines:
- Use only the `df` variable.
- Do not add explanations or markdown.
- Always return complete and executable Python code.
"""

# User question
user_prompt = "Show average account balance by customer industry."

# Call the model
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

response = llm.create_chat_completion(messages=messages)
print(response["choices"][0]["message"]["content"])
