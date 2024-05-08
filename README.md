# RailEase :Railway Reservation System

## Let's get started
[![](https://img.shields.io/badge/author-@SagarDarji-blue.svg?style=flat)](https://www.linkedin.com/in/sagar-darji-7b7011165/)
[![](https://img.shields.io/badge/author-@SonuSoni-blue.svg?style=flat)](https://www.linkedin.com/in/sonu-soni-516b22306/)


Sure, here's a step-by-step guide to set up a Flask application:

1. **Install Python**: Ensure Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/). Make sure to check the option to add Python to your system PATH during installation.

2. **Install Dependencies**: Open a terminal or command prompt and install dependencies using pip, Python's package manager:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run a Flask Application**: In your terminal or command prompt, navigate to your project directory and run your Flask application:

   ```bash
   cd code
   python Code.py
   ```

   You should see output indicating that the Flask development server is running. By default, the server listens on `http://127.0.0.1:5000/`.

6. **Access Our Flask Application**: Open a web browser and navigate to `http://127.0.0.1:5000/`. You should see `RailEase` web app displayed in the browser.


## SQL queries:
### Task 1: Retrieve All Trains Booked by a Passenger (search_by_name)

  ```sql
  SELECT
          Passenger.first_name, Passenger.last_name, Train.TrainNumber, Train." TrainName",
          Train." SourceStation", Train." DestinationStation", Booked.Staus, Booked.Ticket_Type
  FROM Train
  JOIN Booked ON Train.TrainNumber = Booked.Train_Number
  JOIN Passenger ON Booked.Passanger_ssn = Passenger.SSN
  WHERE Passenger.first_name = ? AND Passenger.last_name = ?
  ```
  Search Results
  <table class="table">
                <tr>
                    <th scope="col">First Name</th>
                    <th scope="col">Last Name</th>
                    <th scope="col">Train Number</th>
                    <th scope="col">Train Name</th>
                    <th scope="col">Source Station</th>
                    <th scope="col">Destination Station</th>
                    <th scope="col">Booking Status</th>
                </tr>
                <tr>
                    <td scope="row">James</td>
                    <td scope="row">Butt</td>
                    <td scope="row">3</td>
                    <td scope="row"> Golden Arrow </td>
                    <td scope="row"> Victoria</td>
                    <td scope="row"> Dover</td>
                    <td scope="row">Booked</td>
                </tr>
    </table>

### Task 2: List of Passengers Traveling on a Specific Date with Confirmed Tickets

  ```sql
  SELECT 
          Passenger.first_name,
          Passenger.last_name,
          Train." TrainName" ,
          Train." SourceStation" ,
          Train." DestinationStation",
          Booked.Ticket_Type
  FROM
          Passenger
  JOIN
          Booked ON Passenger.SSN = Booked.Passanger_ssn
  JOIN
          Train ON Train.TrainNumber = Booked.Train_Number
  JOIN
          Train_Status ON Train." TrainName"  = Train_Status." TrainName"
  WHERE
          Booked.Staus = 'Booked' AND Train_Status.TrainDate  = ?
  ```
  Search Results
            <table class="table">
                <tr>
                    <th scope="col">First Name</th>
                    <th scope="col">Last Name</th>
                    <th scope="col">Train Name</th>
                    <th scope="col">Source Station</th>
                    <th scope="col">Destination Station</th>
                    <th scope="col">Ticket Type</th>
                </tr>
                <tr>
                    <td scope="row">Josephine</td>
                    <td scope="row">Darakjy</td>
                    <td scope="row"> Flying Scottsman</td>
                    <td scope="row"> Edinburgh</td>
                    <td scope="row"> London</td>
                    <td scope="row">General</td>
                </tr>
                <tr>
                    <td scope="row">Art</td>
                    <td scope="row">Venere</td>
                    <td scope="row"> Flying Scottsman</td>
                    <td scope="row"> Edinburgh</td>
                    <td scope="row"> London</td>
                    <td scope="row">Premium</td>
                </tr>
                <tr>
                    <td scope="row">Fletcher</td>
                    <td scope="row">Flosi</td>
                    <td scope="row"> Flying Scottsman</td>
                    <td scope="row"> Edinburgh</td>
                    <td scope="row"> London</td>
                    <td scope="row">Premium</td>
                </tr>
                <tr>
                    <td scope="row">Sage</td>
                    <td scope="row">Wieser</td>
                    <td scope="row"> Flying Scottsman</td>
                    <td scope="row"> Edinburgh</td>
                    <td scope="row"> London</td>
                    <td scope="row">General</td>
                </tr>
                <tr>
                    <td scope="row">Kris</td>
                    <td scope="row">Marrier</td>
                    <td scope="row"> Flying Scottsman</td>
                    <td scope="row"> Edinburgh</td>
                    <td scope="row"> London</td>
                    <td scope="row">General</td>
                </tr> 
      </table>
      
### Task 3: Display Train and Passenger Information for Ages 50 to 60

  ```sql
  SELECT
          Passenger.first_name, Passenger.last_name, Passenger.address, 
          Train.TrainNumber, Train." TrainName", Train." SourceStation", Train." DestinationStation",
          Booked.Staus, Booked.Ticket_Type, Passenger.bdate
  FROM Passenger
  JOIN Booked ON Passenger.SSN = Booked.Passanger_ssn
  JOIN Train ON Booked.Train_Number = Train.TrainNumber
  ```
 Then I filtered data on flask application
 ```python
    today = datetime.today()
    filtered_passengers = [
        passenger for passenger in cur.fetchall()
        if age_from <= (today.year - datetime.strptime(passenger[9], "%Y-%m-%d 00:00:00").year) <= age_to
    ]
 ```
Search Results
<table class="table">
                <tr>
                    <th scope="col">First Name</th>
                    <th scope="col">Last Name</th>
                    <th scope="col">Address</th>
                    <th scope="col">Train Number</th>
                    <th scope="col">Train Name</th>
                    <th scope="col">Source Station</th>
                    <th scope="col">Destination Station</th>
                    <th scope="col">Ticket Type</th>
                    <th scope="col">Status</th>
                </tr>
                <tr>
                    <td scope="row">James</td>
                    <td scope="row">Butt</td>
                    <td scope="row">6649 N Blue Gum St</td>
                    <td scope="row">3</td>
                    <td scope="row"> Golden Arrow </td>
                    <td scope="row"> Victoria</td>
                    <td scope="row"> Dover</td>
                    <td scope="row">Booked</td>
                    <td scope="row">Premium</td>
                </tr>  
  </table>


### Task 4: Count of Passengers per Train

  ```sql
  SELECT Train." TrainName", COUNT(Booked.Passanger_ssn) AS Passenger_Count
  FROM Train
  JOIN Booked ON Train.TrainNumber = Booked.Train_Number
  GROUP BY Train.TrainNumber
  ```
  <table class="table">
        <tr>
            <th scope="col">Train Name</th>
            <th scope="col">Passenger Count</th>
        </tr>
         <tr>
            <td scope="row"> Flying Scottsman</td>
            <td scope="row">6</td>
        </tr>
        <tr>
            <td scope="row"> Golden Arrow </td>
            <td scope="row">7</td>
        </tr>
        <tr>
            <td scope="row"> Golden Chariot</td>
            <td scope="row">12</td>
        </tr>
  </table>

### Task 5: Search for Passengers on a Train

  ```sql
  SELECT Passenger.first_name, Passenger.last_name, Passenger.address, Train.TrainNumber, 
         Train." TrainName", Booked.Ticket_Type, Booked.Staus
  FROM Train
  JOIN Booked ON Train.TrainNumber = Booked.Train_Number
  JOIN Passenger ON Booked.Passanger_ssn = Passenger.SSN
  WHERE Train." TrainName" = ? AND Booked.Staus = 'Booked'
  ```
Search Results
<table class="table">
                <tr>
                    <th scope="col">First Name</th>
                    <th scope="col">Last Name</th>
                    <th scope="col">Address</th>
                    <th scope="col">Train Number</th>
                    <th scope="col">Train Name</th>
                    <th scope="col">Ticket Type</th>
                    <th scope="col">Status</th>
                </tr>
                <tr>
                    <td scope="row">Josephine</td>
                    <td scope="row">Darakjy</td>
                    <td scope="row">4 B Blue Ridge Blvd</td>
                    <td scope="row">2</td>
                    <td scope="row"> Flying Scottsman</td>
                    <td scope="row">General</td>
                    <td scope="row">Booked</td>
                </tr>
                <tr>
                    <td scope="row">Art</td>
                    <td scope="row">Venere</td>
                    <td scope="row">8 W Cerritos Ave #54</td>
                    <td scope="row">2</td>
                    <td scope="row"> Flying Scottsman</td>
                    <td scope="row">Premium</td>
                    <td scope="row">Booked</td>
                </tr>
                <tr>
                    <td scope="row">Sage</td>
                    <td scope="row">Wieser</td>
                    <td scope="row">5 Boston Ave #88</td>
                    <td scope="row">2</td>
                    <td scope="row"> Flying Scottsman</td>
                    <td scope="row">General</td>
                    <td scope="row">Booked</td>
                </tr>
                <tr>
                    <td scope="row">Fletcher</td>
                    <td scope="row">Flosi</td>
                    <td scope="row">394 Manchester Blvd</td>
                    <td scope="row">2</td>
                    <td scope="row"> Flying Scottsman</td>
                    <td scope="row">Premium</td>
                    <td scope="row">Booked</td>
                </tr>
                <tr>
                    <td scope="row">Kris</td>
                    <td scope="row">Marrier</td>
                    <td scope="row">228 Runamuck Pl #2808</td>
                    <td scope="row">2</td>
                    <td scope="row"> Flying Scottsman</td>
                    <td scope="row">General</td>
                    <td scope="row">Booked</td>
                </tr>
    </table>

### Task 6: Cancel a Ticket and Update the Waiting List
  Delete ticket
  ```sql
  DELETE FROM Booked
  WHERE Passanger_ssn = ? AND Train_Number = ?
  ```
  Check for waiting list passengers
  ```sql
  SELECT Passanger_ssn FROM Booked
  WHERE Train_Number = ? AND Staus = 'WaitL'
  LIMIT 1
  ```
  Update the first waiting passenger to confirmed
  ```sql
  UPDATE Booked
  SET Staus = 'Booked'
  WHERE Passanger_ssn = ?
  ```
