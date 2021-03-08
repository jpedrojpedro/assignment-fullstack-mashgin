import peewee as pw
from flask import Flask


app = Flask(__name__)
db = pw.SqliteDatabase(
    'data/app.db',
    pragmas={
        'journal_mode': 'wal',
        'cache_size': -1024 * 64
    }
)
