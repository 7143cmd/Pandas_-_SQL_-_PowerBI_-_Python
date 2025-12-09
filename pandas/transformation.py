import pandas as pd
from to_database import csv_2_sql

def DB1():
    df = pd.read_csv('datasets/hotel_bookings.csv')

    df = df.drop_duplicates()


    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else 'Unknown')

    columns_to_drop = ['agent', 'company', 'reservation_status_date']
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

    for col in df.select_dtypes(include=['float64']).columns:
        df[col] = df[col].round(0).astype('int64')

    for col in df.select_dtypes(include=['int64']).columns:
        df[col] = pd.to_numeric(df[col], downcast='integer')

    df['total_guests'] = df['adults'] + df['babies'] + df['children']
    df['total_nights'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']

    df = df.reset_index(drop=True)

    csv_2_sql(df, 'hotel_bookings')

def DB2():
    pass