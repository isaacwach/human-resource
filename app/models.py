from . import db 



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'



class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255))
    position = db.Column(db.String(5555))
    job_id = db.Column(db.String(255))
    department = db.Column(db.String(255))
    awards = db.Column(db.String(1222))
    experience = db.Column(db.String(2222))


    def save_profile(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_profile(cls,id):
        pitches= Profile.query.filter_by(id=id).all()
        return pitches

    def __repr__(self):
        return f'User {self.name}'




