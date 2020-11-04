import random

reino = 'Vaeryn'
nome = ''
classe = ''
equipamento = ''

quest1 = False
quest2 = False
quest3 = False

#Prólogo
def prologo():
    global nome
    global reino
    global classe
    global equipamento
    escolha = 0

    print('\n', 50 * '-', 'Kingdom of Vaeryn the game', 50 * '-','\n')
    input('O jogo consiste em escolher números para realizar escolhas, use ENTER para prosseguir em cada fala.\n')

    input(f'--> O Reino de {reino} irá participar de uma guerra, estão recrutando guerreiros, '
          f'arqueiros e magos de todo o reino para servir na guerra.')
    while nome == '':
        nome = input('Guarda: Obrigado por vir se alistar, qual o seu nome? ')

    while escolha < 1 or escolha > 3:
        escolha = input(f'Guarda: {nome} você é um: '
                       '\n[1] Guerreiro,'
                       '\n[2] Arqueiro '
                       '\n[3] Mago \n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

        if escolha == 1:
            classe = 'Guerreiro'
            equipamento = 'espada'
        elif escolha == 2:
            classe = 'Arqueiro'
            equipamento = 'arco e flecha'
        elif escolha == 3:
            classe = 'Mago'
            equipamento = 'bola de fogo'

    escolha=0
    input(f'--> Chega o dia do confronto, o Reino de {reino} contra o Reino Hedeby. ')
    input(f'--> Dois fortes exércitos travam um embate em um vasto campo aberto, você se aproxima do exército Vaeryano.')
    while escolha < 1 or escolha > 3:
        escolha = input(f'Soldado: {nome} já trouxe sua arma? \n'
                            f'[1] Sim, eu estou sempre pronto para a batalha.\n'
                            f'[2] Não, dê-me uma.\n'
                            f'[3] Sou um {classe} de elite, com minha {equipamento} enfrento tudo e todos.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'Soldado: Ótimo, como esperado de um {classe} como você.')
    elif escolha == 2:
        input(f'Soldado: Tome, que com ela você consiga acabar com o exército inimigo.')
    elif escolha == 3:
        input(f'Soldado: Como sempre um orgulhoso e destemido {classe}.')

    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'O combate tem início e se aproxima da sua posição um pelotão de três inimigos, você:\n'
                            f'[1] Luta solo.\n'
                            f'[2] Corre para reagrupar.\n'
                            f'[3] Se mistura por entre os guerreiros e ataca o pelotão\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'--> Você avança para cima dos inimigos com a {equipamento} derrotando todo o pelotão fácilmente.')
    elif escolha == 2:
        input(f'--> Você recua para próximo de seus aliados e juntos acabam com o pelotão inimigo.')
    elif escolha == 3:
        input(f'--> Você se camufla por entre os inimigos e ataca todos os três a {equipamento}.')

    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'--> Os seus aliados estão levando vantagem sobre o exército oponente,'
                            f'porém você avista o mago Merlin em apuros e vai ajudá-lo:\n'
                            f'[1] Levantando o mago e lutando junto.\n'
                            f'[2] Lutando sozinho para depois ajudar Merlin.\n'
                            f'[3] Pedindo para o mago que se cure com sua magia de cura e o ajudando a levá-lo ao pelotão aliado.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'--> Você ajuda Merlin a se recuperar, e juntos travam um batalha contra os inmigos no alcance, limpando uma boa área de inimigos.')
    elif escolha == 2:
        input(f'--> Você percebe que Merlin está ferido e não pode ajudá-lo no momento. Então derrota os inimigos próximos sozinho \n'
              f'até que consegue ajudar Merlin a se recuperar.')
    elif escolha == 3:
        input(f'--> Você convence o mago para que se cure com magia e juntos tentam recuar para o pelotão aliado, lutando com os inimigos do caminho.')

    input('--> Você e Merlin então em uma tentativa de reagrupar com seu pelotão, encontram um forte inimigo bárbaro.\n ')
    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'--> Então:\n'
                            f'[1] Vocês trabalham em equipe para enfrentar o forte bárbaro.\n'
                            f'[2] Você quer enfrentar o bárbaro em uma luta 1 contra 1 pela honra.\n'
                            f'[3] Você tenta atacar o inimigo desprevinido. \n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'--> Com uma poderosa tática, Merlim usa sua magia Taiokon cegando o bárbaro e você o finaliza com a {equipamento}.')
    elif escolha == 2:
        input(f'--> Você usa todo seu treinamento e habilidades e derrota o bárbaro, \n'
              f'mas fica debilitado pois levou uma machadada poderosa do temível inimigo.')
    elif escolha == 3:
        input(f'--> Você aproveita que o bárbaro não viu vocês, pois está enfrentando dois soldados aliados, \n'
              f'então você o ataca desprevinido sem dar-lhe a mínima chance.')

    escolha = 0
    while escolha < 1 or escolha > 4:
        escolha = input(f'--> Com a derrota do bárbaro que era o mais forte guerreiro inimigo, o exército deles ficou debilitado,\n'
              f'restando somente o líder de exército e vinte soldados, contra o exército aliado que ainda tinha mais de\n'
              f'cem soldados. \nEntão seu exército se aproxima dos inimigos, e você:\n'
                            f'[1] Espera que os líderes do seu exército coloquem um fim na batalha.\n'
                            f'[2] Ameaça-os para que peçam a rendição.\n'
                            f'[3] Vai para matá-los resolvendo tudo. \n'
                            f'[4] Pergunta ao General aliado como prosseguir.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'--> Você espera para que tudo seja resolvido pelos líderes, que rendem os inimigos sendo decretado o fim da guerra.')
    elif escolha == 2:
        input(f'--> Você toma a frente mesmo não sendo um líder ou General, mesmo assim consegue que os inimigos se rendam dando assim um fim a guerra.')
    elif escolha == 3:
        input(f'--> Você no calor do momento avança para cima dos inimigos, mas o General aliado o impede,\n'
              f'pois com a morte de todo o exército inimigo, o povo de Hedeby nunca aceitaria trégua,\n'
              f'então o General rende os inimigos pondo um fim a esta guerra.')
    elif escolha == 4:
        input(f'--> Você pergunta para o General como prosseguir, e ele lhe responde que basta pressionar o exército inimigo,\n'
              f'pois estão enfraquecidos e irão se render. Assim acontece, com a rendição inimiga é colocando um fim a guerra.')

    input(f'--> Você e todo o exército voltam para o Reino de {reino}, sendo recepcionados pelo povo.')

    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'--> Então o General fala:\n'
                            f'Gerenal: Com essa bela vitória de hoje, percebi que nosso reino está bem servido de ótimos soldados,\n'
                            f'{nome} foi o destaque da guerra, com sua determinação e perseverança foi uma peça chave para colocar-nos à frente nessa guerra.\n'
                            f'--> O povo o saudou, e você:\n'
                            f'[1] Agradeçe e conta seus feitos de guerra.\n'
                            f'[2] Fala que não fez mais que sua obrigação.\n'
                            f'[3] Comemora com o povo a vitória da guerra. \n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'--> Você agredeceu a todos e contou-lhes seus feitos e baixas na guerra, com destaque para a luta contra o forte bárbaro.')
        input(f'--> Todos reconheceram seu valor.')
    elif escolha == 2:
        input(f'--> Você mostra sua determinação afirmando que não fez mais que a própria obrigação.')
        input(f'--> Você inspirou muitos a servirem o exército para mostrarem do que são capazes.')
    elif escolha == 3:
        input(f'--> Você vai para o meio da multidão e comemora com o povo a vitória da guerra,\n'
        f'com uma festa no centro da cidade.\n')

    if classe == 'Guerreiro':
        mapaGuerreiro()
    elif classe == 'Arqueiro':
        mapaArqueiro()
    elif classe == 'Mago':
        mapaMago()

def questTavernaGuerreiro():
    global nome
    global classe
    global reino
    global quest1

    input('--> Na taverna do Moe está tudo pacato, pos era um dia normal.')
    input('--> Você se aproxima do balcão, e ele lhe pergunta:')
    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'Moe: Olá {nome}, quer tomar hidromel?\n'
                            f'[1] Claro aqui as três moedas.\n'
                            f'[2] Não.\n'
                            f'[3] Não tenho dinheiro, ajude seu amigo. \n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'Moe: Muito bem rapaz, saindo o melhor hidromel da região.')
        input(f'Moe: Eu ouvi falar de você, o destemido {classe} de {reino}.')
        input(f'{nome}: que isso, estava apenas ajudando o meu reno. O nosso reino!')
        input('Moe: gosto dessa inpolgação, meu rapaz!')
    elif escolha == 2:
        input('MOe: Tudo bem, então veio apenas jogar conversa fora...')
        input(f'Moe: Suas histórias são verdadeiras? O {classe} que derrotou o gigante bárbaro!')
        input('--> Quando você abre sua boca para responder...')
    elif escolha == 3:
        input('Moe: Ah... Entendo... Deixe-me ver... O movimento está fraco mesmo, aqui está!')
        input(f'{nome}: Muito obrigado!')
        input(f'Moe: É apenas um agradecimento por um de nosso mais bravos guerreiros')

    input('--> Entram na taverna a oprtunista e salafrária gangue cascalho.')
    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'--> Eles não percebem quem você é e começam uma discussão com Moe,\n'
                            'mas você espera, pois:\n'
                            f'[1] Espera que eles digam algo importante.\n'
                            f'[2] Mou não gosta de violência desnecessária.\n'
                            f'[3] Percebe que eles estão irritados pois perderam uma briga. \n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('--> Após alguns segundos de discusão, um deles diz:')
        input('--> Capanga da gangue: Entramos em brigas difíceis recentemente, agora estamos sem dinheiro,\n'
            '\tpor isso estamos recorrendo a assaltos e outras vigarices.')
        input('Outro capanga da gangue: É, queremos o seu dinheiro, anda logo!')
    elif escolha == 2:
        input('--> Vendo que eles estavam de cabeça quente, resolveu não entrar na discussão,\n pois Mou não'
                '\tgosta de violênia em sua taverna, embora de vez em quando é impossível não acontecer...')
        input('Capanga da gangue: Estamos com pressa, vai logo e entrega o dinheiro para a gente!')
    elif escolha == 3:
        input('Capanga da gangue: a alguns minutos, brigamos com os vagos e perdemos uma grana agora passa\n'
            '\tO dinheiro pra cá.')

    escolha = 0
    while escolha < 1 or escolha > 4:
        escolha = input('--> Sabendo que eles vão assaltar a taverna de Moe, você decide impedí-los:\n'
                            '[1] Chega atacando todos os cinco.\n'
                            '[2] Se reúne com os demais clientes para ajudar Moe.\n'
                            '[3] Aproveita que não prestaram atenção em você e ataca pelas costas. \n'
                            '[4] Intimída-os.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('--> Você não tem medo de simples gângsters e parte com tudo o que tem para cima deles.')
        print('--> Enfia sua espada com força nas costas do primeiro.')
        print('--> Um deles atira com sua garrucha, mas você se abaixa antes, e o chuta incapacitando-o.')
        input('--> Outro te segura pelas costas te imobilizando, e outro te soca algumas vezes, mas você  \nconsegue se soltar e jogar quem o segurava em cima do outro.')
        input('--> Percebendo que a situação encontrava-se desfavorável, \no último membro da gangue deu um tiro em Moe e fugiu rapidamente da taverna com o dinheiro.')
    elif escolha == 2:
        input('--> Você se reúne comos outros clientes, que também são fortes e partem para cima da gangue.')
        input('--> Gangsters: Acham mesmo que quatro fracotes e um guerreiro irá nos parar?')
        input('--> Você corre arremessando sua espada no crânio de um, e socando o outro num ponto vital, desmaiando-o.')
        input('--> Três dos clientes espancam mais um membro da gangue.')
        input('--> Você corre para nocautear outro que golpeava um cliente, com ele nocauteado só faltou um.')
        input('--> Porém o último percebendo que não acabaria bem a briga, pegou o dinheiro atirou em Moe e fugiu para a sede da gangue.')
    elif escolha == 3:
        input('--> Você se aproxima nas costas, desferindo um corte horizontal acertando três inimigos que estavam perto.')
        input('--> Os dois inimigos restantes ficam surpresos com a emboscada.')
        input('--> Um deles atira em Moe e sai correndo da taverna.')
        input('--> O outro engata um embate com você sendo derrotado rapidamente.')
    elif escolha == 4:
        input('--> Você se aproxima da gangue e mando-os que saiam da taverna antes que tudo acabe pior.')
        input('--> Mas quatro deles partem para a briga com você, te atrasando enquanto um rouba, atira em Moe e foge.')
        input('--> Você espanca os quatro em uma luta corpo a corpo, mas um deles consegue a fuga para a sede da gangue.')

    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input(f'--> Após a fuga de um dos integrantes, você:\n'
                             f'[1] Corre atrás do meliante.\n'
                             f'[2] Socorre Moe que foi baleado.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('--> Corre atrás do meliante, porém ele estava muito a frente.')
        input('--> Para priorar, em um cruzamento precisa esperar até que uma carroça passe, perdendo-o de vista.')
    elif escolha == 2:
        input('--> Vai socorrer Moe que foi baleado, mas quando você se aproxima dele fica sabendo que o tiro passou raspando em seu ombro.')
        input(f'Moe: {nome} eu estou bem, essa gangue nunca tinha sido violenta desse modo, mesmo me roubando as vezes.')
        input('--> Moe: Nunca dispararam contra mim. Agora corra, pegue ele.')
        input('--> Moe: me vingue por favor, para que esse inferno de gangue acabe para sempre.')
        input('--> Você vai atrás do ladrão como um espírito de vingança, mas não sabe onde ele foi, pois ele partiu muito a frente.')

    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'--> Perdido, sem saber onde ele foi, você se aproxima de um aventureiro que estava no cruzamento e diz:\n'
                            f'[1] Aventureiro você viu aonde foi aquele ladrão?.\n'
                            f'[2] Você pode me levar até o escoderijo da guangue cascalho? Lhe darei 10 moedas.\n'
                            f'[3] Me leve até a sede da gangue cascalho, estou com pressa, vamos! \n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('Aventureiro: Vi sim, ele foi pela esquerda subindo o morro.')
        input('Aventureiro: Acho que ja passei perto da sede dessa gangue, fica em cima desse morro.')
        input('--> Você agradece e corre até a sede')
    elif escolha == 2:
        input(f'Aventureiro: Claro, siga-me.')
        input('--> Você segue ele e logo chegam a sede')
    elif escolha == 3:
        input(f'Aventureiro: Vou te ajudar nessa {nome}, vamos.')
        input('Aventureiro: Aconteceu alguma coisa?')
        input('--> Você conta o caso para ele e chegam até a sede.')

    escolha = 0
    print('--> Na sede da gangue há três ladrões, um deles era o que furtou Moe, também estava o líder Evan.')
    while escolha < 1 or escolha > 3:
        print('--> Você estava contra quatro membros da gangue.')
        escolha = input(f'--> Então você:\n'
                            f'[1] Fala a Evan que veio barganhar, para que ele devolva o dinheiro e ninguém se machucará.\n'
                            f'[2] Parte para a briga.\n'
                            f'[3] Corre para chamar reforços. \n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('Evan: Hahahaha. Vem em nossa sede arrumar confusão, mas agora quer barganhar?')
        input('Evan: A unica coisa que vai acontecer aqui é que irá apanhar.')
        input('--> Então eles fecham um círculo em volta de você, mas você os golpeia com um ciclone de espadadas.')
        input('--> Consegue ferir gravemente três capangas.')
        input('--> Evan e o outro sobrevivente desferem facas em seu braço.')
        input('--> Você apara seus golpes e os finaliza com um corte horizontal na garganta de ambos que estavam lado a lado.')
    elif escolha == 2:
        input('--> Você foca os golpes em Evan assassinando-o rapidamente, com a morte do líder, os quatro capangas ficam abalados.')
        input('--> Você aproveita o vacilo de dois deles, os finaliza.')
        input('--> O último tenta com um esforço desesperado em lhe atacar mas você apara o ataque e remove sua cabeça.')
    elif escolha == 3:
        input('--> Você tenta correr para chamar reforços, mas fica cercado pela gangue.')
        input('Evan: Você percebeu que está em desvantagem e quer fugir, não vai a lugar algum.')
        input('--> Você luta com eles aparando golpes e contra atacando, até sobrar somente Evan.')
        input('--> Você o acerta um chute quebrando a defesa dele e o jogando ao chão, finalizando-o rapidamente.')

    input('--> Com toda a gangue derrotada, você leva o dinheiro a Moe e volta ao centro da cidade.')
    quest1 = True

def questFerreiroGuerreiro():
    global nome
    global classe
    global reino
    global quest2

    input('--> Chegando no ferreiro Yudi, você tenta negociar uma espada, porque a sua não é a das melhores.')
    input('Yudi: Estou forjando a mais forte das espadas que já fiz, a qual batizarei de Força!')
    input('Yudi: Gostaria que ela fosse usada por um guerreiro honrado como você, vamos negociar, lhe dou ela em troca de um favor.')
    input('--> Você pergunta qual do que ele precisa.')
    input('Yudi: Este favor não ajudará somente a mim, mas a muitos comerciantes e também a sociedade em geral.')
    input('Yudi: A marinha do reino é corrupta e está roubando minhas espadas e me silenciando, por meio de seu poder.')
    input('Yudi: E isso não ocorre só comigo, fazem isso com diversos comerciantes da costa marítima.')
    input('Yudi: Eles ainda estão negociando com piratas, permitindo que estes roubem lojas.')
    input('Yudi: em troca de uma grande porcentagem do saque por essa "vista grossa".')
    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'--> Diante dessa situação você:\n'
                            f'[1] Negócio fechado, vamos acabar com essa "máfia" e ficarei com a nova espada.\n'
                            f'[2] Essa história está estranha, lutei com pelo reino na guerra.\n'
                            f'[3] Só receberei uma espada por isso? \n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('Yudi: Que bom que aceitou, pode completar o serviço, sua espada estára pronta quando retornar.')
    elif escolha == 2:
        input('Yudi: Mas é exatamente onde você se engana, a marinha não ajudou em nada na guerra,')
        input('Yudi: com a desculpa de que deveriam permanecer para proteger o reino enquanto os soldados estivessem fora,')
        input('Yudi: mas mesmo assim os furtos continuaram. Sem contar que provavelmente essa "máfia" ainda não foi descoberta pelo Rei nem pelos soldados reais,')
        input('Yudi: só lhe contei pois confio que você pode acabar com eles sem causar tumulto e me colocar em perigo, mas quando todos forem mortos,')
        input('Yudi: essa farsa cairá e todos saberão e vão lhe agradecer por ter resolvido tudo.')
        input('--> Para provar seu ponto, Yudi chama comerciantes próximos que confirmam a farsa da marinha.')
        input('--> Você aceita o acordo depois de ser convencido.')
    elif escolha == 3:
        input('Yudi: Não será só uma simples espada, ela possuirá uma resistência incomum e corte afiado.')
        input('Yudi: E o principal, ganhará o reconhecimento de todos quando essa "máfia" acabar e a notícia se espalhar.')
        input('--> Como você precisava de uma espada, você aceita a missão.')


    input('--> Você vai até a marinha, próximo a base há um guarda do reino.')
    input('Guarda do Reino: Hey {nome} o que veio fazer aqui?')
    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input(f'--> Você diz a ele que:\n'
                            f'[1] Veio acabar com a farsa da marinha.\n'
                            f'[2] Veio perguntar se ele vê os almirantes e piratas de papo.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'--> Você conta tudo o que sabe da farsa para ele, e diz que vai acabar com isso, que ele não te impessa .')
        input('Guarda do Reino: Finalmente alguém também sabe dessa máfia e veio por um fim nisso.')
        input('Guarda do Reino: Nunca disse nada pois estava sendo ameaçado e não sou forte como você para derrotar todos eles.')
    elif escolha == 2:
        input(f'--> Ele conta que sim, almirantes e piratas tem um acordo, exatamento como Yudi tinha lhe dito.')

    input('Guarda do Reino: Pode ir resolver isso, agora minha angústia de ser o único que sabe, mas não faz nada poderá acabar.')
    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'--> Você diz a ele:\n'
                            f'[1] Quer ir comigo? Para se vingar desses "mafiosos opressores".\n'
                            f'[2] Estou indo, não deve ser difícil comparado a guerra dos reinos.\n'
                            f'[3] Farei o possível para derrotá-los, deseje-me sorte. \n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'Guarda do Reino: Não tenho mais vigor para isso, estou velho. Eu também era aventureiro como você até que levei uma flechada no joelho.')
        input(f'Guarda do Reino: Pode ir, eu trarei alguns soldados para caso precisa de reforço.')
    elif escolha == 2:
        input(f'Guarda do Reino: Vá e acabe com eles, vou trazer alguns soldados para caso você seja surpreendido por eles.')
    elif escolha == 3:
        input(f'Guarda do Reino: Boa sorte, caso precise de ajuda, recue pois chamarei alguns guardas para lhe prestar apoio.')

    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'--> Ao chegar na base, você precisa entrar então:\n'
                            f'[1] Chuta o portão com toda sua força, não será um portão que irá para um guerreiro como você.\n'
                            f'[2] Olha ao redor procurando alguma entrada.\n'
                            f'[3] Salta o portão, porque ele não é alto como deveria. \n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'--> O portão se abre sem barulhos altos, parece que estava velho e oco. Então você ainda está incógnito.')
    elif escolha == 2:
        input(f'--> Você acha um vão quebrado no murro e passa por ele, avançando para dentro da base.')
    elif escolha == 3:
        input(f'--> Caindo do outro lado, você percebe que nenhum inimigo sabe que você está lá.')

    input('--> Dentro da fortaleza estava ocorrendo uma reunião entre os marinheiros corruptos e os piratas.')

    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'--> Percebendo que estavam negociando, você:\n'
                            f'[1] Ataca todos com a fúria de um guerreiro.\n'
                            f'[2] Espera os piratas saírem da fortaleza após o fechamento do acordo.\n'
                            f'[3] Volta ao Guarda para invadir com os reforços.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    sorte = random.randint(1,3)
    if escolha == 1 and sorte == 1:
        input('--> Você desperta uma força incomum e ataca os marinheiros com um ciclone de espadas,')
        input('--> derrotando metade deles com um único golpe, o restante em estado de choque hesita e ataca você')
        input('--> que apara e contra ataca, mas é acertado pelos piratas.')
        input('--> Estes estavam em menor número que os marinheiro então você se acalma e fica defendendo e contra atacando')
        input('--> até que reduz o número total de inimigos a apenas cinco, mas toma um golpe nas costas.')
        input('--> Você se enfurece e lança sua espada matando um, e finaliza dois com socos. ')
        input('--> Os dois últimos tentaram correr mas você ja de posse da espada novamente os alcançou e os fatiou .')
    elif escolha == 1:
        input('--> Você ativa uma fúria berserker fatiando quase todos os marinheiros, mas os piratas se unem a eles.')
        input('--> Com a união dos inimigos, você é golpeado de diversos lados, mas quase para ser derrotado, o reforço que o Guarda Real chamou chega.')
        input('--> Com a chegada deles, os inimigos se destraem por um instante e você levanta do chão e reagrupa com eles, e derrotam todos os inimigos.')
        input('--> Você encontra o Guarda do Reino e o agradeçe pelo reforço, e também aos demais guardas que vieram ajudá-lo.')

    elif escolha == 2 and sorte == 3:
        input('--> No momento em que os piratas saem da base, você avança sorrateiramente para começar uma chacina, mas com somente três baixas.')
        input('--> Você é avistado e eles formam um círculo ao seu redor e com diversos golpes você cai.')
        input('--> Mas no momento crucial para permanecer vivo aparece os guardas de apoio e assim consegue derrotar os marinheiros corruptos')
        input('--> Você agradeçe aos guardas do reino e principalmente aquele que te ajudou chamando eles.')
    elif escolha == 2:
        input('--> Quando os piratas saem da fortaleza você começa o ataque, pegando dois inmigos sorrateiramente.')
        input('--> Antes que os outros possam perceber sua presença você repete o ataque em outros dois e lança a espada em outro.')
        input('--> Desse modo, metade dos inimigos ja foram, mas você é avistado e eles partem para cima, com aparadas perfeitas você elimina mais dois,')
        input('--> Os últimos três vieram enfileirados avançando sobre você, mas você com um único golpe de estocada frontal perfurou os três no coração.')

    elif escolha == 3:
        input(f'--> Você retorna ao Guarda e agora com uma tropa de guardas vocês invadem a base amedrontando os "mafiosos".')
        input(f'--> vocês fazem uma chacina com toda a fúria por justiça.')

    input('--> Com todos os inimigos derrotados e sua missão cumprida, você volta ao ferreiro Yudi.')

    escolha = 0
    while escolha < 1 or escolha > 4:
        escolha = input(f'--> Já no ferreiro você:\n'
                            f'[1] Agradeçe por ele ter lhe informado sobre essa corrupção, afirmando agora que a cidade está livre dessa escória.\n'
                            f'[2] Fala que fez o que foi combinado, que agora precisa da espada Força.\n'
                            f'[3] Conta para ele que ganhou reputação com o povo e guardas, que não precisa entregar a espada, isso foi suficiente.\n'
                            f'[4] Fala para ele que esta missão estava difícil, para que ele entregue a espada ou terá o mesmo destino dos marinheiros.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'Yudi: Que bom que você também sente que agora tudo está mais tranquilo, sem aqueles marinheiros que enganavam todos.')
        input(f'Yudi: Tome a espada Força. Boa sorte nas suas jornadas, quando enfrentar alguém forte, que a Força esteja com você .')
    elif escolha == 2:
        input(f'Yudi: Agora que libertou a cidade desses malditos, mais que merecido empunhar esta espada, tome é sua. Boa sorte na sua jornada.')
    elif escolha == 3:
        input(f'Yudi: Você pode ter ganhado reputação, mas mesmo recusando eu insisto que fique com a espada Força.')
        input(f'Yudi: A sua aliada a Força será, e poderosa aliada ela é. Leve-a por favor ')
    elif escolha == 4:
        input(f'Yudi: Entendo sua fúria, perdão colocar você nessa missão, mas você como sempre obteve sucesso.')
        input(f'Yudi: Tome a espada, você merece pois é corajoso.')

    input('--> Você pega a espada Força e segue para o centro da cidade.')
    quest2 = True

def questBosqueGigantes():
    global nome
    global classe
    global reino
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
        input('--> Você pensa que se for uma criatura perigosa provável que não foi para a cidade, então está no bosque, então você vai procurá-la.')
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
        input('Menino: Claro que não cara, a gente tá na nossa aventura, perdido deve tá você então cuidado com os gigantes.')
        input(f'{nome}: Não sabia que tinha gigantes aqui, onde eles ficam?')
    elif escolha == 2:
        input('Menino: Sim, tem dois gigantes nesse bosque.')
    elif escolha == 3:
        input('Perigoso? tá zuando com a nossa cara é? acabamos de fazer amizade com os gigantes, somos radicais!.')
        input(f'{nome}: Desculpa "guerreiros radicais", onde fica esses gigantes?')

    input('Menino: Eles ficam um para a direita e o outro para a esqueda do bosque. Eles duelam um contra o outro todos os dias.')
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
        input('Jotun:Eu sou o mais forte gigante desse reino, mas para decretar isso, o combate entre eu e Brog precisa ter fim.')

    input('Jotun: Brog e eu somos gigantes guerreiros de Elbaff, mas por conta de um desintendimento entre nós.')
    input('Jotun: Não podemos retornar para lá, a não ser o vencerdor do duelo.')
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
        input('Jotun: Eu estava descançando, mas vamos, vai que aquele desmiolado está em apuros.')

    input('--> Vocês escutam que tem alguém em perigo pedindo ajuda e correm para procurar, pode ser Brog.')
    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input('--> Vocês chegam perto do pedido, e avista Brog preso por piratas enquanto descançava do duelo diário. Você:\n'
                            '[1] Corre para ajudá-lo.\n'
                            '[2] Deixa ele se resolver, pois é um honrado guerreiro de Elbaff, ajudá-lo pode ferir seu orgulho.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('--> Você corre para cortar as cordas que prenderam Brog enquanto ele descançava.')
        input('--> Mas os piratas apontam canhões para você e Jotun.')
    elif escolha == 2:
        input('--> Você não quer ajudar Brog pois ele pode ficar com o orgulho ferido.')
        input('--> mas Jotun te conta que Brog foi pego desprevino então ele não tem culpa.')
        input('--> Quando você vai ajudar o gigante, os piratas miram canhões em você e Jotun.')

    input('Os piratas ameaçam vocês falando que não teriam chances')
    sorte = random.randint(1,4)
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
        input('--> Jotun entra na briga para ajudar você e o outro gigante, com isso você mesmo caído derrota o pirata que ia lhe golpear.')
        input('--> Consegue ficar de pé novamente, você e Jotun juntos conseguem derrotar os piratas e libertar Brog.')
    elif escolha == 2:
        input('--> Você e Jotun atacam junto destruindo as balas e os canhões com golpes rápidos e fortes.')
        input('--> Vocês acabam com todos os piratas e libertam Brog.')

    input('Os gigantes agradecem a sua ajuda e falam que você possui um espírito e dom de batalha digno de um guerreiro de Elbaff')
    input('Você deseja sorte para que eles consigam resolver esse duelo e volta para a cidade.')
    quest3 = True

def questEsgotoArqueiro():
    global nome
    global quest1
    escolha = 0
    maldicao = False
    flecha = False

    input('--> Está na cidade, na frente do esgoto.')
    input('--> Escuta vozes do seu interiror.')
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
        input(f'{nome}: o que eu vou fazer com isso? Mas vou guardar nesno assim.')
        flecha = True
    elif escolha == 2:
        input('--> Você xinga o mendigo e diz para ele sair dalí.')
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
        input('--> Você segue as tartaruas para ver onde elas irão.')
        input('--> Depois de um tempo, chega a um corredor com um rato e uma pizza estragada')
        input(f'{nome}: não tem nada aqui, só essas tartarugas e esse rato.')
        input('--> Você volta para a entrada do esgoto, depois pega o caminho oposto.')
    elif escolha == 2:
        input(
            '--> Você caminha um pouco e encontra alguns homens encapuzados, parecendo pertencer a algum culto macabro.')
        input('--> Também vê um homem preso e amarrado no meio da sala.')
        input(f'{nome}: Nossa! Eu sabia que tinha algo eatranho por aqui!')

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
        input('--> Você se aproima silenciosamente e fica escondido')
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
        escolha = input()

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
            input('--> Os inimogos restantes te percebem e te atacam desferindo golpes com suas pequenas facas.')
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

def questBosqueArqueiro():
    global nome
    global classe
    global reino
    global quest2

    input('Você chega no bosque e encontra meia dúzia de homens tristes.')
    input('Marcos: Olá viajante, eu sou o Marcos e esse são meus companheiros, somos camponeses e precisamos de ajuda.')
    input('Marcos: Fomos roubados por um homem chamado Ron, ele é fazedeiro e possui uma fazenda que fica próxima daqui.')
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
        input(f'Marcos: Fomos roubados enquantos colhíamos nossos grãos e estacávamos no armazém.')
        input(f'Marcos: Ele chegou com uma espingarda ameaçando-nos de morte e levou toda nossa colheita.')
        input(f'Marcos: Se você quiser nos ajudar basta ir até a grande fazenda dele que fica no leste do bosque.')
    elif escolha == 2:
        input(f'{nome}: Esse homem estava sozinho quando roubou vocês?')
        input(f'Marcos: Sim, ele apontou uma espingarda para que déssemos tudos nossos grãos a ele.')
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

    input('--> Você conta que está procurando por ele porque alguns camponeses acusaram-no de ter roubado todos os grãos deles.')
    input('Trabalhador: Entendi a situação, o patrão Ron não é má pessoa, mas tem uma tremenda ganância.')
    input('Trabalhador: Por isso acho que essas acusações possam até ser verdadeiras.')
    input('--> Você o agradeçe pela ajuda e segue para a casa principal da fazenda.')
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

    input('--> Então vocês partem de carroça para o bosque. Ao chegar nos camponeses você repara que Ron começa a suar de nervoso.')
    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'--> Vocês descem da carroça e você:\n'
                            f'[1] Confia nos camponeses e entrega os grãos que estavam na carroça para eles e obriga Ron a se desculpar.\n'
                            f'[2] Pede para que Ron se denfenda das acusações dos camponeses.\n'
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
        input('--> Você leva essa falta de argumento como uma comprovação de crime e decide entregar os grãos para os camponeses.')
        input('--> Ron então amendrontado pega sua carroça, agora vazia, volta para a fazenda o mais ráidpo possível.')
    elif escolha == 3:
        input(f'--> Você decide confiar em Ron, pois aquelas acusações estão muito infundadas.')
        input('Ron: Agora que você está confiando em mim vou tomar coragem e contar-lhe toda a verdade.')
        input('Ron: Todo os sábados eu passo por este caminho do bosque com a carroça carregada de grãos que comprei na venda.')
        input('Ron: Porém muitas vezes esses vadios que se dizem camponeses, que são na verdade ex-funcionários meus, ficam neste caminho para me roubar.')
        input('Ron: E ainda me ameaçam para que eu não conte a ningúem. Mas com você agora percebi que eles não teriam coragem para me matar neste momento.')
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
                                f'[3] Fala para que ele pare de mendigar e que você não tem interresse no que ele tem a falar.\n')
            if type(escolha) == str and escolha == '':
                escolha = -1
            else:
                escolha = int(escolha)

        if escolha == 1:
            input(f'Bruxo: Obrigado gentil arqueiro, mas tenho algo triste para lhe dizer. Você foi enganado por aqueles camponeses.')
            input('Bruxo: Eles são ex-empregados de Ron e vivem o roubando do caminho da venda a fazenda.')
            input('Bruxo: Provavelmente ele começou a suar e também não te contou isso porque é constantemente ameaçado por eles de morte.')
            input('Bruxo: Eu não o ajudo porque aqueles camponeses também sabem aonde minha família mora e também me ameaçam.')
            input('Bruxo: você poderia ter acabado com esta situação, mas apenas colaborou com eles sem saber, é uma pena.')
            input('--> Após dizer isto o bruxo some com sua bruxaria e você segue triste para o centro da cidade.')
        elif escolha == 2:
            input(f'Bruxo: Sem problemas, mas preciso te contar que você foi enganado pelos camponeses.')
            input('Bruxo: Eles são ex-empregados de Ron e vivem o roubando do caminho da venda a fazenda.')
            input('Bruxo: Provavelmente ele começou a suar e também não te contou isso porque é constantemente ameaçado por eles de morte.')
            input('Bruxo: Eu não o ajudo porque aqueles camponeses também sabem aonde minha família mora e também me ameaçam.')
            input('Bruxo: você poderia ter acabado com esta situação, mas apenas colaborou com eles sem saber, é uma pena.')
            input('--> Após dizer isto o bruxo some com sua bruxaria e você segue decepcionado para o centro da cidade.')
        elif escolha == 3:
            input(f'Bruxo: Agora compreendo o porque os camponeses te engaram facilmente, você é homem ignorante por natureza.')
            input('--> Após dizer isto o bruxo desaparece por um portal. E você ignora esta situação segue seu caminho para o centro da cidade.')


    elif escolha == 3:
        input('--> Após ouvir Ron contar tudo.')
        escolha = 0
        while escolha < 1 or escolha > 2:
            escolha = input(f'--> Você:\n'
                                f'[1] Mata todos os camponeses para livrar Ron do mal que eles lhe faziam.\n'
                                f'[2] Acha que Ron está tentando te manipular e deixa que eles se resolvam.\n')
            if type(escolha) == str and escolha == '':
                escolha = -1
            else:
                escolha = int(escolha)

        if escolha == 1:
            input(f'--> Você agora sabendo da verdade, atira flecha nos camponeses malditos pondo fim aos roubos deles os matando.')
            input(f'Ron: Muito obrigado {nome}, perccebi que você era justo e ainda bem que lhe contei tudo. Obrigado mesmo')
            input('--> Ron volta para a fazenda e você volta ao centro da cidade.')
        elif escolha == 2:
            input(f'{nome}: Esta situação tem muitas reviravoltas e lados a se tomar, estou farto de pensar. Vocês que se resolvam.')
            input('--> Ao dizer isso você vira as costas e vai embora.')
            input('--> Já ao longe você olha para trás e percebe os camponese fugindo com a carroça e Ron morto ao chão.')
            input('Você percebe agora que fez uma péssima e burra escolha e volta triste para o centro da cidade.')
    quest2 = True

def questProtetorArqueiro():
    global nome
    global quest3

    atirou = False#mostra se atirou nos caçadores

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
        input(f'{nome}: O problema não é este, vocês mataram o bando todo, duvido terem que aliementar tantas bocas assim.')

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
        input(f'{nome}: Se contiarem a matar os animais de maneira indiscriminada,\n'
              f'as futuras gerações podem nunca ver esses animais.')
        input('Caçador: Nossa, eu nunca pensei nisso. Imagine se eu não podesse ver todos esses animais...')
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
    input('Sigurd: Espere aqui vou trazer algo para você subir também. Eles me conhecem, mas não sabem dos nosso plano.')

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
            quest3 = True
            return
        else:
            input('--> Ele defende e pisca para você.')
            input('--> Você deixa ele acertar um soco sem força em seu rosto e ele te prende.')
    elif escolha == 2:
        input('--> Você confia nele e o deixa te prender.')

    input('--> Quando o barão se distrái, Sigurd o golpeia com um chute no rosto, e em seguida, você acompanha.')
    input('--> Juntos conseguem o imobilizar.')
    input('Sigurd: Vou colocá-lo na prisão!')
    input('--> Sigurd se torna o novo chefe da mansão.')
    input('Sigurd: De agora em diante, não serão toleradas carnificinas desnecessárias contra os animais!')
    input(f'{nome}: Fico feliz em ouvir isso! É muito bom ver que você está no comando agora.')
    input('--> Você volta para o centro da cidade.')
    quest3 = True


def questRogueArtsMago():
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
    input('--> O professor diz que dentro do baú, está o metamorfobia, um monstro que pode se transformar em seu maior medo.')
    input('--> Ele diz que a forma de derrotá-lo é pensar em algo engraçado e jogá-lo o feitiço hilárius.')

    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input('--> Seu maior medo são dragões.\n'
                         '[1] Imagine um dragão filhote\n'
                         '[2] Imgine um dragão cuspindo bolas de sabão\n'
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
        input('--> O mosro se transforma em um dragão real e muito ameaçador.')
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
        input('--> O professor faz o mostro se tranformar em um sapo e coloca-o no baú.')
    elif escolha == 2:
        input('--> Nada acontece com o vampiro.')
        input('--> Os alunos dizem que o sal ajuda contra espíritos, não contra vampiros.')
        input('--> O professor faz o mostro se tranformar em um sapo e coloca-o no baú.')
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
            'Professora: Você não escutou que o rio poderia ter vários seres das trvas? Provavelmente morreria nadando.')
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

def questDesertoMago():
    global nome
    global quest2

    input('--> Andando pelo deserto, você encontra um pequeno vilarejo.')
    input('--> Ao entrar, percebe que todos estão comemorando.')
    input(f'{nome}: O que estão comemorando?')
    input('Morador: Esta é a festa de abertura do desafio da pirâmide!')
    input('Morador: nesse desafio, os participantes devem entrar em uma pirâmide, passar por desafios, e depois voltar.')
    input(f'{nome}: Gostaria de participar deste desafio, como começo?')
    input('Morador: Tome isto.')
    input('--> O morador lhe enrega um papel e lhe explica onde fica a pirâmide do desafio.')
    input('--> Após caminhar um pouco, você chega à pirâmide. Vários participantes estão procurando a entrada.')

    escolha = 0
    while escolha != 3:
        print('--> Você lê o papel que lhe entregaram. Nele está escrito: \n"O topo é onde os líderes ficam,'
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
    escolha= 0
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
                if type(escolha) == str and escolha == '':#verificar
                    escolha = -1
                else:
                    escolha = int(escolha)
            else:
                escolha = input()
                if type(escolha) == str and escolha == '':#verificar
                    escolha = -1
                else:
                    escolha = int(escolha)

        if escolha == 1:
            input('--> Resolve retornar para a câmara principal.')
        elif escolha == 2:
            input('--> Você tenta soltar a canoa, mas ela está muito bem presa pelas tábuas.')
        elif escolha == 3:
            input('--> você percebe que se queimar as tábuas, provavelmente quaimará também a canoa.')
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
                inundado = False#not inundado
            else:
                input('--> A água começa a ser bombeada para a câmara.')
                input('--> A água inunda todas as câmaras em três metros de altura, mas ainda tem algum espaço para você respirar.')
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
    input('--> Essa cãmara tem quatro alavancas e uma placa que diz:\n'
          '"Com apenas dois símbolos, posso representar o número 10."')

    d1 = 'baixo'#0
    d2 = 'baixo'#0
    d3 = 'baixo'#0
    d4 = 'cima' #1
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
            input('--> Assim que você sai da câmara, as alavancas voltam as suas posições pré definidas para o desafio.')
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

        escolha_Pc = random.randint(1,3)
        if escolha_Pc == 1:
            item_pc = 'planta'
        else:
            if escolha_Pc == 2:
                item_pc = 'fogo'
            else:
                item_pc = 'água'

        print(f'{nome} escolheu: {item_jogador}')
        print(f'{nomeOponente} escolheu: {item_pc}')

        #Verificando empates
        if (item_jogador == item_pc):
            pontosRodada = pontosRodada + 1
            input(f'--> Empate! Ninguém somou ponto! A próxima rodada vale {pontosRodada} pontos.\n')

        #Verificando o jogador
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


            #Verificando o npc
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

def questTorneioMago():
    global nome
    global quest3
    competidores = ['Merlin','Aleneus', 'Zadel', 'Azahr', 'Erius', 'Eneel', 'Babidi', 'Lopianne', 'Strange',
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
    input('Narrdador: Esse ano temos dezesseis competidores.')
    input('Narrador: O competidor que ganhar três jogos com menos de três derrotas é o vencedor!')

    while (jogosGanhos < 3) and (jogosPerdidos < 3):
            oponente = competidores[random.randint(0, len(competidores)-1)]
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

def questFinal():
    global nome
    global reino

    input('--> No centro da cidade, você vê um pelotão de soldados de seu reino.')
    input('--> Eles estavam correndo rumo à montanha Tallhill do reino Hedeby.')
    input('--> Um guarda vem em sua direção.')
    input(f'Guarda: {nome}, você foi uma peça fundamental na nossa última guerra, e estamos precisando da sua ajuda novamente.')
    input('Guarda: com a rendição do reino Hedeby, eles passaram por uma fase de grande vexame, então decidiram usar tudo\n'
          '\to que tem para um último confronto contra nós.')
    input('Guarda: venha nos ajudar, siga o pelotão, para receber mais informações do comandante.')
    input('--> Você segue o pelotão e o comandante diz:')
    input('Comandante: Homens, os hedebyrianos estão montando uma última investida. E eles vão acionar seu ataque anciente.')
    input('Comandante: Se trata de um dragão ancião que permanece selado na montanha Tallhill, e eles pretendem o libertar.')
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
        input('Comandate: Ele já atacou nosso reino uma vez, mas conseguimos expulsá-lo.')
    elif escolha == 2:
        input(f'{nome}: Percebi que este dragão parece ser uma ameaça considerável, então como ele foi selado no passado?')
        input('Comandante: Realmente seu poder não pode ser subestimada.')
        input('Comandante: Na épopca em que ele foi selado, passávamos por uma crise, e nosso exército estava muito fraco.')
        input('Comandante: Então decidimos apenas selá-lo.')

    input('Comandante: Só conseguimos detê-lo usando a técnica suprema para selar inimigos, o mafuuba.')
    input('Comandante: sem mais perguntas, vamos até a montanha impedí-los.')
    input('--> Chegando em Tallhill, vocês avistam o pouco do exército de Hedeby que restou.')
    input('--> Eles estão entrando em uma construção antiga, no inteiror da montanha, para quebrarem o selo que aprisiona o dragão.')
    escolha = 0
    while escolha < 1 or escolha > 3:
        escolha = input(f'--> Então você:\n'
                            f'[1] Tenta convencer a invadir logo, pois a qualquer momento, o dragão pode ser liberto.\n'
                            f'[2] Pergunta ao comandante como proseguir.\n'
                            f'[3] Tenta convencer o seu exército a prendê-los no interior da montanha. \n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input(f'{nome}: Vamos rápido, eles podem libertar aqule monstro a qualquer momento!')
        input(f'Comandante: Não podemos agir por impulso, devemos esperar reforços.')
        input(f'{nome}: Não posso ficar aqui parado enquanto um dragão pode ser libertado.')
        input(f'--> Você entra sozinho na montanha.')
        input('--> Depois de caminhar um pouco, cai em uma armadilha deixada pelos hadebyrianos.')
        input('--> Você grita para pedir ajuda, mas seu exército está muito longe para escutar.')
        input('--> No entanto, os hadebyrianos o escutam e se apressam para o ritual de libertação.')
        input('--> Logo o seu exército aparece com os reforços, contendo agora caçadores para desarmar as armadilhas e te socorrem.')
        input('--> Ao terminar de te soltar, vocês escutam o dragão sendo liberto.')
        input('--> Então se afastam da entrada, pois provavelmente ele sairá por ali.')
        dragaoLiberto()

    elif escolha == 2:
        input(f'--> O comandante diz que acredita ser melhor esperarmos por reforços.')
        input('--> Algum tempo depois, os reforços chegam, e um deles conta de que há armadilhas na passagem que leva ao inteiror.')
        input('--> Vocês avançam com cuidado por causa das armadilhas, desarmando-as no caminho.')
        input('--> No inteiror de Tallhill, encontram os inimigos fazendo um ritual de libertação.')
        input('--> O comandante ordena um ataque, e assim, o ritual é impedido.')
        input('--> Agora que o dragão permanecerá selado, eles terão que lutar somente com os homens que ali estão.')
        dragaoSelado()
    elif escolha == 3:
        input(f'--> Você convence o pelotão de que a melhor escolha é prendê-los dentro da montanha deixando-os sem saída.')
        input(f'--> O conadante concorda, porque segundo ele, essa é a única saída, e o dragão não conseguirá arrumar um jeito de sair.')
        input(f'--> Então vocês utilizam explosivos para destruir a única passagem para o interiror da montanha.')
        input('--> Vocês escutam o despertar do dragão e pensam estar seguros, por ele estar preso dentro da montanha.')
        input('--> Alguns segundos depois, as pedras que bloqueavam a passagem foram explodidas pelo lado de dentro.')
        input('--> O comandate diz que eles deviam estar preparados para caso ficassem presos na caverna, então trouxeram dinamite.')
        dragaoLiberto()
    print('\n',50*'-','FIM',50*'-')

def dragaoLiberto():
    global reino
    global nome
    escolha = 0
    while escolha < 1 or escolha > 2:
        escolha = input(f'--> O dragão sai da caverna e vocês decidem:\n'
                            f'[1] Lutar para por um fim ao dragao.\n'
                            f'[2] Luta para enfraquecê-lo e selá-lo novamente.\n')
        if type(escolha) == str and escolha == '':
            escolha = -1
        else:
            escolha = int(escolha)

    if escolha == 1:
        input('--> Vocês se organizam para formar um ataque que não dê chances de vitória ao dragão.')
        input('--> Esse ataque consiste em avançar em três frentes, uma liderada pelo comandante, outra por você e a última por Merin.')
        input('--> O pelotão de Merlin focará no dragão, imobilizando-o.')
        input('--> Enquanto ele está imobilizado, o pelotão do comandante irá derrubá-lo e prendê-lo no chão.')
        input('--> Durante isso, a sua frente elimanará todo o exército Hedeby.')
        sorte = random.randint(1, 10)
        if sorte <= 5:      # 50% de chance (final bom)
            input('--> O dragão é preso ao chão, sem chances de escapar, e todos os outros inimigos são mortos.')
            input('--> Vocês atacam o dragão que enfim falece, sendo decretado um fim definitivo a esa guerra.')
            input('--> Seu exército volta para a cidade comemorando o fim da guerra, e do dragão.')
            input(f'--> Vocês são considerados heróis de {reino}, pois agora as próximas gerações não precisarão se preocupar como retorno deste monstro.')
        elif sorte <= 8:    # 30% de chance (final médio)
            input('--> Merlin e seus homens infelizmente não conseguem segurar o dragão para que o pelotão do comandante derrubasse o dragão.')
            input('--> Mesmo seus homens aniquilando o enfraquecido exército dos hedebyrianos.')
            input('--> Com essa falha no plano, o dragão consegue escapar voando para longe.')
            input('--> Seu exército volta para a cidade e avisa todos do reino que Hedeby não é mais um problema.')
            input(f'--> Porém o dragão está a solta e poderá retornar à {reino} a qualquer momento, cedo ou tarde, todos devem estar preparados.')
        else:               # 20% de chance (final ruim)
            input('--> Merlin e seus homens infelizmente não conseguem segurar o dragão para que o pelotão do comandante derrubasse o dragão.')
            input('--> Além disso, houve outro problema, pois você e sua tropa encontram muita resistência dos hedebyrianos.')
            input('--> Com o plano sendo totalmente falho, e o dragão tendo apoio da tropa de seus salvadores, ele derrota todo o seu exército.')
            input(f'--> É decretado um fim à guerra, o reino Hedeby vence e assola completamente o reino de {reino}.')
            input('--> E agora, fortalecidos, partem para derrotar outros reinos.')
    elif escolha == 2:
        input(f'--> Seu exército se divide em dois, a sua tropa ficou encarregada de derrotar o restante dos hedebyrianos.')
        input('--> Ao mesmo tempo, o pelotão do comandante segurava o dragão.')
        input('--> Merlin começou a fazer as preliminares para realizar o mafuuba, concentrando-se no dragão.')
        input('--> Passado algum tempo, sua tropa extermina os inimigos, e ajudam a tropa do comandante a enfraquecer o dragão.')
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
        input(f'--> II - Não ataquem o reino de {reino};')
        input(f'--> III - Não tentem libertar o dragão novamente.')
        input('--> Eles concordam e agradecem pela compaixão.')
        input('--> Cada exército volta a seu reino.')
        input('--> Tempos depois, graças a misericórdia sua e dos soldados, os dois reinos fizeram uma aliança.')
        input('--> Esta aliança ajudou ambos os reinos a prosperar, se ajudando no comércio, na proteção do território e na formação de um grande exército para guerras.')
    elif escolha == 2:
        input(f'--> Vocês decidem acabar com o mal pela raiz, pois assim como já se rebelaram de uma rendição, podem fazer de novo.')
        input('--> Além de que são uma ameaça, pois podem liberar o dragão quando bem entenderem caso fiquem vivos.')
        input('--> Você e o exército partem com fúria para cima dos inimigos, massacrando-os.')
        input('--> Todos Voltam para a cidade e comemoram a vitória sobre o reino de Hedeby.')
        input('--> Mas avisam que todos precisam ficar vigilantes pois o dragão ainda está selado podendo ser liberto por inimigos no futuro.')

def mapaGuerreiro():
    global nome
    global quest1#Taverna
    global quest2#Loja do ferreiro
    global quest3#Bosque

    while (quest1 == False) or (quest2 == False) or (quest3 == False):
        escolha = 0
        while escolha < 1 or escolha > 3:
            escolha = input(f'--> Segue para:\n'
                                f'[1] Taverna.\n'
                                f'[2] Loja do ferreiro.\n'
                                f'[3] Bosque. \n')
            if type(escolha) == str and escolha == '':
                escolha = -1
            else:
                escolha = int(escolha)

        if escolha == 1:
            if quest1:
                input('Moe: Eae campeão, obrigado por ter me ajudado. Quer uma bebida?')
                input(f'{nome}: Não foi nada. Claro que quero.')
                input(f'{nome}: está calma hoje não é?')
                input('Moe: para mim é bom que fique assim.')
                input('--> Você retrona à cidade.')
            else:
                questTavernaGuerreiro()
        elif escolha == 2:
            if quest2:
                input(f'Yudi: Vejo que a Força está com você, gostei de ver. Quer comprar algo?')
                input(f'{nome}: Não, estou apenas procurando algo para fazer.')
                input('Yudi: Eu não tenho mais nenhum serviço, mas obrigado por ajudar a acabar com a marinha do forte. ')
                input(f'{nome}: Não foi nada.')
                input('--> Você retrona à cidade.')
            else:
                questFerreiroGuerreiro()
        elif escolha == 3:
            if quest3:
                input('--> Você avista os dois gigantes de Elbaff travando seu duelo diário.')
                input('--> Depois de assitir um pouco, percebe que não tem mais nada para fazer ali.')
                input('--> Você retrona à cidade.')
            else:
                questBosqueGigantes()
    questFinal()

def mapaArqueiro():
    global nome
    global quest1#Subúrbios
    global quest2#Bosque
    global quest3#Floresta

    while (quest1 == False) or (quest2 == False) or (quest3 == False):
        escolha = 0
        while escolha < 1 or escolha > 3:
            escolha = input(f'--> Segue para:\n'
                                f'[1] Subúrbios.\n'
                                f'[2] Bosque.\n'
                                f'[3] Floresta.\n')
            if type(escolha) == str and escolha == '':
                escolha = -1
            else:
                escolha = int(escolha)

        if escolha == 1:
            if quest1:
                input(f'--> Passa perto do esgoto, mas percebe que está tudo normal.')
                input('--> O mendigo não está ali.')
                input('--> Você retrona à cidade.')
            else:
                questEsgotoArqueiro()
        elif escolha == 2:
            if quest2:
                input('--> Você aprecia a natureza. Tudo está calmo.')
                input('--> Você retrona à cidade.')
            else:
                questBosqueArqueiro()
        elif escolha == 3:
            if quest3:
                input('--> Você consegue caçar sem ser interrompido.')
                input('--> Após a caça, não tem muito o que fazer na floresta.')
                input('--> Você retrona à cidade.')
            else:
                questProtetorArqueiro()
    questFinal()

def mapaMago():
    global nome
    global quest1#Escola
    global quest2#Deserto
    global quest3#Floresta

    while (quest1 == False) or (quest2 == False) or (quest3 == False):
        escolha = 0
        while escolha < 1 or escolha > 3:
            escolha = input(f'--> Segue para:\n'
                                f'[1] Escola.\n'
                                f'[2] Deserto.\n'
                                f'[3] Floresta. \n')
            if type(escolha) == str and escolha == '':
                escolha = -1
            else:
                escolha = int(escolha)

        if escolha == 1:
            if quest1:
                input(f'{nome}: Não tenho mais nada para fazer aqui, pois já fiz todas as aulas.')
                input('--> Você retrona à cidade.')
            else:
                questRogueArtsMago()
        elif escolha == 2:
            if quest2:
                input('Morador: Como vai campeão do desafio da pirâmide?')
                input(f'{nome}: Bem. Não tem mais nenhum desafio?')
                input('Morador: Gosta mesmo de desafios, hein? Infelizmente não temos mais desafios.')
                input('--> Você retrona à cidade.')
            else:
                questDesertoMago()
        elif escolha == 3:
            if quest3:
                input('A floresta está calma, agora que o acampamento foi embora')
                input('--> Você retrona à cidade.')
            else:
                questTorneioMago()
    questFinal()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
prologo()
