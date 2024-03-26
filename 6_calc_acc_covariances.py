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

lin_accx_arr = []
lin_accy_arr = []
lin_accz_arr = []


if __name__ == "__main__":
  for i in range(no_of_samples):

    lin_accx, lin_accy, lin_accz = imu.get('acc-cal')
    lin_accx_arr.append(lin_accx)
    lin_accy_arr.append(lin_accy)
    lin_accz_arr.append(lin_accz)

    percent = (i*100)/no_of_samples
    print("reading_sensor_data...  ", percent, " percent complete")

    time.sleep(0.02)

  lin_accx_variance = np.var(lin_accx_arr)
  lin_accy_variance = np.var(lin_accy_arr)
  lin_accz_variance = np.var(lin_accz_arr)

  print('computed ax_variance =', lin_accx_variance)
  print('computed ay_variance =', lin_accy_variance)
  print('computed az_variance =', lin_accz_variance)
  print("")

  imu.send('ax-var', lin_accx_variance)
  imu.send('ay-var', lin_accy_variance)
  imu.send('az-var', lin_accz_variance)
  lin_accx_variance, lin_accy_variance, lin_accz_variance = imu.get('acc-var')

  print('stored ax_variance =', lin_accx_variance)
  print('stored ay_variance =', lin_accy_variance)
  print('stored az_variance =', lin_accz_variance)
  print("")