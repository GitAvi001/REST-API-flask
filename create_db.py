from api import app, db

#will create a database instance
with app.app_context():
    db.create_all()