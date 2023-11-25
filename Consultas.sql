/*Este código contiene las consultas necesarias para generar las tablas
necesarias en el dash. Arrojan todos los datos que se necesitan para
responder y poder analizar todos los escenarios que se plantearon en 
la anterior entrega. 

Para poder correr estas consultas se debe correr los códigos con las tablas
de la anterior entrega. En los puntos 4 y 5 se deben hacer dos consultas 
distintas, debido a que son dos tablas distintas para hacer una comparación*/


/*Punto 1: Determinar mediante los datos en que aeropuerto despegan y aterrizan
mayor cantidad de vuelos, teniendo en cuenta todos los vuelos que están 
en la base de datos. Obteniendo así las zonas más concurridas y que 
tienen más movimiento aéreo a lo largo del tiempo.*/

WITH Departures AS (
    SELECT departure_airport_code, COUNT(departure_airport_code) AS departures_count,
    RANK() OVER (ORDER BY COUNT(departure_airport_code) DESC) AS departure_rank
    FROM flight
    GROUP BY departure_airport_code
),
Arrivals AS (
    SELECT arrival_airport_code, COUNT(arrival_airport_code) AS arrivals_count,
    RANK() OVER (ORDER BY COUNT(arrival_airport_code) DESC) AS arrival_rank
    FROM flight
    GROUP BY arrival_airport_code
)
SELECT COALESCE(Departures.departure_airport_code, Arrivals.arrival_airport_code) AS airport_code,
       COALESCE(departures_count, 0) + COALESCE(arrivals_count, 0) AS total_count,
       COALESCE(departure_rank, arrival_rank) AS total_rank
FROM Departures
FULL OUTER JOIN Arrivals ON Departures.departure_airport_code = Arrivals.arrival_airport_code
ORDER BY total_count DESC;


/*Punto 2: Determinar en un ranking que día del mes se hacen más reservas. Esto 
ubicándolos del mayor al menor sumando la cantidad de reservas que tienen 
en un día determinado sin importar el mes ni el año que sea. Así se podría 
determinar en qué días del mes se debería hacer más publicidad para llegar 
a la audiencia en esas fechas y que la publicidad sea más efectiva y se 
compren más tiquetes.*/

SELECT extract(day from book_date) as booking_day, COUNT(extract(day from book_date)) AS total_bookings_per_day,
    RANK() OVER (ORDER BY COUNT(extract(day from book_date)) DESC) AS sells_days_rank
    FROM bookings
    GROUP BY extract(day from book_date)

/*Punto 3: Analizar cuales acomodaciones son las que más se compran, y de esta 
manera ver la diferencia de ingresos que genera cada una de las acomodaciones. 
Si business al ser más costosa genera más ingresos a comparación de las demás 
o si por la cantidad tan reducida de sillas que hay se generan menos ingresos
que en comfort o economy.*/

SELECT accomm_id, COUNT(accomm_id) AS accomm_count, SUM(amount),
    RANK() OVER (ORDER BY COUNT(accomm_id) DESC) AS accomm_rank
    FROM ticket_flights
    GROUP BY accomm_id

/*Punto 4: Determinar que avión hace los vuelos más largos viendo los cambios de zonas 
horarias o también se podría ver comparando la cantidad de kilómetros que hay 
entre ciudad y ciudad. Con un ranking del range que tiene cada modelo de avión 
mirar si esto afecta en todos sus casos.*/

SELECT 
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
GROUP BY aircraft_code;

select aircraft_code, range, rank() over (order by range desc) as range_rank
from aircrafts_data
group by aircraft_code

/*Punto 5: Determinar que aviones son los más usados para realizar distintos vuelos, y 
ver cuál es el que tiene más vuelos por cada estado, es decir, si está cancelado, 
agendado o si ya aterrizó.*/

SELECT aircraft_code, COUNT(aircraft_code) AS flights_per_aircrafts,
    RANK() OVER (ORDER BY COUNT(aircraft_code) DESC) AS rank
    FROM flight
    GROUP BY aircraft_code
	
	
SELECT aircraft_code, 
	   COALESCE(SUM(CASE WHEN status = 'Arrived' THEN 1 ELSE 0 END), 0) AS Arrived,
	   COALESCE(SUM(CASE WHEN status = 'Scheduled' THEN 1 ELSE 0 END), 0) AS Scheduled,
	   COALESCE(SUM(CASE WHEN status = 'On Time' THEN 1 ELSE 0 END), 0) AS OnTime,
	   COALESCE(SUM(CASE WHEN status = 'Delayed' THEN 1 ELSE 0 END), 0) AS Delayed,
	   COALESCE(SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END), 0) AS Cancelled
FROM flight
GROUP BY aircraft_code

