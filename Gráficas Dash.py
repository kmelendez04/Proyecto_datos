'''Se debe correr punto por punto, los puntos 3, 4 y 5 son 2 gráficas por lo que se deben
correr cada una por separado. Se recomienda comentar el resto del código que no se quiera 
correr. En caso de que no aparezca el link del dash en la consola se abre copiando el 
siguiente: http://127.0.0.1:8050/ 
No es necesario recargar el dash ya que se va actualizando.  '''

# Punto 1
from dash import Dash, html, dcc
import psycopg2
import plotly.express as px
try: 
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'Proyecto_final'
    )
    print("Conexión Exitosa")  
    cursor = connection.cursor()
    cursor.execute("WITH Departures AS (SELECT departure_airport_code, COUNT(departure_airport_code) AS departures_count, RANK() OVER (ORDER BY COUNT(departure_airport_code) DESC) AS departure_rank FROM flight GROUP BY departure_airport_code), Arrivals AS (SELECT arrival_airport_code, COUNT(arrival_airport_code) AS arrivals_count, RANK() OVER (ORDER BY COUNT(arrival_airport_code) DESC) AS arrival_rank FROM flight GROUP BY arrival_airport_code) SELECT COALESCE(Departures.departure_airport_code, Arrivals.arrival_airport_code) AS airport_code, COALESCE(departures_count, 0) + COALESCE(arrivals_count, 0) AS total_count, COALESCE(departure_rank, arrival_rank) AS total_rank FROM Departures FULL OUTER JOIN Arrivals ON Departures.departure_airport_code = Arrivals.arrival_airport_code ORDER BY total_count DESC;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    app = Dash(__name__)
    fig = px.bar(rows, x=0, y=1, color_discrete_sequence = ["blue"])
    app.layout = html.Div(children = [
        html.H1(children = 'Aeropuerto más concurrido'),
        html.Div(children = '''
                 Muestra cuáles son los aeropuertos más concurridos a lo largo del tiempo, cuáles ciudades tienen más 
                 actividad aérea
        '''),
        dcc.Graph(
            id = 'example-graph',
            figure = fig)
    ])
    if __name__ == '__main__':
        app.run_server(debug = True)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexion finalizada")
    
# Punto 2
from dash import Dash, html, dcc
import psycopg2
import plotly.express as px
try: 
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'Proyecto_final'
    )
    print("Conexión Exitosa")  
    cursor = connection.cursor()
    cursor.execute("SELECT extract(day from book_date) as booking_day, COUNT(extract(day from book_date)) AS total_bookings_per_day, RANK() OVER (ORDER BY COUNT(extract(day from book_date)) DESC) AS sells_days_rank FROM bookings GROUP BY extract(day from book_date)")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    app = Dash(__name__)
    fig = px.bar(rows, x=0, y=1, color_discrete_sequence = ["pink"])
    app.layout = html.Div(children = [
        html.H1(children = 'Día del mes con mas ventas'),
        html.Div(children = '''
                 Suma la cantidad de reservas que tienen 
                 en un día determinado sin importar el mes ni el año que sea
        '''),
        dcc.Graph(
            id = 'example-graph',
            figure = fig)
    ])
    if __name__ == '__main__':
        app.run_server(debug = True)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexion finalizada")


# Punto 3 solo con cantidad de reservas por acomodacion
from dash import Dash, html, dcc
import psycopg2
import plotly.express as px

try:
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='perfume',
        database='Proyecto_final'
    )
    print("Conexión Exitosa")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT accomm_id, COUNT(accomm_id) AS accomm_count FROM ticket_flights GROUP BY accomm_id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    app = Dash(__name__)
    fig = px.pie(rows, names=['Business', 'Comfort','Economy'], values=1, title='Reservas por acomodacion')
    
    app.layout = html.Div(children=[
        html.H1(children='Reservas por acomodacion'),
        html.Div(children='''
                 Cuenta la cantidad de reservas que tiene cada acomodación
        '''),
        dcc.Graph(
            id='example-graph',
            figure=fig)
    ])

    if __name__ == '_main_':
        app.run_server(debug=True)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexion finalizada")
    
    
#Punto 3 con ambos datos
from dash import Dash, html, dcc
import psycopg2
import pandas as pd
import plotly.express as px

try: 
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='123456789',
        database='Proyecto_final'
    )
    print("Conexión Exitosa")  
    cursor = connection.cursor()
    cursor.execute("SELECT accomm_id, COUNT(accomm_id) AS accomm_count, SUM(amount) AS total_amount, RANK() OVER (ORDER BY COUNT(accomm_id) DESC) AS accomm_rank FROM ticket_flights GROUP BY accomm_id")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=["accomm_id", "accomm_count", "total_amount", "accomm_rank"])
    melted_df = pd.melt(df, id_vars=["accomm_id"], value_vars=["accomm_count", "total_amount"], var_name="variable", value_name="value")

    app = Dash(__name__)
    fig = px.bar(
        melted_df,
        x="accomm_id",
        y="value",
        color="variable",
        barmode="group",
        opacity=0.7,  
        width=800,
        height=500,  
        labels={"accomm_id": "", "": ""},
    )
    app.layout = html.Div(children=[
        html.H1(children='Datos por acomodación'),
        html.Div(children='''Muestra la cantidad de reservas por cada acomodacion y además muestra 
                 la cantidad de dinero que genera cada uno 
                 '''),
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])

    if __name__ == '__main__':
        app.run_server(debug=True)

