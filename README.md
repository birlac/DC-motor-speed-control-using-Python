# DC-motor-speed-control-using-Python
The motor is controlled using half bridge L293D.

DC motor speed control.xlsx file has 2 sheet. One with pin connections to arduino from L293D called as 'pin conn'
The 'Sheet2' contains table for bidirectional operation of DC motor.

The code dc_motor_speed_control.py uses pyfirmata package for arduino serial communication, and pandas for reading data from excel worksheet.
