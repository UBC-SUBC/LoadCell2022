import keyboard
import serial
import argparse
import pandas as pd
import os
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--COM', help='Enter your arduino\'s COM port', type = str, default = 'COM3')
parser.add_argument('--file', help='Enter desired output file name', type = str, default = 'loadcell.csv')
args = parser.parse_args()

serial_dat = []
path = os.path.abspath(__file__)
realPath = str(Path(path).parent)

com_port = args.COM
out_file = args.file

df = pd.DataFrame(columns = ['Load Cell'])

try:
    arduino = serial.Serial(com_port, 115200)
except:
    print('Could not find Arduino on ' + com_port)
    exit()

while True:
    if keyboard.is_pressed(' '):
        print('Program halted by keypress') 
        df['Load Cell'] = serial_dat
        df.to_csv(realPath + '\\' + out_file)
        exit()

    serial_dat.append(arduino.readline())