except Exception as ex:
    print(ex)

finally:
    connection.close()
    print("Conexion finalizada")
    
# Punto 4 primera gráfica

from dash import Dash, html, dcc
import psycopg2
import plotly.express as px
try: 
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'Proyecto_final'
    )
    print("Conexión Exitosa")  
    cursor = connection.cursor()
    cursor.execute('''SELECT 
    aircraft_code,
    SUM(number_of_time_zone_changes) AS total_time_zone_changes
FROM (
    SELECT 
        f.aircraft_code,
        CASE
            WHEN a1.timezone != a2.timezone THEN 1
            ELSE 0
        END AS number_of_time_zone_changes
    FROM flight f
    JOIN airports_data a1 ON f.departure_airport_code = a1.airport_code
    JOIN airports_data a2 ON f.arrival_airport_code = a2.airport_code
) AS t1
GROUP BY aircraft_code;''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    app = Dash(__name__)
    fig = px.bar(rows, x=0, y=1, color_discrete_sequence = ["pink"])
    app.layout = html.Div(children = [
        html.H1(children = 'Total de cambios de zona horaria en vuelos por cada tipo de avion'),
        html.Div(children = '''
                 Cuenta la cantidad de cambios de zona horaria que tiene cada avion, por ejemplo 
                 cuando pasa de Europa a Asia o viceversa
        '''),
        dcc.Graph(
            id = 'example-graph',
            figure = fig)
    ])
    if __name__ == '__main__':
        app.run_server(debug = True)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexion finalizada")
    
# Punto 4 segunda gráfica

from dash import Dash, html, dcc
import psycopg2
import plotly.express as px
try: 
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'Proyecto_final'
    )
    print("Conexión Exitosa")  
    cursor = connection.cursor()
    cursor.execute('''select aircraft_code, range, rank() over (order by range desc) as range_rank
from aircrafts_data
group by aircraft_code''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    app = Dash(__name__)
    fig = px.bar(rows, x=0, y=1, color_discrete_sequence = ["pink"])
    app.layout = html.Div(children = [
        html.H1(children = 'Rango de cada avión'),
        html.Div(children = '''
                 Dice cuantas millas puede recorrer en promedio un avión en un solo vuelo
        '''),
        dcc.Graph(
            id = 'example-graph',
            figure = fig)
    ])
    if __name__ == '__main__':
        app.run_server(debug = True)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexion finalizada")
    
# Punto 5 primera gráfica

from dash import Dash, html, dcc
import psycopg2
import plotly.express as px
try: 
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'Proyecto_final'
    )
    print("Conexión Exitosa")  
    cursor = connection.cursor()
    cursor.execute('''SELECT aircraft_code, COUNT(aircraft_code) AS flights_per_aircrafts,
    RANK() OVER (ORDER BY COUNT(aircraft_code) DESC) AS rank
    FROM flight
    GROUP BY aircraft_code''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    app = Dash(__name__)
    fig = px.bar(rows, x=0, y=1, color_discrete_sequence = ["pink"])
    app.layout = html.Div(children = [
        html.H1(children = 'Cantidad de vuelos por cada avión'),
        html.Div(children = '''
                 Cuantos vuelos ha hecho cada avión 
        '''),
        dcc.Graph(
            id = 'example-graph',
            figure = fig)
    ])
    if __name__ == '__main__':
        app.run_server(debug = True)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexion finalizada")
    
#Punto 5 gráfica 2

from dash import Dash, html, dcc
import psycopg2
import pandas as pd
import plotly.express as px

try: 
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='123456789',
        database='Proyecto_final'
    )
    print("Conexión Exitosa")  
    cursor = connection.cursor()

    cursor.execute('''SELECT aircraft_code, 
                           COALESCE(SUM(CASE WHEN status = 'Arrived' THEN 1 ELSE 0 END), 0) AS Arrived,
                           COALESCE(SUM(CASE WHEN status = 'Scheduled' THEN 1 ELSE 0 END), 0) AS Scheduled,
                           COALESCE(SUM(CASE WHEN status = 'On Time' THEN 1 ELSE 0 END), 0) AS OnTime,
                           COALESCE(SUM(CASE WHEN status = 'Delayed' THEN 1 ELSE 0 END), 0) AS Delayed,
                           COALESCE(SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END), 0) AS Cancelled
                    FROM flight
                    GROUP BY aircraft_code
    ''')
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=["aircraft_code", "Arrived", "Scheduled", "OnTime", "Delayed", "Cancelled"])

    app = Dash(__name__)
    fig = px.bar(df, x="aircraft_code", y=["Arrived", "Scheduled", "OnTime", "Delayed", "Cancelled"], barmode="stack", color_discrete_sequence=["green", "blue", "orange", "red", "gray"])

    app.layout = html.Div(children=[
        html.H1(children='Cantidad de vuelos por cada avión teniendo en cuenta cada estado del vuelo'),
        html.Div(children='''Muestra cuántos vuelos tiene cada aeronave en cada estado (despegó, aterrizó, a tiempo, demorado, cancelado)'''),
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])

    if __name__ == '__main__':
        app.run_server(debug=True)

except Exception as ex:
    print(ex)

finally:
    connection.close()
    print("Conexion finalizada")
