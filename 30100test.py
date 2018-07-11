import max30100
import time
mx30 = max30100.MAX30100()

mx30.enable_spo2()


while True:
     mx30.read_sensor()
     print(mx30.buffer_red[-5:] + mx30.buffer_ir[-5:])
     time.sleep(0.01)
