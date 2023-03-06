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



malumot.execute("""
    CREATE TABLE IF NOT EXISTS Hayvonlar(
    nomi TEXT,
    rangi TEXT,
    yosh INTEGER
    )
""")


malumot.execute("""
    CREATE TABLE IF NOT EXISTS Gulllar(
    nomi TEXT,
    hidi TEXT,
    rangi INTEGER
    )
""")


malumot.execute("""
    CREATE TABLE IF NOT EXISTS Leptop(
    nomi TEXT,
    rangi TEXT,
    yili INTEGER
    )
""")


malumot.execute("""
    CREATE TABLE IF NOT EXISTS Mashina(
    nomi TEXT,
    yili TEXT,
    rangi INTEGER
    )
""")

malumot.execute("""
    CREATE TABLE IF NOT EXISTS Daftar(
    nomi TEXT,
    varaqi INTEGRR,
    rangi TEXT
    )
""")

malumot.execute("""
    CREATE TABLE IF NOT EXISTS Telefon(
    nomi TEXT,
    yili INTEGER,
    rangi TEXT
    )
""")


malumot.execute("""
    CREATE TABLE IF NOT EXISTS Ruchka(
    nomi TEXT,
    shariki TEXT,
    rangi TEXT
    )
""")

malumot.execute("""
    CREATE TABLE IF NOT EXISTS Mishka(
    nomi TEXT,
    ishlashi TEXT,
    rangi TEXT
    )
""")

malumot.execute("""
    CREATE TABLE IF NOT EXISTS Sumka(
    nomi TEXT,
    rangi TEXT,
    yuki INTEGER
    )
""")