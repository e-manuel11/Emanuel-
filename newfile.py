perguntas = [
    {
        "pergunta": "Qual é o seu nome completo?",
        "resposta": "Emanuel Capinalã Munjenje",
    },
    {
        "pergunta": "Em que cidade angolana reside?",
        "resposta": "Benguela",
    },
    {
        "pergunta": "Em que dia e mês nasceu?",
        "resposta": "19 de Fevereiro",
    },
]

pontuacao = 0

print("Bem-vindo ao Quiz sobre a sua Vida!")

for item in perguntas:
    print("\n" + item["pergunta"])
    resposta_usuario = input("Sua resposta: ")

    if resposta_usuario.strip().lower() == item["resposta"].lower():
        print("Correto!")
        pontuacao += 1
    else:
        print(f"Errado! A resposta era {item['resposta']}.")

print(
    f"\nFim do jogo! A sua pontuação final é: {pontuacao}/{len(perguntas)}"
)