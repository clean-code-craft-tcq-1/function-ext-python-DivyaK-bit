from Controller_Message import *
from Console_message import *

def Threshold(max):
	warn_limit = 5
	return (max * warn_limit) / 100
  
def Check_Warning_Range(battery_parameter, battery_limit_values, value, min_limit, max_limit, lang):
	low_warning = min_limit + Threshold(max_limit)
	high_warning = max_limit - Threshold(max_limit)
	if value >= min_limit and value <= low_warning:
		Display_Msg_on_Console(battery_parameter, battery_limit_values, value, "low_warning", lang)
	elif value >= high_warning and value <= max_limit:
		Display_Msg_on_Console(battery_parameter, battery_limit_values, value, "high_warning", lang)	
	else:
		Display_Msg_on_Console(battery_parameter, battery_limit_values, value, "Okay", lang)

def Check_Off_Limit_Range(battery_parameter, value, battery_limit_values, lang):
	min_limit = battery_limit_values['min']
	max_limit = battery_limit_values['max']
	if value < min_limit:
		Display_Msg_on_Console(battery_parameter, battery_limit_values, value, 'low_breach', lang)
	elif value > max_limit:
		Display_Msg_on_Console(battery_parameter, battery_limit_values, value, 'high_breach',lang)
	else:
		Check_Warning_Range(battery_parameter, battery_limit_values, value, min_limit, max_limit, lang)
