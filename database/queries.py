import pandas as pd

from database.connection import get_connection


def get_lme():

    conn = get_connection()

    df = pd.read_sql("""
        SELECT
            data_referencia,
            valor
        FROM valores_scraping_lme
        ORDER BY data_referencia
    """, conn)

    conn.close()

    return df

def get_dollar():

    conn = get_connection()

    df = pd.read_sql("""
        SELECT
            data_referencia,
            valor_compra
        FROM valores_scraping_dolar
        ORDER BY data_referencia
    """, conn)

    conn.close()

    return df