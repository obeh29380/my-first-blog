import psycopg2


con = psycopg2.connect(
    host = 'localhost',
    port = 5432,
    database='djangodatabase',
    user='djangogirls',
    password='pass')
cur = con.cursor()
cur.execute("NOTIFY test, 'payload_data'")
# コミットを忘れずに
con.commit()
cur.close()
con.close()
