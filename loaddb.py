
from app import create_app
from models import Question, Option, User
from extensions import db
from questions import quiz_data

def load_questions():
    with app.app_context():
        # Clear existing data
        Option.query.delete()
        Question.query.delete()
        db.session.commit()

        # Add new questions and options
        questioncorrectid = None
        for item in quiz_data:
            # Create question
            question = Question(text=item["question"])
            if"tech" not in item:
                   print(f"Tech key missing for {item['question']}")
                   item["tech"] = None
                   break
            if item["tech"] == None:
                print(f"Tech is None for {item['question']}")
            question.tech = item["tech"]
            question.correct_option_id=1
            db.session.add(question)
            db.session.flush()  # To get the question ID

            # Create options
            for i, option_text in enumerate(item["options"]):
                is_correct_t = option_text == item["answer"]
                option = Option(
                    text=option_text,
                    question_id=question.id,
                    is_correct=is_correct_t
                )
                db.session.add(option)
                db.session.flush()

                # If this is the correct answer, update the question
                if is_correct_t:
                    #print(f"Correct option for {question.text}: {option.id} {option.text}")
                    questioncorrectid = option.id

            question.correct_option_id = questioncorrectid
            db.session.commit()

def load_admin():
    with app.app_context():
        from werkzeug.security import generate_password_hash
        from datetime import datetime

        # Create admin user
        admin = User(
            username="admin",
            password=generate_password_hash("admin"),
            is_admin=True,
            #date_created=datetime.now()
        )
        db.session.add(admin)
        db.session.commit()

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    print("Loading admin into database...")
    load_admin()
    print("Loading questions into database...")
    load_questions()
    print("Questions loaded successfully!")
