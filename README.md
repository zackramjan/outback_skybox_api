# Outback Skybox API
### zackramjan 2021-08-22

Access and control Outback Skybox Hybrid Solar inverter via python API. Getting data from the skybox is suprisingly easy since it uses a simple rest interface. 





# Skybox API Reference
## battery_connected
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_connected is ' + status['battery_connected'])
```
> the value of battery_connected is false

### Description
**type:** boolean<br/>
**default:** true<br/>


## battery_state_of_charge
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_state_of_charge is ' + status['battery_state_of_charge'])
```
> the value of battery_state_of_charge is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_PERCENT<br/>
**decimalScale:** 0<br/>


## battery_temperature
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_temperature is ' + status['battery_temperature'])
```
> the value of battery_temperature is 9.9900000000E+02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_CELSIUS<br/>
**decimalScale:** 2<br/>


## battery_voltage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_voltage is ' + status['battery_voltage'])
```
> the value of battery_voltage is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLTAGE<br/>
**decimalScale:** 1<br/>


## battery_watts
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_watts is ' + status['battery_watts'])
```
> the value of battery_watts is -0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 1<br/>


## firmware_ui_action_enable_apply_sdcard_update
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of firmware_ui_action_enable_apply_sdcard_update is ' + status['firmware_ui_action_enable_apply_sdcard_update'])
```
> the value of firmware_ui_action_enable_apply_sdcard_update is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## firmware_ui_action_enable_apply_usb_update
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of firmware_ui_action_enable_apply_usb_update is ' + status['firmware_ui_action_enable_apply_usb_update'])
```
> the value of firmware_ui_action_enable_apply_usb_update is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## firmware_ui_action_enable_download_server_update
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of firmware_ui_action_enable_download_server_update is ' + status['firmware_ui_action_enable_download_server_update'])
```
> the value of firmware_ui_action_enable_download_server_update is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## firmware_usb_present
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of firmware_usb_present is ' + status['firmware_usb_present'])
```
> the value of firmware_usb_present is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## generator_l1_voltage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l1_voltage is ' + status['generator_l1_voltage'])
```
> the value of generator_l1_voltage is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT<br/>
**decimalScale:** 2<br/>


## generator_l1_wattage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l1_wattage is ' + status['generator_l1_wattage'])
```
> the value of generator_l1_wattage is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## generator_l2_voltage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l2_voltage is ' + status['generator_l2_voltage'])
```
> the value of generator_l2_voltage is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT<br/>
**decimalScale:** 2<br/>


## generator_l2_wattage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l2_wattage is ' + status['generator_l2_wattage'])
```
> the value of generator_l2_wattage is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## generator_l3_voltage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l3_voltage is ' + status['generator_l3_voltage'])
```
> the value of generator_l3_voltage is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT<br/>
**decimalScale:** 2<br/>


## generator_l3_wattage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l3_wattage is ' + status['generator_l3_wattage'])
```
> the value of generator_l3_wattage is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## generator_realtime_frequency
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_realtime_frequency is ' + status['generator_realtime_frequency'])
```
> the value of generator_realtime_frequency is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_HERTZ<br/>
**decimalScale:** 2<br/>


## generator_status
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_status is ' + status['generator_status'])
```
> the value of generator_status is 0

### Description
**type:** string<br/>
**default:** 0<br/>
#### Possible Values (Enumeration)
* 0 -> OFF
* 1 -> STARTING
* 2 -> WARMUP
* 3 -> EXERCISING
* 4 -> COOLDOWN
* 5 -> CONNECTED
* 6 -> WAITING
* 7 -> OUT_OF_SPEC


## generator_time_remaining
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_time_remaining is ' + status['generator_time_remaining'])
```
> the value of generator_time_remaining is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MINUTE_SECOND<br/>
**decimalScale:** 0<br/>


## generator_time_running_seconds
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_time_running_seconds is ' + status['generator_time_running_seconds'])
```
> the value of generator_time_running_seconds is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_SECOND<br/>
**decimalScale:** 0<br/>


## generator_wattage_sum
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_wattage_sum is ' + status['generator_wattage_sum'])
```
> the value of generator_wattage_sum is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 1<br/>


