
# Pickle
import  pickle
import psycopg2
from pw import password
import logging
from psycopg2 import extras
from datetime import datetime


gem_colors = {
    'diamond': 'clear',
    'ruby': 'red',
    'sapphire': 'blue',
    'amethyst': 'purple',
}

price_per_carat = [2000, 1200, 800, 975]

def write_data(color, price):
    # Open database connection and initiate cursor
    try:
        conn = psycopg2.connect(dbname='pickle', user='postgres', host='localhost',
                                password=password)
        print("Opened db successfully.")
    except:
        print(datetime.now(), "Unable to connect to the database")
        logging.exception('Unable to open database connection')
        return
    else:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    pickled_colors = pickle.dumps(color)
    pickled_price = pickle.dumps(price)

    cur.execute("""INSERT INTO gems(colors, price) VALUES (%s, %s);""", (pickled_colors, pickled_price))

    conn.commit()
    cur.close()
    conn.close()

    print('data written to db')



def read_data():
    # Open database connection and initiate cursor
    try:
        conn = psycopg2.connect(dbname='pickle', user='postgres', host='localhost',
                                password=password)
        print("Opened db successfully.")
    except:
        print(datetime.now(), "Unable to connect to the database")
        logging.exception('Unable to open database connection')
        return
    else:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute("SELECT * FROM gems;")

    pickled_data = cur.fetchone()

    colors = pickle.loads(pickled_data[1])
    prices = pickle.loads(pickled_data[2])

    print(colors)
    print(prices)

read_data()




