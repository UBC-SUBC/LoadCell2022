# Load Cell Test Setup

## How to set up
### Hardware
* Use an Arduino (we used an Uno during development)
* Connect (Ethernet - Arduino)
    * Orange (VCC) - 5V
    * Blue (GND) - GND
    * Green (dat) - Pin 2
    * Brown (clk) - Pin 3
### Data-logging with Python
* Set up a Python 3 virtual environment using virtualenv or venv (using the name vEnv will get it properly ignored by the .gitignore)
* Activate the virtual environment
* Install requirements using the command ```pip install -r requirements.txt```
* Run the data logger using the command ```python loadcell.py```
    * There is an optional argument for changing the serial port used by the Arduino. You will most likely need to use this.
    * There is an optional argument for changing the output file name. You can use this for doing multiple runs.
    * These look like: ```python loadcell.py --COM COM3 --file test_1.csv``` or ```python loadcell.py --COM /dev/ttyacm1 --file test_2.csv```
