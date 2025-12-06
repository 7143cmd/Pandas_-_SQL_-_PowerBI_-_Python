import pandas as pd
import sqlite3

def csv_2_sql(df):
    conn  = sqlite3.connect('hotel_bookings.db')

    df.to_sql('hotel_bookings', conn, if_exists='replace', index=False)

    conn.close()


if __name__ == "__main__":
    csv_2_sql(df = pd.read_csv('datasets/hotel_bookings.csv'))