

import time
import os
millis = int(round(time.time() * 1000))

starttime=time.time()
while True:
  print "tick"
  time.sleep(60.0 - ((time.time() - starttime) % 60.0))

entety_name = "Abhik"
entity_type = "Human"
entity_uuid = "31415926"

sensor_set = "AbhiksSmartPostureCorrectorTM"#AbhiksCasualLeftHandGlove

#the manufacturer provides documentation regarding the position, purpose and function of each of sensors
imported_sensing_units = [["MPU60500", "AbhiksBeautifulBreathingSensor","MAX30100",....]]



#schema format

#sensor manufacturers make libraries
#import all of the sensors you will need
#extanciate and define them based on the documentation and your desiered configuration [descriptive name, HZ, addressing bits, red_Led_current]
#check and run any nessicarry setup functions (seeting up files, calibrating, etc.)
#loop REFRESH_RATE number of times a second
#if its time for a sensor to be updated then read the data and append it to the relevant files
#if it misses an update then create a new files with the new starting timestamp


#library specifications

#variables:
# string sensor name
# string given name
# float refresh rate #given a default value #default all datastreams but can override individual datastreams
# arbitrary number of config variables (ex: red_Led_current, address_bit)
# list of possible refresh rates for each stream
# list of datastreams names
# list of datstream types
# list of active datastreams

#functions:

# remove datastream ##does not include the removed datastream when the read data function is called and removes the stream from the active streams list
# read data    # takes in an SMbus and returns an arry of sensor readings that lines up with the fields in the active datastreams
# an arbitrary number of setup functions (ex. calabrate)




#["sensor identifier", refresh reate in HZ,["datastream", "datastream", "datastream"]


#["sensor identifier", refresh reate in HZ, prtocol, [protocol specific addressing]]
#i2c protocol specific addressing
#[device address, ["datastream name", "encoding format" [reg_1 ,reg_2,.....]], ["datastream name", "encoding format" [reg_1 ,reg_2,.....]],.....]
imported_sensor_schemas = [["MPU60500",i2c, 0x68, 64, [ACCELL_Y, [REG_N, REG_N+1],[GYRO_Z, [REG_P, REG_P+1]],....]],
                            ["AbhiksBeautifulBreathingSensor", i2c, 0x11, 128, [VAL, [RED_N, REG_N+1]]],...],
                            ["MPU60501",...],
                            ["ExcitingECG"],

#sensors to implemnt

#MPU60500
#MPU60501


#MLX90614ESF GY-906 (IRbodytemp)
#https://www.sparkfun.com/datasheets/Sensors/Temperature/MLX90614_rev001.pdf

#CCS811 (airquality)
#https://cdn.sparkfun.com/datasheets/BreakoutBoards/CCS811_Programming_Guide.pdf

#MAX30100 (SPo2, and HR)
#https://datasheets.maximintegrated.com/en/ds/MAX30100.pdf
#https://github.com/mfitzp/max30100/blob/master/max30100.py

#BME280 (air temp, pressure, humidity)
#https://cdn.sparkfun.com/assets/learn_tutorials/4/1/9/BST-BME280_DS001-10.pdf

#AbhiksBeautifulBreathingSensor
#ExcitingECG
#GreatGSR





#create person floder
#create sensor set folder
#iterate over sensing units and make folders for each, then look it up in schemas and then make folders for every data stream
#start collecting data titiling the files day-month-year-24:HR:MIN:SEC.millis

if not os.path.exists(directory):
    os.makedirs(directory)



starttime=time.time()
while True:
  time.sleep(0.00390625 - ((time.time() - starttime) % 0.00390625))
