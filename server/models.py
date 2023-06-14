from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String) 
    # db.CheckConstraint('len(phone_number) == 10')
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self, key, name_string):
        if not name_string:
            raise ValueError("Author must have a name")
    @validates('phone_number')
    def validate_phone_number(self, key, ph_string):
        if len(ph_string) != 10:
            raise ValueError("Phone number must be 10 characters")


    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('content')
    def validate_content(self, key, content_str):
        if len(content_str) < 250:
            raise ValueError("Content must be at least 250 characters")
        
    @validates('summary')
    def validate_summary(self, key, summary_str):
        if len(summary_str) >= 250:
            raise ValueError("Content cannot be over 250 characters")
    
    @validates('category')
    def validates_category(self, key, cat_str):
        if cat_str != 'Fiction' and cat_str != 'Non-Fiction':
            raise ValueError("Category must be either Fiction or Non-fiction")
    
    @validates('title')
    def validates_title(self, key, title_str):
        clickbait = ["Won't Believe","Secret","Top","Guess"]
        if not any(word in title_str for word in clickbait):
            raise ValueError('Title is not clickbaity enough')


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
