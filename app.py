from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_by_name')
def search_by_name_form():
    return render_template('search_by_name.html')

# # Task 1: Retrieve All Trains Booked by a Passenger (search_by_name)
@app.route('/search_by_name', methods=['POST'])
def search_by_name():
    first_name = request.form['first_name'].title()
    last_name = request.form['last_name'].title()
    
    conn = sqlite3.connect('temp_railway_reservation.db')
    cur = conn.cursor()
    
    cur.execute('''
        SELECT Passenger.first_name, Passenger.last_name, Train.TrainNumber, Train." TrainName", Train." SourceStation", Train." DestinationStation", Booked.Staus, Booked.Ticket_Type
        FROM Train
        JOIN Booked ON Train.TrainNumber = Booked.Train_Number
        JOIN Passenger ON Booked.Passanger_ssn = Passenger.SSN
        WHERE Passenger.first_name = ? AND Passenger.last_name = ?
    ''', (first_name, last_name))
    
    bookings = cur.fetchall()
    conn.close()
    
    return render_template('search_by_name.html', bookings=bookings)

@app.route('/search_by_date')
def search_by_date_form():
    return render_template('search_by_date.html')

@app.route('/search_by_date', methods=['POST'])
def search_by_date():
    date_input = request.form['date']
    
    conn = sqlite3.connect('railway_reservation.db')
    cur = conn.cursor()
    
    cur.execute('''
        SELECT Passenger.first_name, Passenger.last_name, Booked.Train_Number
        FROM Passenger
        JOIN Booked ON Passenger.SSN = Booked.Passanger_ssn
        JOIN Train_Status ON Booked.Train_Number = Train_Status.TrainName
        WHERE Train_Status.TrainDate = ? AND Booked.Status = 'Confirmed'
    ''', (date_input,))
    
    passengers = cur.fetchall()
    conn.close()
    
    return render_template('search_by_date.html', passengers=passengers)

@app.route('/search_by_age')
def search_by_age_form():
    return render_template('search_by_age.html')

@app.route('/search_by_age', methods=['POST'])
def search_by_age():
    age_from = int(request.form['age_from'])
    age_to = int(request.form['age_to'])

    conn = sqlite3.connect('temp_railway_reservation.db')
    cur = conn.cursor()
    
    cur.execute('''
            SELECT
                Passenger.first_name, Passenger.last_name, Passenger.address, 
                Train.TrainNumber, Train." TrainName", Train." SourceStation", Train." DestinationStation",
                Booked.Staus, Booked.Ticket_Type, Passenger.bdate
            FROM Passenger
            JOIN Booked ON Passenger.SSN = Booked.Passanger_ssn
            JOIN Train ON Booked.Train_Number = Train.TrainNumber
    ''')
    
    today = datetime.today()
    filtered_passengers = [
        passenger for passenger in cur.fetchall()
        if age_from <= (today.year - datetime.strptime(passenger[9], "%Y-%m-%d").year) <= age_to
    ]
    
    conn.close()
    
    return render_template('search_by_age.html', passengers=filtered_passengers)


# Task 4: Count of Passengers per Train
@app.route('/passenger_count')
def passenger_count():
    conn = sqlite3.connect('temp_railway_reservation.db')
    cur = conn.cursor()
    
    cur.execute('''
        SELECT Train.TrainNumber, COUNT(Booked.Passanger_ssn) AS Passenger_Count
        FROM Train
        JOIN Booked ON Train.TrainNumber = Booked.Train_Number
        GROUP BY Train.TrainNumber
    ''')
    
    counts = cur.fetchall()
    conn.close()
    
    return render_template('train_counts.html', counts=counts)

# Task 5: Search for Passengers on a Train
@app.route('/search_train_passengers')
def search_train_passengers_form():
    return render_template('search_train_passengers.html')

@app.route('/search_train_passengers', methods=['POST'])
def search_train_passengers():
    train_name = request.form['train_name'].title()
    
    conn = sqlite3.connect('temp_railway_reservation.db')
    cur = conn.cursor()
    
    cur.execute('''
        SELECT Passenger.first_name, Passenger.last_name, Passenger.address, Train.TrainNumber, 
               Train." TrainName", Booked.Ticket_Type, Booked.Staus
        FROM Train
        JOIN Booked ON Train.TrainNumber = Booked.Train_Number
        JOIN Passenger ON Booked.Passanger_ssn = Passenger.SSN
        WHERE Train." TrainName" = ? AND Booked.Staus = 'Booked'
    ''', (train_name,))
    
    passengers = cur.fetchall()
    conn.close()
    
    return render_template('search_train_passengers.html', passengers=passengers, train_name=train_name)


# Task 6: Cancel a Ticket and Update the Waiting List
@app.route('/cancel_ticket_form')
def cancel_ticket_form():
    return render_template('cancel_ticket_form.html')

@app.route('/cancel_ticket', methods=['POST'])
def cancel_ticket():
    passenger_ssn = request.form['passenger_ssn']
    train_number = request.form['train_number']

    conn = sqlite3.connect('temp_railway_reservation.db')
    cur = conn.cursor()
    
    # Start transaction
    conn.execute('BEGIN')
    
    # Cancel the ticket
    cur.execute('''
        DELETE FROM Booked
        WHERE Passanger_ssn = ? AND Train_Number = ?
    ''', (passenger_ssn, train_number))
    
    # Check for waiting list passengers
    cur.execute('''
        SELECT Passanger_ssn FROM Booked
        WHERE Train_Number = ? AND Staus = 'WaitL'
        LIMIT 1
    ''', (train_number,))
    waiting_passenger = cur.fetchone()
    
    if waiting_passenger:
        # Update the first waiting passenger to confirmed
        cur.execute('''
            UPDATE Booked
            SET Staus = 'Booked'
            WHERE Passanger_ssn = ?
        ''', (waiting_passenger[0],))
    
    conn.commit()  # Commit transaction
    conn.close()
    
    return render_template('cancel_ticket_form.html', message="Ticket cancellation and update processed successfully.")

if __name__ == '__main__':
    app.run(debug=True)