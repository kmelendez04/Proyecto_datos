create table aircrafts_data (
aircraft_code varchar (4) unique,
range int,
primary key (aircraft_code));


create table airports_data(
airport_code varchar (3) unique,
airport_name varchar (60),
city varchar (60),
timezone varchar (10),
primary key (airport_code));

create table bookings(
book_ref varchar (6) unique,
book_date date,
total_amount numeric (12,2),
primary key (book_ref));

create table flight(
flight_id int unique,
flight_no varchar (6),
departure_airport_code varchar (3),
arrival_airport_code varchar (3),
status varchar (20),
aircraft_code varchar (4),
primary key (flight_id),
foreign key (departure_airport_code) references airports_data,
foreign key (arrival_airport_code) references airports_data,
foreign key (aircraft_code) references aircrafts_data);

create table accommodation(
accomm_id int unique,
accomm_type varchar (10),
primary key (accomm_id));

create table seats (
seat_no varchar(4),
aircraft_code varchar (4),
accomm_id int,
primary key (seat_no),
foreign key (aircraft_code) references aircrafts_data,
foreign key (accomm_id) references accommodation);

create table ticket_flights(
ticket_no numeric(20,0) unique, 
flight_id int,
accomm_id int,
amount numeric (12,2),
primary key (ticket_no),
foreign key (flight_id) references flight,
foreign key (accomm_id) references accommodation);

create table tickets(
passanger_id numeric(20,0),
ticket_no numeric (30,0),
book_ref varchar (6),
primary key (passanger_id),
foreign key (ticket_no) references ticket_flights,
foreign key (book_ref) references bookings);


create table boarding_passes(
boarding_no int unique,
ticket_no numeric (30,0),
flight_id int,
seat_no varchar (4),
primary key (boarding_no),
foreign key (ticket_no) references ticket_flights,
foreign key (flight_id) references flight,
foreign key (seat_no) references seats);



select*from aircrafts_data
copy aircrafts_data (aircraft_code, range)
from 'C:\Users\Public\datos/aircrafts_data.csv' delimiter ';' csv header;

select*from airports_data
copy airports_data (airport_code, airport_name, city,timezone )
from 'C:\Users\Public\datos/airports_data.csv' delimiter ';' csv header;

select*from bookings
copy bookings (book_ref, book_date, total_amount)
from 'C:\Users\Public\datos/bookings.csv' delimiter ';' csv header;


select*from flight 
copy flight (flight_id, flight_no, departure_airport_code,arrival_airport_code, status, aircraft_code)
from 'C:\Users\Public\datos/flight.csv' delimiter ';' csv header;

select*from accommodation
copy accommodation (accomm_id, accomm_type)
from 'C:\Users\Public\datos/accommodation.csv' delimiter ';' csv header;

select*from seats
copy seats (seat_no, aircraft_code,accomm_id)
from 'C:\Users\Public\datos/seats.csv' delimiter ';' csv header;


select*from ticket_flights
copy ticket_flights (ticket_no, flight_id,accomm_id, amount)
from 'C:\Users\Public\datos/ticket_flights.csv' delimiter ';' csv header;


select*from tickets 
copy tickets (passanger_id, ticket_no,book_ref)
from 'C:\Users\Public\datos/tickets.csv' delimiter ';' csv header;

select*from boarding_passes 
copy boarding_passes (boarding_no, ticket_no,flight_id,seat_no)
from 'C:\Users\Public\datos/boarding_passes.csv' delimiter ';' csv header;


