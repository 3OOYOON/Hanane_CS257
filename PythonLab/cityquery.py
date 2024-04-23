import psycopg2

#Often we want to put a Python variable into an SQL query
def test_query_variable():
    
    # You will need to change the Port and the Password to use this code

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="akeelh",
        user="akeelh",
        password="spring482farm")

    cur = conn.cursor()


    # Here the %s signals that we will replace this with a variable later
    sql = "select * from usa_city_state_population where city = 'Northfield';"

    
    cur.execute( sql )

    print ("is northfield present in this table?")
    if cur.execute( sql ) = none:
        print ("none")
    return

    
    
    sql1= "select city from usa_city_state_population order by population limit 1;"
    
    print ("city with largest population")
    cur.execute( sql1 )

    
    sql2 = "select * from usa_city_state_population where state = 'Minnesota' order by state desc limit 1;"
    
    print ("Minnesota city with smallest population")
    cur.execute( sql2 )
    
    # for north most city
    sql3 = "select city from usa_city_state_population order by latitude limit 1;"
    
    # for south most city 
    sql4 = "select city from usa_city_state_population order by latitude desc limit 1;"

    # for east most city
    sql5 = "select city from usa_city_state_population order by longitude limit 1;"

    # for west most city
    sql6 = "select city from usa_city_state_population order by longitude desc limit 1;"

    print ("northmost city")
    cur.execute( sql3 )

    print ("southmost city")
    cur.execute( sql4 )

    print ("eastmost city")
    cur.execute( sql5 )

    print ("westmost city")
    cur.execute( sql6 )
    

    state_name = input("input a state, for example either MN or Minnesota")

    if len(state_name) <=1 :
        print (improper state name)
    else if len(state_name) = 2:
        sql7 = "select * from usa_city_state_population where code = state_name"

    # IMPORTANT: We need a list of values for the second input to execute
    #   ... Even if we are only inserting my variable, it must be in a list
    # For example,  [state_abb1]
    
    row_list = cur.fetchall()

    for row in row_list:
        print(row)

    return None

print( test_query_one() )

