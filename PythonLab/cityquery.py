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
    cur.execute("select city from usa_city_state_population where city = 'Northfield';")
    result = cur.fetchone()
    if result:
        print(f"Northfield is present in the data")
    else:
        print("Northfield is not present in the database.")


    # City with the largest population
    cur.execute("select city from usa_city_state_population order by population limit 1")
    print("City with the largest population:", cur.fetchone()[0])


    # City in Minnesota with the smallest population
    cur.execute("select city from usa_city_state_population where state = 'Minnesota' order by state desc limit 1;")
    print("Minnesota city with the smallest population:", cur.fetchone()[0])


    # Extremes in geographical location
    cur.execute("select city from usa_city_state_population order by latitude limit 1;")
    print("Northmost city:", cur.fetchone()[0])

    cur.execute("select city from usa_city_state_population order by latitude desc limit 1;")
    print("Southmost city:", cur.fetchone()[0])

    cur.execute("select city from usa_city_state_population order by longitude limit 1;")
    print("Eastmost city:", cur.fetchone()[0])

    cur.execute("select city from usa_city_state_population order by longitude desc limit 1;")
    print("Westmost city:", cur.fetchone()[0])


    # Total population by state input
    state_name = input("Enter a state (abbreviation or full name): ")
    if len(state_name) == 2:
        cur.execute("select sum(population) from usa_city_state_population where state in (select name from states where code = %s);", (state_name,))
    else:
        cur.execute("select sum(population) from us_state_pop where state = %s;", (state_name,))
    total_pop = cur.fetchone()[0]
    print(f"Total population for {state_name}: {total_pop}")

    cur.close()
    conn.close()

    query_db()
