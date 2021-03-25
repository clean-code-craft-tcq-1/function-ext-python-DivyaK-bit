from Controller_Message import *
from Console_message import *

battery_limits = {'Temperature': {'min' : 0, 'max' : 45, 'de' : "Temperatur"}, 
		  'SOC': {'min' : 20, 'max' : 80, 'de' : "SOC"}, 
		  'Rate_of_Charge': {'min' : 0, 'max' : 0.8, 'de' : "Rate_der_Gebühr"}}

lang = "EN"

def Threshold(max):
	warn_limit = 5
	return (max * warn_limit) / 100

def Check_Warning_Range(battery_parameter, battery_limit_values, value, min_limit, max_limit):
	low_warning = min_limit + Threshold(max_limit)
	high_warning = max_limit - Threshold(max_limit)
	if value >= min_limit and value <= low_warning:
		Display_Msg_on_Console(battery_parameter, battery_limit_values, value, "low_warning", lang)
	elif value >= high_warning and value <= max_limit:
		Display_Msg_on_Console(battery_parameter, battery_limit_values, value, "high_warning", lang)	
	else:
		Display_Msg_on_Console(battery_parameter, battery_limit_values, value, "Okay", lang)

def Check_Off_Limit_Range(battery_parameter, value, battery_limit_values):
	min_limit = battery_limit_values['min']
	max_limit = battery_limit_values['max']
	if value < min_limit:
		Display_Msg_on_Console(battery_parameter, battery_limit_values, value, 'low_breach', lang)
	elif value > max_limit:
		Display_Msg_on_Console(battery_parameter, battery_limit_values, value, 'high_breach',lang)
	else:
		Check_Warning_Range(battery_parameter, battery_limit_values, value, min_limit, max_limit)
		
def Is_Battery_OK(Battery_Value_Parameters):
	print("Here is the result for the input values:")
	for battery_parameter in Battery_Value_Parameters:
		Check_Off_Limit_Range(battery_parameter, Battery_Value_Parameters[battery_parameter], battery_limits[battery_parameter])
	print("\n")

if __name__ == '__main__':
	Is_Battery_OK({'Temperature' : 25, 'SOC' : 77, 'Rate_of_Charge' : 0})
	Is_Battery_OK({'Temperature' : 50, 'SOC' : 23, 'Rate_of_Charge' : 0.8})
	lang = "DE"
	Is_Battery_OK({'Temperature' : 25, 'SOC' : 70, 'Rate_of_Charge' : 0.7})
	Is_Battery_OK({'Temperature' : 50, 'SOC' : 85, 'Rate_of_Charge' : 0})
