# Outback Skybox API
### zackramjan 2021-08-22

Access and control Outback Skybox Hybrid Solar inverter via python API. Getting data from the skybox is suprisingly easy since it uses a simple rest interface. 

In terms of current functionality, you can:
* login in with the default or custom password
* read most metrics 
* read alerts
* read notices

A next step for this project would be to write or change settings. For example, force the battery to charge


the following snippet shows the basics:
```python
    import json
    import SkyboxAPI
    # make sure you have enabled remote login in Global Settings -> System -> Remote Security -> Enable Remote Login. 
    s = SkyboxAPI.SkyboxAPI()

    # The web interface will be running on port 3000. you can check your skybox IP address on the skybox in the Global Settings -> Network
    # It will attempt to use the outback default remote access account of username = "I" and password = "skybox"
    # You can change this to a custom userename password like this:
    # loginStatus = s.login("http://192.168.1.142:3000","I","mypassword") 
    # this will log you into the skybox and allow you to perform further inquiries
    loginStatus = s.login("http://192.168.1.142:3000") 
    # optionally, we can save and print the login status 
    # loginStatus = s.login("http://192.168.1.142:3000") 
    # print(loginStatus)
    
    # Lets get the current status and print a few metrics
    status = s.getStatus()

    # display the status of the pv input
    # the status is a value from 0 to 6
    print(status['pv_status'])

    # for every 'metric', there is usually a corresponding 'metric_property' which describes the range of values the metric returns.
    # here we can see that 1 means "producing" and 3 means "sleeping"
    print(status['pv_status_property'])
    
    # get and print the Alerts, these are the red-marked alerts from the skybox graphical interface
    # Also note the timestamps are typically in millisecond epoch time (int), so we can convert them to python datetimes if desired
    for alert in s.getAlerts():
        print(str(alert["fileIndex"]) + " " + str(datetime.datetime.fromtimestamp(int(alert["Timestamp"])/1000))  + "\t" + alert["Message"])

    # get and print the Notifcations, these are the in the "log" section of the skybox graphical interface
    for notifcation in s.getNotifications():
        print(str(notifcation["fileIndex"]) + " " + str(datetime.datetime.fromtimestamp(int(notifcation["Timestamp"])/1000))  + "\t" + notifcation["Message"])
```    


# Sending data to influxDB for visualization in influx/grafana 

**See skyboxInfux.py**

basically, we pull all metrics and then send them to a free cloud instance of influxDB. Your key and influx parameters are specific in the config.json ( see example). In my home setup, I have script running in a docker container (see DockerFile) and uploaded every 10seconds. We use line protocol with influx to keep things simple and straightforward

