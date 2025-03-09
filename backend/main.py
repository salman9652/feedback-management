from fastapi import FastAPI
from pydantic import BaseModel
import pymysql

app = FastAPI()

# Database Connection
db = pymysql.connect(host="db", user="root", password="password", database="feedback_db")
cursor = db.cursor()

class Feedback(BaseModel):
    name: str
    email: str
    rating: int
    comments: str

@app.post("/feedback")
def submit_feedback(feedback: Feedback):
    sql = "INSERT INTO feedback (name, email, rating, comments) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (feedback.name, feedback.email, feedback.rating, feedback.comments))
    db.commit()
    return {"message": "Feedback submitted successfully"}

@app.get("/feedback")
def get_feedback():
    cursor.execute("SELECT * FROM feedback")
    return cursor.fetchall()
