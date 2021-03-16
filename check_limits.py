battery_limits = {'temperature': {'min' : 0, 'max' : 45}, 'soc': {'min' : 20, 'max' : 80}, 'charge_rate': {'min' : 0, 'max' : 0.8} }
					
def threshold_val(max):
	warn_limit = 5
	return (max * warn_limit) / 100

lang_msg ={'DE' : {'warning' : "Warnung! Werte haben Schwellenwert erreicht" , 'Okay' : "Batterie ist in einwandfreiem Zustand", 'fail' : "Batterielimits A-Range!"},
	   'EN' : {'warning' : "Warning! Values have reached threshold limit" , 'Okay' : "Battery in Perfect Condition", 'fail' : " Battery Limits out of Range!"}}

lang = "EN"

def Msg(temperature, soc, roc, attribute):
	if (lang == "EN"):
		print(lang_msg['EN'][attribute], "Temperature:", temperature, "SOC:", soc, "Rate of Charge:", roc)
	elif(lang =="DE"):
		print(lang_msg['DE'][attribute], "Temperatur:", temperature, "SOC:", soc, "Rate der Gebühr:", roc)
		


def battery_is_ok(temperature, soc, roc):
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
	assert (battery_is_ok(25, ) is True)
	assert (battery_is_ok(50, ) is False)
	assert (battery_is_ok(, , 0}) is False)
	assert (battery_is_ok(, 23, ) is True)
	language = "DE"
	assert (battery_is_ok(, 77, ) is True)
	assert (battery_is_ok(50, ) is False)
