import sqlite3
import psycopg2

import click
from flask import current_app, g
from flask.cli import with_appcontext

#DATABASE_URL = 'postgresql+psycopg2://wkgfzugsoqiodi:069315c61275af8149802e0a8431883970eae396e0b0f59127ee4e781bde7505@ec2-54-246-87-132.eu-west-1.compute.amazonaws.com:5432/d655c1e7ookde1'


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            "mood_db", detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))

@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