## grid_l1_realtime_ac_voltage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l1_realtime_ac_voltage is ' + status['grid_l1_realtime_ac_voltage'])
```
> the value of grid_l1_realtime_ac_voltage is 1.2169999695E+02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT_AC<br/>
**decimalScale:** 2<br/>


## grid_l1_realtime_wattage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l1_realtime_wattage is ' + status['grid_l1_realtime_wattage'])
```
> the value of grid_l1_realtime_wattage is 249

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 1<br/>


## grid_l2_realtime_ac_voltage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l2_realtime_ac_voltage is ' + status['grid_l2_realtime_ac_voltage'])
```
> the value of grid_l2_realtime_ac_voltage is 1.1959999847E+02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT_AC<br/>
**decimalScale:** 2<br/>


## grid_l2_realtime_wattage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l2_realtime_wattage is ' + status['grid_l2_realtime_wattage'])
```
> the value of grid_l2_realtime_wattage is -234

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 1<br/>


## grid_l3_realtime_ac_voltage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l3_realtime_ac_voltage is ' + status['grid_l3_realtime_ac_voltage'])
```
> the value of grid_l3_realtime_ac_voltage is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT_AC<br/>
**decimalScale:** 2<br/>


## grid_l3_realtime_wattage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l3_realtime_wattage is ' + status['grid_l3_realtime_wattage'])
```
> the value of grid_l3_realtime_wattage is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 1<br/>


## grid_realtime_frequency
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_realtime_frequency is ' + status['grid_realtime_frequency'])
```
> the value of grid_realtime_frequency is 5.9986999512E+01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_HERTZ<br/>
**decimalScale:** 2<br/>


## grid_realtime_wattage_sum
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_realtime_wattage_sum is ' + status['grid_realtime_wattage_sum'])
```
> the value of grid_realtime_wattage_sum is 15

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 1<br/>


## grid_sell_reconnect_timer
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_sell_reconnect_timer is ' + status['grid_sell_reconnect_timer'])
```
> the value of grid_sell_reconnect_timer is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MINUTE_SECOND<br/>
**decimalScale:** 0<br/>


## grid_status
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_status is ' + status['grid_status'])
```
> the value of grid_status is 3

### Description
**type:** string<br/>
**default:** 0<br/>
#### Possible Values (Enumeration)
* 0 -> OFF_GRID
* 1 -> OUT_OF_SPEC
* 2 -> WAITING_TO_CONNECT
* 3 -> GRID_ZERO
* 4 -> DROPPED
* 5 -> CONNECTED


