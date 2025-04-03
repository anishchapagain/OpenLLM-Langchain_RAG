import ollama

response = ollama.list() 
# Multiple models will get listed

print(f"Total models availbale: {len(response.models)}")

for model in response.models:
    name = model.get('model','')
    format = model.details.get('format','')
    families = model.details.families
    parameters = model.details.get('parameter_size','')
    quantization = model.details.get('quantization_level','')
    
    print(f"Model: {name} - Format: {format} - Param_Size: {parameters} - Q: {quantization} - Families: {families}")