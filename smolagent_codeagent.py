from smolagents import CodeAgent, HfApiModel, InferenceClientModel

# HfApiModel was renamed to InferenceClientModel in version 1.14.0

# Step 1: Configure model to be used by Agent
model = InferenceClientModel( # HfApiModel
    max_tokens=2096,
    temperature=0.5,
    model_id='Qwen/Qwen2.5-Coder-32B-Instruct',# it is possible that this model may be overloaded
    custom_role_conversions=None,
    api_key="ADD_HF_API_KEY", # ADD_HF_API_KEY
)
# Step 2: Create the agent
# agent = CodeAgent(
#     model=model,
#     tools=[], 
#     max_steps=6,
#     verbosity_level=1,
#     grammar=None,
#     planning_interval=None,
#     name=None,
#     description=None,
#     # prompt_templates=prompt_templates
# )

agent = CodeAgent(
    model = model,
    max_steps=5,
    verbosity_level = 1,
    tools=[]
)

# print(agent.max_steps)

# Step 3: Ask the agent a question that requires code
response = agent.run("If there are two rows and two columns for person age and name in pandas dataframe, find the maximum age")

#   # Create a list of dictionaries with person age and name                                                                                                                      
#   people = [                                                                                                                                                                    
#       {'Name': 'Alice', 'Age': 25},                                                                                                                                             
#       {'Name': 'Bob', 'Age': 30}                                                                                                                                                
#   ]                                                                                                                                                                             
                                                                                                                                                                                
#   # Find the maximum age                                                                                                                                                        
#   max_age = max(person['Age'] for person in people)                                                                                                                             
#   print(max_age)                                                                                                                                                                
                                                                                                                                                                                
#   final_answer(max_age)  

# Step 4: See the result
print(response) # 30

# Example: 2

response_csv = agent.run("Read the file 'sales.csv' from folder 'docs' and show total sales amount per region.") 
print(response_csv)

# Cases: 
# 1. sales.csv in same location works fine
# 2. sales.csv inside 'doc': 
#       Code execution failed at line 'with open(file_path, mode='r') as file:
#       lines = file.readlines()' due to: InterpreterError: Forbidden function evaluation: 'open' is not among the explicitly allowed tools or defined/imported in the preceding    
#       code