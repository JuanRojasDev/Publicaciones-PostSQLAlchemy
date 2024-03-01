from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class publicaciones(db.Model):
    # __tablename__ = 'publicaciones'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    category = db.Column(db.Text)
    images = db.Column(db.ARRAY(db.Text))
    videos = db.Column(db.ARRAY(db.Text))
    owner = db.Column(db.Integer)
    created_at = db.Column(db.Date)
    update_at = db.Column(db.Date)
    
    def __init__(self, title, content, category, images, videos, owner, created_at, update_at=None):
        self.title = title
        self.content = content
        self.category = category
        self.images = images
        self.videos = videos
        self.owner = owner
        self.created_at = created_at
        self.update_at = update_at

    def __repr__(self):
        return f'<Publi {self.title}>'
