# sic_mpu9250_setup_py_codes
This is a child project of the **`sic_mpu9250`** project. it consist of a set of step by step codes to help calibrate, compute necessary covariances, and visualize the filtered readings of the IMU (`MPU9250 module`) connected to the **sic_mpu9250_driver module**. The application codes requires that you have the **`sic_mpu9250_driver module`** connected to your PC via the FTDI programmer for USB serial communication.


## Run The Codes
- Ensure you have python3 installed on your PC

- Download (by clicking on the green Code button above) or clone the repo into your PC
	> you can use this command if you want to clone the repo:
  >
	>  ```git clone https://github.com/samuko-things-company/sic_mpu9250_setup_py_codes.git``` 

- Install the following python packages before you run the application codes
	> PySerial:
	> ```pip3 install pyserial``` 
  >
	> Matplotlib:
	>  ```pip3 install matplotlib``` 
  >
  > Vpython:
	>  ```pip3 install vpython``` 

- Connect the driver to your PC and run each step by step code to calibrate and setup the IMU.
  > **NOTE:** the `mode1` codes require that the `calibration code` is uploaded and running on the sic_mpu9250_driver module (i.e you should see the blue LED turned on).

  > **NOTE:** the `mode2` codes require that the `madgwick filter code` is uploaded and running on the sic_mpu9250_driver module (i.e you should see the green LED turned on).

- after complete setup, you should leave the `madgwick filter code` (i.e **MODE 2**) running on the sic_mpu9250_driver module.

- with the `madgwick filter code` (i.e **MODE 2**) uploaded and running on the driver module, you can use it with your prefered library - `sic_mpu9250_ros` or `sic_mpu9250_i2c_lib` or `sic_mpu9250_pyserial_lib` or `sic_mpu9250_cppserial_lib`.
