import psycopg2

# PostgreSQL への接続情報
DB_HOST = "localhost"
DB_NAME = "mydatabase"
DB_USER = "rikimaru"
DB_PASS = "P4ssW0rd#!"
DB_PORT = "5432"

try:
    # PostgreSQL への接続
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT)
    cur = conn.cursor()

    # テーブルの作成
    cur.execute("DROP TABLE IF EXISTS users;")
    cur.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(50), email VARCHAR(100));")
    conn.commit()
    print("テーブル 'users' を作成しました。")

    # データの挿入
    cur.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');")
    cur.execute("INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com');")
    conn.commit()
    print("データを挿入しました。")

    # データの読み込み
    cur.execute("SELECT id, name, email FROM users;")
    rows = cur.fetchall()
    print("users テーブルのデータ:")
    for row in rows:
        print(f"ID: {row[0]}, 名前: {row[1]}, メール: {row[2]}")

except psycopg2.Error as e:
    print(f"PostgreSQL エラー: {e}")

finally:
    # 接続のクローズ
    if conn:
        cur.close()
        conn.close()
        print("PostgreSQL 接続を閉じました。")

