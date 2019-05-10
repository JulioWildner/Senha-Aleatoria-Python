#ADIVINHA SENHA ALEATÓRIA EM PYTHON                   |
#Técnico em informática                               |
#Fundamentos de Lógica e Algoritmos                   |
#Trabalho Prático                                     |
#ALUNOS: Guilherme Cavalli, Julio Cesar Pick Wildner  |
#-----------------------------------------------------|
#================== IMPORT ====================
import random, os # Importa o módulo "random" no python para o sorteio aleatório das senhas, "os" para limpar no terminal (SHELL).
#=================== WHILE DO JOGO ====================
playgame = True # Variável com valor igual a "True" para iniciar o while ou pará-lo.
while playgame == True:  # While executado enquanto "playgame" ter valor "True". Ele contém todo o jogo, com objetivo de dar opção para jogar novamente assim que acabar.
    def jogo_da_senha(): # Função que armazena todo o jogo com finalidade de chamá-la para executar o jogo.
        #================== VARIÁVEIS =================
        global tentativas,insere,limpar,digito1,digito2,digito3,digito4,digito5,tem1,tem2,tem3,tem4,tem5 # Deixa várias variáveis em globais para utilizar durante def's de print que vem antes dos input's e if's.
        tentativas = 10 # Insere um valor para a variável "tentativas", que corresponde ao número de vezes que o jogador irá tentar acertar a senha aleatória.
        insere ='' # Variável utilizada no input para a senha informada pelo usuário.
        limpar="os.system('cls' if os.name == 'nt' else 'clear')" #Executa um comando no terminal (Shell) para limpá-lo.
        digito1 = '-';digito2 = '-';digito3 = '-';digito4 = '-';digito5 = '-';tem1 = '-';tem2 = '-';tem3 = '-';tem4 = '-';tem5 = '-'; # Variáveis de -1,+1 e 0 e variáveis dos digitos do usuário com "-" armazenados para utilizar numa def antes dos input's e if's sem dar algum erro.
        #==============================================
        #======== DEF QUE CONTEM TODO O JOGO ==========
        #==============================================
        #=== - Limpar Terminal (Shell)
        eval(limpar) #Executa um comando no terminal (Shell) para limpá-lo.
        #================== MENU ======================
        def titulo1(): #-----------------------------------\
            print('+-----------------------------------+')#| = Função que printa um título para o jogo.
            print("|  ADIVINHA SENHA EM PYTHON ?'-'?   |")#|
            print('+-----------------------------------+')#/
        def titulo2(): #-----------------------------------\                     
            print('+-----------------------------------+')#| = Função que printa um título em cima do printa da def "informacoes()".
            print("|        INFROMAÇÕES DO JOGO        |")#/
        def como_jogar(): #--------------------------------\   
            print('|            COMO JOGAR?            |')#|
            print('|- - - - - - - - - - - - - - - - - -|')#|
            print('| Informe uma senha quando se pede. |')#|
            print('| A senha informada sera comparada  |')#|
            print('| com outra senha gerada de maneira |')#|
            print('| aleatórai e oculta, pela CPU.     |')#|
            print('| Como jogador, você terá 10 tenta- |')#| = Função que printa instruçoes de como jogar este jogo.
            print('| tivas para acertar a senha.       |')#|
            print('| Sua senha será analisada e será   |')#|
            print('| printada com, respectivamente, as |')#|
            print('| informações -1, 0, ou +1 para     |')#|
            print('| cada digito da senha informado.   |')#|
            print('| Recomendado jogar em algum        |')#|
            print('| terminal (Shell) como por exemplo |')#|
            print('| o CMD do Windows.                 |')#/
        def informacoes(): #-------------------------------\
            print('|- - - - - - - - - - - - - - - - - -|')#|
            print('|(-1) = Dígito informado não está   |')#|
            print('|       na senha gerada.            |')#|
            print('|(0) = Dígito está na senha mas não |')#| = Função que printa os significados de -1, 0 e +1 logo abaixo da def "titulo2()".
            print('|      na posição correspondente.   |')#|
            print('|(+1) = Dígito está na senha e na   |')#|
            print('|       posição correspondente.     |')#|
            print('+-----------------------------------+')#/
        #================== SORTEIO ===================
        def printar(): #---------------------------------------------------------------------------\
            print('+-----------------------------------+') #                                       |
            print('>>> RESPECTIVAMENTE...') #                                                      | = Função que printa a senha do input do usuário e a senha comparada respectivamente
            print('>>> SENHA INFORMADA: %s,%s,%s,%s,%s'%(digito1,digito2,digito3,digito4,digito5))#|
            print('>>> SENHA COMPARADA: %s,%s,%s,%s,%s'%(tem1,tem2,tem3,tem4,tem5)) #--------------/ 
        #======== WINNER WINNER CHICKERN DINNER =======
        def winner(): #---------------------------------------------------------------------------\           
            print('+====================================') #                                      |
            print('|   WINNER WINNER CHICKEN DINNER!   |') #                                      |
            print('+===================================+') #                                      | = Função printada após o jogador acertar a senha.
            print('|===== PARABÉNS, VOCE ACERTOU! =====|') #                                      |
            print('|======= A SENHA ERA:',senha1 + senha2 + senha3 + senha4 + senha5,' =======|')#|
            print('+===================================+') #--------------------------------------/
        #============ YOU LOSE, FATALITY ==============
        def loser(): #----------------------------------------------------------------------------------\
            print('+============== VOCE PERDEU ==============+') #                                      |
            print('|Sua última tentativa digitada foi:',insere,'|') #                                   | = Função printada após as tentativas acabarem e o jogador não acertar a senha.
            print('|Acabou as tentativas! A senha era:',senha1 + senha2 + senha3 + senha4 + senha5,'|')#|
            print('+============== VOCE PERDEU ===============+') #--------------------------------------/
        #==============================================          
        senha1 = str(random.randint(0,9))#\
        senha2 = str(random.randint(0,9))#|
        senha3 = str(random.randint(0,9))#| = Vai sortear um digito de 0 a 9 e armazenar numa variável. São 5 variáveis, uma para cada digito sorteado.
        senha4 = str(random.randint(0,9))#|
        senha5 = str(random.randint(0,9))#/
        senhatoda = [senha1,senha2,senha3,senha4,senha5]# = Todas as senhas listadas em uma só variável, para ver se o numero do usuario esta na senha e se contém os digitos da variável mais abaixo "digitotodo".
        #================== INFORMAR ==================
        start = True # Variável com valor "True" para executar o while.
        while start == True: # While com "start" igual a "True", vai começar os input's e if's no jogo.
            titulo1() #---\
            como_jogar() #| = Vai printar os alguns def's vistos acima no código.
            titulo2() #   |
            informacoes()#/
            print('|-> OBS: Você tem %s tentativas!      '%tentativas) # Printa as tentativas restantes do usuário.
            printar() # Printa a função de comparação da senha aleatoria com a informada pelo usuário com os -1,0 e +1.
            print('+-----------------------------------+') # Print para deixar mais organizado durante a execução.
            insere = input('>>> Informe a senha de 5 dígitos: ') # Input da senha informada pelo usuário.
            print('') # Print para deixar mais organizado durante a execução.
            verificar = len(insere) # Variável para armazenar a quantidade de elementos do input do usuário, exemplo: input = 12345, verificar = 5 -> (5 elementos).
        #================== VERIFICAR =================
            while verificar != 5: # While que é executado caso o usuário informar uma senha com mais ou menos de 5 digitos. Para a execução assim que for informado uma senha numérica de 5 digitos.
                print('OPA! Senha inválida! Necessário 5 digitos de 0 a 9!') # Print avisando que a senha não vale.
                insere = input('>>> Informe a senha de 5 dígitos: ') # Input novamente uma senha do usuário
                print('') # Print para deixar mais organizado durante a execução.
                verificar = len(insere) # Variável para armazenar a quantidade de elementos do input do usuário, exemplo: input = 12345, verificar = 5 -> (5 elementos).
        #================== DIGITADO =================
            digito1 = insere[0]   #\
            digito2 = insere[1]   #|
            digito3 = insere[2]   #| = Cira variáveis com os digitos de 1 a 5 (0 a 4) para comparar com os da senha sorteada.
            digito4 = insere[3]   #|
            digito5 = insere[4]   #/
            digitotodo = [digito1,digito2,digito3,digito4,digito5] # = Varável que armazena todos os digitos para no fim verificar se os digitos sao iguais a "senhatoda" e informar que foi ganhador. 
        #================== COMPARAR ==================
            #=== DIGITO 1: ---------------------------\
            if digito1 in senhatoda: #                |
                tem1 = '0' #                          |
                if digito1 == senha1: #               |
                    tem1 = '+1' #                     |
            else: #                                   |
                tem1 = '-1' #                         |
            #=== DIGITO 2:                            |
            if digito2 in senhatoda: #                |
                tem2 = '0' #                          |
                if digito2 == senha2: #               |
                    tem2 = '+1' #                     |
            else: #                                   |
                tem2 = '-1' #                         |
            #=== DIGITO 3:                            |
            if digito3 in senhatoda: #                |
                tem3 = '0' #                          | = Serve para comparar se os digitos da senha do usuário estão nao senha gerada e nas respectivas posiçõies, ou não, e adicionar os -1, 0 e +1 em variáveis para printar na def "printar()"
                if digito3 == senha3: #               |
                    tem3 = '+1' #                     |
            else: #                                   |
                tem3 = '-1' #                         |
            #=== DIGITO 4:                            |
            if digito4 in senhatoda: #                |
                tem4 = '0' #                          |
                if digito4 == senha4: #               |
                    tem4 = '+1' #                     |
            else: #                                   |
                tem4 = '-1' #                         |
            #=== DIGITO 5: #                          |
            if digito5 in senhatoda: #                |
                tem5 = '0' #                          |
                if digito5 == senha5: #               |
                    tem5 = '+1' #                     |
            else: #                                   |
                tem5 = '-1' #-------------------------/
            #=== - Limpar Terminal (Shell)
            eval(limpar) #Executa um comando no terminal (Shell) para limpá-lo.
            #=== - SE GANHOU:
            if digitotodo == senhatoda: #--\
                winner() #                 | = if para verificar se todos os digitos da senha do usuário estão, respectivamente, iguais ao da senha gerada. Se esse for o caso, ira printar que acertou a senha e parar a execução do jogo, iniciando um input para jogar novamente. 
                start = False #------------/
            #=== - TENTATIVAS:
            tentativas -= 1 # Desconta 1 das tentativas a cada vez que o usuário informa uma senha e não corresponde igualmente a senha gerada.
            if tentativas == 0 and digitotodo != senhatoda: #--\
                loser() #                                      | = if para verificar se as tentativas ficaram igual a 0 e se a senha informada pelo usuário não corresponde igualmente a senha gerada. Se esse for o caso, ira printar que não acertou a senha e parar a execução do jogo, iniciando um input para jogar novamente.
                start = False #--------------------------------/
    #===== EXECUTANDO O JOGO ========
    jogo_da_senha() # Chama a função que armazena todo o jogo.
    #=============================================
    #========= JOGAR NOVAMENTE??? ================
    #=============================================
    restart = input('\n>>> Gostaria de jogar novamente? (s/n): ') # Input perguntando se quer jogar novamente. S pra sim e N pra não.
    if restart == 's' or restart == 'S': #\ = if que se input for igual a S ou s, "playgame" ficará "True", reiniciando o jogo dentro do while.
        playgame = True # ----------------/
    elif restart == 'n' or restart == 'N': #\ = if que se input for igual a "N" ou "n", "playgame" ficará "True", encerrando o jogo ao para o while.
        playgame = False #------------------/
    while restart != 'n' and restart != 'N' and restart != 's' and restart != 'S': #\ 
        eval(limpar) #Executa um comando no terminal (Shell) para limpá-lo. ------  | = while verificando que, se o input nao for igual a "s" ou "n", irá printar entrada inválida e perguntar o input novamente, e caso novamente não ser igual a "s" ou "n", repetir até ser.
        print('>>> Entrada inválida! Digite "S" ou "N"!') #-------------------------|
        restart = input('\n>>> Gostaria de jogar novamente? (s/n): ') #-------------/
