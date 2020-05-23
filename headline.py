from db import get_db

class Headline():
    def __init__(self, headline):
        self.headline = headline

    #This means you can put a function inside a class 
    #but you can't access the instance of that class (this is useful when your method does not use the instance).
    @staticmethod
    def get():
        db = get_db()
        headlines = db.execute("SELECT * FROM headlines").fetchall()            
        return headlines

    @staticmethod
    def create(headline):
        db = get_db()
        db.execute(
            "INSERT INTO headlines (headline) "
            "VALUES (?)",
            (headline),
        )
        db.commit()
    
    @staticmethod
    def delete():
        db = get_db()
        db.execute("DELETE FROM headlines")
        db.commit()
    
