from app import app, db, Question, Option, quiz_data

def load_questions():
    with app.app_context():
        # Clear existing data
        Option.query.delete()
        Question.query.delete()
        db.session.commit()

        # Add new questions and options
        for item in quiz_data:
            # Create question
            question = Question(text=item["question"])
            db.session.add(question)
            db.session.flush()  # To get the question ID

            # Create options
            for i, option_text in enumerate(item["options"]):
                is_correct = option_text == item["answer"]
                option = Option(
                    text=option_text,
                    question_id=question.id,
                    is_correct=is_correct
                )
                db.session.add(option)
                
                # If this is the correct answer, update the question
                if is_correct:
                    question.correct_option_id = option.id

            db.session.commit()

if __name__ == "__main__":
    print("Loading questions into database...")
    load_questions()
    print("Questions loaded successfully!")
