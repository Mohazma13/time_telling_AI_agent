import google.generativeai as genai
import os
from tools import get_current_time

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-pro",
    tools=[get_current_time]
)

def run_agent():
    print("Ask the time of any city:")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        response = model.generate_content(query)
        print("Agent:", response.text)

if __name__ == "__main__":
    run_agent()
