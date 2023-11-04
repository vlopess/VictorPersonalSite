import pathlib
import sys
from flask import Flask, render_template, request, make_response, flash
from flask.helpers import redirect
from models.Dica import Dica
from services.Cryptografy import Crypt
from services.lastfm import LastFmController
from services.medium import getDadosFromMedium
from services.password import PasswordController
from services.projetos import ProjetosController
import datetime as dt
from models.Thought import Thought
from services.thought import ThougthController
from services.recomendation import RecomendacoesController
from models.Projeto import Projeto
from run import app



@app.route("/")
@app.route("/home")
def index():
  try:
    song = LastFmController.getrecenttrack()  
    hour = (dt.datetime.now().hour)  
    artigo = getDadosFromMedium()  
    artistaSemana = LastFmController.getDadosFromLastfm('7day ')
    toptrack = LastFmController.gettoptracks()
    scrobbles = LastFmController.getInfo()  
    projeto = ProjetosController.getLastProjeto()
    return render_template('index.html', song=song, hour=hour, artigo=artigo, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack, projeto=projeto)
  except Exception as exception:
    return redirect('/500')


@app.route("/aboutme")
def aboutme():
  try:
    song = LastFmController.getrecenttrack()
    favorito = LastFmController.getDadosFromLastfm()
    musica =   LastFmController.gettoptracks()    
    artistaSemana = LastFmController.getDadosFromLastfm('7day ')
    toptrack = LastFmController.gettoptracks()
    scrobbles = LastFmController.getInfo()  
    return render_template('aboutme.html', song=song, favorito=favorito, musica=musica, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack)
  except Exception as exception:
    return redirect('/500')

@app.route("/recomendacoes")
def recomendacoes():
  try:
    song = LastFmController.getrecenttrack()   
    artistaSemana = LastFmController.getDadosFromLastfm('7day ')
    toptrack = LastFmController.gettoptracks()
    scrobbles = LastFmController.getInfo()  
    data = RecomendacoesController.getRecomendacoes()
    return  render_template('recomendacoes.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack, data=data)
  except Exception as exception:
    return redirect('/500')

@app.route("/recomendacoes/add/<password>")
def recomendacoesAdd(password):  
  try:
    song = LastFmController.getrecenttrack()   
    artistaSemana = LastFmController.getDadosFromLastfm('7day ')
    toptrack = LastFmController.gettoptracks()
    scrobbles = LastFmController.getInfo()  
    if(password != 'rottenapple'):
        return render_template('404.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack)
    else:    
        return render_template('addRecomendacoes.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack)
  except Exception as exception:
    return redirect('/500')

@app.route("/recomendacoes/addRecomendacoes", methods=['POST'])
def Addrecomendacoes():
  try:
    texto = request.form['texto']
    tipo = request.form['tipo']
    image_url = request.form['image_url']
    url = request.form['url']
    password = request.form['password']    
    crypt = Crypt()
    decrypt = senha.map['Recomendation']
    passwordcorrect = crypt.decrypt(enc_str=decrypt)
    if(password == passwordcorrect):
      RecomendacoesController.addRecomendacoes(Dica(url, texto, image_url, tipo))
      flash('Recomendação adicionada com sucesso')
    else:
      flash('Senha incorreta')
    return redirect('/recomendacoes')
  except Exception as exception:
    return redirect('/500')

@app.route("/thoughts")
def thoughts():
  try:
    song = LastFmController.getrecenttrack()   
    artistaSemana = LastFmController.getDadosFromLastfm('7day ')
    toptrack = LastFmController.gettoptracks()
    scrobbles = LastFmController.getInfo()  
    data = ThougthController.getThought()
    return render_template("thoughts.html", song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack, data=data)
  except Exception as exception:
    return redirect('/500')
  

@app.route("/thoughts/add/<password>")
def thoughtAdd(password):  
  try:
    song = LastFmController.getrecenttrack()   
    artistaSemana = LastFmController.getDadosFromLastfm('7day ')
    toptrack = LastFmController.gettoptracks()
    scrobbles = LastFmController.getInfo()  
    if(password != "swlabr"):
      return render_template('404.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack)
    else:    
      return render_template('addThought.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack)
  except Exception as exception:
    return redirect('/500')


@app.route("/thoughts/addthoughts", methods=['POST'])
def Addthought():
  try:
    texto = request.form['texto']
    password = request.form['password']
    crypt = Crypt()
    passwordcorrect = crypt.decrypt(enc_str=senha.map['Thought'])
    if(password == passwordcorrect):
      ThougthController.addThought(Thought(texto, dt.datetime.now().strftime("%c")))
      flash('Pensamento adicionado com sucesso')
    else:
      flash('Senha incorreta')
    return redirect('/thoughts')
  except Exception as exception:
    return redirect('/500')
  
@app.route("/projetos")
def projetos():
  try:
    song = LastFmController.getrecenttrack()   
    artistaSemana = LastFmController.getDadosFromLastfm('7day ')
    toptrack = LastFmController.gettoptracks()
    scrobbles = LastFmController.getInfo()  
    projetos = ProjetosController.getProjetos()
    return render_template('projetos.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack, projetos=projetos)
  except Exception as exception:
    return redirect('/500')

@app.route("/projetos/add/<password>")
def projetoAdd(password):  
  try:
    song = LastFmController.getrecenttrack()   
    artistaSemana = LastFmController.getDadosFromLastfm('7day ')
    toptrack = LastFmController.gettoptracks()
    scrobbles = LastFmController.getInfo()  
    if(password != 'dunno'):
        return render_template('404.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack)
    else:    
        return render_template('addProjetos.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack)
  except Exception as exception:
    return redirect('/500')

@app.route("/projetos/addProjetos", methods=['POST'])
def addProjetos():
  try:
    titulo = request.form['titulo']
    link = request.form['link']
    password = request.form['password']
    crypt = Crypt()
    passwordcorrect = crypt.decrypt(enc_str=senha.map['Projeto'])
    if(password == passwordcorrect):
      ProjetosController.addProjeto(Projeto(titulo,link))
      flash('Projeto adicionado com sucesso')
    else:
      flash('Senha incorreta')
    return redirect('/projetos')
  except Exception as exception:
    return redirect('/500')
  
@app.route("/contato")
def contato():  
  try:
    song = LastFmController.getrecenttrack()   
    artistaSemana = LastFmController.getDadosFromLastfm('7day ')
    toptrack = LastFmController.gettoptracks()
    scrobbles = LastFmController.getInfo()  
    return render_template('contato.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack)
  except Exception as exception:
    return redirect('/500')
  

@app.errorhandler(404)
def page_not_found(e):
    song = LastFmController.getrecenttrack()   
    artistaSemana = LastFmController.getDadosFromLastfm('7day ')
    toptrack = LastFmController.gettoptracks()
    scrobbles = LastFmController.getInfo()    
    return render_template('404.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack), 404

@app.route("/500")
@app.errorhandler(500)
def error():
  song = LastFmController.getrecenttrack()   
  artistaSemana = LastFmController.getDadosFromLastfm('7day ')
  toptrack = LastFmController.gettoptracks()
  scrobbles = LastFmController.getInfo()    
  return render_template('500.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack), 500


if __name__ == '__main__':
  senha = PasswordController()
  app.run("0.0.0.0",8080, debug=True)
  
