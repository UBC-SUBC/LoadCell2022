import keyboard
import serial
import argparse
import pandas as pd
import os
import datetime as dt

parser = argparse.ArgumentParser()
parser.add_argument('--COM', help='Enter your arduino\'s COM port', type = str, default = 'COM3')
parser.add_argument('--file', help='Enter desired output file name', type = str, default = 'loadcell.csv')
args = parser.parse_args()

serial_dat = []
timestamp = []
path = os.path.dirname(__file__)

com_port = args.COM
out_file = args.file

df = pd.DataFrame(columns = ['Timestamp', 'Load Cell'])

try:
    arduino = serial.Serial(com_port, 115200)
    print("connection to arduino successful, script running!")
except:
    print('Could not find Arduino on ' + com_port)
    exit()

while True:
    if keyboard.is_pressed(' '):
        print('Program halted by keypress') 
        df['Load Cell'] = serial_dat
        df['Timestamp'] = timestamp
        df.to_csv(path + '\\' + out_file)
        exit()

    if (arduino.in_waiting):
        serial_dat.append(arduino.readline().decode().strip())
        timestamp.append(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))