# src/agent_controller.py
import json
from src.retriever import Retriever
from src.functions import book_appointment, generate_referral
import os
import openai    # used conceptually

retriever = Retriever()

SYSTEM_PROMPT = """
You are Community Health Navigator. Use provided sources when possible. If user asks for booking or referral generate a JSON and call the appropriate function. Always return a short human message and the machine JSON.
"""

def create_prompt(user_message, retrieved_docs):
    docs_text = "\n\n".join([f"[{d['source']}] {d['text']}" for d in retrieved_docs])
    prompt = f"{SYSTEM_PROMPT}\n\nCONTEXT:\n{docs_text}\n\nUSER: {user_message}\n\nINSTRUCTIONS: If the user needs an appointment, call the function book_appointment with JSON: {{'name','phone','clinic_id','datetime','reason'}}. If they need a referral, call generate_referral with JSON: {{...}}. Provide sources and a confidence level (0-1)."
    return prompt

def run_agent_openai(user_message, functions=None):
    retrieved = retriever.retrieve(user_message, top_k=3)
    prompt = create_prompt(user_message, retrieved)
    # Example OpenAI-style function-calling request (replace model / key as needed)
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini", 
        messages=[{"role":"system", "content":SYSTEM_PROMPT},
                  {"role":"user", "content": prompt}],
        functions=functions,
        function_call="auto",
        temperature=0.1,
    )
    message = response["choices"][0]["message"]
    if message.get("function_call"):
        fname = message["function_call"]["name"]
        args = json.loads(message["function_call"]["arguments"])
        if fname == "book_appointment":
            result = book_appointment(**args)
        elif fname == "generate_referral":
            result = generate_referral(**args)
        else:
            result = {"error":"unknown function"}
        # Respond back with the function result
        return {"assistant_text": message["content"] or "", "function_result": result}
    else:
        return {"assistant_text": message["content"], "sources": retrieved}
