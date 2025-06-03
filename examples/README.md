# Ejemplos

Este directorio contiene ejemplos sencillos para interactuar con Dify.

## `market_persona_agent.py`

Genera **UserPersonas** de forma sintética analizando información de mercado obtenida de Internet.

Al ejecutar el script se preguntará al usuario sobre qué sector desea realizar el análisis. A continuación se utiliza DuckDuckGo para recopilar texto relevante y la API de OpenAI para redactar tres UserPersonas.

```bash
python3 market_persona_agent.py
```

Es necesario contar con la biblioteca `openai` instalada y definir la variable de entorno `OPENAI_API_KEY`.
