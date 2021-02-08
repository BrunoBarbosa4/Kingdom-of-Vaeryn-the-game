from random import randint
from time import sleep
from os import system

system('cls')

# Formatação do texto
none = '\033[m'
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
grey = '\033[1;37m'

# Informações do jogador
nome = ''
classe = ''
equipamento = ''
quest1 = False
quest2 = False
quest3 = False


def validar(decisao):
    if (decisao == '1') or (decisao == '2') or (decisao == '3') or (decisao == '4') or (decisao == '5'):
        return int(decisao)
    else:
        return 0


def teste(sorte):
    return randint(1, sorte)


def alistamento():
    global nome
    global classe
    global equipamento
    system('cls')

    input('--> O Reino de Vaeryn irá participar de uma guerra. ')
    input('--> Estão recrutando guerreiros, arqueiros e magos de todo o reino para servir.')

    while nome == '':
        nome = input(f'{grey}Guarda:{none} Obrigado por vir se alistar, qual o seu nome?\n')

    escolha_alistamento = 0
    while escolha_alistamento < 1 or escolha_alistamento > 3:
        escolha_alistamento = input(f'{grey}Guarda:{none} {nome}, você é um:'
                                    '\n[1] Guerreiro'
                                    '\n[2] Arqueiro'
                                    '\n[3] Mago\n')

        escolha_alistamento = validar(escolha_alistamento)
        if escolha_alistamento == 1:
            classe = 'Guerreiro'
            equipamento = 'espada'
        elif escolha_alistamento == 2:
            classe = 'Arqueiro'
            equipamento = 'flecha e arco'
        elif escolha_alistamento == 3:
            classe = 'Mago'
            equipamento = 'bola de fogo'

    for espera in range(2):
        sleep(1)
        print('.')


def guerra():
    system('cls')

    print('\n', 10 * '=', 'Parte 1 - A Guerra', 10 * '=')
    input('--> Meses após se alistar, chega o dia do confronto entre o Reino de Vaeryn e o Reino de Hedeby.')
    input('--> Você se aproxima do exército vaeryano enquanto os dois travam um embate no vasto campo aberto.')

    escolha1 = 0  # fala com o soldado
    while escolha1 < 1 or escolha1 > 3:
        escolha1 = input(f'\n{grey}Soldado:{none} {nome}, já trouxe sua arma?'
                         '\n[1] Sim, eu estou sempre pronto para a batalha.'
                         '\n[2] Não, dê-me uma.'
                         f'\n[3] Sou um {classe} de elite, com minha {equipamento} enfrento tudo e todos.\n')

        escolha1 = validar(escolha1)
        if escolha1 == 1:
            print(f'\n{grey}Soldado:{none} Ótimo, como esperado de um {classe} como você.\n')
        elif escolha1 == 2:
            print(f'\n{grey}Soldado:{none} Tome, que com ela você consiga acabar com o exército hedebyriano.\n')
        elif escolha1 == 3:
            print(f'\n{grey}Soldado:{none} Como sempre, um orgulhoso e destemido {classe}.\n')
        sleep(2)

    escolha2 = 0  # luta com o pelotão
    while escolha2 < 1 or escolha2 > 3:
        escolha2 = input('--> O combate se inicia e aproximam-se de sua posição um pelotão de três inimigos, você:'
                         '\n[1] Luta sozinho.'
                         '\n[2] Corre para reagrupar.'
                         '\n[3] Se mistura por entre os soldados e ataca o pelotão.\n')

        escolha2 = validar(escolha2)
        if escolha2 == 1:
            input(f'--> Você avança para cima dos inimigos com a {equipamento}, derrotando todo o pelotão facilmente.')
        elif escolha2 == 2:
            input('--> Você recua para próximo de seus aliados e juntos acabam com o pelotão inimigo.')
        elif escolha2 == 3:
            input(f'--> Você se camufla por entre os soldados inimigos e ataca os três com a sua {equipamento}.')

    escolha3 = 0  # encontro com Merlin
    while escolha3 < 1 or escolha3 > 3:
        escolha3 = input('--> Enquanto seus aliados levam vantagem sobre o exército oponente, '
                         'você avista o mago Merlin em apuros e decide ajuda-lo:'
                         '\n[1] Levantando-o e lutando lado a lado.'
                         '\n[2] Lutando sozinho primeiro para depois levanta-lo.'
                         '\n[3] Pedindo ao mago que lhe cure com sua magia enquanto leva-o ao pelotão aliado.\n')

        escolha3 = validar(escolha3)
        if escolha3 == 1:
            input('--> Você ajuda Merlin a se recuperar e juntos travam um batalha contra os inimigos no alcance, '
                  'limpando uma boa área de inimigos.')
        elif escolha3 == 2:
            input('--> Você percebe que Merlin está ferido e não pode ajudá-lo no momento, '
                  'então derrota os inimigos próximos sozinho para então ajuda-lo a se recuperar.')
        elif escolha3 == 3:
            input('--> Você convence o mago para que o cure com magia e juntos tentam recuar para o pelotão aliado, '
                  'lutando com os inimigos no caminho.')

    escolha4 = 0  # forte inimigo
    while escolha4 < 1 or escolha4 > 3:
        escolha4 = input('--> Enquanto tentam reagrupar com o pelotão, você e Merlin encontram um forte inimigo. Vocês:'
                         '\n[1] Atacam o soldado-tenente desprevenido.'
                         '\n[2] Trabalham em equipe para enfrentar o forte.'
                         '\n[3] Se separam para poder enfrentar os inimigos sozinhos, pela honra.\n')

        escolha4 = validar(escolha4)
        if escolha4 == 1:
            input('--> Você aproveita que o soldado-tenente não viu vocês, pois enfrentava dois soldados aliados, '
                  'e o ataca desprevenido, sem dar-lhe a mínima chance.')
        elif escolha4 == 2:
            input('--> Com uma poderosa tática, Merlim usa sua magia Taiokon, '
                  f'cegando os soldados, e você os finaliza com a sua {equipamento}.')
        elif escolha4 == 3:
            input('--> Você usa todo seu treinamento e habilidades e derrota os soldados do forte, '
                  'mas fica debilitado devido a uma machadada poderosa de um deles.')

    escolha5 = 0  # fim da guerra
    while escolha5 < 1 or escolha5 > 4:
        input('--> Com a derrota do soldado-tenente, que era o mais forte do pelotão inimigo, '
              'o exército deles ficou debilitado.')
        input('--> Restava agora somente o líder de exército mais vinte soldados contra o exército aliado, '
              'que ainda tinha mais de cem soldados.')

        escolha5 = input('--> Seu exército se aproxima do exército inimigo, e você:'
                         '\n[1] Espera que os líderes do seu exército coloquem um fim na batalha.'
                         '\n[2] Ameaça-os para que peçam a rendição.'
                         '\n[3] Vai para mata-los, resolvendo tudo.'
                         '\n[4] Pergunta ao General aliado como prosseguir.\n')

        escolha5 = validar(escolha5)
        if escolha5 == 1:
            input('--> Você espera que tudo seja resolvido pelos líderes, '
                  'que rendem os inimigos e decretam o fim da guerra.')
        elif escolha5 == 2:
            input('--> Você toma a frente, mesmo não sendo um líder ou General, '
                  'e faz com que os inimigos se rendam, dando assim um fim à guerra.')
        elif escolha5 == 3:
            input('--> Você avança para cima dos inimigos mas o seu General o impede, '
                  'pois com a morte de todo o exército o Reino de Hedeby nunca aceitaria trégua.')
            input('--> Após render todos os soldados, o General põe um fim à guerra.')
        elif escolha5 == 4:
            input('--> Você pergunta ao General como prosseguir, e ele lhe diz que bastava pressiona-los, '
                  'pois estão enfraquecidos e irão se render.')
            input('--> Assim acontece, e com a rendição inimiga coloca-se um fim à guerra.')

    escolha6 = 0  # volta ao reino
    while escolha6 < 1 or escolha6 > 3:
        input(f'--> Você e todo o exército voltam para o Reino de Vaeryn, sendo recepcionados pelo povo.')
        print('--> Então, o General fala:\n')
        sleep(1)
        input(f'{grey}General:{none} Com essa bela vitória de hoje, '
              f'percebi que o reino está bem servido de ótimos soldados. {nome} foi o que mais se destacou, '
              'com sua determinação e perseverança que foram a chave para colocar-nos à frente nessa guerra.\n')

        escolha6 = input('--> O povo o saudou, e você:'
                         '\n[1] Agradece e conta seus feitos de guerra.'
                         '\n[2] Fala que não fez mais que sua obrigação.'
                         '\n[3] Comemora com o povo a vitória da guerra.\n')

        escolha6 = validar(escolha6)
        if escolha6 == 1:
            input('--> Você agradeceu a todos e contou-lhes seus feitos e baixas na guerra, '
                  'com destaque para a luta contra o soldado-tenente.')
            input('--> Todos reconheceram seu valor.')
        elif escolha6 == 2:
            input('--> Você mostra sua determinação afirmando que não fez mais do que a própria obrigação.')
            input('--> Você inspirou muitos a servirem o exército para mostrarem do que são capazes.')
        elif escolha6 == 3:
            input('--> Você vai para o meio da multidão e comemora a vitória com uma festa no centro da cidade.')

        for espera in range(2):
            sleep(1)
            print('.')


def mapa_classes():
    global quest1
    global quest2
    global quest3
    system('cls')

    print('\n', 10 * '=', 'Parte 2 - A Aventura', 10 * '=')

    while (quest1 == False) or (quest2 == False) or (quest3 == False):
        escolha_mapa = 0
        while escolha_mapa < 1 or escolha_mapa > 3:
            if classe == 'Guerreiro':
                escolha_mapa = input('--> Seguir para:'
                                     '\n[1] Taverna.'
                                     '\n[2] Loja do Ferreiro.'
                                     '\n[3] Bosque.\n')

                escolha_mapa = validar(escolha_mapa)

                if escolha_mapa == 1:
                    if quest1:
                        input(f'{green}Moe:{none} E aí {nome}, obrigado por ter me ajudado. Quer uma bebida?')
                        input(f'{nome}: Não foi nada. Claro que quero.')
                        input(f'{nome}: está calma hoje, né?')
                        input(f'{green}Moe:{none} para mim é bom que fique assim.\n')
                        input('--> Você retorna à cidade.')
                    else:
                        guerreiro_quest1()
                elif escolha_mapa == 2:
                    if quest2:
                        input(f'{green}Yudi:{none} Vejo que a Força está com você, gostei de ver. Quer comprar algo?')
                        input(f'{nome}: Não, estou apenas procurando algo para fazer.')
                        input(f'{green}Yudi:{none} Não tenho mais nenhum serviço, '
                              'mas obrigado por ajudar a acabar com a marinha do forte.')
                        input(f'{nome}: Não foi nada.\n')
                        input('--> Você retorna à cidade.')
                    else:
                        guerreiro_quest2()
                elif escolha_mapa == 3:
                    if quest3:
                        input('--> Você avista os dois gigantes de Elbaff travando seu duelo diário.')
                        input('--> Depois de assistir um pouco, percebe que não tem mais nada para fazer ali.')
                        input('--> Você retorna à cidade.')
                    else:
                        guerreiro_quest3()

            elif classe == 'Arqueiro':
                escolha_mapa = input('--> Seguir para:'
                                     '\n[1] Subúrbios.'
                                     '\n[2] Bosque.'
                                     '\n[3] Floresta.\n')

                escolha_mapa = validar(escolha_mapa)

                if escolha_mapa == 1:
                    if quest1:
                        input('--> Você passa perto do esgoto, mas percebe que está tudo normal.')
                        input('--> O mendigo não está ali.')
                        input('--> Você retorna à cidade.')
                    else:
                        arqueiro_quest1()
                elif escolha_mapa == 2:
                    if quest2:
                        input('--> Você aprecia a natureza. Tudo está calmo.')
                        input('--> Você retorna à cidade.')
                    else:
                        arqueiro_quest2()
                elif escolha_mapa == 3:
                    if quest3:
                        input('--> Você consegue caçar sem ser interrompido.')
                        input('--> Após a caça, não tem muito o que fazer na floresta.')
                        input('--> Você retorna à cidade.')
                    else:
                        arqueiro_quest3()

            elif classe == 'Mago':
                escolha_mapa = input('--> Seguir para:'
                                     '\n[1] Escola.'
                                     '\n[2] Deserto.'
                                     '\n[3] Floresta.\n')

                escolha_mapa = validar(escolha_mapa)

                if escolha_mapa == 1:
                    if quest1:
                        input(f'{nome}: Não tenho mais nada para fazer aqui, pois já fiz todas as aulas.\n')
                        input('--> Você retorna à cidade.')
                    else:
                        mago_quest1()
                elif escolha_mapa == 2:
                    if quest2:
                        input(f'{green}Morador:{none} Como vai, campeão do Desafio da Pirâmide?')
                        input(f'{nome}: Bem. Não tem mais nenhum desafio?')
                        input(f'{green}Morador:{none} Gosta mesmo de desafios, hein? '
                              'Infelizmente não temos mais desafios.\n')
                        input('--> Você retorna à cidade.')
                    else:
                        mago_quest2()
                elif escolha_mapa == 3:
                    if quest3:
                        input('--> A floresta está calma, agora que o acampamento foi embora.')
                        input('--> Você retorna à cidade.')
                    else:
                        mago_quest3()


