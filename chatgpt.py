import openai
openai.api_key = "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"

def obter_resposta(texto):
    response = openai.Completion.create(
      engine="davinci",
      prompt=texto,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
    )
    return response.choices[0].text.strip()

texto = "Escreva sobre carros"
resposta = obter_resposta(texto)
print(resposta)
