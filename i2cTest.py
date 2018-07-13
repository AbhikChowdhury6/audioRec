
#!/usr/bin/python
import smbus

bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1

#address = 0x54       # via i2cdetect

#firstbyte =  bus.read_byte(address)
#secondbyte = bus.read_byte(address)
#print firstbyte
#print secondbyte
#print (firstbyte << 8)+ secondbyte

millis = int(round(time.time() * 1000))

starttime=time.time()
while True:
  print "tick"
  time.sleep(60.0 - ((time.time() - starttime) % 60.0))
