from src.agent_controller import run_agent_openai

user_msg = "I have had a fever for 3 days and I am in Bangalore. I need to see a doctor and I can't pay much."
res = run_agent_openai(user_msg)
print(res["assistant_text"])
if res.get("function_result"):
    print("Function result:", res["function_result"])
else:
    print("Sources:", res.get("sources"))
