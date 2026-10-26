# Uncensored LLM API for developers in the Philippines — quickstart
# pip install openai
import os
from openai import OpenAI

client = OpenAI(base_url="https://uncensored-llm.sbs/v1", api_key=os.environ["UNLLM_KEY"])
r = client.chat.completions.create(
    model="uncensored-llm",
    messages=[{"role": "user", "content": "Explain plainly how crypto market cap is computed."}],
)
print(r.choices[0].message.content)
