import peewee as pw
from flask import Flask


app = Flask(__name__)
db = pw.SqliteDatabase(
    __name__ + '.db',
    pragmas={
        'journal_mode': 'wal',
        'cache_size': -1024 * 64
    }
)