## inverter_current_status
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_current_status is ' + status['inverter_current_status'])
```
> the value of inverter_current_status is 1

### Description
**type:** string<br/>
**default:** 0<br/>
#### Possible Values (Enumeration)
* 0 -> OFF
* 1 -> NORMAL
* 2 -> OVER_TEMP
* 3 -> UNDER_TEMP
* 4 -> FAULT


## inverter_event_ac_disconnect
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_event_ac_disconnect is ' + status['inverter_event_ac_disconnect'])
```
> the value of inverter_event_ac_disconnect is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## inverter_event_ac_over_volt
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_event_ac_over_volt is ' + status['inverter_event_ac_over_volt'])
```
> the value of inverter_event_ac_over_volt is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## inverter_event_ac_under_volt
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_event_ac_under_volt is ' + status['inverter_event_ac_under_volt'])
```
> the value of inverter_event_ac_under_volt is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## inverter_event_blown_string_fuse
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_event_blown_string_fuse is ' + status['inverter_event_blown_string_fuse'])
```
> the value of inverter_event_blown_string_fuse is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## inverter_event_cabinet_open
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_event_cabinet_open is ' + status['inverter_event_cabinet_open'])
```
> the value of inverter_event_cabinet_open is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## inverter_event_dc_disconnect
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_event_dc_disconnect is ' + status['inverter_event_dc_disconnect'])
```
> the value of inverter_event_dc_disconnect is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## inverter_event_dc_over_volt
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_event_dc_over_volt is ' + status['inverter_event_dc_over_volt'])
```
> the value of inverter_event_dc_over_volt is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## inverter_event_grid_disconnect
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_event_grid_disconnect is ' + status['inverter_event_grid_disconnect'])
```
> the value of inverter_event_grid_disconnect is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## inverter_event_ground_fault
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_event_ground_fault is ' + status['inverter_event_ground_fault'])
```
> the value of inverter_event_ground_fault is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## inverter_event_hardware_test_failure
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_event_hardware_test_failure is ' + status['inverter_event_hardware_test_failure'])
```
> the value of inverter_event_hardware_test_failure is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## inverter_event_manual_shutdown
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_event_manual_shutdown is ' + status['inverter_event_manual_shutdown'])
```
> the value of inverter_event_manual_shutdown is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## inverter_event_memory_loss
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_event_memory_loss is ' + status['inverter_event_memory_loss'])
```
> the value of inverter_event_memory_loss is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## inverter_event_over_frequency
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_event_over_frequency is ' + status['inverter_event_over_frequency'])
```
> the value of inverter_event_over_frequency is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## inverter_event_over_temp
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_event_over_temp is ' + status['inverter_event_over_temp'])
```
> the value of inverter_event_over_temp is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## inverter_event_under_frequency
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_event_under_frequency is ' + status['inverter_event_under_frequency'])
```
> the value of inverter_event_under_frequency is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## inverter_event_under_temp
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_event_under_temp is ' + status['inverter_event_under_temp'])
```
> the value of inverter_event_under_temp is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## inverter_fault_status_battery_input
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_fault_status_battery_input is ' + status['inverter_fault_status_battery_input'])
```
> the value of inverter_fault_status_battery_input is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## inverter_fault_status_battery_other
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_fault_status_battery_other is ' + status['inverter_fault_status_battery_other'])
```
> the value of inverter_fault_status_battery_other is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## inverter_fault_status_battery_output
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_fault_status_battery_output is ' + status['inverter_fault_status_battery_output'])
```
> the value of inverter_fault_status_battery_output is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## inverter_fault_status_generator_input
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_fault_status_generator_input is ' + status['inverter_fault_status_generator_input'])
```
> the value of inverter_fault_status_generator_input is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## inverter_fault_status_generator_other
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_fault_status_generator_other is ' + status['inverter_fault_status_generator_other'])
```
> the value of inverter_fault_status_generator_other is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## inverter_fault_status_generator_output
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_fault_status_generator_output is ' + status['inverter_fault_status_generator_output'])
```
> the value of inverter_fault_status_generator_output is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## inverter_fault_status_grid_input
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_fault_status_grid_input is ' + status['inverter_fault_status_grid_input'])
```
> the value of inverter_fault_status_grid_input is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## inverter_fault_status_grid_other
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_fault_status_grid_other is ' + status['inverter_fault_status_grid_other'])
```
> the value of inverter_fault_status_grid_other is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## inverter_fault_status_grid_output
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_fault_status_grid_output is ' + status['inverter_fault_status_grid_output'])
```
> the value of inverter_fault_status_grid_output is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## inverter_fault_status_load_input
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_fault_status_load_input is ' + status['inverter_fault_status_load_input'])
```
> the value of inverter_fault_status_load_input is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## inverter_fault_status_load_other
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_fault_status_load_other is ' + status['inverter_fault_status_load_other'])
```
> the value of inverter_fault_status_load_other is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## inverter_fault_status_load_output
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_fault_status_load_output is ' + status['inverter_fault_status_load_output'])
```
> the value of inverter_fault_status_load_output is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## inverter_fault_status_solar_input
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_fault_status_solar_input is ' + status['inverter_fault_status_solar_input'])
```
> the value of inverter_fault_status_solar_input is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## inverter_fault_status_solar_other
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_fault_status_solar_other is ' + status['inverter_fault_status_solar_other'])
```
> the value of inverter_fault_status_solar_other is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## inverter_fault_status_solar_output
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_fault_status_solar_output is ' + status['inverter_fault_status_solar_output'])
```
> the value of inverter_fault_status_solar_output is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## inverter_operating_state_generic
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_operating_state_generic is ' + status['inverter_operating_state_generic'])
```
> the value of inverter_operating_state_generic is 1

### Description
**type:** string<br/>
**default:** 1<br/>
#### Possible Values (Enumeration)
* 1 -> OFF
* 2 -> SLEEPING
* 3 -> STARTING
* 4 -> MPPT
* 5 -> THROTTLED
* 6 -> SHUTTING_DOWN
* 7 -> FAULT
* 8 -> STANDBY


## inverter_paralleling_units_discovered
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of inverter_paralleling_units_discovered is ' + status['inverter_paralleling_units_discovered'])
```
> the value of inverter_paralleling_units_discovered is 1

### Description
**type:** number<br/>
**default:** 1<br/>
**decimalScale:** 0<br/>


