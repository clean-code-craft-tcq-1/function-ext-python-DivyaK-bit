from check_limits import *

Msg_Info = {'low_breach': {'DE' : "Nicht! Wert ist zu niedrig", 'EN' : "Failing! value is too low"}, 
	    'low_warning' : {'DE' : "Warnung! Wert ist zu niedrig", 'EN' : "Warning! value is too Low"},
	    'Okay' : {'DE' : "Wert ist perfekt", 'EN' : "Value is perfect"},
	    'high_warning' : {'DE' : "Warnung! Wert ist zu hoch", 'EN' : "Warning! value is too High"},
	    'high_breach' : {'DE' : "Nicht! Wert ist zu hoch", 'EN' : "Failing! value is too High"}}

def Display_Msg_on_Console(battery_parameter, battery_limit_values, value, attribute, lang):
	if (lang == "EN"):
		return print(Msg_Info[attribute][lang], battery_parameter, ":", value)
	else:
		return print(Msg_Info[attribute][lang], battery_limit_values['de'], ":", value)
