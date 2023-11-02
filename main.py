from flask import Flask, render_template, request, make_response, flash
from flask.helpers import redirect
from lastfm import getDadosFromLastfm, getrecenttrack, gettoptracks, getInfo
from medium import getDadosFromMedium
from projetos import getProjetos, getLastProjeto, addProjeto
import datetime as dt
from Dica import Dica
from Thought import Thought
from thought import addThought, getThought
from recomendation import getRecomendacoes, addRecomendacoes
from Projeto import Projeto
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__,template_folder='templates',   static_folder='static')
app.secret_key = 'dunno'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Pensamento(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  texto = db.Column(db.String(500), nullable=False)
  time = db.Column(db.DateTime, default=dt.datetime.utcnow,nullable=False)
  def __repr__(self):
    return '<Pensamento {}>'.format(self.texto)




@app.route("/")
@app.route("/home")
def index():
  song = getrecenttrack()  
  hour = (dt.datetime.now().hour)  
  hour = hour + 24 - 3 if hour - 3 < 0 else hour - 3
  artigo = getDadosFromMedium()  
  artistaSemana = getDadosFromLastfm('7day ')
  toptrack = gettoptracks()
  scrobbles = getInfo()  
  projeto = getLastProjeto()
  return render_template('index.html', song=song, hour=hour, artigo=artigo, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack, projeto=projeto)


@app.route("/aboutme")
def aboutme():
  song = getrecenttrack()
  favorito = getDadosFromLastfm()
  musica =   gettoptracks()    
  artistaSemana = getDadosFromLastfm('7day ')
  toptrack = gettoptracks()
  scrobbles = getInfo()  
  return render_template('aboutme.html', song=song, favorito=favorito, musica=musica, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack)

@app.route("/recomendacoes")
def recomendacoes():
  song = getrecenttrack()   
  artistaSemana = getDadosFromLastfm('7day ')
  toptrack = gettoptracks()
  scrobbles = getInfo()  
  addRecomendacoes(Dica('https://altabooks.com.br/produto/use-a-cabeca-c-2/', 'Recomendo Use a cabeça! C, com ele entendi sobre ponteiros e ainda vi sobre sockets', 'https://altabooks.com.br/wp-content/uploads/2021/07/Use_a_Cabeca_C.jpg', "LIVRO"))
  addRecomendacoes(Dica('https://www.amazon.com.br/Desenvolvimento-Web-com-Flask-Desenvolvendo/dp/8575226819', 'Graças a esse livro consegui ter uma base melhor sobre Flask para fazer esse site.', 'https://th.bing.com/th/id/OIP.UdJJOPDmekiiYHOzd5l7xwHaJt?w=194&h=255&c=7&r=0&o=5&pid=1.7', 'LIVRO'))
  addRecomendacoes(Dica('https://www.youtube.com/@TsodingDaily', 'Esse cara faz coisas incríveis com C e outras linguagens de baixo nível, vale a pena dar uma olhada.', 'https://yt3.googleusercontent.com/cZljVId4IP-aLqPRcHrhh0XrZERakcfUkYZQs0nh8e71evPy3IZEuvcl9YZLaAENAevkq9On=s176-c-k-c0x00ffffff-no-rj', 'CANAL'))
  addRecomendacoes(Dica('https://www.amazon.com.br/C-completo-total-Herbert-Schildt/dp/8534605955', 'Como o nome já diz, C: Completo e Total, é um ótimo livro para ter uma base sólida sobre a linguagem C.', "https://th.bing.com/th/id/R.f1f6d0183e57a40dc27a712400da4961?rik=CIudeoM7Zlkwdw&riu=http%3a%2f%2f1.bp.blogspot.com%2f-qyK6qMrgR4g%2fUa9cWhg2k9I%2fAAAAAAAAAP4%2fJnLPIgQSiyc%2fs1600%2fc.jpg&ehk=wXKRn0tzztGyqGmJv5psOJhkT%2bXFbDjADEdTHQ5Njv8%3d&risl=&pid=ImgRaw&r=0","LIVRO"))
  data = getRecomendacoes()
  return  render_template('recomendacoes.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack, data=data)

@app.route("/recomendacoes/add/<password>")
def recomendacoesAdd(password):  
  song = getrecenttrack()   
  artistaSemana = getDadosFromLastfm('7day ')
  toptrack = gettoptracks()
  scrobbles = getInfo()  
  if(password != 'rottenapple'):
      return render_template('404.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack)
  else:    
      return render_template('addRecomendacoes.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack)

@app.route("/recomendacoes/addRecomendacoes", methods=['POST'])
def Addrecomendacoes():
  texto = request.form['texto']
  tipo = request.form['tipo']
  image_url = request.form['image_url']
  url = request.form['url']
  password = request.form['password']
  if(password == "4l!ce1nch4!ns"):
    addRecomendacoes(Dica(url, texto, image_url, tipo))
    flash('Recomendação adicionado com sucesso')
  else:
    flash('Senha incorreta')
  return redirect('/recomendacoes')

@app.route("/thoughts")
def thoughts():
  song = getrecenttrack()   
  artistaSemana = getDadosFromLastfm('7day ')
  toptrack = gettoptracks()
  scrobbles = getInfo()  
  data = getThought()
  return render_template("thoughts.html", song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack, data=data)

@app.route("/thoughts/add/<password>")
def thoughtAdd(password):  
  song = getrecenttrack()   
  artistaSemana = getDadosFromLastfm('7day ')
  toptrack = gettoptracks()
  scrobbles = getInfo()  
  if(password != "swlabr"):
    return render_template('404.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack)
  else:    
    return render_template('addThought.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack)


@app.route("/thoughts/addthoughts", methods=['POST'])
def Addthought():
  texto = request.form['texto']
  password = request.form['password']
  if(password == "SheWalksLikeABeardedRainbow"):
    addThought(Thought(texto, dt.datetime.now().strftime("%c")))
    flash('Pensamento adicionado com sucesso')
  else:
    flash('Senha incorreta')
  return redirect('/thoughts')
  
@app.route("/projetos")
def projetos():
  song = getrecenttrack()   
  artistaSemana = getDadosFromLastfm('7day ')
  toptrack = gettoptracks()
  scrobbles = getInfo()  
  projetos = getProjetos()
  return render_template('projetos.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack, projetos=projetos)

@app.route("/projetos/add/<password>")
def projetoAdd(password):  
  song = getrecenttrack()   
  artistaSemana = getDadosFromLastfm('7day ')
  toptrack = gettoptracks()
  scrobbles = getInfo()  
  if(password != 'dunno'):
      return render_template('404.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack)
  else:    
      return render_template('addProjetos.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack)

@app.route("/projetos/addProjetos", methods=['POST'])
def addProjetos():
  titulo = request.form['titulo']
  link = request.form['link']
  password = request.form['password']
  if(password == "SheWalksLikeABeardedRainbow"):
    addProjeto(Projeto(titulo,link))
    flash('Projeto adicionado com sucesso')
  else:
    flash('Senha incorreta')
  return redirect('/projetos')
  
@app.route("/contato")
def contato():  
  song = getrecenttrack()   
  artistaSemana = getDadosFromLastfm('7day ')
  toptrack = gettoptracks()
  scrobbles = getInfo()  
  return render_template('contato.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack)
  

@app.errorhandler(404)
def page_not_found(e):
  song = getrecenttrack()   
  artistaSemana = getDadosFromLastfm('7day ')
  toptrack = gettoptracks()
  scrobbles = getInfo()    
  return render_template('404.html', song=song, scrobbles=scrobbles, artistaSemana=artistaSemana, toptrack=toptrack), 404

  
if __name__ == '__main__':
  app.run("0.0.0.0",8080)
  