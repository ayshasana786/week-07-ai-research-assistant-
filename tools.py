import requests
from langchain_core.tools import tool


@tool
def research_topic(topic: str) -> str:
    """Search Wikipedia and retrieve information about a research topic."""

    search_url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "list": "search",
        "srsearch": topic,
        "format": "json",
        "srlimit": 3
    }

    headers = {
        "User-Agent": "AI-Research-Assistant/1.0"
    }

    try:
        response = requests.get(
            search_url,
            params=params,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        results = data.get("query", {}).get("search", [])

        if not results:
            return "No research information was found."

        research = ""

        for result in results:
            title = result.get("title", "")
            snippet = result.get("snippet", "")

            snippet = snippet.replace("<span class=\"searchmatch\">", "")
            snippet = snippet.replace("</span>", "")

            research += "\nTitle: " + title
            research += "\nInformation: " + snippet
            research += "\n"

        return research

    except Exception as e:
        return "Research search failed: " + str(e)