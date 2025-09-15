import random
import time

def animar_texto(texto, delay=0.03):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(delay)
    print()

def gerar_inimigo(nivel, chefe=False):
    tipos = [
        {"nome": "Zumbi", "vida": 1, "pontos": 1, "ataque": 0.3},
        {"nome": "Alienígena", "vida": 2, "pontos": 2, "ataque": 0.5},
        {"nome": "Soldado inimigo", "vida": 3, "pontos": 3, "ataque": 0.6},
        {"nome": "Robô", "vida": 4, "pontos": 4, "ataque": 0.7},
    ]
    inimigo = random.choice(tipos)
    inimigo['vida'] += nivel // 3
    if chefe:
        inimigo = {"nome": f"Chefe {inimigo['nome']}", "vida": inimigo['vida'] + 3,
                   "pontos": inimigo['pontos'] * 5, "ataque": min(inimigo['ataque']+0.2, 0.9)}
    return inimigo

def escolher_caminho():
    animar_texto("\nEscolha seu caminho para o próximo round:")
    animar_texto("1 - Mais inimigos, mais pontos")
    animar_texto("2 - Menos inimigos, chance de item")
    animar_texto("3 - Caminho equilibrado")
    escolha = input("Digite 1, 2 ou 3: ")
    while escolha not in ["1","2","3"]:
        escolha = input("Escolha inválida. Digite 1, 2 ou 3: ")
    return int(escolha)

def jogo_campanha():
    vida = 5
    pontos = 0
    nivel = 1

    armas = {
        "pistola": {"dano": 1, "municao": 10},
        "rifle": {"dano": 2, "municao": 5},
        "bazuca": {"dano": 4, "municao": 2}
    }

    animar_texto("=== Bem-vindo à Campanha Estratégica de Tiro ===\n")
    animar_texto("Complete as missões, derrote chefes e escolha seu caminho!\n")

    while vida > 0:
        animar_texto(f"\n--- Round {nivel} ---")
        
        # Decisão estratégica
        caminho = escolher_caminho()
        if caminho == 1:
            num_inimigos = random.randint(2, nivel + 3)
        elif caminho == 2:
            num_inimigos = random.randint(1, nivel)
        else:
            num_inimigos = random.randint(1, nivel + 1)

        # Chefes a cada 5 níveis
        chefe = (nivel % 5 == 0)
        inimigos_nivel = [gerar_inimigo(nivel, chefe=chefe) for _ in range(num_inimigos)]

        for inimigo in inimigos_nivel:
            inimigo_vida = inimigo["vida"]
            animar_texto(f"\nUm {inimigo['nome']} apareceu! Vida: {inimigo_vida}")

            while inimigo_vida > 0 and vida > 0:
                animar_texto(f"Vidas: {vida} | Pontos: {pontos}")
                status_armas = ", ".join([f"{arma}({info['municao']})" for arma, info in armas.items()])
                animar_texto(f"Armas disponíveis: {status_armas} | Ou digite 'esquivar'")
                acao = input("Sua ação: ").lower()

                if acao in armas:
                    if armas[acao]['municao'] <= 0:
                        animar_texto(f"Sua {acao} não tem munição!")
                        continue
                    dano = armas[acao]['dano']
                    inimigo_vida -= dano
                    armas[acao]['municao'] -= 1
                    if inimigo_vida <= 0:
                        pontos += inimigo['pontos'] * nivel
                        animar_texto(f"Você derrotou o {inimigo['nome']}! Ganhou {inimigo['pontos']*nivel} pontos.\n")
                        break
                    else:
                        animar_texto(f"Você acertou! Vida do {inimigo['nome']}: {inimigo_vida}")
                        if random.random() < inimigo['ataque']:
                            vida -= 1
                            animar_texto(f"O {inimigo['nome']} te atacou! Vidas restantes: {vida}\n")
                elif acao == "esquivar":
                    if random.random() < 0.7:
                        animar_texto(f"Você escapou do {inimigo['nome']}!\n")
                        break
                    else:
                        vida -= 1
                        animar_texto(f"Falhou na esquiva! O {inimigo['nome']} te acertou! Vidas restantes: {vida}\n")
                else:
                    animar_texto("Ação inválida! Tente novamente.\n")
                time.sleep(0.5)

        # Chance de itens especiais
        item_aleatorio = random.random()
        if item_aleatorio < 0.2:
            cura = random.randint(1,3)
            vida += cura
            animar_texto(f"Você encontrou um kit de primeiros socorros! Recuperou {cura} vidas. Vidas: {vida}")
        elif item_aleatorio < 0.4:
            arma = random.choice(list(armas.keys()))
            muni = random.randint(1,3)
            armas[arma]['municao'] += muni
            animar_texto(f"Você encontrou munição extra para {arma}! +{muni} tiros.")
        elif item_aleatorio < 0.5:
            upgrade = random.choice(list(armas.keys()))
            armas[upgrade]['dano'] += 1
            animar_texto(f"Sua arma {upgrade} foi aprimorada! Dano agora: {armas[upgrade]['dano']}")

        nivel += 1
        time.sleep(1)

    animar_texto("\n=== CAMPANHA FINALIZADA ===")
    animar_texto(f"Sua pontuação final foi: {pontos}")

# Inicia o jogo
jogo_campanha()
