from projeto import db


class User(db.Model):
    __tablename__ = 'funcionarios'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(86), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    telefone = db.Column(db.String(40), nullable=False)
    cod_registro = db.Column(db.String(40), nullable=False)

    def __init__(self, name, email, telefone, cod_registro):
        self.name = name
        self.email = email
        self.telefone = telefone
        self.cod_registro = cod_registro
        

