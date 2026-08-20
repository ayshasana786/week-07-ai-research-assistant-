from dotenv import load_dotenv

load_dotenv()

from typing import TypedDict

from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

from tools import research_topic


class ResearchState(TypedDict):
    question: str
    research: str
    answer: str


llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)


def research_node(state: ResearchState):
    question = state["question"]

    research = research_topic.invoke(question)

    return {
        "research": research
    }


def summary_node(state: ResearchState):
    question = state["question"]
    research = state["research"]

    prompt = """
You are an AI Research Assistant.

Question:
""" + question + """

Research information:
""" + research + """

Based only on the research information above, provide a clear and simple
summary.

Include:
1. Short introduction
2. Important points
3. Conclusion

Do not invent information.
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }


graph_builder = StateGraph(ResearchState)

graph_builder.add_node("research", research_node)
graph_builder.add_node("summarize", summary_node)

graph_builder.add_edge(START, "research")
graph_builder.add_edge("research", "summarize")
graph_builder.add_edge("summarize", END)

research_graph = graph_builder.compile()