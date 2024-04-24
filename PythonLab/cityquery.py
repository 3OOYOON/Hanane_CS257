import psycopg2

def query_db():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="akeelh",
        user="akeelh",
        password="spring482farm")
    cur = conn.cursor()

    # Check if Northfield is present
    cur.execute("SELECT city, latitude, longitude FROM cities WHERE city = 'Northfield';")
    result = cur.fetchone()
    if result:
        print(f"Northfield is at latitude {result[1]} and longitude {result[2]}.")
    else:
        print("Northfield is not present in the database.")

    # City with the largest population
    cur.execute("SELECT city FROM cities ORDER BY population DESC LIMIT 1;")
    print("City with the largest population:", cur.fetchone()[0])

    # City in Minnesota with the smallest population
    cur.execute("SELECT city FROM cities WHERE state = 'Minnesota' ORDER BY population ASC LIMIT 1;")
    print("Minnesota city with the smallest population:", cur.fetchone()[0])

    # Extremes in geographical location
    cur.execute("SELECT city FROM cities ORDER BY latitude DESC LIMIT 1;")
    print("Northmost city:", cur.fetchone()[0])
    cur.execute("SELECT city FROM cities ORDER BY latitude LIMIT 1;")
    print("Southmost city:", cur.fetchone()[0])
    cur.execute("SELECT city FROM cities ORDER BY longitude DESC LIMIT 1;")
    print("Eastmost city:", cur.fetchone()[0])
    cur.execute("SELECT city FROM cities ORDER BY longitude LIMIT 1;")
    print("Westmost city:", cur.fetchone()[0])

    # Total population by state input
    state_name = input("Enter a state (abbreviation or full name): ")
    if len(state_name) == 2:
        cur.execute("SELECT SUM(population) FROM cities WHERE state IN (SELECT name FROM states WHERE abbreviation = %s);", (state_name,))
    else:
        cur.execute("SELECT SUM(population) FROM cities WHERE state = %s;", (state_name,))
    total_pop = cur.fetchone()[0]
    print(f"Total population for {state_name}: {total_pop}")

    cur.close()
    conn.close()

query_db()
