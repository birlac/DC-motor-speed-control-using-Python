from pyfirmata import Arduino, util
import time

#Read data from excel sheet for bidirectional dc motor control
import pandas as pd

df = pd.read_excel (r'C:\Users\Chirag\Desktop\PyArduino\Dc motor speed control.xlsx', sheet_name = 'Sheet2')

index_ = ['EN_OFF','EN_L','EN_R']
df.index = index_
print(df)
#print(df.loc['EN_R','IN2A'])

board = Arduino('COM3')

#Turn dc motor on for turning left
board.digital[9].write(df.loc['EN_R','EN12'])
board.digital[10].write(df.loc['EN_OFF','EN12'])

it = util.Iterator(board)
it.start()

#set EN pin as pwm input
pwm_en12 = board.get_pin('d:3:p') 

#accelerate from 0 to max speed by controlling pwm duty cycle
for i in range(0,100,10):
    pwm_en12.write(i/100)
    print(i)   #in pwm mode write varies from 0 to 1
    time.sleep(2)

#deaccelerate from max speed to complete halt
for j in range(100,0,-10):
    pwm_en12.write(j/100)
    print(j)
    time.sleep(2)

#Turn dc motor off
board.digital[9].write(df.loc['EN_OFF','EN12'])
board.digital[10].write(df.loc['EN_OFF','EN12'])

    
    