def guerreiro_quest1():
    global quest1

    input('--> Na taverna do Moe está tudo pacato, um dia normal como qualquer outro.')
    input('--> Você se aproxima do balcão, e ele lhe pergunta:')

    escolha1 = 0    # conversa com Moe
    while escolha1 < 1 or escolha1 > 3:
        escolha1 = input(f'{green}Moe:{none} Olá {classe}, quer tomar hidromel?'
                         '\n[1] Claro, aqui as três moedas!'
                         '\n[2] Não.'
                         '\n[3] Não tenho dinheiro, ajude seu amigo.\n')

        escolha1 = validar(escolha1)
        if escolha1 == 1:
            input(f'{green}Moe:{none} Muito bem rapaz, saindo o melhor hidromel da região.')
            input(f'{green}Moe:{none} Eu ouvi falar de você, o destemido {classe} de Vaeryn.')
            input(f'{nome}: Imagina, eu estava apenas servindo o meu reino. O NOSSO reino!')
            input(f'{green}Moe:{none} Gosto dessa empolgação, meu rapaz!')
        elif escolha1 == 2:
            input(f'{green}Moe:{none} Tudo bem, então veio apenas para jogar conversa fora, hein?')
            input(f'{green}Moe:{none} Suas histórias são verdadeiras? O {classe} que derrotou os hedebyrianos?\n')
            input('--> Quando você abre sua boca para responder...')
        elif escolha1 == 3:
            input(f'{green}Moe:{none} Ah, entendo... Deixe-me ver... O movimento está fraco mesmo, aqui está.')
            input(f'{nome}: Muito obrigado.')
            input(f'{green}Moe:{none} É apenas um agradecimento por um de nossos mais bravos guerreiros!')

    escolha2 = 0    # escutar a gangue
    while escolha2 < 1 or escolha2 > 3:
        input('--> De repente, entra na taverna a oportunista gangue Cascalho.')

        escolha2 = input('--> Eles não percebem quem você é e começam uma discussão com Moe, mas você espera pois:'
                         '\n[1] Espera que eles digam algo importante.'
                         '\n[2] Moe não gosta de violência desnecessária.'
                         '\n[3] Percebe que eles estão irritados por terem perdido uma briga.\n')

        escolha2 = validar(escolha2)
        if escolha2 == 1:
            input('--> Após alguns segundos de discussão, um deles diz:\n')
            input(f'{red}Capanga da gangue:{none} Entramos em brigas difíceis recentemente, '
                  'agora estamos sem dinheiro e por isso estamos recorrendo a assaltos e outras vigarices.')
            input(f'{red}Outro capanga da gangue:{none} É, queremos o seu dinheiro, anda logo!\n')
        elif escolha2 == 2:
            input('--> Percebendo que eles eram cabeça-quente, você resolveu não entrar na discussão '
                  'pois o Moe não gosta de violência em sua taverna.')
            input('--> (Mesmo que, de vez em quando, é impossível não acontecer...), você pensou.\n')
            input(f'{red}Capanga da gangue:{none} Estamos com pressa, vai logo e entrega o dinheiro pra gente!\n')
        elif escolha2 == 3:
            input(f'{red}Capanga da gangue:{none} Há alguns minutos, brigamos com os Vagos e perdemos uma grana,'
                  ' então passa logo o dinheiro pra cá.\n')

    escolha3 = 0    # reagindo ao assalto
    while escolha3 < 1 or escolha3 > 4:
        escolha3 = input('--> Sabendo que eles vão assaltar a taverna de Moe, você decide impedi-los:'
                         '\n[1] Atacando os cinco capangas ao mesmo tempo.'
                         '\n[2] Se reunindo com os demais clientes para ajudar o Moe.'
                         '\n[3] Aproveitando que não prestaram atenção em você e atacando-os pelas costas.'
                         '\n[4] Intimidando-os.\n')

        escolha3 = validar(escolha3)
        if escolha3 == 1:
            input('--> Você não tem medo de simples gangsters e parte com tudo o que tem para cima deles.')
            input(f'--> Você enfia sua {equipamento} com força nas costas do primeiro capanga.')
            input('--> Um deles atira com sua garrucha, mas você se abaixa antes e o chuta, incapacitando-o.')
            input('--> Um capanga te segura pelas costas e te imobiliza enquanto outro te socava algumas vezes, '
                  'mas você consegue se soltar e jogar quem o segurava em cima dele.')
            input('--> Percebendo que a situação encontrava-se desfavorável, '
                  'o último membro da gangue deu um tiro em Moe e fugiu rapidamente da taverna com o dinheiro.')
        elif escolha3 == 2:
            input('--> Você se reúne com os outros clientes e partem para cima da gangue.\n')
            input(f'--> {red}Gangsters:{none} Acham mesmo que quatro fracotes e um {classe} irá nos parar?\n')
            input(f'--> Você corre e arremessa sua {equipamento} no crânio do primeiro capanga, '
                  f'partindo para o próximo desferindo socos nos pontos vitais e desmaiando-o.')
            input('--> Três dos clientes espancam mais um membro da gangue.')
            input('--> Você corre para nocautear o capanga que golpeava o quarto cliente.')
            input('--> Com ele nocauteado, só restava um.')
            input('--> Porém, ao perceber que estava em desvantagem, o último capanga pegou o dinheiro, '
                  'atirou em Moe e fugiu para o esconderijo da gangue.')
        elif escolha3 == 3:
            input(f'--> Você se aproxima por trás e balançada sua {equipamento} horizontalmente, '
                  'acertando três capangas consecutivamente.')
            input('--> Os dois inimigos restantes ficam surpresos com a emboscada.')
            input('--> Um deles atira em Moe e sai correndo da taverna com o dinheiro.')
            input('--> Você tenta ir atrás dele, mas o outro capanga lhe impede.')
            input('--> Você derrota o último capanga sem muitas dificuldades.')
        elif escolha3 == 4:
            input('--> Você se aproxima da gangue e manda-os saírem da taverna, antes que aquilo acabasse pior.')
            input('--> Quatro deles partem pra cima de você, enquanto o outro roubava a taverna.')
            input('--> Você espanca-os numa luta corpo a corpo, mas um deles foge com o dinheiro e atira em Moe.')

    escolha4 = 0    # fuga do último capanga
    while escolha4 < 1 or escolha4 > 2:
        escolha4 = input('--> Após a fuga de um dos capangas, você:'
                         '\n[1] Corre atrás dele.'
                         '\n[2] Socorre Moe que foi baleado.\n')

        escolha4 = validar(escolha4)
        if escolha4 == 1:
            input('--> Você corre atrás do capanga, porém ele estava muito à frente.')
            input('--> Para piorar, você perde-o de vista após ser parado por uma carroça que cruzava a rua.')
        elif escolha4 == 2:
            input('--> Você vai socorrer Moe, mas quando se aproxima vê que o tiro passou raspando em seu ombro.\n')
            input(f'{green}Moe:{none} Eu estou bem {nome}, a gangue Cascalho nunca tinha sido violenta dessa maneira, '
                  'eles devem estar realmente desesperados para dispararem contra mim.')
            input(f'{green}Moe:{none} Agora corra {nome}, pegue o último deles.\n')
            input('--> Antes de você sair da taverna, Moe implora para você:\n')
            input(f'{green}Moe:{none} Coloque um fim nisso, por favor! Que esse inferno de gangue acabe para sempre.\n')
            input('--> Você vai atrás do ladrão, mas não sabe onde ele foi, pois ele partiu muito antes.')

    escolha5 = 0    # encontro com o Aventureiro
    while escolha5 < 1 or escolha5 > 3:
        escolha5 = input('--> Perdido, sem saber onde ele foi, '
                         'você se aproxima de um aventureiro que estava no cruzamento e diz:'
                         '\n[1] Aventureiro, você viu para onde foi aquele ladrão?'
                         '\n[2] Você pode me levar até o esconderijo da gangue Cascalho? Lhe darei 10 moedas.'
                         '\n[3] Me leve até esconderijo da gangue Cascalho agora, estou com pressa! \n')

        escolha5 = validar(escolha5)
        if escolha5 == 1:
            input(f'{blue}Aventureiro:{none} Vi sim, ele foi pela esquerda, subindo o morro.')
            input(f'{blue}Aventureiro:{none} Acho que já passei perto do esconderijo dele, fica em cima desse morro.\n')
            input('--> Você agradece e corre até o esconderijo.')
        elif escolha5 == 2:
            input(f'{blue}Aventureiro:{none} Claro, siga-me.\n')
            input('--> Você segue ele e logo chegam ao esconderijo.')
        elif escolha5 == 3:
            input(f'{blue}Aventureiro:{none} Vou te ajudar nessa, {classe}. Vamos.')
            input(f'{blue}Aventureiro:{none} Aconteceu alguma coisa?\n')
            input('--> Você conta o caso para ele e chegam até o esconderijo.')

    escolha6 = 0    # chegada ao esconderijo
    while escolha6 < 1 or escolha6 > 3:
        input('--> No esconderijo da gangue haviam quatro ladrões, sendo um o que furtou Moe, e o líder deles, Evan.')
        input('--> Você estava sozinho contra cinco inimigos.')

        escolha6 = input('--> Você então:'
                         '\n[1] Fala a Evan que veio barganhar, para que ele devolva o dinheiro e ninguém se machucará.'
                         '\n[2] Parte para a briga.'
                         '\n[3] Corre para chamar reforços.\n')

        escolha6 = validar(escolha6)
        if escolha6 == 1:
            input(f'{red}Evan:{none} Haha, que engraçado... Você vem até a nossa sede para arrumar confusão, '
                  'mas agora quer barganhar?')
            input(f'{red}Evan:{none} A única coisa que vai acontecer aqui é a sua morte.\n')
            input('--> Os capangas então fecham um círculo em volta de você, '
                  'mas você os golpeia com um ciclone de espadadas.')
            input('--> Você consegue ferir gravemente três capangas.')
            input('--> Evan e o outro capanga desferem facas no seu braço direito.')
            input('--> Você apara as lâminas e os finaliza com um corte horizontal na garganta de ambos.')
        elif escolha6 == 2:
            input('--> Você vira-se para Evan e o assassina rapidamente.')
            input('--> Com a morte do líder, os quatro capangas ficam abalados.')
            input('--> Você aproveita o choque de dois deles e os finaliza.')
            input('--> O último capanga tenta desesperadamente lhe atacar, '
                  'mas você defende-se do ataque e corta sua cabeça.')
        elif escolha6 == 3:
            input('--> Você corre para chamar reforços, mas é cercado pela gangue.')
            input(f'{red}Evan:{none} Você percebeu que está em desvantagem e quer fugir? Você não irá a lugar algum.\n')
            input('--> Você luta contra eles aparando e contra-atacando, até sobrar somente Evan.')
            input('--> Você quebra a defesa dele com poderoso chute, jogando-o no chão e finalizando-o rapidamente.')

        input('--> Com toda a gangue derrotada, você devolve o dinheiro ao Moe e volta ao centro da cidade.')

    quest1 = True


