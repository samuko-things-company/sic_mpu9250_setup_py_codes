import time
from sic_mpu9250_serial_comm import SIC # samuko IMU compute


# portName = '/dev/ttyACM0'
portName = '/dev/ttyUSB0'
imu = SIC(portName)


for i in range(5):
  time.sleep(1.0)
  print(i+1, " sec")


def main():
  isSuccessful = imu.send("reset")
  if isSuccessful:
    print("\nSUCCESS: parameters reset successful\nrestart the imu cct to see effect.\n")
  else:
    print("\nERROR: parameters reset not successful\n")


if __name__ == "__main__":
  # check if it's the calibration code running
  mode = int(imu.get("mode"))
  try:
    if mode == 1:
      main()
    else:
      raise Exception("ERROR: Cannot Excecute Code, Upload Calibration Code")
  except Exception as e:
    print(e)
  