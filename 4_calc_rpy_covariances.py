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

roll_rad_arr = []
pitch_rad_arr = []
yaw_rad_arr = []


if __name__ == "__main__":
  for i in range(no_of_samples):
    r_rad, p_rad, y_rad = imu.get('rpy-rad')
    roll_rad_arr.append(r_rad)
    pitch_rad_arr.append(p_rad)
    yaw_rad_arr.append(y_rad)

    percent = (i*100)/no_of_samples
    print("reading_sensor_data...  ", percent, " percent complete")

    time.sleep(0.02)
  
  roll_rad_variance = np.var(roll_rad_arr)
  pitch_rad_variance = np.var(pitch_rad_arr)
  yaw_rad_variance = np.var(yaw_rad_arr)

  print('computed roll_angle_variance =', roll_rad_variance)
  print('computed pitch_angle_variance =', pitch_rad_variance)
  print('computed yaw_angle_variance =', yaw_rad_variance)
  print("")

  imu.send('r-ang-var', roll_rad_variance)
  imu.send('p-ang-var', pitch_rad_variance)
  imu.send('y-ang-var', yaw_rad_variance)
  roll_rad_variance, pitch_rad_variance, yaw_rad_variance = imu.get('rpy-ang-var')

  print('stored roll_angle_variance =', roll_rad_variance)
  print('stored pitch_angle_variance =', pitch_rad_variance)
  print('stored yaw_angle_variance =', yaw_rad_variance)
  print("")