# sic_calibration_py_codes
This is a child project of the Samuko IMU Compute (**`sic`**) project. it consist of a set of step by step codes to help calibrate, compute necessary covariances, and visualize the filtered readings of the IMU (`MPU9250 module`) connected to the **sic_mpu9250_driver module**. The application codes requires that you have the **`sic_mpu9250_driver module`** connected to your PC via the FTDI programmer for USB serial communication.


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

- Connect the driver to your PC and run each code step by step to calibrate and setup the IMU.
