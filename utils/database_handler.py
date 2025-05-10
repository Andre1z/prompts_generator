import sqlite3

try:
    import pymysql
except ImportError:
    pymysql = None

def analyze_sqlite_database(db_path):
    """Analiza una base de datos SQLite y devuelve su estructura (tablas y columnas)."""
    db_details = f"SQLite Database: {db_path}\n"
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        table_details = []
        for table in tables:
            table_name = table[0]
            table_details.append(f"    Table: {table_name}")
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            for col in columns:
                table_details.append(f"        Column: {col[1]} ({col[2]})")
        conn.close()
        db_details += "\n".join(table_details)
    except Exception as e:
        db_details += f"\n    Error leyendo la base de datos SQLite: {e}"
    return db_details

def analyze_mysql_database(server, user, password, database):
    """Analiza una base de datos MySQL y devuelve su estructura (tablas y columnas)."""
    db_details = f"MySQL Database on {server} - {database}\n"
    if pymysql is None:
        return db_details + "    pymysql no está instalado."
    try:
        conn = pymysql.connect(host=server, user=user, password=password, database=database)
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        table_details = []
        for table in tables:
            table_name = table[0]
            table_details.append(f"    Table: {table_name}")
            cursor.execute(f"SHOW COLUMNS FROM {table_name};")
            columns = cursor.fetchall()
            for col in columns:
                table_details.append(f"        Column: {col[0]} ({col[1]})")
        conn.close()
        db_details += "\n".join(table_details)
    except Exception as e:
        db_details += f"\n    Error conectando/leyendo la base de datos MySQL: {e}"
    return db_details

# Ejemplo de uso
if __name__ == "__main__":
    sqlite_db_path = "example.sqlite"
    print(analyze_sqlite_database(sqlite_db_path))

    if pymysql:
        mysql_config = {"server": "localhost", "user": "root", "password": "", "database": "test_db"}
        print(analyze_mysql_database(**mysql_config))