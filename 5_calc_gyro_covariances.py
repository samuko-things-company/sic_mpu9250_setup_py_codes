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

roll_rate_arr = []
pitch_rate_arr = []
yaw_rate_arr = []


if __name__ == "__main__":
  for i in range(no_of_samples):
    r_rate, p_rate, y_rate = imu.get('gyro-cal')
    roll_rate_arr.append(r_rate)
    pitch_rate_arr.append(p_rate)
    yaw_rate_arr.append(y_rate)

    percent = (i*100)/no_of_samples
    print("reading_sensor_data...  ", percent, " percent complete")

    time.sleep(0.02)


  roll_rate_variance = np.var(roll_rate_arr)
  pitch_rate_variance = np.var(pitch_rate_arr)
  yaw_rate_variance = np.var(yaw_rate_arr)

  print('computed gx_variance =', roll_rate_variance)
  print('computed gy_variance =', pitch_rate_variance)
  print('computed gz_variance =', yaw_rate_variance)
  print("")

  imu.send('gx-var', roll_rate_variance)
  imu.send('gy-var', pitch_rate_variance)
  imu.send('gz-var', yaw_rate_variance)
  roll_rate_variance, pitch_rate_variance, yaw_rate_variance = imu.get('gyro-var')

  print('stored gx_variance =', roll_rate_variance)
  print('stored gy_variance =', pitch_rate_variance)
  print('stored gz_variance =', yaw_rate_variance)
  print("")