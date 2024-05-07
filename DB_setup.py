import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('/Users/sagardarji/Library/CloudStorage/OneDrive-UTArlington/Mac/FOC/DB Project/RailEase/temp_railway_reservation.db')

# Read CSV files into DataFrame
df_train = pd.read_csv('/Users/sagardarji/Library/CloudStorage/OneDrive-UTArlington/Mac/FOC/DB Project/RRS//Train.csv')
df_train_status = pd.read_csv('/Users/sagardarji/Library/CloudStorage/OneDrive-UTArlington/Mac/FOC/DB Project/RRS//Train_status.csv')
df_passenger = pd.read_csv('/Users/sagardarji/Library/CloudStorage/OneDrive-UTArlington/Mac/FOC/DB Project/RRS//Passenger.csv')
df_booked = pd.read_csv('/Users/sagardarji/Library/CloudStorage/OneDrive-UTArlington/Mac/FOC/DB Project/RRS/booked.csv')

df_passenger['bdate'] = pd.to_datetime(df_passenger['bdate'])
df_train_status['TrainDate'] = pd.to_datetime(df_train_status['TrainDate'])

# Create tables and import data
df_train.to_sql('Train', conn, if_exists='replace', index=False)
df_train_status.to_sql('Train_Status', conn, if_exists='replace', index=False)
df_passenger.to_sql('Passenger', conn, if_exists='replace', index=False)
df_booked.to_sql('Booked', conn, if_exists='replace', index=False)

# Close the connection
conn.close()
