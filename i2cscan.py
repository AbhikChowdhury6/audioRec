

import time
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

imported_sensor_schemas = [["MPU60500",i2c, 0x68, 64, [ACCELL_Y, [REG_N, REG_N+1],[GYRO_Z, [REG_P, REG_P+1]],....]],
                            ["AbhiksBeautifulBreathingSensor", i2c, 0x11, 128, [VAL, [RED_N, REG_N+1]]],...],
                            ["MPU60501",...],
                            ["ExcitingECG"],


#create person floder
#create sensor set folder
#iterate over sensing units and make folders for each, then look it up in schemas and then make folders for every data stream
#start collecting data
