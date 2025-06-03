"""Example agent that generates synthetic UserPersonas from internet market analysis.

Este script pregunta al usuario por el sector a analizar, obtiene información del
internet mediante DuckDuckGo y genera UserPersonas utilizando la API de OpenAI.
Necesitas tener instalada la dependencia ``openai`` y definir la variable de
entorno ``OPENAI_API_KEY`` antes de ejecutarlo.
"""
import os
import re
import urllib.parse
import urllib.request

import openai


def search_web(query: str, num_results: int = 5) -> list[str]:
    """Return a list of text snippets from DuckDuckGo search results."""
    url = f"https://duckduckgo.com/html/?q={urllib.parse.quote_plus(query)}"
    with urllib.request.urlopen(url) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
    pattern = re.compile(r'class="result__snippet">(.*?)<', re.S)
    snippets = [re.sub(r"<.*?>", "", s).strip() for s in pattern.findall(html)]
    return snippets[:num_results]


def generate_personas(sector: str, context: str) -> str:
    """Use OpenAI to generate user personas based on provided context."""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = (
        f"Basándote en la siguiente información de mercado sobre {sector}, "
        f"genera tres UserPersonas en formato de puntos:\n{context}"
    )
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un analista de mercado."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )
    return completion["choices"][0]["message"]["content"].strip()


def main() -> None:
    sector = input("¿Sobre qué sector quieres generar las UserPersonas? ")
    snippets = search_web(f"{sector} market analysis")
    context = " ".join(snippets)
    personas = generate_personas(sector, context)
    print("\nPersonas generadas:\n")
    print(personas)


if __name__ == "__main__":
    main()
