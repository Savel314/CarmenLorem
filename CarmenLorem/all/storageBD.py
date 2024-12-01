import sqlite3

db_file = 'three_tablets.sqlite'
con = sqlite3.connect(db_file)
all_author = con.execute("""Select * from authors""").fetchall()  # возвращает [(1, 'Rick Astley')]


def get_author_id(author_name):
    cur = con.cursor()
    try:
        cur.execute("SELECT id FROM authors WHERE author = ?", (author_name,))
        result = cur.fetchone()
        if result:
            return result[0]
        else:
            cur.execute("INSERT INTO authors (author) VALUES (?)", (author_name,))
            con.commit()
            cur.execute("SELECT id FROM authors WHERE author = ?", (author_name,))
            result = cur.fetchone()
            return result[0]
    except Exception as e:
        con.rollback()
        print(f"Ошибка при получении или добавлении автора '{author_name}': {e}")
        return None


def sort_nameDB():
    cur = con.cursor()
    try:
        sort_name = cur.execute("""
                        SELECT 
                            f.name, 
                            f.link, 
                            a.author AS authore
                        FROM 
                            _foundation f
                        JOIN 
                            authors a ON f.authore = a.id
                        ORDER BY 
                            f.name ASC
                    """).fetchall()
        # возвращает [('Never Gonna Give You Up', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 1)]
        # """SELECT f.name, f.link, a.author AS authore FROM _foundation f
        #     JOIN authors a ON f.authore = a.id ORDER BY f.name ASC"""
        return sort_name
    except Exception as e:
        print(f"Ошибка при сортировке данных по имени: {e}")
        return None


def sort_authorDB():
    cur = con.cursor()
    try:
        sort_author = cur.execute("""
                        SELECT 
                            f.name, 
                            f.link, 
                            a.author AS authore
                        FROM 
                            _foundation f
                        JOIN 
                            authors a ON f.authore = a.id
                        ORDER BY 
                            a.author ASC
                    """).fetchall()
        return sort_author
    except Exception as e:
        print(f"Ошибка при сортировке данных: {e}")
        return None


def addBD(name, link, author):
    cur = con.cursor()
    try:
        author_id = get_author_id(author)
        cur.execute("""INSERT INTO 
                                    _foundation 
                                    (name, link, authore) 
                                VALUES 
                                    (?, ?, ?)
                                """, (name, link, author_id))
        con.commit()
    except Exception as e:
        con.rollback()
        print(f"Ошибка при добавлении записи с именем '{name}': {e}")


def renameBD(old_name, new_name):
    cur = con.cursor()
    try:
        cur.execute("""UPDATE _foundation SET name = ? WHERE name = ?""", (new_name, old_name))
        con.commit()
    except Exception as e:
        con.rollback()
        print(f"Ошибка при переименовании записи с именем : {e}")


def delBD(name):
    cur = con.cursor()
    try:
        cur.execute("""DELETE FROM 
                                    _foundation 
                                WHERE 
                                    name = ?
                                """, (name,))
        con.commit()
    except Exception as e:
        con.rollback()
        print(f"Ошибка при удалении записи с именем '{name}': {e}")
