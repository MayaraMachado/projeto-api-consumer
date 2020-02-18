from flask import Flask, jsonify, request, redirect
from flask_cors import CORS, cross_origin
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
#from urllib2 import urlopen
import os   

app = Flask(__name__)
CORS(app)

@app.route('/api/v1/filmes', methods=['GET'])
def filmes():
    URL = "http://www.adorocinema.com/filmes/todos-filmes/notas-espectadores/"
    
    html_doc = urlopen(URL).read()
    soup = BeautifulSoup(html_doc, "html.parser")
    data = []
    for dataBox in soup.find_all("div", class_="data_box"):
        titleObj = dataBox.find("a", class_="no_underline")
        imgObj = dataBox.find(class_="img_side_content").find_all(class_="acLnk")[0]
        sinopseObj = dataBox.find("div", class_="content").find_all("p")[0]
        dateObj = dataBox.find("div", class_="content").find("div", class_="oflow_a")
        movieLinkObj = dataBox.find(class_="img_side_content").find_all("a")[0]
        generoObj = dataBox.find("div", class_="content").find_all('li')[3].find('div',class_="oflow_a")
        detailsLink = 'http://www.adorocinema.com' + movieLinkObj.attrs['href']

        #LOAD FULL SINOPSE 
        htmldocMovieDetail = urlopen(detailsLink).read()
        soupMovieDetail = BeautifulSoup(htmldocMovieDetail, "html.parser")
        fullSinopse = soupMovieDetail.find(class_="content-txt")     
        fullImgObj = soupMovieDetail.find("meta",  property="og:image")   

        data.append({'titulo': titleObj.text.strip(),
                    'genero': generoObj.text.replace('\n','').strip(),
                    'poster' : fullImgObj["content"], 
                    'sinopse' : sinopseObj.text.strip(),
                    'data' :  dateObj.text[0:11].strip(),
                    'link' : detailsLink,
                    'sinopseFull': fullSinopse.text})
                
    return jsonify({'filmes': data})  

@app.route('/api/v1/filmes/<page_id>', methods=['GET'])
def NotasEspectadores(page_id):
    URL = "http://www.adorocinema.com/filmes/todos-filmes/notas-espectadores/?page={}".format(page_id)
    
    html_doc = urlopen(URL).read()
    soup = BeautifulSoup(html_doc, "html.parser")
    data = []
    for dataBox in soup.find_all("div", class_="data_box"):
        titleObj = dataBox.find("a", class_="no_underline")
        imgObj = dataBox.find(class_="img_side_content").find_all(class_="acLnk")[0]
        sinopseObj = dataBox.find("div", class_="content").find_all("p")[0]
        dateObj = dataBox.find("div", class_="content").find("div", class_="oflow_a")
        movieLinkObj = dataBox.find(class_="img_side_content").find_all("a")[0]
        generoObj = dataBox.find("div", class_="content").find_all('li')[3].find('div',class_="oflow_a")
        detailsLink = 'http://www.adorocinema.com' + movieLinkObj.attrs['href']

        #LOAD FULL SINOPSE 
        htmldocMovieDetail = urlopen(detailsLink).read()
        soupMovieDetail = BeautifulSoup(htmldocMovieDetail, "html.parser")
        fullSinopse = soupMovieDetail.find(class_="content-txt")        
        fullImgObj = soupMovieDetail.find("meta",  property="og:image")   

        data.append({'titulo': titleObj.text.strip(),
                    'genero': generoObj.text.replace('\n','').strip(),
                    'poster' : fullImgObj["content"], 
                    'sinopse' : sinopseObj.text.strip(),
                    'data' :  dateObj.text[0:11].strip(),
                    'link' : detailsLink,
                    'sinopseFull': fullSinopse.text})
                
    return jsonify({'filmes': data})    

@app.route('/api/v1/filmes/emcartaz', methods=['GET'])
def EmCartaz():
    html_doc = urlopen("http://www.adorocinema.com/filmes/mais-recentes/").read()
    soup = BeautifulSoup(html_doc, "html.parser")
    

    data = []
    for dataBox in soup.find_all("div", class_="card entity-card entity-card-list cf"):
        nomeObj = dataBox.find("h2", class_="meta-title")
        imgObj = dataBox.find(class_="thumbnail ")
        sinopseObj = dataBox.find("div", class_="synopsis")
        dataObj = dataBox.find(class_="meta-body").find(class_="meta-body-item meta-body-info")
        movieLinkObj = dataBox.find(class_="meta-title-link")
        # detailsLink = 'http://www.adorocinema.com' + movieLinkObj.attrs['href']

        #LOAD FULL SINOPSE 
        # htmldocMovieDetail = urlopen(detailsLink).read()
        # soupMovieDetail = BeautifulSoup(htmldocMovieDetail, "html.parser")
        # fullSinopse = soupMovieDetail.find(class_="content-txt")        

        data.append({   'nome': nomeObj.text.strip(),
                        'poster' : imgObj.img['src'].strip(),
                        'sinopse' : sinopseObj.text.strip(),
                        'data' :  dataObj.text[1:23].strip().replace('/',' '),
                        # 'link' : detailsLink,
                        # 'sinopseFull': fullSinopse.text
                    })
                
    return jsonify({'filmes': data})
    