def guerreiro_quest2():
    global quest2

    input('--> Chegando no ferreiro Yudi, você tenta negociar uma espada, porque a sua não é a das melhores.\n')
    input(f'{green}Yudi:{none} Estou forjando a mais forte das espadas que já fiz, a qual batizarei de Força!')
    input(f'{green}Yudi:{none} Gostaria que ela fosse usada por um {classe} honrado como você. '
          f'Vamos negociar, lhe dou ela em troca de um favor.\n')
    input('--> Você pergunta qual do que ele precisa.\n')
    input(f'{green}Yudi:{none} Este favor não ajudará somente a mim, mas a muitos comerciantes e a sociedade em geral.')
    input(f'{green}Yudi:{none} A Marinha do reino é corrupta. Estão roubando minhas espadas e me silenciando '
          'por meio de seu poder.')
    input(f'{green}Yudi:{none} Isso não ocorre só comigo, fazem isso com diversos comerciantes da costa marítima.')
    input(f'{green}Yudi:{none} Eles ainda estão negociando com piratas, permitindo que os mesmos roubem lojas '
          'em troca de uma porcentagem dos saques.\n')

    escolha1 = 0    # informações sobre a Marinha
    while escolha1 < 1 or escolha1 > 3:
        escolha1 = input('--> Diante dessa situação, você diz:'
                         '\n[1] Negócio fechado, acabarei com essa máfia e ficarei com a espada.'
                         '\n[2] Essa história está estranha... Lutei pelo reino na guerra.'
                         '\n[3] Só receberei uma espada por isso?\n')

        escolha1 = validar(escolha1)
        if escolha1 == 1:
            input(f'{green}Yudi:{none} Que bom que aceitou, pode completar o serviço. '
                  'Sua espada estará pronta quando retornar.\n')
        elif escolha1 == 2:
            input(f'{green}Yudi:{none} Mas é aí que você se engana, a Marinha não ajudou em nada na guerra.')
            input(f'{green}Yudi:{none} Disseram que deveriam permanecer no reino para protege-lo enquanto '
                  'os soldados estavam fora, mas mesmo assim os furtos continuaram.')
            input(f'{green}Yudi:{none} Esse esquema ainda não foi descoberto pelo Rei ou os soldados reais, '
                  'só estou lhe contando pois acredito que você pode acabar com eles sem causar tumulto.')
            input(f'{green}Yudi:{none} Quando você derrota-los, todos saberão da farsa e lhe agradecerão por isso.\n')
            input('--> Para provar seu ponto, o ferreiro chama comerciantes próximos, que confirmam a tal farsa.')
            input('--> Convencido, você aceita o acordo.')
        elif escolha1 == 3:
            input(f'{green}Yudi:{none} Não será uma simples espada, ela possuirá uma resistência e corte incomuns.')
            input(f'{green}Yudi:{none} E o principal, você ganhará o reconhecimento de todos quando a notícia vier.\n')
            input('--> Como você precisava de uma espada, você aceita a missão.')

    escolha2 = 0    # conversa com o guarda
    while escolha2 < 1 or escolha2 > 2:
        input('--> Você vai até a Marinha, e próximo à base há um guarda do reino.\n')
        input(f'{yellow}Guarda do Reino:{none} Ei {classe}, o que veio fazer aqui?\n')

        escolha2 = input('--> Você diz que:'
                         '\n[1] Veio acabar com a farsa da Marinha.'
                         '\n[2] Veio perguntar se ele vê os almirantes e piratas de papo.\n')

        escolha2 = validar(escolha2)
        if escolha2 == 1:
            input('--> Você conta tudo o que sabe do esquema para ele e diz que vai acabar com isso.')
            input(f'{yellow}Guarda do Reino:{none} Finalmente alguém para por um fim nesses corruptos.')
            input(f'{yellow}Guarda do Reino:{none} Nós não dizemos nada pois somos ameaçados por nossos superiores.\n')
        elif escolha2 == 2:
            input('--> Ele afirma com a cabeça. Almirantes e piratas então têm um acordo, como o ferreiro lhe dissera.')

    escolha3 = 0    # despedida do guarda
    while escolha3 < 1 or escolha3 > 3:
        input(f'{yellow}Guarda do Reino:{none} Vá então, agora a angústia de não poder fazer nada acabará.\n')

        escolha3 = input('--> Antes de entrar, você diz:'
                         '\n[1] Quer ir comigo? Você terá a oportunidade de se vingar desses corruptos opressores.'
                         '\n[2] Estou indo, não será tão difícil quanto à Guerra dos Reinos.'
                         '\n[3] Farei o possível para derrota-los, deseje-me sorte!\n')

        escolha3 = validar(escolha3)
        if escolha3 == 1:
            input(f'{yellow}Guarda do Reino:{none} Não tenho mais vigor para isso, estou velho. '
                  'Eu costumava ser um aventureiro como você, até que levei uma flechada no joelho...')
            input(f'{yellow}Guarda do Reino:{none} Pode ir, eu trarei alguns soldados para caso precise de reforço.\n')
        elif escolha3 == 2:
            input(f'{yellow}Guarda do Reino:{none} Vá e acabe com eles. '
                  'Vou trazer alguns soldados para caso você seja surpreendido por eles.\n')
        elif escolha3 == 3:
            input(f'{yellow}Guarda do Reino:{none} Boa sorte. '
                  'Caso precise de ajuda, recue e eu chamarei mais guardas para lhe apoiarem.\n')

    escolha4 = 0    # invasão à base
    while escolha4 < 1 or escolha4 > 3:
        escolha4 = input('--> Ao chegar na base, você entra:'
                         f'\n[1] Chutando o portão com força, pois não é um portão que irá parar um {classe} como você.'
                         '\n[2] Olhando ao redor, procurando alguma entrada.'
                         '\n[3] Saltando o portão, que não é tão alto assim.\n')

        escolha4 = validar(escolha4)
        if escolha4 == 1:
            input('--> O portão, que estava velho e oco, se abre sem barulhos altos, então você ainda está incógnito.')
        elif escolha4 == 2:
            input('--> Você acha um vão quebrado no muro e passa por ele, avançando para dentro da base.')
        elif escolha4 == 3:
            input('--> Caindo do outro lado, você percebe que nenhum inimigo sabe que você está lá.')

    escolha5 = 0    # ataque à Marinha
    while escolha5 < 1 or escolha5 > 3:
        input('--> Dentro da fortaleza ocorria uma reunião entre os marinheiros corruptos e os piratas.')

        escolha5 = input('--> Percebendo que estavam negociando, você:'
                         '\n[1] Ataca todos com a fúria de um guerreiro.'
                         '\n[2] Espera os piratas saírem da fortaleza após o fechamento do acordo.'
                         '\n[3] Volta ao Guarda do Reino para invadir com os reforços.\n')

        escolha5 = validar(escolha5)
        sorte = teste(3)
        if escolha5 == 1:
            if sorte == 1:
                input('--> Você desperta uma força berserk e ataca os marinheiros com um ciclone de espadadas, '
                      'derrotando metade deles com um único golpe.')
                input('--> O restante, chocados e hesitantes, atacam você.')
                input('--> Você apara e contra-ataca os marinheiros, mas é acertado pelos piratas.')
                input('--> Como estes estavam em menor número, você os ignora e continua defendendo e contra-atacando.')
                input(f'--> Reduzido o número de inimigos a cinco, você lança sua {equipamento} em um deles e mata-o.')
                input('--> Com apenas seus punhos, você finaliza mais dois inimigos.')
                input(f'--> Os dois últimos tentam correr, mas você retoma sua {equipamento} novamente e os alcança, '
                      'fatiando-os.')
            else:
                input('--> Você desperta uma fúria incomum e fatia alguns marinheiros, mas os piratas se unem a eles.')
                input('--> Com os inimigos unidos, você é golpeado de diversos lados.')
                input('--> Quando você está prestes a ser derrotado, o reforço que o Guarda do Reino chamou chega.')
                input('--> Com a chegada deles, os inimigos se distraem por um instante e você levanta do chão, '
                      'se reagrupa com eles, e derrotam o restante dos inimigos.')
                input('--> Você encontra o Guarda do Reino e agradece a ele e aos outros pelo reforço.')
        elif escolha5 == 2:
            if sorte == 3:
                input('--> Quando os piratas saem da base, você avança sorrateiramente e mata três marinheiros.')
                input('--> Você é avistado e eles formam um círculo ao redor. Após receber vários golpes, você cai.')
                input('--> Então, aparecem os guardas de apoio, e com a distração você consegue se recuperar.')
                input('--> Reagrupado a eles, você consegue derrotar o restante dos marinheiros corruptos.')
                input('--> Você agradece aos guardas do reino e àquele que chamou os reforços.')
            else:
                input('--> Assim que os piratas saem da fortaleza você ataca, matando dois inimigos sorrateiramente.')
                input('--> Antes que os outros pudessem perceber sua presença, '
                      f'você derrota mais dois inimigos e lança a sua {equipamento} em um a frente.')
                input('--> Desse modo, metade dos marinheiros já foram derrotados.')
                input('--> Você é avistado e partem para cima, mas você apara seus ataques tão habilmente que '
                      'consegue eliminar três inimigos.')
                input('--> Os dois restantes avançam sobre você, e com uma estocada você os perfura simultaneamente.')
        elif escolha5 == 3:
            input('--> Você retorna ao Guarda do Reino.')
            input('--> Agora com uma tropa de guardas, vocês invadem a base, surpreendendo os marinheiros e piratas.')
            input('--> Vocês derrotam todos os inimigos facilmente.')

    escolha6 = 0    # retorno ao ferreiro
    while escolha6 < 1 or escolha6 > 4:
        input('--> Com todos os inimigos derrotados e sua missão cumprida, você retorna ao ferreiro Yudi.')

        escolha6 = input('--> Chegado ao ferreiro, você:'
                         '\n[1] Agradece por ele ter lhe informado sobre a Marinha, '
                         'e afirma que a cidade agora está livre da corrupção.'
                         '\n[2] Diz que cumpriu o que foi combinado e que agora precisa da espada Força.'
                         '\n[3] Conta que ganhou reputação com o povo e os guardas e ele não precisa entregar a espada.'
                         '\n[4] Fala para ele que a missão foi difícil e que ele entregue a espada, '
                         'ou terá o mesmo destino dos marinheiros e piratas.\n')

        escolha6 = validar(escolha6)
        if escolha6 == 1:
            input(f'{green}Yudi:{none} Que bom que tudo está resolvido, sem àqueles marinheiros que enganavam todos.')
            input(f'{green}Yudi:{none} Tome a espada Força. Boa sorte nas suas jornadas, '
                  'quando enfrentar alguém forte, espero que a Força esteja com você.')
        elif escolha6 == 2:
            input(f'{green}Yudi:{none} Agora que libertou a cidade desses corruptos, você merece empunhar esta espada.')
            input(f'{green}Yudi:{none} Tome, é sua. Boa sorte na sua jornada.')
        elif escolha6 == 3:
            input(f'{green}Yudi:{none} Você pode ter ganhado reputação, mas mesmo assim eu insisto que fique com ela.')
            input(f'{green}Yudi:{none} A sua aliada a Força será, e poderosa aliada ela é. Leve-a.')
        elif escolha6 == 4:
            input(f'{green}Yudi:{none} Entendo sua fúria {nome}, desculpe-me colocar você nessa missão, '
                  'mas você, como sempre, obteve sucesso.')
            input(f'{green}Yudi:{none} Tome a espada, você a merece pois é corajoso.')

        input('--> Você pega a espada Força e segue para o centro da cidade.')

    quest2 = True


