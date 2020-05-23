from db import get_db

class Current():
    def __init__(self,mood):
        self.mood = mood

    #This means you can put a function inside a class 
    #but you can't access the instance of that class (this is useful when your method does not use the instance).
    @staticmethod
    def get():
        db = get_db()
        current = db.execute('SELECT mood FROM current ORDER BY id DESC LIMIT 3').fetchall()
        return current
    
    @staticmethod
    def create(mood,hour):
        db = get_db()
        db.execute(
            "INSERT INTO current (mood, hour) "
            "VALUES (?,?)",
            (mood,hour),
        )
        db.commit()
    
    @staticmethod
    def delete():
        db = get_db()
        db.execute("DELETE FROM current")
        db.commit()
    
