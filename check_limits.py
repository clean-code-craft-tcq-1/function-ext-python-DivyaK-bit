battery_limits = {'Temperature': {'min' : 0, 'max' : 45}, 'SOC': {'min' : 20, 'max' : 80}, 'Rate_of_Charge': {'min' : 0, 'max' : 0.8}}

Msg_Info = {'low_breach': {'DE' : "Nicht! Wert ist zu niedrig", 'EN' : "Failing! value is too low"}, 
	    'low_warning' : {'DE' : "Warnung! Wert ist zu niedrig", 'EN' : "Warning! value is too Low"},
	    'Okay' : {'DE' : "Wert ist perfekt", 'EN' : "Value is perfect"},
	    'high_warning' : {'DE' : "Warnung! Wert ist zu hoch", 'EN' : "Warning! value is too High"},
	    'high_breach' : {'DE' : "Nicht! Wert ist zu hoch", 'EN' : "Failing! value is too High"}}

Controller_Msg_EN = ["", "", "Battery in Stable Condition. Maintain It", "", ""]
Controller_Msg_DE = ["","" ,"Batterie in Stabilem Zustand. Maintain It", "", ""]

factor_en = ["Temperature","SOC", "Rate_of_Charge"]
factor_de = ["Temperatur","SOC", "Rate_der_Gebühr"]

lang = "EN"

def Threshold(max):
	warn_limit = 5
	return (max * warn_limit) / 100

def Display_Msg_on_Console(num, value, attribute):
	if (lang == "EN"):
		return print(Msg_Info[attribute][lang], factor_en[num], ":", value)
	else:
		return print(Msg_Info[attribute][lang], factor_de[num], ":", value)

def Controller_Info(val):
	if (lang == "EN"):
		return Controller_Msg_EN[val]
	else:
		return Controller_Msg_DE[val]

def Check_Warning_Range(value, min_limit, max_limit):
	low_warning = min_limit + Threshold(max_limit)
	high_warning = max_limit - Threshold(max_limit)
	if value >= min_limit and value <= low_warning:
		Display_Msg_on_Console(index_value, value, "low_warning")
	elif value >= high_warning and value <= max_limit:
		Display_Msg_on_Console(index_value, value, "high_warning")	
	else:
		Display_Msg_on_Console(index_value, value, "Okay")

def Check_Off_Limit_Range(index_value, value, battery_limit_values):
	min_limit = battery_limit_values['min']
	max_limit = battery_limit_values['max']
	if value < min_limit:
		Display_Msg_on_Console(index_value, value, 'low_breach')
	elif value > max_Limit:
		Display_Msg_on_Console(index_value, value, 'high_breach')
	else:
		Check_Warning_Range(value, min_limit, max_limit)
		
def Is_Battery_OK(Battery_Value_Parameters):
	print("Here is the result for the input values:")
	for battery_parameter, index_value in enumerate(Battery_Value_Parameters):
		Check_Off_Limit_Range(index_value, Battery_Value_Parameters[battery_parameter], battery_limits[battery_parameter])
	print("\n")

if __name__ == '__main__':
	Is_Battery_OK({'Temperature' : 25, 'SOC' : 77, 'Rate_Of_Charge' : 0})
	Is_Battery_OK({'Temperature' : 50, 'SOC' : 23, 'Rate_Of_Charge' : 0.8})
	lang = "DE"
	Is_Battery_OK({'Temperature' : 25, 'SOC' : 70, 'Rate_Of_Charge' : 0.7})
	Is_Battery_OK({'Temperature' : 50, 'SOC' : 85, 'Rate_Of_Charge' : 0})
