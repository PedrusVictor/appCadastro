from flask_sqlalchemy import SQLAlchemy
from app import db
class Luta(db.Model):
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

    def __init__(self,player1pers1,player1pers2,player1pers3,player1pers4,player1pet,player1pb,
    player2pers1,player2pers2,player2pers3,player2pers4,player2pers5,player2pers6,player2pers7,player2pers8,player2pet,player2pet2,player2pb,resultado):
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
        self.player2pb=player2pb
        self.resultado=resultado
        
    def __rep__(self):
        return "<Luta{}>".format(self.resultado)