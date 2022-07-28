from classe import Pesquisa


#Perguntas e código principal
perguntas = ["Pergunta 1 - Você realiza alguma atividade fisica regularmente ?",
             "Pergunta 2 - Você já sofreu de algum problema cardiaco ?",
             "Pergunta 3 - Você faz exames médicos a cada 3 meses ?",
             "Pergunta 4 - Você ja tomou alguma vacina contra o Covid ?"]

pesquisaClasse = Pesquisa(perguntas, "path.csv")

pesquisaClasse.iniciarPesquisa()
