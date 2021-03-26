
from Controller_Message import *
from Console_message import *

warn_limit = 5

def Check_Warning_Range(battery_parameter, battery_limit_values, value, min_limit, max_limit, lang):
	low_warning = min_limit + ((max * warn_limit) / 100)
	high_warning = max_limit - ((max * warn_limit) / 100)
	if value >= min_limit and value <= low_warning:
		Display_Msg_on_Console(battery_parameter, battery_limit_values, value, "low_warning", lang)
	elif value >= high_warning and value <= max_limit:
		Display_Msg_on_Console(battery_parameter, battery_limit_values, value, "high_warning", lang)	
	else:
		Display_Msg_on_Console(battery_parameter, battery_limit_values, value, "Okay", lang)
