from dotenv import load_dotenv

from graph import research_graph


load_dotenv()


print("===================================")
print("     AI RESEARCH ASSISTANT")
print("===================================")

question = input("\nEnter your research topic: ")

result = research_graph.invoke({
    "question": question,
    "research": "",
    "answer": ""
})

print("\n========== RESEARCH SUMMARY ==========\n")
print(result["answer"])