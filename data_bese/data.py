import sqlite3 as sql

boglash = sql.connect("databese.db")

malumot  = boglash.cursor()

malumot.execute("""
    CREATE TABLE IF NOT EXISTS Odam(
    ism TEXT,
    fam TEXT,
    yosh INTEGER
    )
""")