## load_combined_l1_wattage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_combined_l1_wattage is ' + status['load_combined_l1_wattage'])
```
> the value of load_combined_l1_wattage is 74

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## load_combined_l2_wattage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_combined_l2_wattage is ' + status['load_combined_l2_wattage'])
```
> the value of load_combined_l2_wattage is 548

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## load_combined_l3_wattage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_combined_l3_wattage is ' + status['load_combined_l3_wattage'])
```
> the value of load_combined_l3_wattage is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## load_combined_wattage_sum
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_combined_wattage_sum is ' + status['load_combined_wattage_sum'])
```
> the value of load_combined_wattage_sum is 622

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## load_realtime_frequency
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_realtime_frequency is ' + status['load_realtime_frequency'])
```
> the value of load_realtime_frequency is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_HERTZ<br/>
**decimalScale:** 2<br/>


## load_status
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_status is ' + status['load_status'])
```
> the value of load_status is 1

### Description
**type:** string<br/>
**default:** 0<br/>
#### Possible Values (Enumeration)
* 0 -> OFF
* 1 -> POWERED
* 2 -> SUPPORT
* 3 -> PASS_THROUGH
* 4 -> AC_COUPLE


## network_optics_status
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of network_optics_status is ' + status['network_optics_status'])
```
> the value of network_optics_status is 0

### Description
**type:** string<br/>
**default:** 0<br/>
#### Possible Values (Enumeration)
* 0 -> DISABLED
* 1 -> CONNECTING
* 2 -> CONNECTED
* 3 -> SYNCHING
* 4 -> ERROR_TIMEOUT
* 5 -> ERROR_COMM_FAILURE


## network_placeholder_skybox_count
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of network_placeholder_skybox_count is ' + status['network_placeholder_skybox_count'])
```
> the value of network_placeholder_skybox_count is 1

### Description
**type:** number<br/>
**default:** 1<br/>
**decimalScale:** 0<br/>


## pv_input_power
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_input_power is ' + status['pv_input_power'])
```
> the value of pv_input_power is 7.5827526855E+02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 1<br/>


## pv_kwh_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_kwh_today is ' + status['pv_kwh_today'])
```
> the value of pv_kwh_today is 5.1325979233E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## pv_max_voc_date_time_of_occurrence
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_max_voc_date_time_of_occurrence is ' + status['pv_max_voc_date_time_of_occurrence'])
```
> the value of pv_max_voc_date_time_of_occurrence is 1431518123

### Description
**type:** number<br/>
**default:** 0<br/>


## pv_max_voc_voltage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_max_voc_voltage is ' + status['pv_max_voc_voltage'])
```
> the value of pv_max_voc_voltage is 5.5240002441E+02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT_DC<br/>
**decimalScale:** 2<br/>


## pv_mwh_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_mwh_lifetime is ' + status['pv_mwh_lifetime'])
```
> the value of pv_mwh_lifetime is 1.7283636332E-01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## pv_peak_power_date_time
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_peak_power_date_time is ' + status['pv_peak_power_date_time'])
```
> the value of pv_peak_power_date_time is 1628877005

### Description
**type:** number<br/>
**default:** 0<br/>


## pv_peak_power_wattage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_peak_power_wattage is ' + status['pv_peak_power_wattage'])
```
> the value of pv_peak_power_wattage is 3.7113469238E+03

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_WATT<br/>
**decimalScale:** 2<br/>


## pv_status
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_status is ' + status['pv_status'])
```
> the value of pv_status is 1

### Description
**type:** string<br/>
**default:** 0<br/>
#### Possible Values (Enumeration)
* 0 -> NONE
* 1 -> PRODUCING
* 2 -> WAITING
* 3 -> SLEEPING
* 4 -> FAULT
* 5 -> SWEEPING
* 6 -> TESTING


## schema_version_number
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of schema_version_number is ' + status['schema_version_number'])
```
> the value of schema_version_number is 27

### Description
**type:** string<br/>
**default:** 27<br/>


## time_stamp
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of time_stamp is ' + status['time_stamp'])
```
> the value of time_stamp is 2021-08-22 10:54:53

### Description
**type:** string<br/>
**default:** 0<br/>


## time_stamp_utc
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of time_stamp_utc is ' + status['time_stamp_utc'])
```
> the value of time_stamp_utc is 1629629693

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_SECOND<br/>
**decimalScale:** 0<br/>









