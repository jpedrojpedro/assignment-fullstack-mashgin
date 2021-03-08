from init import app
import views
import models


if __name__ == '__main__':
    print("Creating tables")
    models.create_tables()
    print("Populating database")
    models.populate_database()
    app.run(host='0.0.0.0')
