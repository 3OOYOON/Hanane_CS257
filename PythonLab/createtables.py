def test_query_one():
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="akeelh",
        user="akeelh",
        password="spring482farm")

    cur = conn.cursor()

    sql1 = """DROP TABLE IF EXISTS USA City State Population;
            CREATE TABLE USA Cities And State Population (
                City text,
                State text,
                Population int,
                Latitude decimal,
                Longitude decimal
            );"""
            
    sql2 = """DROP TABLE IF EXISTS USA State Population;
            CREATE TABLE USA State Population (
                Code text,
                State text,
                Population int
            );"""

    cur.execute( sql1 )
    cur.execute( sql2 )
    row = cur.fetchone()

    conn.commit()
    
    return row
