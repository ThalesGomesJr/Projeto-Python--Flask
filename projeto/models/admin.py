from projeto import db

class Admin(db.Model):
    __tablename__ = 'administrador'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    usuario = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)


    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)


    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    