# sic_mpu9250_setup_py_codes
This is a child project of the **`sic_mpu9250`** project. it consist of a set of step by step codes to help calibrate, compute necessary covariances, and visualize the filtered readings of the IMU (`MPU9250 module`) connected to the **sic_mpu9250_driver module**. The application codes requires that you have the **`sic_mpu9250_driver module`** connected to your PC via the FTDI programmer for USB serial communication.


## Run The Codes
- Ensure you have python3 installed on your PC

- Download (by clicking on the green Code button above) or clone the repo into your PC
	> you can use this command if you want to clone the repo:
  >
	>  ```git clone https://github.com/samuko-things-company/smc_app.git``` 

- Ensure you have the **`smc_l298n_pid_driver module`** interfaced with your preferred motors and connected to the PC.

- Install the following python packages before you run the application
	> PySerial:
	> ```pip3 install pyserial``` 
  >
	> Matplotlib:
	>  ```pip3 install matplotlib``` 
  >
  > Vpython:
	>  ```pip3 install vpython``` 

- ensure it is the calibration code that is running in the driver module (i.e you should see the blue LED turn on). if not, upload it. It also comes by default with the module.

- Connect the driver to your PC and run each step by step code 0 to 6 to calibrate and setup the IMU. the `_vizualize_rpy_data.py` and `_plot_rpy_data.py` codes will not work with the calibration code, only the ros2 package works with the calibration code.

- you can now use it with your ros2 project using the [sic_mpu9250_ros2_imu_tools](https://github.com/samuko-things-company/sic_mpu9250_ros2_imu_tools)  package.

- to run the `_vizualize_rpy_data.py` and `_plot_rpy_data.py` code as well as use with your arduino project, the kalman filter code from the driver code must be uploaded to the module. you should see the green LED turn on
