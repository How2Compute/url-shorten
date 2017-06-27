from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import uuid

app = Flask(__name__)

# Grab the environment variables contianing PostgreSQL details & store them in a dict
PostgresLogin = {
        'username': os.getenv('DB_USER', 'postgres'),
        'password': os.getenv('DB_PASS', 'raspberry'),
        'host': os.getenv('DB_HOST', '127.0.0.1'),
        'port': os.getenv('DB_PORT', '5432'),
        'db': os.getenv('DB_DB', 'url_short')
        }

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(username)s:%(password)s@%(host)s:%(port)s/%(db)s' % PostgresLogin
db.init_app(app)

class ShortenedUrl(db.Model):
    """Stores a shortened URL"""
    __tablename__ = 'urls'
    
    # Default constructor
    def __init__(self, short_code, full_url):
        self.short_code = short_code
        self.full_url = full_url

    id = db.Column(db.Integer, primary_key=True)
    short_code = db.Column(db.Text)
    full_url = db.Column(db.Text)

@app.route("/")
def index():
    results = ShortenedUrl.query.all()
    # Debug log all the records in the database
    for result in results:
        print("ID: {}\nSHORT CODE: {}\nURL: {}".format(result.id, result.short_code, result.full_url))

    return render_template('index.html')

@app.route('/', methods=['POST', 'PUT'])
def shortenUrl():
    # Attempt to generate a unique id (really low chance of collisions, so don't care about the odd error). TODO check out namespaces
    shortCode = str(uuid.uuid4()).replace('-', '')
    # Create a new shortened url
    short = ShortenedUrl(shortCode, request.form.get('url', 'https://localhost'))
    db.session.add(short)
    db.session.commit()

#    except:
#        return "An error occured while shortening your URL! Please try again later."
