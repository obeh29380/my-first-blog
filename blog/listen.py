import select
import psycopg2

def start_listen(on=0):
    con = psycopg2.connect(
        host = 'localhost',
        port = 5432,
        database='djangodatabase',
        user='djangogirls',
        password='pass')
    con.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    curs = con.cursor()
    curs.execute('LISTEN test;')
    print("Waiting for notifications on channel 'test'")
    while on:
        if select.select([con],[],[],5) == ([],[],[]):
            print('Timeout')
        else:
            con.poll()
            while con.notifies:
                notify = con.notifies.pop(0)
                print('Got NOTIFY:', notify.pid, notify.channel, notify.payload)
                 