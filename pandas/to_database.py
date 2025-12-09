import pandas as pd
import sqlite3

def csv_2_sql(df, dbname):
    conn  = sqlite3.connect(dbname)

    df.to_sql('AI_impact', conn, if_exists='replace', index=False)

    conn.close()


if __name__ == "__main__":
    csv_2_sql(pd.read_csv('datasets/AI_Impact_on_Jobs_2030.csv'), 'AI_impact.db')