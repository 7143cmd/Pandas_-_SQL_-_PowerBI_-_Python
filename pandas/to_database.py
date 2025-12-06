import pandas as pd
import sqlite3


df = pd.read_csv('datasets/hotel_bookings.csv')

conn  = sqlite3.connect('hotel_bookings.db')

df.to_sql('hotel_bookings', conn, if_exists='replace', index=False)

conn.close()