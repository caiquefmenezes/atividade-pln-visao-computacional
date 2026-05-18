from textblob import TextBlob

textos = [
    "I love Python! It is an amazing and wonderful programming language.",
    "This code is terrible. I hate debugging errors all day long.",
    "The program runs and produces an output.",
    "This movie is absolutely fantastic and I enjoyed every minute of it!",
    "The service was disappointing and the food was cold and tasteless.",
]

print("=" * 60)
print("ANALISE DE SENTIMENTOS COM TEXTBLOB")
print("=" * 60)

for texto in textos:
    blob = TextBlob(texto)
    polaridade = blob.sentiment.polarity
    subjetividade = blob.sentiment.subjectivity

    if polaridade > 0:
        sentimento = "POSITIVO"
    elif polaridade < 0:
        sentimento = "NEGATIVO"
    else:
        sentimento = "NEUTRO"

    print(f"\nTexto: {texto}")
    print(f"Polaridade: {polaridade:.2f} | Subjetividade: {subjetividade:.2f}")
    print(f"Sentimento detectado: {sentimento}")

print("\n" + "=" * 60)
print("Analise concluida!")
print("=" * 60)