def guerreiro_quest3():     # TODO - Revisar função
    global nome
    global classe
    global quest3

    input('--> Ao chegar no bosque você encontra uma rachadura enorme no solo, parecia um golpe de uma espada gigante')
    escolha = 0
    while escolha < 1 or escolha > 4:
        escolha = input(f'--> Então você:\n'
                        f'[1] Vai investigar se foi causada por algum terremoto ou tremor.\n'
                        f'[2] Pensa que pode ser de um gigante e vai procurá-lo.\n'
                        f'[3] Pensa que pode ser alguma criatura perigosa que precisa morta. \n'
                        f'[4] Segue andando pelo bosque.')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('--> Você decide que pode ter sido causada por terremotos e avança para explorar o bosque.')
    elif escolha == 2:
        input('--> Pensa que pode ser um gigante, então vai procurá-lo avante no bosque.')
    elif escolha == 3:
        input(
            '--> Você pensa que se for uma criatura perigosa provável que não foi para a cidade, então está no bosque, então você vai procurá-la.')
    elif escolha == 4:
        input('--> Continua caminhando sem pensar em que pode ser aquilo.')

    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input('--> No caminho você encontro um menino e um cão, você pergunta:\n'
                        '[1] Vocês estão perdidos?\n'
                        '[2] Vocês sabem se tem algum gigante ou alguma criatura perigosa neste bosque?\n'
                        '[3] O que vocês estão fazendo aqui é perigoso. \n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(
            'Menino: Claro que não cara, a gente tá na nossa aventura, perdido deve tá você então cuidado com os gigantes.')
        input(f'{nome}: Não sabia que tinha gigantes aqui, onde eles ficam?')
    elif escolha == 2:
        input('Menino: Sim, tem dois gigantes nesse bosque.')
    elif escolha == 3:
        input('Perigoso? tá zoando com a nossa cara é? acabamos de fazer amizade com os gigantes, somos radicais!.')
        input(f'{nome}: Desculpa "guerreiros radicais", onde fica esses gigantes?')

    input(
        'Menino: Eles ficam um para a direita e o outro para a esquerda do bosque. Eles duelam um contra o outro todos os dias.')
    input('Menino: Agora falou, tá na hora de aventura, vem Jack')

    escolha = 0
    input('--> Você chega ao local de um dos gigantes, ele te fala que se chama Jotun.')
    while escolha < 1 or escolha > 3:
        escolha = input(f'Jotun: O que você quer?\n'
                        f'[1] Quero treinar minha força duelando com você.\n'
                        f'[2] Quero saber se é verdade que tem outro gigante no bosque.\n'
                        f'[3] Quero saber se é verdade que os gigantes tem dez vezes a força de um humano comum. \n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'Jotun: Não posso agora, estou exausto de lutar com o outro gigante, o Brog.')
    elif escolha == 2:
        input(f'Jotun: Há o Brog meu rival de duelo.')
    elif escolha == 3:
        input(f'Jotun: Sim, mesmo que o gigantes não treinem para se fortalecer esta é sua força mínima.')
        input(
            'Jotun:Eu sou o mais forte gigante desse reino, mas para decretar isso, o combate entre eu e Brog precisa ter fim.')

    input('Jotun: Brog e eu somos gigantes guerreiros de Elbaff, mas por conta de um desentendimento entre nós.')
    input('Jotun: Não podemos retornar para lá, a não ser o vencedor do duelo.')
    input('Jotun: Porém este duelo já persiste por 10 anos só empatando')

    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'--> Ele pergunta se você quer saber de mais alguma coisa. Você responde:\n'
                        f'[1] Sim, por que vocês ainda insistem nesse duelo?\n'
                        f'[2] Sim, me explique o que é Elbaff.\n'
                        f'[3] Não, vamos até Brog parece que está pegando fogo para o lado que ele fica.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('Jotun: Pela esperança de retornar para Elbaff e voltar a ser um guerreiro honrado e defender a nação.')
    elif escolha == 2:
        input('Jotun: Elbaff é a nação de gigantes guerreiros, os mais fortes e gloriosos guerreiros estão lá.')
    elif escolha == 3:
        input('Jotun: Eu estava descansando, mas vamos, vai que aquele desmiolado está em apuros.')

    input('--> Vocês escutam que tem alguém em perigo pedindo ajuda e correm para procurar, pode ser Brog.')
    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input(
            '--> Vocês chegam perto do pedido, e avista Brog preso por piratas enquanto descansava do duelo diário. Você:\n'
            '[1] Corre para ajudá-lo.\n'
            '[2] Deixa ele se resolver, pois é um honrado guerreiro de Elbaff, ajudá-lo pode ferir seu orgulho.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('--> Você corre para cortar as cordas que prenderam Brog enquanto ele descansava.')
        input('--> Mas os piratas apontam canhões para você e Jotun.')
    elif escolha == 2:
        input('--> Você não quer ajudar Brog pois ele pode ficar com o orgulho ferido.')
        input('--> mas Jotun te conta que Brog foi pego desprevino então ele não tem culpa.')
        input('--> Quando você vai ajudar o gigante, os piratas miram canhões em você e Jotun.')

    input('Os piratas ameaçam vocês falando que não teriam chances')
    sorte = randint(1, 4)
    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input('--> Você:\n'
                        '[1] Ataca com o orgulho de um guerreiro para salvar Brog.\n'
                        '[2] Ataca junto com Jotun para que juntos derrotem os piratas e libertem Brog.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1 and sorte == 1:
        input('--> Você ataca com orgulho e fúria de um guerreiro cortando as balas de canhão, apavorando os piratas.')
        input('--> Você não deixa que eles escapem e corre atrás de cada um cortando-os.')
        input('--> Assim com todos os piratas mortos, Brog é salvo.')
    elif escolha == 1:
        input(f'--> Você corre para atacar os piratas porém eles disparam o canhão que explode próximo a você.')
        input(
            '--> Jotun entra na briga para ajudar você e o outro gigante, com isso você mesmo caído derrota o pirata que ia lhe golpear.')
        input('--> Consegue ficar de pé novamente, você e Jotun juntos conseguem derrotar os piratas e libertar Brog.')
    elif escolha == 2:
        input('--> Você e Jotun atacam junto destruindo as balas e os canhões com golpes rápidos e fortes.')
        input('--> Vocês acabam com todos os piratas e libertam Brog.')

    input(
        'Os gigantes agradecem a sua ajuda e falam que você possui um espírito e dom de batalha digno de um guerreiro de Elbaff')
    input('Você deseja sorte para que eles consigam resolver esse duelo e volta para a cidade.')
    quest3 = True


def arqueiro_quest1():
    global nome
    global quest1
    escolha = 0
    maldicao = False
    flecha = False

    input('--> Está na cidade, na frente do esgoto.')
    input('--> Escuta vozes do seu interior.')
    while escolha < 1 or escolha > 3:
        escolha = input('\n--> Vê um mendigo próximo a entrada.\n'
                        '[1] Ajuda o mendigo e depois entra.\n'
                        '[2] Espanta o mendigo e entra.\n'
                        '[3] Ignora-o e entra.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('--> Você dá para o mendigo algumas moedas.')
        input('Mendigo: muito obrigado aventureiro, na verdade eu não sou um mendigo,\n'
              'eu sou um nobre disfarçado para descobrir e premiar os de coração caridoso.')
        input('Mendigo: aceite este presente pela dedicação de bondade!')
        input('--> Recebeu uma flecha de fedor!')
        input(f'{nome}: o que eu vou fazer com isso? Mas vou guardar mesmo assim.')
        flecha = True
    elif escolha == 2:
        input('--> Você xinga o mendigo e diz para ele sair dali.')
        input('Mendigo: Que mau humor! Não deveria tratar ninguém assim.')
        input('Mendigo: agora vai receber o que merece!')
        input('--> Você foi amaldiçoado.')
        input(f'{nome}: vou entrar logo.')
        maldicao = True
    elif escolha == 3:
        input('--> Você resolve passar longe do mendigo e entra no esgoto.')

    input('--> Você entra no esgoto, e sente um cheiro nada agradável.')
    input(f'{nome}: Que cheiro insuportável, só entrei porque ouvi umas vozes sinistras...')
    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input('--> Quando olha para o chão vê quatro pequenas tartarugas fugindo de  algo.\n'
                        '[1] Segue as tartarugas\n'
                        '[2] Vai no sentido contrário\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('--> Você segue as tartarugas para ver onde elas irão.')
        input('--> Depois de um tempo, chega a um corredor com um rato e uma pizza estragada')
        input(f'{nome}: não tem nada aqui, só essas tartarugas e esse rato.')
        input('--> Você volta para a entrada do esgoto, depois pega o caminho oposto.')
    elif escolha == 2:
        input(
            '--> Você caminha um pouco e encontra alguns homens encapuzados, parecendo pertencer a algum culto macabro.')
        input('--> Também vê um homem preso e amarrado no meio da sala.')
        input(f'{nome}: Nossa! Eu sabia que tinha algo estranho por aqui!')

    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input(f'{nome}: O que eu vou fazer?\n'
                        '[1] Se aproxima silenciosamente\n'
                        '[2] Exige explicações\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('--> Você se aproxima silenciosamente e fica escondido')
        input('--> Espera mais um pouco e escuta um dos homens encapuzados dizer:')
        input('Cultista: muito bem, meus irmãos, como devemos sacrificá-lo?')
        input('Outro cultista: eu acredito que a melhor forma seria afogá-lo na água do esgoto.')
    elif escolha == 2:
        input('--> Você toma coragem e quando vai começar a falar escuta:')
        input('Cultista: muito bem, meus irmãos, como devemos sacrificá-lo?')
        input(
            '--> Percebendo as intenções dos cultistas, você desiste de pedir explicações e se aproxima silenciosamente.')

    input(f'{nome}: esses caras realmente não estão brincando aqui.')
    input(f'{nome}: eu não sei a razão por que querem sacrificá-lo, mas eu não vou deixar!')

    escolha = 0
    acoes = 2
    if flecha:
        acoes = 3
    while escolha < 1 or escolha > acoes:
        print('--> Você deve fazer algo:\n'
              '[1] Ataca os cultistas violentamente.\n'
              '[2] Pega um por um silenciosamente.')
        if acoes == 3:
            print('[3] Atira a bomba de fedor.\n')
        escolha = int(input())

        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('--> Você começa lançando flechas nos cultistas que não tem muito como se defender.')
        input('--> Alguns deles lançam suas pequenas facas. A maioria erra, mas uma acerta seu ombro.')
        input(f'--> Com dor, {nome} senta no chão e descansa por alguns momentos.')
        input('Membro do culto: o que foi, já foi derrotado?')
        input('--> Os membros do culto restantes vão para cima de você.')
        input('--> Com toda a sua experiência de combate,\n'
              'já previa isso, e já estava com o arco carregado com múltiplas flechas.')
        input('--> Acerta todos os inimigos restantes.')
    elif escolha == 2:
        input('--> Você pega o cultista mais próximo pelas costas, e consegue\n'
              'abater mais três individualmente.')
        if maldicao:
            input('--> Os inimigos restantes te percebem e te atacam desferindo golpes com suas pequenas facas.')
            input('--> Alguns dos golpes pegam de raspão, mas fazem rasgos em sua pele.')
            input(
                '--> Por ter um arco e flechas você não se sai tao bem no combate corpo a corpo, então recua e os lança algumas flechas.')
        else:
            input('--> Os homens estão um pouco afastados uns dos outros, e não te percebem.')
            input('--> Você continua com a sua estratégia até que o último o percebe.')
            input('--> vendo que todos os outros membros estão no chão, ele foge.')
    elif escolha == 3:
        input('--> Você atira a bomba de fedor que o mendigo te deu, no chão, no meio dos homens encapuzados.')
        input('Membro dos cultistas: O que é isso? De onde vem esse cheiro?')
        input(
            f'{nome}: Caramba! esse cheiro é muito pior que o cheiro normal do esgoto, não quero nem saber como aquele homem conseguiu isso.')
        input('--> Todos os cultistas saem correndo do esgoto e deixam o homem amarrado ali.')
        input('--> Após alguns segundos, o cheiro desaparece.')

    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input('--> Agora só sobraram você e o homem preso.\n'
                        '[1] Liberte o homem preso\n'
                        '[2] Pergunte porque ele seria sacrificado\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('--> Você solta o homem')
        input('Homem: Não sei quem te enviou mas obrigado pela ajuda!')
        input(f'{nome}: eu não iria te deixar morrer neste tribunal esquisito!')
        input('Homem: isso não era um tribunal, eles iriam me sacrificar para as chuvas voltarem.')
    elif escolha == 2:
        input('Homem: eles são  loucos, eu não fiz nada!')
        input('--> Você solta o homem')
        input('Homem: Não sei quem te enviou mas obrigado pela ajuda!')
        input(f'{nome}: eu não iria te deixar morrer neste tribunal esquisito!')
        input('Homem: isso não era um tribunal, eles iriam me sacrificar para as chuvas voltarem.')

    input('Homem: só que eles estavam certos, graças a minha magia esta região não terá chuvas por um bom tempo')
    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input('O homem que é um mago, começa a abrir um portal\n'
                        '[1] Pergunte porque ele quer que não chova mais\n'
                        '[2] Mate-o\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'{nome}: porque você quer impedir a chuva?')
        input('Mago: Eu quero que um fazendeiro da região perca sua colheita.')
        input(f'{nome}: não entendi,  ele fez alguma coisa errada?')
        input('Mago: não sei se você já o conheceu, mas se conhecer, vai entender o porque...')
        input('--> Percebendo que você está distraído, o mago entra no portal.')
    elif escolha == 2:
        input(f'{nome}:eu não vou deixar você impedir as chuvas, os fazendeiros precisam delas para\n'
              'as colheitas, e indiretamente, você matará muitas pessoas por falta de alimentos!')
        input('--> O mago lança  uma magia deixando-o cego, e depois se esforça para terminar o portal.')
        input('--> Você consegue se recuperar e atira uma flecha no peito do mago que cai no chão.')
        input(f'{nome}: me desculpe, mas esse é o meu trabalho, ajudar as pessoas.')
        input('--> Você assassina o mago.')
    input('--> Não tendo mais nada, você sai do esgoto e volta para a cidade.')
    quest1 = True


def arqueiro_quest2():
    global nome
    global classe
    global reino
    global quest2

    input('Você chega no bosque e encontra meia dúzia de homens tristes.')
    input('Marcos: Olá viajante, eu sou o Marcos e esse são meus companheiros, somos camponeses e precisamos de ajuda.')
    input(
        'Marcos: Fomos roubados por um homem chamado Ron, ele é fazendeiro e possui uma fazenda que fica próxima daqui.')
    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'--> Você:\n'
                        f'[1] Questiona como eles foram roubados.\n'
                        f'[2] Pergunta se o homem que os roubou estava sozinho.\n'
                        f'[3] Pergunta para onde ele foi.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'{nome}: Como vocês foram roubados?')
        input(f'Marcos: Fomos roubados enquanto colhíamos nossos grãos e estacávamos no armazém.')
        input(f'Marcos: Ele chegou com uma espingarda ameaçando-nos de morte e levou toda nossa colheita.')
        input(f'Marcos: Se você quiser nos ajudar basta ir até a grande fazenda dele que fica no leste do bosque.')
    elif escolha == 2:
        input(f'{nome}: Esse homem estava sozinho quando roubou vocês?')
        input(f'Marcos: Sim, ele apontou uma espingarda para que déssemos todos os nossos grãos a ele.')
        input(f'Marcos: E levou tudo para a grande fazenda dele que está no leste do bosque.')
    elif escolha == 3:
        input(f'{nome}: Onde ele foi com o que é de vocês?')
        input(f'Marcos: Ele levou nossos grãos para a grande fazenda dele que fica no leste desse bosque.')

    input('--> Você vai rumo a fazenda de Ron para ajudar os camponeses.')
    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input(f'--> Perto da fazenda do leste você encontra um trabalhador e pergunta:\n'
                        f'[1] {nome}: O dono dessa fazenda está?\n'
                        f'[2] {nome}: Você sabe se o dono dessa fazenda chegou com alguma carga hoje?.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'Trabalhador: Sim, o patrão está na casa principal da fazenda. Mas o que você quer com o patrão?')
    elif escolha == 2:
        input(f'Trabalhador: O patrão chegou com uma carroça cheia de grãos há umas duas horas.')
        input('Trabalhador: Guardou no silo e agora está na casa principal. Mas o que você quer com ele?')

    input(
        '--> Você conta que está procurando por ele porque alguns camponeses acusaram-no de ter roubado todos os grãos deles.')
    input('Trabalhador: Entendi a situação, o patrão Ron não é má pessoa, mas tem uma tremenda ganância.')
    input('Trabalhador: Por isso acho que essas acusações possam até ser verdadeiras.')
    input('--> Você o agradece pela ajuda e segue para a casa principal da fazenda.')
    input('--> Chegando na casa principal encontra o Ron levando munições de espingarda para a carroça.')
    input('--> Ele quando avista você entra em um estado de choque e começa a correr de você.')
    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'--> Então você:\n'
                        f'[1] Lança uma flecha em seu joelho.\n'
                        f'[2] Corre na direção dele e o derruba.\n'
                        f'[3] Grita para que ele pare de fugir.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'--> Você acerta a flecha de raspão no joelho dele que machucado cai no chão.')
        input('Ron: Quem é você e o que quer? Seu desgraçado, por que me lançou essa flecha?')
    elif escolha == 2:
        input(f'--> Você corre até ele e com uma ombrada o derruba no chão.')
        input('Ron: Quem é você e o que quer? Miserável porque veio aqui? Para me derrubar?')
    elif escolha == 3:
        input(f'--> Pare de fugir, preciso falar com você! .')
        input('--> Ron com uma expressão de confuso para de fugir para que ouça o que você quer.')

    input(f'{nome}: Sou o {nome}, vim até aqui porque encontrei pessoas que falaram que você as roubou.')
    input(f'{nome}: Perdão pela atitude rude, mas não ia deixá-lo fugir sem que esta situação fosse resolvida.')
    input('Ron: Eu não roubei nada de ninguém, peguei até outro caminho no bosque para não arrumar confusão.')
    input('Ron: Eu corri pois pensei que você tinha sido enviado por alguns imbecis que pegam no meu pé.')
    input(f'{nome}: Mas então o que você trouxe nessa carroça?')
    input('Ron: Grãos e minha espingarda.')
    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'--> Com essa situação você:\n'
                        f'[1] Decide levar o carregamento de grãos para os camponeses.\n'
                        f'[2] Tenta convencer Ron para irem ao bosque com a carroça e resolverem essa questão.\n'
                        f'[3] Fala que está situação está muito confusa e que você vai embora. \n')

    if escolha == 1:
        input(f'{nome}: Eu vou levar essa carroça de grãos para os camponeses que você roubou e não tente me impedir.')
        input('Ron: Então me leve junto para que eu encontre os mentirosos que me acusam')
    elif escolha == 2:
        input(f' {nome}: Vamos com a carroça de grão ao bosque para que lá resolvamos esta situação.')
        input('--> Ron com receio de sua rudeza concorda.')
    elif escolha == 3:
        input(f'{nome}: Essa situação está confusa demais, vou voltar para a cidade e não vou ajudar ninguém.')
        input(f'{nome}: E falarei para os camponeses que resolvam esta pendência com você.')
        input(f'Ron: Vamos para esse bosque de carroça para que eu encontre os mentirosos que me estão acusando.')

    input(
        '--> Então vocês partem de carroça para o bosque. Ao chegar nos camponeses você repara que Ron começa a suar de nervoso.')
    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'--> Vocês descem da carroça e você:\n'
                        f'[1] Confia nos camponeses e entrega os grãos que estavam na carroça para eles e obriga Ron a se desculpar.\n'
                        f'[2] Pede para que Ron se defenda das acusações dos camponeses.\n'
                        f'[3] Confia em Ron e conversa com ele.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'--> Você entrega todos os grãos para os camponeses que agradecem,\n '
              f'e Ron com essa situação pede desculpas com uma voz quase inaudível e volta para a fazenda em sua carroça o mais rápido possível.')
    elif escolha == 2:
        input(f'--> Ron parece intimidado pelos camponeses e as acusações e não consegue falar nada.')
        input(
            '--> Você leva essa falta de argumento como uma comprovação de crime e decide entregar os grãos para os camponeses.')
        input('--> Ron então amedrontado pega sua carroça, agora vazia, volta para a fazenda o mais rápido possível.')
    elif escolha == 3:
        input(f'--> Você decide confiar em Ron, pois aquelas acusações estão muito infundadas.')
        input('Ron: Agora que você está confiando em mim vou tomar coragem e contar-lhe toda a verdade.')
        input(
            'Ron: Todo os sábados eu passo por este caminho do bosque com a carroça carregada de grãos que comprei na venda.')
        input(
            'Ron: Porém muitas vezes esses vadios que se dizem camponeses, que são na verdade ex-funcionários meus, ficam neste caminho para me roubar.')
        input(
            'Ron: E ainda me ameaçam para que eu não conte a ninguém. Mas com você agora percebi que eles não teriam coragem para me matar neste momento.')
        input('Ron: Então por favor, dê uma lição neles, mate esses ladrões para que não me importunem mais.')

    if (escolha == 1) or (escolha == 2):
        input('--> Após o assunto estar resolvido, você decide seguir para que saia do bosque e volte à cidade.')
        input('--> Mas um bruxo que estava sentado na grama lhe chama e diz')
        input('Bruxo: Gostaria de lhe esclarecer uma coisa. Mas antes, dê um trocado ao seu Bruxo.')
        escolha = 0
        while escolha < 1 or escolha > 3:
            escolha = input(f'--> Então você:\n'
                            f'[1] Da duas moedas a ele e pergunta o que ele quer esclarecer.\n'
                            f'[2] Fala que não tem dinheiro, mas pergunta o que ele quer falar.\n'
                            f'[3] Fala para que ele pare de mendigar e que você não tem interesse no que ele tem a falar.\n')
            if type(escolha) == str and escolha == '':
                escolha = -1
            else:
                escolha = int(escolha)

        if escolha == 1:
            input(
                f'Bruxo: Obrigado gentil arqueiro, mas tenho algo triste para lhe dizer. Você foi enganado por aqueles camponeses.')
            input('Bruxo: Eles são ex-empregados de Ron e vivem o roubando do caminho da venda a fazenda.')
            input(
                'Bruxo: Provavelmente ele começou a suar e também não te contou isso porque é constantemente ameaçado por eles de morte.')
            input(
                'Bruxo: Eu não o ajudo porque aqueles camponeses também sabem aonde minha família mora e também me ameaçam.')
            input(
                'Bruxo: você poderia ter acabado com esta situação, mas apenas colaborou com eles sem saber, é uma pena.')
            input('--> Após dizer isto o bruxo some com sua bruxaria e você segue triste para o centro da cidade.')
        elif escolha == 2:
            input(f'Bruxo: Sem problemas, mas preciso te contar que você foi enganado pelos camponeses.')
            input('Bruxo: Eles são ex-empregados de Ron e vivem o roubando do caminho da venda a fazenda.')
            input(
                'Bruxo: Provavelmente ele começou a suar e também não te contou isso porque é constantemente ameaçado por eles de morte.')
            input(
                'Bruxo: Eu não o ajudo porque aqueles camponeses também sabem aonde minha família mora e também me ameaçam.')
            input(
                'Bruxo: você poderia ter acabado com esta situação, mas apenas colaborou com eles sem saber, é uma pena.')
            input(
                '--> Após dizer isto o bruxo some com sua bruxaria e você segue decepcionado para o centro da cidade.')
        elif escolha == 3:
            input(
                f'Bruxo: Agora compreendo o porque os camponeses te engaram facilmente, você é homem ignorante por natureza.')
            input(
                '--> Após dizer isto o bruxo desaparece por um portal. E você ignora esta situação segue seu caminho para o centro da cidade.')

    elif escolha == 3:
        input('--> Após ouvir Ron contar tudo.')
        escolha = 0
        while escolha < 1 or escolha > 2:
            escolha = input('--> Você:\n'
                            '[1] Mata todos os camponeses para livrar Ron do mal que eles lhe faziam.\n'
                            '[2] Acha que Ron está tentando te manipular e deixa que eles se resolvam.\n')
            if type(escolha) == str and escolha == '':
                escolha = -1
            else:
                escolha = int(escolha)

        if escolha == 1:
            input(
                f'--> Você agora sabendo da verdade, atira flecha nos camponeses malditos pondo fim aos roubos deles os matando.')
            input(
                f'Ron: Muito obrigado {nome}, percebi que você era justo e ainda bem que lhe contei tudo. Obrigado mesmo')
            input('--> Ron volta para a fazenda e você volta ao centro da cidade.')
        elif escolha == 2:
            input(
                f'{nome}: Esta situação tem muitas reviravoltas e lados a se tomar, estou farto de pensar. Vocês que se resolvam.')
            input('--> Ao dizer isso você vira as costas e vai embora.')
            input(
                '--> Já ao longe você olha para trás e percebe os camponeses fugindo com a carroça e Ron morto ao chão.')
            input('Você percebe agora que fez uma péssima e burra escolha e volta triste para o centro da cidade.')
    quest2 = True


def arqueiro_quest3():
    global nome
    global quest3

    atirou = False  # mostra se atirou nos caçadores

    input('--> Você está com um alce na mira, apenas esperando ele ficar parado.')
    input('--> De repente o alce leva um tiro de outros caçadores.')
    input('--> Todos do bando também são atingidos e morrem.')

    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input('--> Você fica bravo com essa atitude.\n'
                        '[1] Vai atrás dos caçadores.\n'
                        '[2] Vai procurar outros animais para caçar.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('--> Você pergunta porque mataram o bando inteiro.')
        input(f'{nome}: Porque vocês mataram todos?')
        input(f'{nome}: Se continuarem desse jeito, os animais não vão conseguir mais se reproduzir.')
    elif escolha == 2:
        input('--> Você começa a ir embora, quando um dos caçadores começa a gritar com você.')
        input('Caçador: O que foi, pegamos sua presa?')
        input(
            f'{nome}: O problema não é este, vocês mataram o bando todo, duvido terem que alimentar tantas bocas assim.')

    input('Caçador: Eu já cansei de ser caçador que caça apenas para sustento.')
    input('Caçador: Quero mesmo é que esses animais morram para que não resistam quando a cidade chegar aqui.')

    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input('--> Você resolve fazer algo:\n'
                        '[1] Tenta convencê-los de que a vida nativa é importante para o ecossistema.\n'
                        '[2] Ameaça-os para pararem.\n'
                        '[3] Atira em todos.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'{nome}: Se continuarem a matar os animais de maneira indiscriminada,\n'
              f'as futuras gerações podem nunca ver esses animais.')
        input('Caçador: Nossa, eu nunca pensei nisso. Imagine se eu não pudesse ver todos esses animais...')
        input('Outro caçador: É tudo mentira isso! Eles nunca vão desaparecer.')
        input('Caçador comovido: Cala boca! Não quero mais te ver hoje!')
        input('--> O caçador comovido começa a lutar contra os outros.')
        input('--> Você o ajuda e juntos derrotam os outros que ficam no chão.')
    elif escolha == 2:
        input(f'{nome}: Também gosto da caça, porém só abato animais para consumo.\n'
              f'{nome}: Não faço exagero, pois sei que a mãe natureza fará todos pagarem.')
        input(f'{nome}: Por isso, eu a defenderei para que continue para as próximas gerações.')
        input('Caçador: Não quero ser o responsável por acabar com a natureza!')
        input('Outro caçador: isso é tudo bobagem de defensor do meio ambiente!')
        input('--> O caçador comovido começa a lutar contra os outros.')
        input('--> Você o ajuda e juntos derrotam os outros que fogem.')
    elif escolha == 3:
        input('--> Você atira em todos, e eles caem no chão.')
        input(f'{nome}: Não adianta deixar homens como vocês vivos.')
        input('--> Você mata um por um dos caçadores, menos o último.')
        input('Caçador ferido: Se me deixar viver, eu juro que te ajudarei nessa luta a favor do meio ambiente.')
        input(f'{nome}: E porque eu acreditaria em você?')
        input('Caçador ferido: porque eu não quero ver a natureza acabar, ela sempre me ajudou no meu sustento.')
        input(f'{nome}: Tudo bem, na luta pela natureza, precisamos de muitos.')
        input('--> O ajuda com os ferimentos do caçador.')
        atirou = True

    input(f'{nome}: Qual o seu nome?')
    input(f'Sigurd: Me chamo Sigurd...')
    input(f'{nome}: Me chamo {nome}.')
    input(f'{nome}: Para quem vocês trabalham?')
    input('Sigurd: para o barão Barnet Riley de Nydoelith.')
    input(f'{nome}: vocês fazem uma carnificina apenas por que querem, ou esse barão que incentiva?')
    input('Sigurd: Na verdade, ele sempre disse que os animais dessa região estão amaldiçoados.')
    input('Sigurd: Por isso dizia que estávamos liberados para cometer atrocidades como a que viu a pouco.')
    input('--> Vocês seguiram até a residência do barão Barnet.')
    input('Sigurd: está vendo alí em cima, na janela? Aquele é o barão Barnet Riley.')
    input('--> A residência é bem protegida, então vocês decidem entrar pelos fundos.')

    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input('--> Tem apenas dois guardas vigiando a porta dos fundos.\n'
                        '[1] Cada um pega um dos guardas pelas costas.\n'
                        '[2] Você ataca os dois sozinho.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'{nome}: Tudo bem, no três. Um, dois, três...')
        input('--> Vocês conseguem apunhalar os dois guardas pelas costas.')
        input('Sigurd: Bom trabalho!')
    elif escolha == 2:
        input(f'{nome}: Deixa comigo.')
        input('--> Você apunhala um dos guardas, mas o outro te vê.')
        input('--> Quando o guarda vai abrir a boca, Sigurd o pega pelas costas.')
        input(f'{nome}: Eu disse que faria sozinho.')
        input('Sigurd: como é orgulhoso, ou será que não confia em mim?')
        input('Sigurd: Se eu não tivesse ajudado, todos já saberiam que estamos aqui.')

    input('--> Entram na mansão pelos fundos, e param em um pequeno armazém.')
    input('Sigurd: Tudo bem, por onde vamos?')
    input(f'{nome}: Precisamos subir, foi onde o avistamos.')
    input('Sigurd: Mas é arriscado demais subir pela escada principal, ela sempre é bem protegida...')
    input('Sigurd: Podemos subir por aqui. É uma escada velha que os funcionários usam, mas ninguém fica a vigiando.')
    input('--> Sigurd sobe primeiro. Quando ele estava terminando de subir, a escada quebrou, mas ele conseguiu subir.')
    input(
        'Sigurd: Espere aqui vou trazer algo para você subir também. Eles me conhecem, mas não sabem dos nosso plano.')

    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input('--> Com a quebra da escada, fez um barulho e um guarda próximo foi até o armazém investigar.\n'
                        '[1] Mata o funcionário silenciosamente.\n'
                        '[2] Continua em silêncio.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('--> Você espera o guarda virar de costas e o assassina.')
        input('--> Resolve esconder o corpo.')
    elif escolha == 2:
        input('--> Você continua escondido, torcendo para o guarda não te encontrar.')
        input('--> Depois de algum tempo, o guarda diz:')
        input('Guarda: foi só a escada. Ela já era velha mesmo, só precisamos saber se o último a usar está bem.')
        input('Guarda: Tudo bem, vou voltar pra minha posição, depois colocam outra escada no lugar.')
        input('--> O guarda vai embora.')

    input('--> Já se passou um tempo considerável desde que Sigurd foi buscar uma forma de subir.')
    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input('--> Você: \n'
                        '[1] Continua esperando.\n'
                        '[2] Procura uma forma de subir sozinho.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'{nome}: ele deve estar tendo dificuldades de encontrar algo para me ajudar a subir.')
        input('--> Espera mais um pouco.')
    elif escolha == 2:
        input('--> Começa a andar pela casa e escuta Sigurd conversando.')
        input('Sigurd: A escada quebrou, preciso de algo para usar no lugar.')
        input(f'{nome}: Ele está atraindo os funcionários para me pegarem no armazém.')
        input('--> Um guarda se aproxima, e você tem que voltar de onde veio.')

    input('--> Logo Sigurd aparece com uma corda dizendo:')
    input('Sigurd: Vamos lá, suba logo!')
    input('--> Você sobe para o andar de cima.')
    input('--> Caminham um pouco desviando dos guardas até chegarem a frente da sala do barão.')
    input('--> Entra e diz:')
    input(f'{nome}: Você vai pagar por ter mandado matar tantos animais inocentes.')
    input('Barão: Não sabia que tinha um protetor dos animais. Sigurd, o que está esperando, prenda-o.')

    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input('--> Rapidamente Sigurd começa a te prender.\n'
                        '[1] Luta contra Sigurd.\n'
                        '[2] Deixa ele te prender.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('--> Você se vira e dá um soco em Sigurd.')
        if atirou:
            input('--> Ele defende e contra ataca lhe chutando.')
            input('--> Você se afasta e o joga uma bandeja cheia de pratos')
            input('--> Ouvindo a luta, vários guardas chegaram na sala.')
            input('--> Você dispara uma flecha no chão que faz uma fumaça e pula da janela direto para o solo.')
            input('Barão: deixe-o ir embora.')
            input(f'{nome}: Nossa! Quem mandou eu confiar nele.')
            input(f'{nome}: Embora, eu quase o matei, agora recebi o troco.')
            input('--> Você volta para o centro da cidade.')
            input('--> Você volta para o centro da cidade.')
            return
        else:
            input('--> Ele defende e pisca para você.')
            input('--> Você deixa ele acertar um soco sem força em seu rosto e ele te prende.')
    elif escolha == 2:
        input('--> Você confia nele e o deixa te prender.')

    input('--> Quando o barão se distrai, Sigurd o golpeia com um chute no rosto, e em seguida, você acompanha.')
    input('--> Juntos conseguem o imobilizar.')
    input('Sigurd: Vou colocá-lo na prisão!')
    input('--> Sigurd se torna o novo chefe da mansão.')
    input('Sigurd: De agora em diante, não serão toleradas carnificinas desnecessárias contra os animais!')
    input(f'{nome}: Fico feliz em ouvir isso! É muito bom ver que você está no comando agora.')
    input('--> Você volta para o centro da cidade.')
    quest3 = True


def mago_quest1():
    global nome
    global quest1
    aulasFeitas = 0
    aulaDefesa = False
    aulaHistoria = False
    aulaPocoes = False

    input('--> Você caminha um pouco e então chega na frente da escola de magia e bruxaria de Roguearts.')

    escolha = 0
    while aulasFeitas < 3:
        while escolha < 1 or escolha > 3:
            escolha = input('--> Você entra na escola e se depara com três portas:\n'
                            '[1] Sala de defesa pessoal\n'
                            '[2] Sala de história\n'
                            '[3] Sala de poções\n')
            if type(escolha) == str and escolha == '':
                escolha = -1
            else:
                escolha = int(escolha)

        if escolha == 1:
            aulasFeitas = aulasFeitas + salaDefesaPessoal(aulaDefesa)
            aulaDefesa = True
        elif escolha == 2:
            aulasFeitas = aulasFeitas + salaHistoria(aulaHistoria)
            aulaHistoria = True
        elif escolha == 3:
            aulasFeitas = aulasFeitas + salaPocoes(aulaPocoes)
            aulaPocoes = True
        escolha = 0
    input('--> Percebendo que já havia feito todas as aulas daquele dia, você decide ir embora para a cidade.\n')
    quest1 = True


def salaDefesaPessoal(jaFez):
    if jaFez:
        input('--> Você já fez essa aula.')
        input('--> Percebendo que não teria muito o que fazer naquela sala, você volta para o corredor.\n')
        return 0

    input('--> Entra na sala de defesa pessoal')
    input('--> Vê os estudantes em fila, e você entra no final.')
    input(
        '--> O professor diz que dentro do baú, está o metamorfobia, um monstro que pode se transformar em seu maior medo.')
    input('--> Ele diz que a forma de derrotá-lo é pensar em algo engraçado e jogá-lo o feitiço Hilarius.')

    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input('--> Seu maior medo são dragões.\n'
                        '[1] Imagine um dragão filhote\n'
                        '[2] Imagine um dragão cuspindo bolas de sabão\n'
                        '[3] Tente imaginar um dragão engraçado\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('--> O mostro se transforma em um dragão filhote, que pousa na sua mão.')
        input('--> Todos dizem que ele é fofo. Logo depois ele morde o seu dedo.')
    elif escolha == 2:
        input('--> O mostro se transforma em um dragão, e agora ele esta cuspindo bolhas de sabão')
        input('--> Todos se divertem estourando as bolhas de sabão.')
    elif escolha == 3:
        input('--> Você falha ao tentar imaginar um dragão que seja engraçado.')
        input('--> O monstro se transforma em um dragão real e muito ameaçador.')
        input('--> O professor percebendo o perigo, consegue trancá-lo novamente no baú.')

    input('--> O professor diz:')
    input('Professor: Tudo bem, quem é o próximo?')
    input('--> Você volta para o fim da fila.')
    input('--> O primeiro aluno da fila, faz o mostro se transformar em um vampiro')

    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input('--> Você:\n'
                        '[1] Conjura dentes de alho e joga no vampiro\n'
                        '[2] Conjura sal e arremessa nele\n'
                        '[3] Mira luz e a aponta no vampiro\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('--> O vampiro desvia do alho.')
        input('--> O professor faz o mostro se transformar em um sapo e coloca-o no baú.')
    elif escolha == 2:
        input('--> Nada acontece com o vampiro.')
        input('--> Os alunos dizem que o sal ajuda contra espíritos, não contra vampiros.')
        input('--> O professor faz o mostro se transformar em um sapo e coloca-o no baú.')
    elif escolha == 3:
        input('--> Você acerta uma forte luz nele.')
        input('--> O vampiro começa a brilhar e todos riem.')
        input('--> O mostro volta para o baú.')
        input('--> Todos te aplaudem pela boa ideia.')
    input('--> Vendo que não terá mais nada para fazer nesta sala, volta ao corredor.\n')
    return 1


def salaHistoria(jaFez):
    if jaFez:
        input('--> Você já fez essa aula.')
        input('--> Percebendo que não teria muito o que fazer naquela sala, você volta para o corredor.\n')
        return 0

    global nome
    escolha = 0

    input('--> Percebe que a professora está contando uma história para os alunos.')
    input('--> Se senta rapidamente para não perceberem que chegou atrasado.')
    input('Professora: Os três irmãos precisavam atravessar o rio para chegarem ao outro lado.')
    input('Professora: se fossem vocês, o que fariam para atravessarem o rio.')
    while escolha < 1 or escolha > 3:
        escolha = input('--> Você decide responder:\n'
                        '[1] Nadaria para chegar ao outro lado.\n'
                        '[2] Faria uma ponte.\n'
                        '[3] Me levitaria até o outro lado.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(
            'Professora: Você não escutou que o rio poderia ter vários seres das trevas? Provavelmente morreria nadando.')
        input('Professora: Na história, os irmãos fazem uma ponte para atravessarem o rio.')
    elif escolha == 2:
        input('Professora: Muito bem, é exatamente o que eles fazem e conseguem enganar a morte.')
        input('Professora: já ouviu essa história?')
        input(f'{nome}: Acho que sim...')
    elif escolha == 3:
        input('Professora: é uma ideia interessante, mas seria muito arriscado, '
              'pois qualquer segundo de desconcentração, você poderia cair.')
        input('Professora: Na história, os irmãos fazem uma ponte para atravessarem o rio.')

    input('--> Percebendo que não teria muito o que fazer naquela sala, você volta para o corredor.\n')
    return 1


def salaPocoes(jaFez):
    if jaFez:
        input('--> Você já fez essa aula.')
        input('--> Percebendo que não teria muito o que fazer naquela sala, você volta para o corredor.')
        return 0

    global nome
    escolha = 0

    input('--> Você entra na sala de poções e senta em um lugar vazio.')
    input('Professor: em cada mesa, tem três ingredientes para preparar a poção, mas apenas dois serão usados.')

    ingredientesNaMesa = ['Chifre de unicórnio', 'Asa de morcego', 'Sangue de dragão']

    while escolha < 1 or escolha > 3:
        escolha = input('Você coloca primeiro:\n'
                        '[1] Chifre de unicórnio\n'
                        '[2] Asa de morcego\n'
                        '[3] Sangue de dragão\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    removido = ingredientesNaMesa[escolha - 1]
    ingredientesNaMesa.remove(removido)
    print('--> Voce adiciona ', removido, ' na poção.')
    input()

    escolha = 0
    while escolha < 1 or escolha > 2:
        opcoes = 1
        print('Você coloca depois:')
        if 'Chifre de unicórnio' in ingredientesNaMesa:
            print('[', opcoes, '] Chifre de unicórnio')
            opcoes = opcoes + 1
        if 'Asa de morcego' in ingredientesNaMesa:
            print('[', opcoes, '] Asa de morcego')
            opcoes = opcoes + 1
        if 'Sangue de dragão' in ingredientesNaMesa:
            print('[', opcoes, '] Sangue de dragão')
            opcoes = opcoes + 1

        escolha = input()
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    removido = ingredientesNaMesa[escolha - 1]
    ingredientesNaMesa.remove(removido)
    print('Você adiciona ', removido, 'na poção')
    input()

    if not ('Chifre de unicórnio' in ingredientesNaMesa):  # Se não tiver o chifre
        input('--> O professor toma a poção feita por você e se transforma em um sapo.')
    elif not ('Asa de morcego' in ingredientesNaMesa):  # Se não tiver a asa de morcego
        input('--> O professor toma a poção feita por você e fica com a boca quente')
    elif not ('Sangue de dragão' in ingredientesNaMesa):  # Se não tiver o sangue de dragão
        input('--> O professor toma a poção feita por você e fica com o corpo todo inchado')

    input('--> O professor muito bravo, pede para você se retirar.')
    input('--> Volta ao corredor.\n')
    return 1


def mago_quest2():
    global nome
    global quest2

    input('--> Andando pelo deserto, você encontra um pequeno vilarejo.')
    input('--> Ao entrar, percebe que todos estão comemorando.')
    input(f'{nome}: O que estão comemorando?')
    input('Morador: Esta é a festa de abertura do desafio da pirâmide!')
    input(
        'Morador: nesse desafio, os participantes devem entrar em uma pirâmide, passar por desafios, e depois voltar.')
    input(f'{nome}: Gostaria de participar deste desafio, como começo?')
    input('Morador: Tome isto.')
    input('--> O morador lhe enrega um papel e lhe explica onde fica a pirâmide do desafio.')
    input('--> Após caminhar um pouco, você chega à pirâmide. Vários participantes estão procurando a entrada.')

    escolha = 0
    while escolha != 3:
        print('--> Você lê o papel que lhe entregaram. Nele está escrito: \n"O topo é onde os líderes ficam, '
              'de lá é possível controlar quem entra e quem sai."')
        escolha = input('[1] Procura uma entrada.\n'
                        '[2] Escala a pirâmide.\n'
                        '[3] Atira uma pedra no topo.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

        if escolha == 1:
            input('--> Você fica procurando a entrada como todo mundo.')
            input('--> Após um tempo, percebendo que não vai adiantar procurar deste jeito, você desiste.')
        elif escolha == 2:
            input('--> Tenta escalar a pirâmide.')
            input('--> Após alguns metros de escalada, fica muito cansativo e difícil de escalar, então você desiste.')

    input('--> Você acerta um botão bem escondido no topo da pirâmide e uma passagem secreta se abre.')
    input(f'{nome}: Consegui entrar, nem foi tão difícil. Isso vai ser bem fácil.')
    input('--> Você está em uma câmara com três passagens e outra que está mais em cima, inalcançável do solo.')
    input(f'{nome}: De acordo com o que está escrito no papel, acho que preciso chegar ao topo.')

    canoaSolta = False
    inundado = False
    temMachado = False
    while (not canoaSolta) or (not inundado):
        escolha = 0
        while escolha < 1 or escolha > 3:
            escolha = input('--> Você segue por qual passagem: \n'
                            '[1] A primeira passagem.\n'
                            '[2] A segunda passagem.\n'
                            '[3] A terceira passagem.\n')
            if type(escolha) == str and escolha == '':
                escolha = -1
            else:
                escolha = int(escolha)

        if escolha == 1:
            canoaSolta = camara1(canoaSolta, inundado, temMachado)
        elif escolha == 2:
            inundado = camara2(inundado)
        elif escolha == 3:
            temMachado = camara3(inundado, temMachado)

    input('--> Você nada até a canoa, e sobe nela')
    input('--> Navega até a entrada que antes era inacessível e entra.')
    input('--> Você sobe por uma escadaria bem grande até o topo da pirâmide.')
    input('--> Quando chega ao topo, um som bem alto proclama que você é o vencedor do desafio da pirâmide.')
    input('--> O teto se abre e todos no solo gritam seu nome.')
    input(f'Participantes: {nome}, {nome}, {nome}, {nome}!')
    input('--> Depois da comemoração, você volta para o centro da cidade.')
    quest2 = True


def camara1(canoaSolta, inundado, temMachado):
    if inundado:
        input('--> Você não pode fazer nada, pois está tudo alagado.')
        return canoaSolta

    global nome

    input('--> Está na primeira câmara.')

    escolha = 0
    opcoes = 3
    if temMachado:
        opcoes = 4
    while escolha != 1:
        escolha = 0
        while escolha < 1 or escolha > opcoes:
            print('--> A primeira câmara tem uma canoa presa por tábuas.\n'
                  '[1] Volta à câmara principal.\n'
                  '[2] Tenta soltar a canoa.\n'
                  '[3] Queima as tábuas que prendem a canoa.')
            if temMachado:
                escolha = input('[4] Corta as tábuas com o machado.\n')
                if type(escolha) == str and escolha == '':  # verificar
                    escolha = -1
                else:
                    escolha = int(escolha)
            else:
                escolha = input()
                if type(escolha) == str and escolha == '':  # verificar
                    escolha = -1
                else:
                    escolha = int(escolha)

        if escolha == 1:
            input('--> Resolve retornar para a câmara principal.')
        elif escolha == 2:
            input('--> Você tenta soltar a canoa, mas ela está muito bem presa pelas tábuas.')
        elif escolha == 3:
            input('--> você percebe que se queimar as tábuas, provavelmente queimará também a canoa.')
            input(f'{nome}: Eu posso precisar dessa canoa.')
        elif escolha == 4:
            input('--> Você consegue cortar as tábuas e deixar a canoa intacta e livre.')
            return True

    return canoaSolta


def camara2(inundado):
    input('--> Está na segunda câmara.')

    escolha = 0
    while escolha != 1:
        escolha = 0
        while escolha < 1 or escolha > 2:
            escolha = input('Esta câmara tem um sistema de bombeamento de água e uma alavanca\n'
                            '[1] Volta à câmara principal.\n'
                            '[2] Usa a alavanca.\n')
            if type(escolha) == str and escolha == '':
                escolha = -1
            else:
                escolha = int(escolha)

        if escolha == 1:
            input('--> Resolve retornar para a câmara principal.')
            return inundado
        elif escolha == 2:
            if inundado:
                input('--> Com bastante esforço, por causa do local estar alagado, você consegue usar a alavanca.')
                input('--> A água para de ser bombeadas para as câmaras.')
                input('--> Abrem-se ralos no chão.')
                input('--> Depois de pouco tempo, todas as câmaras estão secas novamente.')
                inundado = False  # not inundado
            else:
                input('--> A água começa a ser bombeada para a câmara.')
                input(
                    '--> A água inunda todas as câmaras em três metros de altura, mas ainda tem algum espaço para você respirar.')
                inundado = True

    return inundado


def camara3(inundado, temMachado):
    if temMachado:
        input('--> Não tem mais nada para fazer aqui.')
        input('--> Você retorna para a câmara principal.')
        return temMachado

    if inundado:
        input('--> Você não pode fazer nada, pois está tudo alagado.')
        return temMachado

    input('--> Está na terceira câmara.')
    input('--> Essa câmara tem quatro alavancas e uma placa que diz:\n'
          '"Com apenas dois símbolos, posso representar o número 10."')

    d1 = 'baixo'  # 0
    d2 = 'baixo'  # 0
    d3 = 'baixo'  # 0
    d4 = 'cima'  # 1
    escolha = 0
    while escolha != 5:
        escolha = 0
        while escolha < 1 or escolha > 5:
            print('--> A posição das alavancas é:')
            print('1 - Para ', d1)
            print('2 - Para ', d2)
            print('3 - Para ', d3)
            print('4 - Para ', d4)

            escolha = input('\n[1] Usar a primeira alavanca.\n'
                            '[2] Usar a segunda alavanca.\n'
                            '[3] Usar a terceira alavanca.\n'
                            '[4] Usar a quarta alavanca.\n'
                            '[5] Volta à câmara principal.\n')
            if type(escolha) == str and escolha == '':
                escolha = -1
            else:
                escolha = int(escolha)

        if escolha == 1:
            if d1 == 'baixo':
                d1 = 'cima'
            else:
                d1 = 'baixo'
            input('--> Você altera a posição da primeira alavanca.')
        elif escolha == 2:
            if d2 == 'baixo':
                d2 = 'cima'
            else:
                d2 = 'baixo'
            input('--> Você altera a posição da segunda alavanca.')
        elif escolha == 3:
            if d3 == 'baixo':
                d3 = 'cima'
            else:
                d3 = 'baixo'
            input('--> Você altera a posição da terceira alavanca.')
        elif escolha == 4:
            if d4 == 'baixo':
                d4 = 'cima'
            else:
                d4 = 'baixo'
            input('--> Você altera a posição da quarta alavanca.')
        elif escolha == 5:
            input('--> Resolve retornar para a câmara principal.')
            input('--> Assim que você sai da câmara, as alavancas voltam as suas posições predefinidas para o desafio.')
            return temMachado

        if (d1 == 'cima') and (d2 == 'baixo') and (d3 == 'cima') and (d4 == 'baixo'):
            input('--> Você sente um pequeno tremor.')
            input('--> Um machado cai do teto da câmara.')
            input('--> Você pega o machado e sai da câmara.')
            return True


def verificaVitoria(agua, fogo, planta):
    if (agua >= 3) or (fogo >= 3) or (planta >= 3):
        return True
    else:
        return (agua > 0) and (fogo > 0) and (planta > 0)


def jogo(nomeOponente):
    global nome
    jogAgua = 0
    jogPlanta = 0
    jogFogo = 0
    iniAgua = 0
    iniPlanta = 0
    iniFogo = 0

    pontosRodada = 1

    while not (verificaVitoria(jogAgua, jogFogo, jogPlanta)) and not (verificaVitoria(iniAgua, iniFogo, iniPlanta)):
        print('|---------------------------------------|')
        print(f'| {nome[0:5]}:\tplanta: {jogPlanta}\tfogo: {jogFogo}\tágua: {jogAgua} |')
        print(f'| {nomeOponente[0:5]}:\tplanta: {iniPlanta}\tfogo: {iniFogo}\tágua: {iniAgua} |')
        print('|---------------------------------------|')

        escolha = 0
        while escolha < 1 or escolha > 3:
            escolha = input('Você escolhe:\n'
                            '[1] planta\n'
                            '[2] fogo\n'
                            '[3] água\n')

            if type(escolha) == str and escolha == '':
                escolha = -1
            else:
                escolha = int(escolha)

        item_jogador = ''
        if escolha == 1:
            item_jogador = 'planta'
        else:
            if escolha == 2:
                item_jogador = 'fogo'
            else:
                if escolha == 3:
                    item_jogador = 'água'

        escolha_Pc = randint(1, 3)
        if escolha_Pc == 1:
            item_pc = 'planta'
        else:
            if escolha_Pc == 2:
                item_pc = 'fogo'
            else:
                item_pc = 'água'

        print(f'{nome} escolheu: {item_jogador}')
        print(f'{nomeOponente} escolheu: {item_pc}')

        # Verificando empates
        if item_jogador == item_pc:
            pontosRodada = pontosRodada + 1
            input(f'--> Empate! Ninguém somou ponto! A próxima rodada vale {pontosRodada} pontos.\n')

        # Verificando o jogador
        if (item_jogador == 'água') and (item_pc == 'fogo'):
            jogAgua = jogAgua + pontosRodada
            pontosRodada = 1
            input('--> Você venceu usando água!\n')

        if (item_jogador == 'fogo') and (item_pc == 'planta'):
            jogFogo = jogFogo + pontosRodada
            pontosRodada = 1
            input('--> Você venceu usando fogo!\n')

        if (item_jogador == 'planta') and (item_pc == 'água'):
            jogPlanta = jogPlanta + pontosRodada
            pontosRodada = 1
            input('--> Você venceu usando planta!\n')

        # Verificando o NPC
        if (item_pc == 'água') and (item_jogador == 'fogo'):
            iniAgua = iniAgua + pontosRodada
            pontosRodada = 1
            input(f'--> {nomeOponente} venceu usando água!')

        if (item_pc == 'fogo') and (item_jogador == 'planta'):
            iniFogo = iniFogo + pontosRodada
            pontosRodada = 1
            input(f'--> {nomeOponente} venceu usando fogo!')

        if (item_pc == 'planta') and (item_jogador == 'água'):
            iniPlanta = iniPlanta + pontosRodada
            pontosRodada = 1
            input(f'--> {nomeOponente} venceu usando planta!')

    if verificaVitoria(jogAgua, jogFogo, jogPlanta):
        input(f'--> {nome} venceu! Muito bem!')
        return True
    else:
        input(f'--> {nomeOponente} venceu! Muito bem!')
        return False


def mago_quest3():
    global nome
    global quest3
    competidores = ['Merlin', 'Aleneus', 'Zadel', 'Azahr', 'Erius', 'Eneel', 'Babidi', 'Lopianne', 'Strange',
                    'Oliver', 'Salazar', 'Egorin', 'Ronaldinho', 'Albus', 'Uranai']
    jogosGanhos = 0
    jogosPerdidos = 0

    input('--> Caminha em direção às montanhas.')
    input('--> Lá encontra um acampamento.')
    input('Funcionário do acampamento: Bem vindo aventureiro!')
    input(f'{nome}: Que lugar é esse?')
    input('Funcionário: Este é o 12° acampamento de magos do leste!')
    input('Funcionário: vejo que você também é um mago, já se inscreveu para participar do troneio de\n'
          '\tFoplanau?')
    input(f'{nome}: Não, onde me inscrevo?')
    input('Funcionário: É por alí.')
    input('--> Você se inscreve para o torneiro de Foplanau e espera a abertura.')
    input('Narrador: Senhoras e senhores, bem vindos ao 12° acampamento de magos do leste!')
    input('Narrador: Muito bem, agora vamos as regras.')
    input('Narrador: Cada jogo é disputado por dois competidores.')
    input('Narrador: A cada rodada, cada participante deve escolher um dos três elementos:')
    input('Narrador: Planta: representante da natureza. Forte contra a água, mas fraca contra o fogo.')
    input('Narrador: Fogo: representante da destruição. Forte contra a planta, mas fraca contra a água.')
    input('Narrador: Água: representante da manutenção da vida. Forte contra o fogo, mas fraca contra a planta.')
    input('Narrador: Se houver um empate, os pontos dessa rodada acumulam para a próxima.')
    input('Narrador: o primeiro competidor a conseguir três vitórias com o mesmo elemento ou \n'
          '\tpelo menos um com cada um dos três elementos, ganha o jogo')
    input('Narrador: Esse ano temos dezesseis competidores.')
    input('Narrador: O competidor que ganhar três jogos com menos de três derrotas é o vencedor!')

    while (jogosGanhos < 3) and (jogosPerdidos < 3):
        oponente = competidores[randint(0, len(competidores) - 1)]
        competidores.remove(oponente)
        input(f'Narrador: O próximo jogo será ente: {nome} X {oponente}')
        if jogo(oponente):
            jogosGanhos = jogosGanhos + 1
        else:
            jogosPerdidos = jogosPerdidos + 1

    if jogosGanhos >= 3:
        input(f'Narrador: Senhoras e senhores, o mais novo campeão de Foplanau é {nome}!')
        input('narrador: aplaudam o campeão!')
        input('--> Todos te aplaudem.')
    else:
        input('Narrador: Não fique triste meu caro, a vida é cheia de vitórias e derrotas!')

    input('--> Após o torneio, você volta ao centro da cidade.')
    quest3 = True


def quest_final():
    global nome

    input('--> No centro da cidade, você vê um pelotão de soldados de seu reino.')
    input('--> Eles estavam correndo rumo à montanha Tallhill do reino de Hedeby.')
    input('--> Um guarda vem em sua direção.')
    input(
        f'Guarda: {nome}, você foi uma peça fundamental na nossa última guerra, e estamos precisando da sua ajuda novamente.')
    input(
        'Guarda: com a rendição do reino de Hedeby, eles passaram por uma fase de grande vexame, então decidiram usar tudo\n'
        '\to que tem para um último confronto contra nós.')
    input('Guarda: venha nos ajudar, siga o pelotão, para receber mais informações do comandante.')
    input('--> Você segue o pelotão e o comandante diz:')
    input(
        'Comandante: Homens, os hedebyrianos estão montando uma última investida. E eles vão acionar seu ataque ancestral.')
    input(
        'Comandante: Se trata de um dragão ancião que permanece selado na montanha Tallhill, e eles pretendem o libertar.')
    input('Comandante: alguma dúvida?')
    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input(f'--> Você: \n'
                        f'[1] Pergunta o quanto esse dragão é perigoso.\n'
                        f'[2] Pergunta como esse dragão foi selado.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'{nome}: Mas esse dragão é uma ameaça tão grande ao nosso reino?')
        input(f'{nome}: Pergunto isso, pois o exército heberyano está enfraquecido, esse dragão conseguirá cobrir a\n'
              f'\tdiferença entre nossos exércitos?')
        input('Comandante: Acreditamos que sim, porque no passado ele já nos causou problemas.')
        input('Comandante: Ele já atacou nosso reino uma vez, mas conseguimos expulsá-lo.')
    elif escolha == 2:
        input(
            f'{nome}: Percebi que este dragão parece ser uma ameaça considerável, então como ele foi selado no passado?')
        input('Comandante: Realmente seu poder não pode ser subestimada.')
        input(
            'Comandante: Na época em que ele foi selado, passávamos por uma crise, e nosso exército estava muito fraco.')
        input('Comandante: Então decidimos apenas selá-lo.')

    input('Comandante: Só conseguimos detê-lo usando a técnica suprema para selar inimigos, o mafuuba.')
    input('Comandante: sem mais perguntas, vamos até a montanha impedi-los.')
    input('--> Chegando em Tallhill, vocês avistam o pouco do exército de Hedeby que restou.')
    input(
        '--> Eles estão entrando em uma construção antiga, no interior da montanha, para quebrarem o selo que aprisiona o dragão.')
    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'--> Então você:\n'
                        f'[1] Tenta convencer a invadir logo, pois a qualquer momento, o dragão pode ser liberto.\n'
                        f'[2] Pergunta ao comandante como prosseguir.\n'
                        f'[3] Tenta convencer o seu exército a prendê-los no interior da montanha. \n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'{nome}: Vamos rápido, eles podem libertar aquele monstro a qualquer momento!')
        input(f'Comandante: Não podemos agir por impulso, devemos esperar reforços.')
        input(f'{nome}: Não posso ficar aqui parado enquanto um dragão pode ser libertado.')
        input(f'--> Você entra sozinho na montanha.')
        input('--> Depois de caminhar um pouco, cai em uma armadilha deixada pelos hedebyrianos.')
        input('--> Você grita para pedir ajuda, mas seu exército está muito longe para escutar.')
        input('--> No entanto, os hedebyrianos o escutam e se apressam para o ritual de libertação.')
        input(
            '--> Logo o seu exército aparece com os reforços, contendo agora caçadores para desarmar as armadilhas e te socorrem.')
        input('--> Ao terminar de te soltar, vocês escutam o dragão sendo liberto.')
        input('--> Então se afastam da entrada, pois provavelmente ele sairá por ali.')
        dragaoLiberto()

    elif escolha == 2:
        input(f'--> O comandante diz que acredita ser melhor esperarmos por reforços.')
        input(
            '--> Algum tempo depois, os reforços chegam, e um deles conta de que há armadilhas na passagem que leva ao interior.')
        input('--> Vocês avançam com cuidado por causa das armadilhas, desarmando-as no caminho.')
        input('--> No interior de Tallhill, encontram os inimigos fazendo um ritual de libertação.')
        input('--> O comandante ordena um ataque, e assim, o ritual é impedido.')
        input('--> Agora que o dragão permanecerá selado, eles terão que lutar somente com os homens que ali estão.')
        dragaoSelado()
    elif escolha == 3:
        input(
            f'--> Você convence o pelotão de que a melhor escolha é prendê-los dentro da montanha deixando-os sem saída.')
        input(
            f'--> O comandante concorda, porque segundo ele, essa é a única saída, e o dragão não conseguirá arrumar um jeito de sair.')
        input(f'--> Então vocês utilizam explosivos para destruir a única passagem para o interior da montanha.')
        input('--> Vocês escutam o despertar do dragão e pensam estar seguros, por ele estar preso dentro da montanha.')
        input('--> Alguns segundos depois, as pedras que bloqueavam a passagem foram explodidas pelo lado de dentro.')
        input(
            '--> O comandante diz que eles deviam estar preparados para caso ficassem presos na caverna, então trouxeram dinamite.')
        dragaoLiberto()
    print('\n', 50 * '-', 'FIM', 50 * '-')


def dragaoLiberto():
    global reino
    global nome
    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input(f'--> O dragão sai da caverna e vocês decidem:\n'
                        f'[1] Lutar para por um fim ao dragão.\n'
                        f'[2] Luta para enfraquecê-lo e selá-lo novamente.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('--> Vocês se organizam para formar um ataque que não dê chances de vitória ao dragão.')
        input(
            '--> Esse ataque consiste em avançar em três frentes, uma liderada pelo comandante, outra por você e a última por Merlin.')
        input('--> O pelotão de Merlin focará no dragão, imobilizando-o.')
        input('--> Enquanto ele está imobilizado, o pelotão do comandante irá derrubá-lo e prendê-lo no chão.')
        input('--> Durante isso, a sua frente eliminará todo o exército de Hedeby.')
        sorte = randint(1, 10)
        if sorte <= 5:  # 50% de chance (final bom)
            input('--> O dragão é preso ao chão, sem chances de escapar, e todos os outros inimigos são mortos.')
            input('--> Vocês atacam o dragão que enfim falece, sendo decretado um fim definitivo a esa guerra.')
            input('--> Seu exército volta para a cidade comemorando o fim da guerra, e do dragão.')
            input(
                f'--> Vocês são considerados heróis de Vaeryn, pois agora as próximas gerações não precisarão se preocupar como retorno deste monstro.')
        elif sorte <= 8:  # 30% de chance (final médio)
            input(
                '--> Merlin e seus homens infelizmente não conseguem segurar o dragão para que o pelotão do comandante derrubasse o dragão.')
            input('--> Mesmo seus homens aniquilando o enfraquecido exército dos hedebyrianos.')
            input('--> Com essa falha no plano, o dragão consegue escapar voando para longe.')
            input('--> Seu exército volta para a cidade e avisa todos do reino que Hedeby não é mais um problema.')
            input(
                f'--> Porém o dragão está a solta e poderá retornar à Vaeryn a qualquer momento, cedo ou tarde, todos devem estar preparados.')
        else:  # 20% de chance (final ruim)
            input(
                '--> Merlin e seus homens infelizmente não conseguem segurar o dragão para que o pelotão do comandante derrubasse o dragão.')
            input(
                '--> Além disso, houve outro problema, pois você e sua tropa encontram muita resistência dos hedebyrianos.')
            input(
                '--> Com o plano sendo totalmente falho, e o dragão tendo apoio da tropa de seus salvadores, ele derrota todo o seu exército.')
            input(f'--> É decretado um fim à guerra, o reino de Hedeby vence e assola completamente o reino de Vaeryn.')
            input('--> E agora, fortalecidos, partem para derrotar outros reinos.')
    elif escolha == 2:
        input(
            f'--> Seu exército se divide em dois, a sua tropa ficou encarregada de derrotar o restante dos hedebyrianos.')
        input('--> Ao mesmo tempo, o pelotão do comandante segurava o dragão.')
        input('--> Merlin começou a fazer as preliminares para realizar o mafuuba, concentrando-se no dragão.')
        input(
            '--> Passado algum tempo, sua tropa extermina os inimigos, e ajudam a tropa do comandante a enfraquecer o dragão.')
        input('--> Merlin enfim, termina o mafuuba, e pede que os outros se distanciem do dragão.')
        input('Merlin: um, dois, três... Mafuuba!')
        input('--> O dragão é selado em Tallhill.')
        input('--> Todos retornam à cidade e contam as boas novas para a população.')
        input('--> Agora seu reino precisará impedir que qualquer inimigo cheguem à Tallhill, e libertem o dragão.')
        input('--> Mantendo assim seu reino em paz.')


def dragaoSelado():
    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input(f'--> Então vocês:\n'
                        f'[1] Decidem poupá-los.\n'
                        f'[2] Decidem matá-los.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'--> Vocês decidem poupá-los pois eles estão em menor número, já enfraquecidos e com o plano arruinado.')
        input(f'--> Porém com as condições:')
        input(f'--> I - Que os hedebyrianos aceitem a derrota na guerra;')
        input(f'--> II - Não ataquem o reino de Vaeryn;')
        input(f'--> III - Não tentem libertar o dragão novamente.')
        input('--> Eles concordam e agradecem pela compaixão.')
        input('--> Cada exército volta a seu reino.')
        input('--> Tempos depois, graças a misericórdia sua e dos soldados, os dois reinos fizeram uma aliança.')
        input(
            '--> Esta aliança ajudou ambos os reinos a prosperar, se ajudando no comércio, na proteção do território e na formação de um grande exército para guerras.')
    elif escolha == 2:
        input(
            f'--> Vocês decidem acabar com o mal pela raiz, pois assim como já se rebelaram de uma rendição, podem fazer de novo.')
        input('--> Além de que são uma ameaça, pois podem liberar o dragão quando bem entenderem caso fiquem vivos.')
        input('--> Você e o exército partem com fúria para cima dos inimigos, massacrando-os.')
        input('--> Todos Voltam para a cidade e comemoram a vitória sobre o reino de Hedeby.')
        input(
            '--> Mas avisam que todos precisam ficar vigilantes pois o dragão ainda está selado podendo ser liberto por inimigos no futuro.')


# ---------------------------------------------------------------------------------------------------------------------
print('\n', 50 * '-', 'Kingdom of Vaeryn - The Game', 50 * '-', '\n')
input('O jogo consiste em escolher números para realizar escolhas, use ENTER para prosseguir em cada fala.\n')

# Criação do personagem
alistamento()

# Início do jogo
guerra()

# Divisão das quests
mapa_classes()

# Final do jogo
quest_final()
