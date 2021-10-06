personagem=input("qual o nome do personagem?")

primeiro_local= int(input("""você se perdeu do seu grupo de amigos e está,em uma floresta,sem saber para onde ir.encontra uma trilha e decide segui-la.depois de horas percorrendo uma trilha,você chega a uma bifurcação

(1)à direita se encontra uma casa abandonada caindo aos pedaços,com a porta fechada.
(2)à esquerda encontra um enorme castelo antes escondido pelas folhagens.seu enorme portão está aberto.

para onde você vai?"""))

# CASA ABANDONADA
if primeiro_local==1:
    escolha_1=int(input("""você seguiu para a casa e forçou a porta.a casa está completamente vazia, a não serpor uma espada fincada em uma mesa de madeira.o que você faz?
(1)pegar a espada
(2)sair da casa
"""))

    if escolha_1 == 1 :
        print("não parece ter mais nada na casa, e você sai com sua nova espada.")
    elif escolha_1==2:
        print("VOCÊ SAI.")

# De qualquer forma, vamos para o castelo
primeiro_local = 2


# CASTELO
if primeiro_local==2:
    escolha_2=int(input("""você segue pelo meio das folhagens até o castelo.
atravessa uma ponte sobre um grande fosso e entra em uma sala enorme.no meio do corredor existe uma pesada armadura medieval.
oquê você faz?
(1)vestir a armadura
(2)ignorar armadura """))


# você escolheu vestir a armadura mas ela estava muito pesada é presiso então decidir se ficara ou não com ela.
# caso contrario não há escolha a ser feita:
if escolha_2 == 1:
    armadura_pesada=int(input("""você veste a armadura e fica muito pesado. tem certeza que não prefere tirar?
    
    (1)tirar armadura
    (2)manter a armadura"""))

    # após passar pela sala da armadura você vê um corredor.
    # segue por ele  e se encontra diante de duas portas:
    porta=int(input("""na extremidade oposta da sala.você encontra 2 portas.em qual delas você entra?
    
    esquerda (1)
    direita (2)"""))

    # na sala atrás da porta direita existe um elfo protegendo um enorme tessouro para pegar o tessouro é necessario presentear o elfo voce trouxe a espada?
    # PORTA ESQUERDA
    if porta==1:
        if escolha_2==2:
            print("""ops,tirar a armadura não foi uma boa ideia.voce encontrou um imenso dragão e,
            sem proteção acabou sendo queimado.game over""")
        if escolha_2==1 and armadura_pesada==1:
            print("""ops,tirar a armadura não foi uma boa ideia.voce encontrou um imenso dragão e,
            sem proteção acabou sendo queimado.game over""")
        if armadura_pesada==2 and escolha_2==1:
            print("""ao entrar pela porta esquerda você encontrou um imenso dragão.
            mas a sua armadura te protegeu contra o fogo lançado por ele.
            você retorna e entra na porta a direita""")
            if escolha_1 == 1:
                print("""VOCê ENCONTRA O ELFO E O PRESENTEIA COM A ESPADA. O ELFO TE PERMITE
                PEGAR TODO O TESOURA. PARABENS!!!""")
            elif escolha_1 == 2:
                escolha_3 = int(input("""O ELFO FICOU MUITO BRAVO POR VOCE NAO POSSUIR UM PRESENTE PARA ELE.
                
                (1) voltar e pegar a espada.
                (2) Enfrentar o elfo e roubar o tesouro.
                 """))
                if escolha_3 == 1:
                    print("VOCE PRESENTEOU O ELFO E GANHOU TODO TESOURO. PARABENS!!!")
                elif escolha_3 == 2:
                    print("""O ELFO ERA MAIS PODEROSO DO QUE PARECIA. COM UM PASSE DE MAGICA TE
                    TRANSFORMOU EM UM RATINHO. GAME OVER!! """)

    # PORTA DIREITA
    if porta==2:
        if escolha_1==1:
            print("""você encontra o elfo e presentea com a espada.o elfo te permite pegar todo o tessouro.parabéns:""")
    
        if escolha_1==2:
            escolha_3=int(input("""ops, o elfo ficou muito bravo por você não possuir um presente para ele
            (1)voltar e pegar a espada
            (2)enfrentar o elfo e roubar o tesouro"""))

            if escolha_3==1:
                print("""você presenteo o elfo e ganhou todo o tessouro. parabéns:!!!""")

            if escolha_3==2:
                print("""o elfo era mais poderoso que parecia .
                como um passe de mágica ele te transformou em um ratinho.game over:!!!""")
