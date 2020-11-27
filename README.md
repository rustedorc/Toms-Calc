# SUVAT

Simple SUVAT solver made in python to improve my own understanding of the topic

## Getting Started

### Dependencies

* Python 3
* Any OS

### Installing

* Cba to upload to Pypi at this moment in time
* Download python file and place it in same directory as file you want to import to

### Executing program

* Type the following command into your python project or console:
```
from Suvat import SUVAT
```
* Create an instance and add the values you know; for example:
```
Question1 = SUVAT(U=20,T=70,A=9.8)
```
* Use the 'Find' function to automatically solve all unknowns:
```
Question1.Find()
```
* You can also manually enter the equations using the following functions:
```
instance_name.v_equals_u_plus_at()
instance_name.v_squared_equals_u_squared_plus_2as()
instance_name.s_equals_ut_plus_half_at_squared()
instance_name.s_equals_vt_minus_half_at_squared()
instance_name.s_equals_half_u_plus_v_t()
```
## Help

You must a mininum of 3 known values for this to find the two unknowns

If you want any help or want to help improve this code feel free to message me.

## Authors

Contributors names and contact info

Thomas Moldon
[My website](https://moldon.me)

## Version History
* 0.1
    * Initial Release
* 0.2
    * Completed Find() function
* 0.3
    * Fully completed 'Suvat.py'

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details
