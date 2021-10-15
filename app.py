from flask import Flask,request,render_template,redirect,json,url_for
from flask.globals import session
from flask_sqlalchemy import SQLAlchemy

from util.utils import buscaricones
import secrets
from modelopreview import BuscTime
secret_key=secrets.token_hex(12)
app=Flask(__name__)

app.config["SECRET_KEY"]=secret_key
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db=SQLAlchemy(app)
import os
preview=BuscTime.Time()

class Luta(db.Model):
    __tablename__="appflaskSqlAlchemy"
    id=db.Column(db.Integer, primary_key=True)
    player1pers1=db.Column(db.String(80), nullable=False)
    player1pers2=db.Column(db.String(80), nullable=False)
    player1pers3=db.Column(db.String(80), nullable=False)
    player1pers4=db.Column(db.String(80), nullable=False)
    player1pet=db.Column(db.String(80), nullable=False)
    player1pb=db.Column(db.Integer,nullable=False)
    player2pers1=db.Column(db.String(80), nullable=False)
    player2pers2=db.Column(db.String(80), nullable=False)
    player2pers3=db.Column(db.String(80), nullable=False)
    player2pers4=db.Column(db.String(80), nullable=False)
    player2pers5=db.Column(db.String(80), nullable=False)
    player2pers6=db.Column(db.String(80), nullable=False)
    player2pers7=db.Column(db.String(80), nullable=False)
    player2pers8=db.Column(db.String(80), nullable=False)
    player2pet=db.Column(db.String(80), nullable=False)
    player2pet2=db.Column(db.String(80), nullable=False)
    player2ban1=db.Column(db.String(80), nullable=False)
    player2ban2=db.Column(db.String(80), nullable=False)
    player2pb=db.Column(db.Integer,nullable=False)
    resultado=db.Column(db.String(2), nullable=False)

    def __init__(self,player1pers1,player1pers2,player1pers3,player1pers4,player1pet,player1pb,player2pers1,player2pers2,player2pers3,player2pers4,player2pers5,player2pers6,player2pers7,player2pers8,player2pet,player2pet2,ban1,ban2,player2pb,resultado):
        self.player1pers1=player1pers1
        self.player1pers2=player1pers2
        self.player1pers3=player1pers3
        self.player1pers4=player1pers4
        self.player1pet=player1pet
        self.player1pb=player1pb
        self.player2pers1=player2pers1
        self.player2pers2=player2pers2
        self.player2pers3=player2pers3
        self.player2pers4=player2pers4
        self.player2pers5=player2pers5
        self.player2pers6=player2pers6
        self.player2pers7=player2pers7
        self.player2pers8=player2pers8
        self.player2pet=player2pet
        self.player2pet2=player2pet2
        self.player2ban1=ban1
        self.player2ban2=ban2
        self.player2pb=player2pb
        self.resultado=resultado
        
    def __rep__(self):
        return "<Luta{}>".format(self.resultado)



@app.route("/")
def index():
    #lista=buscaricones("static/img")
    itensPers=[a for a in os.walk("static/pers")][0][1]
    lista=[buscaricones("static/pers/"+a) for a in itensPers]
    #lista2=buscaricones("static/pets")
    itens=[a for a in os.walk("static/pet")][0][1]
    lista2=[buscaricones("static/pet/"+a) for a in itens]
    return render_template("index.html",lista=lista,lista2=lista2)

@app.route("/comp")
def comp():
    itensPers=[a for a in os.walk("static/pers")][0][1]
    lista=[buscaricones("static/pers/"+a) for a in itensPers]
    itens=[a for a in os.walk("static/pet")][0][1]
    lista2=[buscaricones("static/pet/"+a) for a in itens]
    return render_template("comppage.html",lista=lista,lista2=lista2)

@app.route("/time",methods=["POST"])
def time():
    enemyPers=[request.form["p1"+str(a)] for a in range(10)]
    #banlist=request.form["p110"].split(",")
    #print(banlist)
    
    sugest=(preview.MontarTime(enemyPers) )
    return render_template("sugest.html",time=sugest)
"""@app.route("/sugest",methods=["get"])
def sugest(time):
    
    return render_template("sugest.html",time=time)"""

@app.route("/add", methods=["POST"])
def add():
    
    playerpPers=[request.form["p0"+str(a)] for a in range(5)]
    enemyPers=[request.form["p1"+str(a)] for a in range(10)]
    banlist=request.form["p110"].split(",")
    pb1=request.form["pb1"]
    pb2=request.form["pb2"]
    resultado=request.form["resultado"]
    #print(playerpPers)
    #print(enemyPers)
    #print(banlist)
    cad=Luta(playerpPers[0],playerpPers[1],playerpPers[2],playerpPers[3],playerpPers[4],pb1,enemyPers[0],enemyPers[1],enemyPers[2],enemyPers[3],enemyPers[4],enemyPers[5],enemyPers[6],enemyPers[7],enemyPers[8],enemyPers[9],banlist[0],banlist[1],pb2,resultado
    )
    db.session.add(cad)
    db.session.commit()
    
    return redirect(url_for("index"))

@app.route("/get")
def get():
    data=[{"p1pers1":a.player1pers1,"p1pers2":a.player1pers2,"p1pers3":a.player1pers3,"p1pers4":a.player1pers4,"p1perspet":a.player1pet,
    "p1pb":a.player1pb,"p2pers1":a.player2pers1,"p2pers2":a.player2pers2,"p2pers3":a.player2pers3,"p2pers4":a.player2pers4,"p2pers5":a.player2pers5,"p2pers6":a.player2pers6,"p2pers7":a.player2pers7,"p2pers8":a.player2pers8,"p2pet":a.player2pet,"p2pet2":a.player2pet2,"p2pb":a.player2pb,
    "resultado":a.resultado
    }for a in Luta.query.all()]
    
    return json.dumps(data,ensure_ascii=False).encode("UTF-8")
@app.route("/deleteall")
def delAll():
    data=Luta.query.all()
    for a in data:

        db.session.delete(a)
    db.session.commit()
    return redirect(url_for("index"))
db.init_app(app)
@app.route("/salve")
def getDados():
    import pandas as pd
    data=[{"p1pers1":a.player1pers1,"p1pers2":a.player1pers2,"p1pers3":a.player1pers3,"p1pers4":a.player1pers4,"p1perspet":a.player1pet,
    "p1pb":a.player1pb,"p2pers1":a.player2pers1,"p2pers2":a.player2pers2,"p2pers3":a.player2pers3,"p2pers4":a.player2pers4,"p2pers5":a.player2pers5,"p2pers6":a.player2pers6,"p2pers7":a.player2pers7,"p2pers8":a.player2pers8,"p2pet":a.player2pet,"p2pet2":a.player2pet2,"p2ban":a.player2ban1,"p2ban2":a.player2ban2,"p2pb":a.player2pb,
    "resultado":a.resultado
    }for a in Luta.query.all()]
    dados=pd.DataFrame(data)
    dados.to_csv("dadoEsxtraido.csv")
    return redirect(url_for("index"))
if __name__== "__main__":
    
    app.config['DEBUG'] = True
    
    app.run(port=80)