@app.route('/api/v1/filmes/<page_id>')
def filmes_api_page(page_id):
    
    if int(page_id) > 6:
        return redirect("http://python--bergpb.c9users.io/api/v1/filmes", code=200)
        
    else:
        url = "http://www.adorocinema.com/filmes/numero-cinemas/?page={}".format(page_id)
        
        html_doc = urlopen(url).read()
        soup = BeautifulSoup(html_doc, "html.parser")
    
        data = []
        for dataBox in soup.find_all("div", class_="card card-entity card-entity-list cf"):
            nomeObj = dataBox.find("h2", class_="meta-title")
            imgObj = dataBox.find(class_="thumbnail ")
            sinopseObj = dataBox.find("div", class_="synopsis")
            dataObj = dataBox.find(class_="meta-body").find(class_="meta-body-item meta-body-info")
    
            data.append({   'nome': nomeObj.text.strip(),
                            'poster' : imgObj.img['data-src'].strip(),
                            'sinopse' : sinopseObj.text.strip(),
                            'data' :  dataObj.text[1:23].strip().replace('/',' ')})
                    
        return jsonify({'filmes': data})

@app.route('/api/v2/filmes', methods=['GET'])
def filmes_api_page2():
    
    data = [
                {
                  "data": "13 de fevereiro de 202", 
                  "nome": "Sonic - O Filme", 
                  "poster": "http://br.web.img2.acsta.net/c_215_290/pictures/19/11/12/13/02/4217574.jpg", 
                  "sinopse": "Sonic, o porco-espinho azul mais famoso do mundo, se junta com os seus amigos para derrotar o terr\u00edvel Doutor Eggman, um cientista louco que planeja dominar o mundo, e o Doutor Robotnik, respons\u00e1vel por aprisionar animais inocentes em rob\u00f4s. A sinopse oficial ainda n\u00e3o foi divulgada.Classifica\u00e7\u00e3o indicativa a definir por ..."
                }, 
                {
                  "data": "13 de fevereiro de 202", 
                  "nome": "Antologia da Cidade Fantasma", 
                  "poster": "http://br.web.img3.acsta.net/c_215_290/pictures/19/01/11/22/15/4829804.jpg", 
                  "sinopse": "Em uma pequena e distante cidade do interior do Canad\u00e1, um homem morre em um acidente de carro sob circunst\u00e2ncias misteriosas. Enquanto os poucos habitantes do local permanecem relutantes em debater as poss\u00edveis causas da trag\u00e9dia, a fam\u00edlia do falecido e o prefeito Smallwood come\u00e7am a perceber estranhos e at\u00edpicos eventos que mudam suas ..."
                }, 
                {
                  "data": "13 de fevereiro de 202", 
                  "nome": "Inaudito", 
                  "poster": "data:image/gif;base64,R0lGODlhAwAEAIAAAAAAAAAAACH5BAEAAAAALAAAAAADAAQAAAIDhI9WADs=", 
                  "sinopse": "Nascido na China, Lanny Gordin fez carreira como m\u00fasico no Brasil, durante as d\u00e9cadas de 60 e 70. Neste per\u00edodo, trabalhou em discos e shows de Gal Costa, Gilberto Gil, Caetano Veloso, Erasmo Carlos, Jards Macal\u00e9 e outros \u00edcones da m\u00fasica poupular brasileira. O ostracismo veio no final da d\u00e9cada de 70, associado ao desenvolvimento de ..."
                }, 
                {
                  "data": "6 de fevereiro de 2020", 
                  "nome": "Aves de Rapina - Arlequina e sua Emancipa\u00e7\u00e3o Fantabulosa", 
                  "poster": "data:image/gif;base64,R0lGODlhAwAEAIAAAAAAAAAAACH5BAEAAAAALAAAAAADAAQAAAIDhI9WADs=", 
                  "sinopse": "Arlequina (Margot Robbie), Can\u00e1rio Negro (Jurnee Smollett-Bell), Ca\u00e7adora (Mary Elizabeth Winstead), Cassandra Cain e a policial\u00a0Ren\u00e9e Montoya (Rosie Perez) formam um grupo inusitado de hero\u00ednas. Quando um perigoso criminoso come\u00e7a a causar destrui\u00e7\u00e3o em Gotham, as cinco mulheres precisam se unir para defender a cidade."
                }, 
                {
                  "data": "6 de fevereiro de 2020", 
                  "nome": "Jojo Rabbit", 
                  "poster": "data:image/gif;base64,R0lGODlhAwAEAIAAAAAAAAAAACH5BAEAAAAALAAAAAADAAQAAAIDhI9WADs=", 
                  "sinopse": "Alemanha, durante a Segunda Guerra Mundial. Jojo (Roman Griffin Davis) \u00e9 um jovem nazista de 10 anos, que trata Adolf Hitler (Taika Waititi) como um amigo pr\u00f3ximo, em sua imagina\u00e7\u00e3o. Seu maior sonho \u00e9 participar da Juventude Hitlerista, um grupo pr\u00f3-nazista composto por outras pessoas que concordam com os seus ideais. Um dia, Jojo descobre ..."
                }, 
                {
                  "data": "6 de fevereiro de 2020", 
                  "nome": "A Chance de Fahim", 
                  "poster": "data:image/gif;base64,R0lGODlhAwAEAIAAAAAAAAAAACH5BAEAAAAALAAAAAADAAQAAAIDhI9WADs=", 
                  "sinopse": "For\u00e7ado a fugir de Bangladesh, sua terra natal, o jovem Fahim (Assad Ahmed) e seu pai deixam o resto da fam\u00edlia e partem para Paris. Ap\u00f3s a sua chegada \u00e0 Fran\u00e7a, eles come\u00e7am uma verdadeira maratona de obst\u00e1culos para obter asilo pol\u00edtico. Gra\u00e7as ao seu talento com xadrez, Fahim conhece Sylvain (G\u00e9rard Depardieu), um dos melhores ..."
                }, 
                {
                  "data": "30 de janeiro de 2020", 
                  "nome": "Bad Boys para Sempre", 
                  "poster": "data:image/gif;base64,R0lGODlhAwAEAIAAAAAAAAAAACH5BAEAAAAALAAAAAADAAQAAAIDhI9WADs=", 
                  "sinopse": "Terceiro epis\u00f3dio das hist\u00f3rias dos policiais Burnett (Martin Lawrence) e Lowrey (Will Smith), que devem encontrar e prender os mais perigosos traficantes de drogas da cidade."
                }, 
                {
                  "data": "30 de janeiro de 2020", 
                  "nome": "Judy - Muito Al\u00e9m do Arco-\u00cdris", 
                  "poster": "data:image/gif;base64,R0lGODlhAwAEAIAAAAAAAAAAACH5BAEAAAAALAAAAAADAAQAAAIDhI9WADs=", 
                  "sinopse": "Inverno de 1968. Com a carreira em baixa, Judy Garland (Ren\u00e9e Zellweger) aceita estrelar uma turn\u00ea em Londres, por mais que tal trabalho a mantenha afastada dos filhos menores. Ao chegar ela enfrenta a solid\u00e3o e os conhecidos problemas com \u00e1lcool e rem\u00e9dios, compensando o que deu errado em sua vida pessoal com a dedica\u00e7\u00e3o no palco."
                }, 
                {
                  "data": "30 de janeiro de 2020", 
                  "nome": "Os \u00d3rf\u00e3os", 
                  "poster": "data:image/gif;base64,R0lGODlhAwAEAIAAAAAAAAAAACH5BAEAAAAALAAAAAADAAQAAAIDhI9WADs=", 
                  "sinopse": "Kate (Mackenzie Davis) \u00e9 uma jovem professora contratada para trabalhar como governanta na mans\u00e3o de uma fam\u00edlia rica. Na casa, localizada em Essex, Londres, vive Flora (Brooklynn Prince) e Miles (Finn Wolfhard), irm\u00e3os \u00f3rf\u00e3os que perderam ambos os pais em um acidente pr\u00f3ximo \u00e0 casa. No entanto, ela logo percebe que no local existem outros ..."
                }, 
                {
                  "data": "30 de janeiro de 2020", 
                  "nome": "Testemunha Invis\u00edvel", 
                  "poster": "data:image/gif;base64,R0lGODlhAwAEAIAAAAAAAAAAACH5BAEAAAAALAAAAAADAAQAAAIDhI9WADs=", 
                  "sinopse": "Adriano Doria (Riccardo Scamarcio) \u00e9 o empres\u00e1rio do ano em Mil\u00e3o. Ele dirige uma BMW, usa um Rolex extravagante, tem uma ador\u00e1vel esposa e filha e, tamb\u00e9m, uma bela amante. Mas agora ele est\u00e1 em pris\u00e3o domiciliar, acusado de assassinato ap\u00f3s ser flagrado em um quarto de hotel com a amante morta, cujo corpo estava coberto de dinheiro."
                }, 
                {
                  "data": "23 de janeiro de 2020", 
                  "nome": "1917", 
                  "poster": "data:image/gif;base64,R0lGODlhAwAEAIAAAAAAAAAAACH5BAEAAAAALAAAAAADAAQAAAIDhI9WADs=", 
                  "sinopse": "Os cabos Schofield (George MacKay) e Blake (Dean-Charles Chapman) s\u00e3o jovens soldados brit\u00e2nicos durante a Primeira Guerra Mundial. Quando eles s\u00e3o encarregados de uma miss\u00e3o aparentemente imposs\u00edvel, os dois precisam atravessar territ\u00f3rio inimigo, lutando contra o tempo, para entregar uma mensagem que pode salvar cerca de 1600 colegas de batalh\u00e3o."
                }, 
                {
                  "data": "23 de janeiro de 2020", 
                  "nome": "Um Espi\u00e3o Animal", 
                  "poster": "data:image/gif;base64,R0lGODlhAwAEAIAAAAAAAAAAACH5BAEAAAAALAAAAAADAAQAAAIDhI9WADs=", 
                  "sinopse": "Lance Sterling (voz de Will Smith/L\u00e1zaro Ramos) \u00e9 o melhor espi\u00e3o do mundo. Elegante, atraente e sofisticado, ele \u00e9 convencido pelo\u00a0inventor\u00a0Walter\u00a0Beccket (voz de Tom Holland)\u00a0a tomar uma po\u00e7\u00e3o que o deixar\u00e1 \"invis\u00edvel\" aos inimigos. Por\u00e9m, ele acaba sendo transformado em um pombo. Diante do evento inesperado, ele precisar\u00e1 unir com ..."
                }, 
                {
                  "data": "23 de janeiro de 2020", 
                  "nome": "Um Lindo Dia na Vizinhan\u00e7a", 
                  "poster": "data:image/gif;base64,R0lGODlhAwAEAIAAAAAAAAAAACH5BAEAAAAALAAAAAADAAQAAAIDhI9WADs=", 
                  "sinopse": "Fred Rogers (Tom Hanks) foi o criador do Mister Rogers' Neighborhood, um programa infantil de TV muito popular na d\u00e9cada de 1960, nos Estados Unidos. Em 1998, Tom Junod (Matthew Rhys), at\u00e9 ent\u00e3o um c\u00ednico jornalista investigativo, aceitou escrever o perfil de Rogers para a revista Esquire. Durante as entrevistas para a materia, Junod mudou n\u00e3o ..."
                }, 
                {
                  "data": "23 de janeiro de 2020", 
                  "nome": "O Melhor Ver\u00e3o das Nossas Vidas", 
                  "poster": "data:image/gif;base64,R0lGODlhAwAEAIAAAAAAAAAAACH5BAEAAAAALAAAAAADAAQAAAIDhI9WADs=", 
                  "sinopse": "Tr\u00eas melhores amigas s\u00e3o aprovadas para participar da final de um famoso festival de m\u00fasica. Por\u00e9m, elas descobrem que est\u00e3o de recupera\u00e7\u00e3o na escola e precisam arranjar uma maneira de comparecer ao evento em Guaruj\u00e1 sem que seus pais descubram."
                }, 
                {
                  "data": "23 de janeiro de 2020", 
                  "nome": "O Filme do Bruno Aleixo", 
                  "poster": "data:image/gif;base64,R0lGODlhAwAEAIAAAAAAAAAAACH5BAEAAAAALAAAAAADAAQAAAIDhI9WADs=", 
                  "sinopse": "Bruno Aleixo \u00e9 alguma coisa entre um cachorro e um urso de pel\u00facia. O personagem de anima\u00e7\u00e3o portugu\u00eas que ganhou fama por uma web-s\u00e9rie de com\u00e9dia chamada 'Os Conselhos que Vos Deixo' ganha seu pr\u00f3prio filme. Na obra c\u00f4mica, ao decidir criar a pr\u00f3pria autobiografia, Bruno procura inspira\u00e7\u00e3o entre amigos para escrever o texto."
                }
              ]
    return jsonify({'filmes': data})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 443))
    app.run(debug=True, host='0.0.0.0', port=port)