### Dashboarding on influxdb
One the data is up at influx db, it can be easily viewed as a dashboard. My definition is in influxDashboard.json and looks like the following:
![alt text](https://github.com/zackramjan/outback_skybox_api/blob/main/influxScreenshot.png?raw=true)


# Skybox Available Metrics Reference
## battery_absorb_time_remaining
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_absorb_time_remaining is ' + status['battery_absorb_time_remaining'])
```
> the value of battery_absorb_time_remaining is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_HOUR_MINUTE<br/>
**decimalScale:** 0<br/>


## battery_ah_charging_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_ah_charging_today is ' + status['battery_ah_charging_today'])
```
> the value of battery_ah_charging_today is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AH<br/>
**decimalScale:** 2<br/>


## battery_ah_discharging_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_ah_discharging_today is ' + status['battery_ah_discharging_today'])
```
> the value of battery_ah_discharging_today is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AH<br/>
**decimalScale:** 2<br/>


## battery_amps
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_amps is ' + status['battery_amps'])
```
> the value of battery_amps is -3.1682762504E-01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## battery_charge_cycle_count
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_charge_cycle_count is ' + status['battery_charge_cycle_count'])
```
> the value of battery_charge_cycle_count is 2

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## battery_charging_state
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_charging_state is ' + status['battery_charging_state'])
```
> the value of battery_charging_state is 0

### Description
**type:** string<br/>
**default:** 0<br/>
#### Possible Values (Enumeration)
* 0 -> OFF
* 1 -> BULK
* 2 -> ABSORB
* 3 -> FLOAT
* 4 -> FLOAT_CC
* 5 -> FLOAT_CV
* 6 -> EQ
* 7 -> RESTING


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


## battery_days_since_last_equalization
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_days_since_last_equalization is ' + status['battery_days_since_last_equalization'])
```
> the value of battery_days_since_last_equalization is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_DAY<br/>
**decimalScale:** 0<br/>


## battery_days_since_last_full_charge
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_days_since_last_full_charge is ' + status['battery_days_since_last_full_charge'])
```
> the value of battery_days_since_last_full_charge is 16568

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_DAY<br/>
**decimalScale:** 0<br/>


## battery_dc_bus_current
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_dc_bus_current is ' + status['battery_dc_bus_current'])
```
> the value of battery_dc_bus_current is 4.5224554837E-02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## battery_dc_bus_power
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_dc_bus_power is ' + status['battery_dc_bus_power'])
```
> the value of battery_dc_bus_power is 1.2690319061E+01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## battery_dc_bus_voltage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_dc_bus_voltage is ' + status['battery_dc_bus_voltage'])
```
> the value of battery_dc_bus_voltage is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLTAGE<br/>
**decimalScale:** 2<br/>


## battery_discharge_cycle_count
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_discharge_cycle_count is ' + status['battery_discharge_cycle_count'])
```
> the value of battery_discharge_cycle_count is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## battery_eq_time_remaining
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_eq_time_remaining is ' + status['battery_eq_time_remaining'])
```
> the value of battery_eq_time_remaining is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_HOUR_MINUTE<br/>
**decimalScale:** 0<br/>


## battery_float_time_remaining
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_float_time_remaining is ' + status['battery_float_time_remaining'])
```
> the value of battery_float_time_remaining is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_HOUR_MINUTE<br/>
**decimalScale:** 0<br/>


## battery_kah_charging_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_kah_charging_lifetime is ' + status['battery_kah_charging_lifetime'])
```
> the value of battery_kah_charging_lifetime is 5.2830081433E-02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KAH<br/>
**decimalScale:** 2<br/>


## battery_kah_discharging_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_kah_discharging_lifetime is ' + status['battery_kah_discharging_lifetime'])
```
> the value of battery_kah_discharging_lifetime is 4.5308038592E-02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KAH<br/>
**decimalScale:** 2<br/>


## battery_kwh_charging_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_kwh_charging_today is ' + status['battery_kwh_charging_today'])
```
> the value of battery_kwh_charging_today is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## battery_kwh_discharge_cumulative
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_kwh_discharge_cumulative is ' + status['battery_kwh_discharge_cumulative'])
```
> the value of battery_kwh_discharge_cumulative is 2.1133244038E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## battery_kwh_discharging_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_kwh_discharging_today is ' + status['battery_kwh_discharging_today'])
```
> the value of battery_kwh_discharging_today is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## battery_measurement_status
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_measurement_status is ' + status['battery_measurement_status'])
```
> the value of battery_measurement_status is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## battery_mwh_charging_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_mwh_charging_lifetime is ' + status['battery_mwh_charging_lifetime'])
```
> the value of battery_mwh_charging_lifetime is 2.5160906371E-03

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## battery_mwh_discharging_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_mwh_discharging_lifetime is ' + status['battery_mwh_discharging_lifetime'])
```
> the value of battery_mwh_discharging_lifetime is 2.1133245900E-03

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## battery_nameplate_ahrtg
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_nameplate_ahrtg is ' + status['battery_nameplate_ahrtg'])
```
> the value of battery_nameplate_ahrtg is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## battery_nameplate_discharte
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_nameplate_discharte is ' + status['battery_nameplate_discharte'])
```
> the value of battery_nameplate_discharte is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## battery_nameplate_soc_max
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_nameplate_soc_max is ' + status['battery_nameplate_soc_max'])
```
> the value of battery_nameplate_soc_max is 100

### Description
**type:** number<br/>
**default:** 100<br/>
**decimalScale:** 0<br/>


## battery_nameplate_soc_min
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_nameplate_soc_min is ' + status['battery_nameplate_soc_min'])
```
> the value of battery_nameplate_soc_min is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## battery_nameplate_wcharte_max
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_nameplate_wcharte_max is ' + status['battery_nameplate_wcharte_max'])
```
> the value of battery_nameplate_wcharte_max is 5750

### Description
**type:** number<br/>
**default:** 5750<br/>
**decimalScale:** 0<br/>


## battery_nameplate_wdischarte_max
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_nameplate_wdischarte_max is ' + status['battery_nameplate_wdischarte_max'])
```
> the value of battery_nameplate_wdischarte_max is 5000

### Description
**type:** number<br/>
**default:** 5000<br/>
**decimalScale:** 0<br/>


## battery_nameplate_whrtg
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_nameplate_whrtg is ' + status['battery_nameplate_whrtg'])
```
> the value of battery_nameplate_whrtg is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## battery_remaining_runtime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_remaining_runtime is ' + status['battery_remaining_runtime'])
```
> the value of battery_remaining_runtime is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_HOUR_MINUTE<br/>
**decimalScale:** 0<br/>


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


## battery_state_of_charge_historical_minimum
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_state_of_charge_historical_minimum is ' + status['battery_state_of_charge_historical_minimum'])
```
> the value of battery_state_of_charge_historical_minimum is 75

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_PERCENT<br/>
**decimalScale:** 0<br/>


## battery_state_of_health
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_state_of_health is ' + status['battery_state_of_health'])
```
> the value of battery_state_of_health is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_PERCENT<br/>
**decimalScale:** 0<br/>


## battery_suns_bank_state
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_suns_bank_state is ' + status['battery_suns_bank_state'])
```
> the value of battery_suns_bank_state is 1

### Description
**type:** string<br/>
**default:** 1<br/>
#### Possible Values (Enumeration)
* 1 -> DISCONNECTED
* 2 -> INITIALIZING
* 3 -> CONNECTED
* 4 -> STANDBY
* 5 -> SOC_PROTECTION
* 99 -> FAULT


## battery_suns_charging_state
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_suns_charging_state is ' + status['battery_suns_charging_state'])
```
> the value of battery_suns_charging_state is 1

### Description
**type:** string<br/>
**default:** 1<br/>
#### Possible Values (Enumeration)
* 1 -> OFF
* 2 -> EMPTY
* 3 -> DISCHARGING
* 4 -> CHARGING
* 5 -> FULL
* 6 -> HOLDING
* 7 -> TESTING


## battery_suns_type
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_suns_type is ' + status['battery_suns_type'])
```
> the value of battery_suns_type is 0

### Description
**type:** string<br/>
**default:** 0<br/>
#### Possible Values (Enumeration)
* 0 -> UNKNOWN
* 1 -> LEAD_ACID
* 2 -> NICKEL_METAL_HYDRATE
* 3 -> NICKEL_CADMIUM
* 4 -> LITHIUM_ION
* 5 -> CARBON_ZINC
* 6 -> ZINC_CHLORIDE
* 7 -> ALKALINE
* 8 -> RECHARGEABLE_ALKALINE
* 9 -> SODIUM_SULFUR
* 10 -> FLOW
* 99 -> OTHER


## battery_sunspec_event_1
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_sunspec_event_1 is ' + status['battery_sunspec_event_1'])
```
> the value of battery_sunspec_event_1 is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## battery_temp_comp_offset
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_temp_comp_offset is ' + status['battery_temp_comp_offset'])
```
> the value of battery_temp_comp_offset is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLTAGE<br/>
**decimalScale:** 1<br/>


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


## battery_temperature_fet
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_temperature_fet is ' + status['battery_temperature_fet'])
```
> the value of battery_temperature_fet is 35

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_CELSIUS<br/>
**decimalScale:** 0<br/>


## battery_temperature_igbt
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_temperature_igbt is ' + status['battery_temperature_igbt'])
```
> the value of battery_temperature_igbt is 29

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_CELSIUS<br/>
**decimalScale:** 0<br/>


## battery_temperature_mcu_adc
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_temperature_mcu_adc is ' + status['battery_temperature_mcu_adc'])
```
> the value of battery_temperature_mcu_adc is 1967

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## battery_time_since_last_eq
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_time_since_last_eq is ' + status['battery_time_since_last_eq'])
```
> the value of battery_time_since_last_eq is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MINUTE<br/>
**decimalScale:** 0<br/>


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


## battery_voltage_historical_maximum
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_voltage_historical_maximum is ' + status['battery_voltage_historical_maximum'])
```
> the value of battery_voltage_historical_maximum is 5.9306350708E+01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT<br/>
**decimalScale:** 2<br/>


## battery_voltage_historical_minimum
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_voltage_historical_minimum is ' + status['battery_voltage_historical_minimum'])
```
> the value of battery_voltage_historical_minimum is 4.4821647644E+01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT<br/>
**decimalScale:** 2<br/>


## battery_voltage_temp_comp
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of battery_voltage_temp_comp is ' + status['battery_voltage_temp_comp'])
```
> the value of battery_voltage_temp_comp is 0.0000000000E+00

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
**decimalScale:** 2<br/>


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


## generator_ac_current_sum
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_ac_current_sum is ' + status['generator_ac_current_sum'])
```
> the value of generator_ac_current_sum is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## generator_ags_status
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_ags_status is ' + status['generator_ags_status'])
```
> the value of generator_ags_status is 0

### Description
**type:** string<br/>
**default:** 0<br/>
#### Possible Values (Enumeration)
* 0 -> DISABLED
* 1 -> ENABLED
* 2 -> EXERCISE_DEFERRED
* 3 -> QUIET_TIME_DEFERRED


## generator_l1_apparent_power
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l1_apparent_power is ' + status['generator_l1_apparent_power'])
```
> the value of generator_l1_apparent_power is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT_AMPERE<br/>
**decimalScale:** 2<br/>


## generator_l1_current
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l1_current is ' + status['generator_l1_current'])
```
> the value of generator_l1_current is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## generator_l1_dc_current
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l1_dc_current is ' + status['generator_l1_dc_current'])
```
> the value of generator_l1_dc_current is -2.9999999329E-02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## generator_l1_kwh_bought_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l1_kwh_bought_today is ' + status['generator_l1_kwh_bought_today'])
```
> the value of generator_l1_kwh_bought_today is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## generator_l1_kwh_sold_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l1_kwh_sold_today is ' + status['generator_l1_kwh_sold_today'])
```
> the value of generator_l1_kwh_sold_today is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## generator_l1_mwh_bought_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l1_mwh_bought_lifetime is ' + status['generator_l1_mwh_bought_lifetime'])
```
> the value of generator_l1_mwh_bought_lifetime is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## generator_l1_mwh_sold_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l1_mwh_sold_lifetime is ' + status['generator_l1_mwh_sold_lifetime'])
```
> the value of generator_l1_mwh_sold_lifetime is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## generator_l1_power_factor
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l1_power_factor is ' + status['generator_l1_power_factor'])
```
> the value of generator_l1_power_factor is 1.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


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


## generator_l1_voltage_variance_average
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l1_voltage_variance_average is ' + status['generator_l1_voltage_variance_average'])
```
> the value of generator_l1_voltage_variance_average is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## generator_l1_voltage_variance_high
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l1_voltage_variance_high is ' + status['generator_l1_voltage_variance_high'])
```
> the value of generator_l1_voltage_variance_high is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## generator_l1_voltage_variance_low
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l1_voltage_variance_low is ' + status['generator_l1_voltage_variance_low'])
```
> the value of generator_l1_voltage_variance_low is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
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


## generator_l2_apparent_power
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l2_apparent_power is ' + status['generator_l2_apparent_power'])
```
> the value of generator_l2_apparent_power is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT_AMPERE<br/>
**decimalScale:** 2<br/>


## generator_l2_current
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l2_current is ' + status['generator_l2_current'])
```
> the value of generator_l2_current is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## generator_l2_dc_current
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l2_dc_current is ' + status['generator_l2_dc_current'])
```
> the value of generator_l2_dc_current is -1.9999999553E-02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## generator_l2_kwh_bought_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l2_kwh_bought_today is ' + status['generator_l2_kwh_bought_today'])
```
> the value of generator_l2_kwh_bought_today is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## generator_l2_kwh_sold_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l2_kwh_sold_today is ' + status['generator_l2_kwh_sold_today'])
```
> the value of generator_l2_kwh_sold_today is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## generator_l2_mwh_bought_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l2_mwh_bought_lifetime is ' + status['generator_l2_mwh_bought_lifetime'])
```
> the value of generator_l2_mwh_bought_lifetime is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## generator_l2_mwh_sold_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l2_mwh_sold_lifetime is ' + status['generator_l2_mwh_sold_lifetime'])
```
> the value of generator_l2_mwh_sold_lifetime is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## generator_l2_power_factor
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l2_power_factor is ' + status['generator_l2_power_factor'])
```
> the value of generator_l2_power_factor is 1.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
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


## generator_l2_voltage_variance_average
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l2_voltage_variance_average is ' + status['generator_l2_voltage_variance_average'])
```
> the value of generator_l2_voltage_variance_average is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## generator_l2_voltage_variance_high
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l2_voltage_variance_high is ' + status['generator_l2_voltage_variance_high'])
```
> the value of generator_l2_voltage_variance_high is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## generator_l2_voltage_variance_low
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l2_voltage_variance_low is ' + status['generator_l2_voltage_variance_low'])
```
> the value of generator_l2_voltage_variance_low is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
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


## generator_l3_apparent_power
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l3_apparent_power is ' + status['generator_l3_apparent_power'])
```
> the value of generator_l3_apparent_power is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT_AMPERE<br/>
**decimalScale:** 2<br/>


## generator_l3_current
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l3_current is ' + status['generator_l3_current'])
```
> the value of generator_l3_current is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## generator_l3_dc_current
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l3_dc_current is ' + status['generator_l3_dc_current'])
```
> the value of generator_l3_dc_current is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## generator_l3_kwh_bought_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l3_kwh_bought_today is ' + status['generator_l3_kwh_bought_today'])
```
> the value of generator_l3_kwh_bought_today is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## generator_l3_kwh_sold_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l3_kwh_sold_today is ' + status['generator_l3_kwh_sold_today'])
```
> the value of generator_l3_kwh_sold_today is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## generator_l3_mwh_bought_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l3_mwh_bought_lifetime is ' + status['generator_l3_mwh_bought_lifetime'])
```
> the value of generator_l3_mwh_bought_lifetime is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## generator_l3_mwh_sold_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l3_mwh_sold_lifetime is ' + status['generator_l3_mwh_sold_lifetime'])
```
> the value of generator_l3_mwh_sold_lifetime is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## generator_l3_power_factor
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l3_power_factor is ' + status['generator_l3_power_factor'])
```
> the value of generator_l3_power_factor is 1.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
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


## generator_l3_voltage_variance_average
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l3_voltage_variance_average is ' + status['generator_l3_voltage_variance_average'])
```
> the value of generator_l3_voltage_variance_average is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## generator_l3_voltage_variance_high
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l3_voltage_variance_high is ' + status['generator_l3_voltage_variance_high'])
```
> the value of generator_l3_voltage_variance_high is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## generator_l3_voltage_variance_low
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_l3_voltage_variance_low is ' + status['generator_l3_voltage_variance_low'])
```
> the value of generator_l3_voltage_variance_low is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
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


## generator_last_start_reason
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_last_start_reason is ' + status['generator_last_start_reason'])
```
> the value of generator_last_start_reason is 0

### Description
**type:** string<br/>
**default:** 0<br/>
#### Possible Values (Enumeration)
* 0 -> NONE
* 1 -> MANUAL
* 2 -> BATTERY_VOLTAGE
* 3 -> SOC
* 4 -> LOAD
* 5 -> EXERCISE


## generator_last_stop_reason
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_last_stop_reason is ' + status['generator_last_stop_reason'])
```
> the value of generator_last_stop_reason is 0

### Description
**type:** string<br/>
**default:** 0<br/>
#### Possible Values (Enumeration)
* 0 -> NONE
* 1 -> MANUAL
* 2 -> BATTERY_VOLTAGE
* 3 -> SOC
* 4 -> LOAD
* 5 -> EXERCISE


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


## generator_started_date_time
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_started_date_time is ' + status['generator_started_date_time'])
```
> the value of generator_started_date_time is 1970-01-01 00:00:00

### Description
**type:** number<br/>
**default:** 0<br/>


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


## generator_total_lifetime_hours
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_total_lifetime_hours is ' + status['generator_total_lifetime_hours'])
```
> the value of generator_total_lifetime_hours is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_HOUR<br/>
**decimalScale:** 0<br/>


## generator_total_time_running_since_reset_seconds
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of generator_total_time_running_since_reset_seconds is ' + status['generator_total_time_running_since_reset_seconds'])
```
> the value of generator_total_time_running_since_reset_seconds is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_HOUR<br/>
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
**decimalScale:** 2<br/>


## grid_kw_max
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_kw_max is ' + status['grid_kw_max'])
```
> the value of grid_kw_max is 10

### Description
**type:** number<br/>
**default:** 10<br/>
**decimalScale:** 0<br/>


## grid_kw_min
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_kw_min is ' + status['grid_kw_min'])
```
> the value of grid_kw_min is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## grid_l1_apparent_power
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l1_apparent_power is ' + status['grid_l1_apparent_power'])
```
> the value of grid_l1_apparent_power is 7.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT_AMPERE<br/>
**decimalScale:** 2<br/>


## grid_l1_dc_amps
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l1_dc_amps is ' + status['grid_l1_dc_amps'])
```
> the value of grid_l1_dc_amps is 1.9999999553E-02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## grid_l1_kwh_bought_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l1_kwh_bought_today is ' + status['grid_l1_kwh_bought_today'])
```
> the value of grid_l1_kwh_bought_today is 2.1895999908E+01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## grid_l1_kwh_sold_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l1_kwh_sold_today is ' + status['grid_l1_kwh_sold_today'])
```
> the value of grid_l1_kwh_sold_today is 1.6380000114E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## grid_l1_mwh_bought_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l1_mwh_bought_lifetime is ' + status['grid_l1_mwh_bought_lifetime'])
```
> the value of grid_l1_mwh_bought_lifetime is 4.4292870164E-01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## grid_l1_mwh_sold_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l1_mwh_sold_lifetime is ' + status['grid_l1_mwh_sold_lifetime'])
```
> the value of grid_l1_mwh_sold_lifetime is 2.0614467561E-02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## grid_l1_power_factor
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l1_power_factor is ' + status['grid_l1_power_factor'])
```
> the value of grid_l1_power_factor is 1.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## grid_l1_realtime_ac_amps
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l1_realtime_ac_amps is ' + status['grid_l1_realtime_ac_amps'])
```
> the value of grid_l1_realtime_ac_amps is 7.0000000298E-02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## grid_l1_realtime_ac_voltage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l1_realtime_ac_voltage is ' + status['grid_l1_realtime_ac_voltage'])
```
> the value of grid_l1_realtime_ac_voltage is 1.2019999695E+02

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
> the value of grid_l1_realtime_wattage is -2399

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## grid_l1_voltage_variance_average
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l1_voltage_variance_average is ' + status['grid_l1_voltage_variance_average'])
```
> the value of grid_l1_voltage_variance_average is 1.2019999695E+02

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## grid_l1_voltage_variance_high
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l1_voltage_variance_high is ' + status['grid_l1_voltage_variance_high'])
```
> the value of grid_l1_voltage_variance_high is 1.2019999695E+02

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## grid_l1_voltage_variance_low
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l1_voltage_variance_low is ' + status['grid_l1_voltage_variance_low'])
```
> the value of grid_l1_voltage_variance_low is 1.2019999695E+02

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## grid_l2_apparent_power
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l2_apparent_power is ' + status['grid_l2_apparent_power'])
```
> the value of grid_l2_apparent_power is 7.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT_AMPERE<br/>
**decimalScale:** 2<br/>


## grid_l2_dc_amps
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l2_dc_amps is ' + status['grid_l2_dc_amps'])
```
> the value of grid_l2_dc_amps is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## grid_l2_kwh_bought_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l2_kwh_bought_today is ' + status['grid_l2_kwh_bought_today'])
```
> the value of grid_l2_kwh_bought_today is 2.7246999741E+01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## grid_l2_kwh_sold_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l2_kwh_sold_today is ' + status['grid_l2_kwh_sold_today'])
```
> the value of grid_l2_kwh_sold_today is 7.2999998927E-02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## grid_l2_mwh_bought_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l2_mwh_bought_lifetime is ' + status['grid_l2_mwh_bought_lifetime'])
```
> the value of grid_l2_mwh_bought_lifetime is 5.4245275259E-01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## grid_l2_mwh_sold_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l2_mwh_sold_lifetime is ' + status['grid_l2_mwh_sold_lifetime'])
```
> the value of grid_l2_mwh_sold_lifetime is 8.8011128828E-03

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## grid_l2_power_factor
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l2_power_factor is ' + status['grid_l2_power_factor'])
```
> the value of grid_l2_power_factor is 1.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## grid_l2_realtime_ac_amps
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l2_realtime_ac_amps is ' + status['grid_l2_realtime_ac_amps'])
```
> the value of grid_l2_realtime_ac_amps is 5.9999998659E-02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## grid_l2_realtime_ac_voltage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l2_realtime_ac_voltage is ' + status['grid_l2_realtime_ac_voltage'])
```
> the value of grid_l2_realtime_ac_voltage is 1.2050000000E+02

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
> the value of grid_l2_realtime_wattage is -2542

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## grid_l2_voltage_variance_average
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l2_voltage_variance_average is ' + status['grid_l2_voltage_variance_average'])
```
> the value of grid_l2_voltage_variance_average is 1.2050000000E+02

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## grid_l2_voltage_variance_high
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l2_voltage_variance_high is ' + status['grid_l2_voltage_variance_high'])
```
> the value of grid_l2_voltage_variance_high is 1.2050000000E+02

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## grid_l2_voltage_variance_low
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l2_voltage_variance_low is ' + status['grid_l2_voltage_variance_low'])
```
> the value of grid_l2_voltage_variance_low is 1.2050000000E+02

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## grid_l3_apparent_power
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l3_apparent_power is ' + status['grid_l3_apparent_power'])
```
> the value of grid_l3_apparent_power is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT_AMPERE<br/>
**decimalScale:** 2<br/>


## grid_l3_dc_amps
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l3_dc_amps is ' + status['grid_l3_dc_amps'])
```
> the value of grid_l3_dc_amps is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## grid_l3_kwh_bought_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l3_kwh_bought_today is ' + status['grid_l3_kwh_bought_today'])
```
> the value of grid_l3_kwh_bought_today is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## grid_l3_kwh_sold_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l3_kwh_sold_today is ' + status['grid_l3_kwh_sold_today'])
```
> the value of grid_l3_kwh_sold_today is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## grid_l3_mwh_bought_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l3_mwh_bought_lifetime is ' + status['grid_l3_mwh_bought_lifetime'])
```
> the value of grid_l3_mwh_bought_lifetime is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## grid_l3_mwh_sold_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l3_mwh_sold_lifetime is ' + status['grid_l3_mwh_sold_lifetime'])
```
> the value of grid_l3_mwh_sold_lifetime is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## grid_l3_power_factor
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l3_power_factor is ' + status['grid_l3_power_factor'])
```
> the value of grid_l3_power_factor is 1.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## grid_l3_realtime_ac_amps
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l3_realtime_ac_amps is ' + status['grid_l3_realtime_ac_amps'])
```
> the value of grid_l3_realtime_ac_amps is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


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
**decimalScale:** 2<br/>


## grid_l3_voltage_variance_average
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l3_voltage_variance_average is ' + status['grid_l3_voltage_variance_average'])
```
> the value of grid_l3_voltage_variance_average is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## grid_l3_voltage_variance_high
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l3_voltage_variance_high is ' + status['grid_l3_voltage_variance_high'])
```
> the value of grid_l3_voltage_variance_high is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## grid_l3_voltage_variance_low
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_l3_voltage_variance_low is ' + status['grid_l3_voltage_variance_low'])
```
> the value of grid_l3_voltage_variance_low is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## grid_measurement_status
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_measurement_status is ' + status['grid_measurement_status'])
```
> the value of grid_measurement_status is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## grid_realtime_ac_amps_sum
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_realtime_ac_amps_sum is ' + status['grid_realtime_ac_amps_sum'])
```
> the value of grid_realtime_ac_amps_sum is 1.2999999523E-01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## grid_realtime_frequency
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of grid_realtime_frequency is ' + status['grid_realtime_frequency'])
```
> the value of grid_realtime_frequency is 6.0035999298E+01

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
> the value of grid_realtime_wattage_sum is -4941

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


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
> the value of grid_status is 5

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


## load_ac_current_sum
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_ac_current_sum is ' + status['load_ac_current_sum'])
```
> the value of load_ac_current_sum is 1.2999999523E-01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## load_combined_l1_wattage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_combined_l1_wattage is ' + status['load_combined_l1_wattage'])
```
> the value of load_combined_l1_wattage is 2399

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
> the value of load_combined_l2_wattage is 2542

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
> the value of load_combined_wattage_sum is 4941

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## load_consuming_total_kw_max
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_consuming_total_kw_max is ' + status['load_consuming_total_kw_max'])
```
> the value of load_consuming_total_kw_max is 20

### Description
**type:** number<br/>
**default:** 20<br/>
**decimalScale:** 0<br/>


## load_consuming_total_kw_min
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_consuming_total_kw_min is ' + status['load_consuming_total_kw_min'])
```
> the value of load_consuming_total_kw_min is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## load_l1_ac_amps
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l1_ac_amps is ' + status['load_l1_ac_amps'])
```
> the value of load_l1_ac_amps is 1.0999999940E-01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## load_l1_ac_voltage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l1_ac_voltage is ' + status['load_l1_ac_voltage'])
```
> the value of load_l1_ac_voltage is 1.2009999847E+02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT<br/>
**decimalScale:** 2<br/>


## load_l1_apparent_power
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l1_apparent_power is ' + status['load_l1_apparent_power'])
```
> the value of load_l1_apparent_power is 1.4000000000E+01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT_AMPERE<br/>
**decimalScale:** 2<br/>


## load_l1_dc_amps
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l1_dc_amps is ' + status['load_l1_dc_amps'])
```
> the value of load_l1_dc_amps is 1.4800000191E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## load_l1_kwh_consumed_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l1_kwh_consumed_today is ' + status['load_l1_kwh_consumed_today'])
```
> the value of load_l1_kwh_consumed_today is 2.4259000778E+01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## load_l1_kwh_produced_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l1_kwh_produced_today is ' + status['load_l1_kwh_produced_today'])
```
> the value of load_l1_kwh_produced_today is 4.5000001788E-02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## load_l1_mwh_consumed_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l1_mwh_consumed_lifetime is ' + status['load_l1_mwh_consumed_lifetime'])
```
> the value of load_l1_mwh_consumed_lifetime is 5.0568646193E-01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## load_l1_mwh_produced_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l1_mwh_produced_lifetime is ' + status['load_l1_mwh_produced_lifetime'])
```
> the value of load_l1_mwh_produced_lifetime is 8.3800387802E-04

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## load_l1_output_power_factor
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l1_output_power_factor is ' + status['load_l1_output_power_factor'])
```
> the value of load_l1_output_power_factor is 1.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## load_l1_self_supply
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l1_self_supply is ' + status['load_l1_self_supply'])
```
> the value of load_l1_self_supply is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## load_l1_self_supply_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l1_self_supply_lifetime is ' + status['load_l1_self_supply_lifetime'])
```
> the value of load_l1_self_supply_lifetime is 6.6474147141E-02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## load_l1_self_supply_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l1_self_supply_today is ' + status['load_l1_self_supply_today'])
```
> the value of load_l1_self_supply_today is 2.4920001030E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## load_l1_wattage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l1_wattage is ' + status['load_l1_wattage'])
```
> the value of load_l1_wattage is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## load_l2_ac_amps
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l2_ac_amps is ' + status['load_l2_ac_amps'])
```
> the value of load_l2_ac_amps is 1.9999999553E-02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## load_l2_ac_voltage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l2_ac_voltage is ' + status['load_l2_ac_voltage'])
```
> the value of load_l2_ac_voltage is 1.2050000000E+02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT<br/>
**decimalScale:** 2<br/>


## load_l2_apparent_power
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l2_apparent_power is ' + status['load_l2_apparent_power'])
```
> the value of load_l2_apparent_power is 3.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT_AMPERE<br/>
**decimalScale:** 2<br/>


## load_l2_dc_amps
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l2_dc_amps is ' + status['load_l2_dc_amps'])
```
> the value of load_l2_dc_amps is 3.3000001311E-01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## load_l2_kwh_consumed_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l2_kwh_consumed_today is ' + status['load_l2_kwh_consumed_today'])
```
> the value of load_l2_kwh_consumed_today is 3.1077999115E+01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## load_l2_kwh_produced_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l2_kwh_produced_today is ' + status['load_l2_kwh_produced_today'])
```
> the value of load_l2_kwh_produced_today is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## load_l2_mwh_consumed_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l2_mwh_consumed_lifetime is ' + status['load_l2_mwh_consumed_lifetime'])
```
> the value of load_l2_mwh_consumed_lifetime is 6.1500924826E-01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## load_l2_mwh_produced_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l2_mwh_produced_lifetime is ' + status['load_l2_mwh_produced_lifetime'])
```
> the value of load_l2_mwh_produced_lifetime is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## load_l2_output_power_factor
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l2_output_power_factor is ' + status['load_l2_output_power_factor'])
```
> the value of load_l2_output_power_factor is 1.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## load_l2_self_supply
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l2_self_supply is ' + status['load_l2_self_supply'])
```
> the value of load_l2_self_supply is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## load_l2_self_supply_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l2_self_supply_lifetime is ' + status['load_l2_self_supply_lifetime'])
```
> the value of load_l2_self_supply_lifetime is 7.6204463840E-02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## load_l2_self_supply_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l2_self_supply_today is ' + status['load_l2_self_supply_today'])
```
> the value of load_l2_self_supply_today is 3.9549999237E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## load_l2_wattage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l2_wattage is ' + status['load_l2_wattage'])
```
> the value of load_l2_wattage is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## load_l3_ac_amps
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l3_ac_amps is ' + status['load_l3_ac_amps'])
```
> the value of load_l3_ac_amps is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## load_l3_ac_voltage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l3_ac_voltage is ' + status['load_l3_ac_voltage'])
```
> the value of load_l3_ac_voltage is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT<br/>
**decimalScale:** 2<br/>


## load_l3_apparent_power
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l3_apparent_power is ' + status['load_l3_apparent_power'])
```
> the value of load_l3_apparent_power is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT_AMPERE<br/>
**decimalScale:** 2<br/>


## load_l3_dc_amps
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l3_dc_amps is ' + status['load_l3_dc_amps'])
```
> the value of load_l3_dc_amps is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## load_l3_kwh_consumed_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l3_kwh_consumed_today is ' + status['load_l3_kwh_consumed_today'])
```
> the value of load_l3_kwh_consumed_today is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## load_l3_kwh_produced_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l3_kwh_produced_today is ' + status['load_l3_kwh_produced_today'])
```
> the value of load_l3_kwh_produced_today is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## load_l3_mwh_consumed_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l3_mwh_consumed_lifetime is ' + status['load_l3_mwh_consumed_lifetime'])
```
> the value of load_l3_mwh_consumed_lifetime is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## load_l3_mwh_produced_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l3_mwh_produced_lifetime is ' + status['load_l3_mwh_produced_lifetime'])
```
> the value of load_l3_mwh_produced_lifetime is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## load_l3_output_power_factor
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l3_output_power_factor is ' + status['load_l3_output_power_factor'])
```
> the value of load_l3_output_power_factor is 1.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## load_l3_self_supply
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l3_self_supply is ' + status['load_l3_self_supply'])
```
> the value of load_l3_self_supply is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## load_l3_self_supply_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l3_self_supply_lifetime is ' + status['load_l3_self_supply_lifetime'])
```
> the value of load_l3_self_supply_lifetime is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## load_l3_self_supply_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l3_self_supply_today is ' + status['load_l3_self_supply_today'])
```
> the value of load_l3_self_supply_today is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## load_l3_wattage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_l3_wattage is ' + status['load_l3_wattage'])
```
> the value of load_l3_wattage is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## load_percentage_inverter_capacity
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_percentage_inverter_capacity is ' + status['load_percentage_inverter_capacity'])
```
> the value of load_percentage_inverter_capacity is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_PERCENT<br/>
**decimalScale:** 0<br/>


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
> the value of load_status is 3

### Description
**type:** string<br/>
**default:** 0<br/>
#### Possible Values (Enumeration)
* 0 -> OFF
* 1 -> POWERED
* 2 -> SUPPORT
* 3 -> PASS_THROUGH
* 4 -> AC_COUPLE


## load_total_self_supply
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_total_self_supply is ' + status['load_total_self_supply'])
```
> the value of load_total_self_supply is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## load_total_self_supply_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_total_self_supply_lifetime is ' + status['load_total_self_supply_lifetime'])
```
> the value of load_total_self_supply_lifetime is 1.5148065984E-01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## load_total_self_supply_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_total_self_supply_today is ' + status['load_total_self_supply_today'])
```
> the value of load_total_self_supply_today is 7.7899999619E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KWH<br/>
**decimalScale:** 2<br/>


## load_unprotected_l1_wattage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_unprotected_l1_wattage is ' + status['load_unprotected_l1_wattage'])
```
> the value of load_unprotected_l1_wattage is 2399

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## load_unprotected_l2_wattage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_unprotected_l2_wattage is ' + status['load_unprotected_l2_wattage'])
```
> the value of load_unprotected_l2_wattage is 2542

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## load_unprotected_l3_wattage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_unprotected_l3_wattage is ' + status['load_unprotected_l3_wattage'])
```
> the value of load_unprotected_l3_wattage is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## load_wattage_sum
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of load_wattage_sum is ' + status['load_wattage_sum'])
```
> the value of load_wattage_sum is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


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


## pv_array_temperature_realtime_celsius
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_array_temperature_realtime_celsius is ' + status['pv_array_temperature_realtime_celsius'])
```
> the value of pv_array_temperature_realtime_celsius is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_CELSIUS<br/>
**decimalScale:** 0<br/>


## pv_bb_input_voltage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_bb_input_voltage is ' + status['pv_bb_input_voltage'])
```
> the value of pv_bb_input_voltage is 5.5334889889E-01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT<br/>
**decimalScale:** 2<br/>


## pv_input_current
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_input_current is ' + status['pv_input_current'])
```
> the value of pv_input_current is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## pv_input_power
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_input_power is ' + status['pv_input_power'])
```
> the value of pv_input_power is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**scalingFactor:** 0.001<br/>
**decimalScale:** 2<br/>


## pv_kwh_today
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_kwh_today is ' + status['pv_kwh_today'])
```
> the value of pv_kwh_today is 9.1020164490E+00

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


## pv_measurement_status
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_measurement_status is ' + status['pv_measurement_status'])
```
> the value of pv_measurement_status is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## pv_mpp_state
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_mpp_state is ' + status['pv_mpp_state'])
```
> the value of pv_mpp_state is 0

### Description
**type:** string<br/>
**default:** 0<br/>
#### Possible Values (Enumeration)
* 0 -> OFF
* 1 -> TRACKING
* 2 -> NETZERO
* 3 -> POWER_LIMITED


## pv_mwh_lifetime
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_mwh_lifetime is ' + status['pv_mwh_lifetime'])
```
> the value of pv_mwh_lifetime is 1.8664027750E-01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_MWH<br/>
**decimalScale:** 2<br/>


## pv_output_current_dc
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_output_current_dc is ' + status['pv_output_current_dc'])
```
> the value of pv_output_current_dc is 2.9377471656E-02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_AMPERE<br/>
**decimalScale:** 2<br/>


## pv_output_power_dc
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_output_power_dc is ' + status['pv_output_power_dc'])
```
> the value of pv_output_power_dc is 9.0553846359E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_KW<br/>
**decimalScale:** 2<br/>


## pv_output_voltage_dc
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_output_voltage_dc is ' + status['pv_output_voltage_dc'])
```
> the value of pv_output_voltage_dc is 3.0842050171E+02

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT<br/>
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


## pv_pmb_ird_ratio_a
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_pmb_ird_ratio_a is ' + status['pv_pmb_ird_ratio_a'])
```
> the value of pv_pmb_ird_ratio_a is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## pv_pmb_ird_ratio_b
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_pmb_ird_ratio_b is ' + status['pv_pmb_ird_ratio_b'])
```
> the value of pv_pmb_ird_ratio_b is 0.0000000000E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 2<br/>


## pv_pmb_positive_voltage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_pmb_positive_voltage is ' + status['pv_pmb_positive_voltage'])
```
> the value of pv_pmb_positive_voltage is 8.1999998093E+00

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT<br/>
**decimalScale:** 2<br/>


## pv_pmb_voltage
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_pmb_voltage is ' + status['pv_pmb_voltage'])
```
> the value of pv_pmb_voltage is 1.5100000381E+01

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_VOLT<br/>
**decimalScale:** 2<br/>


## pv_production_realtime_kw_max
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_production_realtime_kw_max is ' + status['pv_production_realtime_kw_max'])
```
> the value of pv_production_realtime_kw_max is 6

### Description
**type:** number<br/>
**default:** 6<br/>
**decimalScale:** 0<br/>


## pv_production_realtime_kw_min
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_production_realtime_kw_min is ' + status['pv_production_realtime_kw_min'])
```
> the value of pv_production_realtime_kw_min is 0

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## pv_status
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_status is ' + status['pv_status'])
```
> the value of pv_status is 3

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


## pv_temperature_bb
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_temperature_bb is ' + status['pv_temperature_bb'])
```
> the value of pv_temperature_bb is 37

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_CELSIUS<br/>
**decimalScale:** 0<br/>


## pv_temperature_inductor
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_temperature_inductor is ' + status['pv_temperature_inductor'])
```
> the value of pv_temperature_inductor is 37

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_CELSIUS<br/>
**decimalScale:** 0<br/>


## pv_temperature_lenso
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of pv_temperature_lenso is ' + status['pv_temperature_lenso'])
```
> the value of pv_temperature_lenso is 37

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_CELSIUS<br/>
**decimalScale:** 0<br/>


## rt_action_enable_afci_test
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of rt_action_enable_afci_test is ' + status['rt_action_enable_afci_test'])
```
> the value of rt_action_enable_afci_test is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## rt_action_enable_gfdi_test
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of rt_action_enable_gfdi_test is ' + status['rt_action_enable_gfdi_test'])
```
> the value of rt_action_enable_gfdi_test is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## rt_action_enable_ird_test
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of rt_action_enable_ird_test is ' + status['rt_action_enable_ird_test'])
```
> the value of rt_action_enable_ird_test is false

### Description
**type:** boolean<br/>
**default:** false<br/>


## rt_last_ran_time_afci
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of rt_last_ran_time_afci is ' + status['rt_last_ran_time_afci'])
```
> the value of rt_last_ran_time_afci is 1629715500

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## rt_last_ran_time_gfdi
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of rt_last_ran_time_gfdi is ' + status['rt_last_ran_time_gfdi'])
```
> the value of rt_last_ran_time_gfdi is 1629715499

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## rt_last_ran_time_ird
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of rt_last_ran_time_ird is ' + status['rt_last_ran_time_ird'])
```
> the value of rt_last_ran_time_ird is 1629715495

### Description
**type:** number<br/>
**default:** 0<br/>
**decimalScale:** 0<br/>


## rt_test_result_afci
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of rt_test_result_afci is ' + status['rt_test_result_afci'])
```
> the value of rt_test_result_afci is true

### Description
**type:** boolean<br/>
**default:** false<br/>


## rt_test_result_gfdi
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of rt_test_result_gfdi is ' + status['rt_test_result_gfdi'])
```
> the value of rt_test_result_gfdi is true

### Description
**type:** boolean<br/>
**default:** false<br/>


## rt_test_result_ird
#### Example
```python
import json
import SkyboxAPI
s = SkyboxAPI.SkyboxAPI()
status = s.getStatus()
print('The value of rt_test_result_ird is ' + status['rt_test_result_ird'])
```
> the value of rt_test_result_ird is true

### Description
**type:** boolean<br/>
**default:** false<br/>


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
> the value of time_stamp is 2021-08-24 01:59:47

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
> the value of time_stamp_utc is 1629770387

### Description
**type:** number<br/>
**default:** 0<br/>
**unitOfMeasure:** UNIT_SECOND<br/>
**decimalScale:** 0<br/>











