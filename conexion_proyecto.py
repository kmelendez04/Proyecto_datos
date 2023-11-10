''' Se puede correr todo el código y aparecerán todas las tablas con sus 
respectivas divisiones. Si se quiere ver el codigo tabla por tabla 
se podrá evidenciar despue de cada # el cual estará acompañada del nombre
de la tabla a la cual se le hará el proceso de carga de informacion'''

'''A pesar de lo anterior, al ser tantas filas la consola no muestra todo
por lo que se debe correr de 3 en 3 tablas, para que se muestre toda la 
información de cada una de ellas'''

#aircrafts_data
import psycopg2

try: 
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'Proyecto_final'
    )
    print("Conexión Exitosa")  
    print("\n--------------------------AIRCRAFTS_DATA--------------------------")
    print("\naircrafts_data: aircraft_code, range")
    cursor = connection.cursor()
    cursor.execute("select * from aircrafts_data")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)

finally:
    connection.close()
    
#airports_data
import psycopg2

try: 
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'Proyecto_final'
    )
    print("Conexión Exitosa")  
    print("\n--------------------------AIRPORTS_DATA--------------------------")
    print("\nairports_data: (airport_code, airport_name, city, timezone)")
    cursor = connection.cursor()
    cursor.execute("select * from airports_data")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)

finally:
    connection.close()
    
#bookings
import psycopg2

try: 
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'Proyecto_final'
    )
    print("Conexión Exitosa")  
    print("\n--------------------------BOOKINGS--------------------------")
    print("\nbookings: (book_ref, book_date, total_amount)")
    cursor = connection.cursor()
    cursor.execute("select * from bookings")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)

finally:
    connection.close()
#flight
import psycopg2

try: 
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'Proyecto_final'
    )
    print("Conexión Exitosa")  
    print("\n--------------------------FLIGHT--------------------------")
    print("\nflight: (flight_id, flight_no, departure_airport_code, arrival_airport_code, status, aircraft_code)")
    cursor = connection.cursor()
    cursor.execute("select * from flight")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)

finally:
    connection.close()
#accommodation
import psycopg2

try: 
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'Proyecto_final'
    )
    print("Conexión Exitosa")  
    print("\n--------------------------ACCOMMODATION--------------------------")
    print("\naccommodation: (accomm_id, accom_type)")
    cursor = connection.cursor()
    cursor.execute("select * from accommodation")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)

finally:
    connection.close()
#seats
import psycopg2

try: 
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'Proyecto_final'
    )
    print("Conexión Exitosa")  
    print("\n--------------------------SEATS--------------------------")
    print("\nseats: (seat_no, aircraft_code, accomm_id)")
    cursor = connection.cursor()
    cursor.execute("select * from seats")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)

finally:
    connection.close()
#ticket_flights
import psycopg2

try: 
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'Proyecto_final'
    )
    print("Conexión Exitosa")  
    print("\n--------------------------TICKET_FLIGHTS--------------------------")
    print("\nticket_flights: (ticket_no, flight_id, accomm_id, amount)")
    cursor = connection.cursor()
    cursor.execute("select * from ticket_flights")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)

finally:
    connection.close()
#tickets
import psycopg2

try: 
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'Proyecto_final'
    )
    print("Conexión Exitosa")  
    print("\n--------------------------TICKETS--------------------------")
    print("\ntickets: (passanger_id, ticket_no, book_ref)")
    cursor = connection.cursor()
    cursor.execute("select * from tickets")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)

finally:
    connection.close()
#boarding_passes
import psycopg2

try: 
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'Proyecto_final'
    )
    print("Conexión Exitosa")  
    print("\n--------------------------BOARDING_PASSES--------------------------")
    print("\nboarding_passes: (boarding_no, ticket_no, flight_id, seat_no)")
    print()
    cursor = connection.cursor()
    cursor.execute("select * from boarding_passes")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)

finally:
    connection.close()