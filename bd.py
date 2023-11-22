import sqlite3

#Variable para la BD y cursor
bd = sqlite3.connect('shop')
cur = bd.cursor()

def table_exist(nametable):
    cur.execute('''SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{}' '''.format(nametable))

    if cur.fetchone()[0] == 1:
        return True
    else:
        cur.execute('''CREATE TABLE {} (ID INTEGER PRIMARY KEY AUTOINCREMENT, ORGANIC INTEGER, GLASS INTEGER, METAL INTEGER, PAPER INTEGER, APPLE INTEGER, BANANA INTEGER, CHERRY INTEGER, BLUEBOTTLE INTEGER, GREENBOTTLE INTEGER, YELLOWBOTTLE INTEGER, BLUECAN INTEGER, PURPLECAN INTEGER, REDCAN INTEGER, BLUEBOOK INTEGER, PURPLEBOOK INTEGER, REDBOOK INTEGER)'''.format(nametable))
        return False

#table_exist('shop')

def insert_data(nametable, organic, glass, metal, paper):
    # Verificar si la tabla ya existe
    if table_exist(nametable):
        # Actualizar los valores existentes en lugar de insertar una nueva fila
        cur.execute(f'''
            UPDATE {nametable}
            SET ORGANIC = ORGANIC + ?,
                GLASS = GLASS + ?,
                METAL = METAL + ?,
                PAPER = PAPER + ?
        ''', (organic, glass, metal, paper))
    else:
        # Si la tabla no existe, crearla y luego insertar los valores
        cur.execute(f'''
            CREATE TABLE {nametable} (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                ORGANIC INTEGER,
                GLASS INTEGER,
                METAL INTEGER,
                PAPER INTEGER,
                APPLE INTEGER,
                BANANA INTEGER,
                CHERRY INTEGER,
                BLUEBOTTLE INTEGER,
                GREENBOTTLE INTEGER,
                YELLOWBOTTLE INTEGER,
                BLUECAN INTEGER,
                PURPLECAN INTEGER,
                REDCAN INTEGER,
                BLUEBOOK INTEGER,
                PURPLEBOOK INTEGER,
                REDBOOK INTEGER
            )
        ''')
        cur.execute(f'''
            INSERT INTO {nametable} (ORGANIC, GLASS, METAL, PAPER)
            VALUES (?, ?, ?, ?)
        ''', (organic, glass, metal, paper))

    bd.commit()

#def insert_data(nametable ,organic, glass, metal, paper):
#    cur.execute('''INSERT INTO {} (ORGANIC, GLASS, METAL, PAPER) VALUES (?, ?, ?, ?)'''.format(nametable), (organic, glass, metal, paper))
#    bd.commit()

def select_data(nametable):
    cur.execute(f'''SELECT * FROM {nametable}''')
    rows = cur.fetchall()

    for row in rows:
        print(row)

def delete_data(nametable, row_id):
    """
    Elimina una fila específica de la tabla.

    :param nametable: Nombre de la tabla.
    :param row_id: ID de la fila que se va a eliminar.
    """
    cur.execute(f'''
        DELETE FROM {nametable}
        WHERE ID = ?
    ''', (row_id,))
    bd.commit()