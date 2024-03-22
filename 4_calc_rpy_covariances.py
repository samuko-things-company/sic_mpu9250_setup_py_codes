import time
from sic_pyserial_lib import SIC # samuko IMU compute
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


if __name__ == "__main__":
  for i in range(no_of_samples):
    r_rad, p_rad, y_rad = imu.get('rpy-raw')
    roll_arr.append(r_rad)
    pitch_arr.append(p_rad)
    yaw_arr.append(y_rad)

    percent = (i*100)/no_of_samples
    print("reading_sensor_data...  ", percent, " percent complete")

    time.sleep(0.02)
  
  roll_variance = np.var(roll_arr)
  pitch_variance = np.var(pitch_arr)
  yaw_variance = np.var(yaw_arr)

  print('computed roll_angle_variance =', roll_variance)
  print('computed pitch_angle_variance =', pitch_variance)
  print('computed yaw_angle_variance =', yaw_variance)
  print("")

  imu.send('r-var', roll_variance)
  imu.send('p-var', pitch_variance)
  imu.send('y-var', yaw_variance)
  roll_rad_variance, pitch_rad_variance, yaw_rad_variance = imu.get('rpy-var')

  print('stored roll_angle_variance =', roll_rad_variance)
  print('stored pitch_angle_variance =', pitch_rad_variance)
  print('stored yaw_angle_variance =', yaw_rad_variance)
  print("")