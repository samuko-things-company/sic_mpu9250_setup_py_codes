import time
from sic_mpu9250_serial_comm import SIC # samuko IMU compute
import numpy as np


# portName = '/dev/ttyACM0'
portName = '/dev/ttyUSB0'
imu = SIC(portName)

for i in range(5):
  time.sleep(1.0)
  print(i+1, " sec")
  

no_of_samples = 1000

roll_arr = []
pitch_arr = []
yaw_arr = []


def set_i2c_address(address):
  isSuccessful = imu.send("i2c", address)
  i2c_address = int(imu.get("i2c"))
  if isSuccessful:
    print(f"\nSUCCESS: 12c address successfully set to: {i2c_address}\nrestart the imu cct to see effect.\n")
  else:
    print("\nERROR: 12c address not successfully set\n")


if __name__ == "__main__":
  # check if it's the madgwick filter code running
  mode = int(imu.get("mode"))
  try:
    if mode == 2:
      set_i2c_address(104) # change this. default 104 (i.e 0x68)
    else:
      raise Exception("ERROR: Cannot Excecute Code, Upload Madgwick filter Code")
  except Exception as e:
    print(e)