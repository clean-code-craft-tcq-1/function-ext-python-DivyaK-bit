battery_limits = {"temperature": [0, 45], "soc": [20, 80], "charge_rate": [0, 0.8]}
					
warn_limit = 5

lang_msg ={'DE' : {'warning' : "Warnung! Bitte halten Sie innerhalb des Bereichs",'Okay' : "Batterie ist in einwandfreiem Zustand", 'fail' : "Batterielimits A-Range!"},
	   'EN' : {'warning' : "Warning! Please maintain wihtin Range", 'Okay' : "Battery in Perfect Condition", 'fail' : " Battery Limits out of Range!"}}

lang = "EN"

def battery_is_ok(battery_values):
	value_range = battery_limits[battery_values["battery_parameter"]]
	low = value_range[0]
	high = value_range[1]
	warning_value = (high * warn_limit) / 100
	low_warning = low + warning_value
	high_warning = high - warning_value
	value = battery_values["value"]
	if value <= low or value >= high:
		print(lang_msg[lang]['fail'])
		return False
	compare_battery_param_value(low_warning, value)
	compare_battery_param_value(value, high_warning)
	return True

def compare_battery_param_value(lower_value, upper_value):
	if lower_value >= upper_value:
		print(lang_msg[lang]['warning'])

if __name__ == '__main__':
	assert (battery_is_ok({"battery_parameter": "temperature", "value": 25}) is True)
	assert (battery_is_ok({"battery_parameter": "temperature", "value": 50}) is False)
	assert (battery_is_ok({"battery_parameter": "charge_rate", "value": 0}) is False)
	assert (battery_is_ok({"battery_parameter": "soc", "value": 23}) is True)
	language = "DE"
	assert (battery_is_ok({"battery_parameter": "soc", "value": 77}) is True)
	assert (battery_is_ok({"battery_parameter": "temperature", "value": 50}) is False)
