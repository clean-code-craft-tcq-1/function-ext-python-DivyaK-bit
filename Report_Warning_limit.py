
from Controller_Message import *
from Console_message import *

def Check_Warning_Range(battery_parameter, battery_limit_values, value, min_limit, max_limit, lang):
	low_warning = min_limit + (max_limit * 0.05)
	high_warning = max_limit - (max_limit * 0.05)
	if value >= min_limit and value <= low_warning:
		Display_Msg_on_Console(battery_parameter, value, "low_warning", lang)
	elif value >= high_warning and value <= max_limit:
		Display_Msg_on_Console(battery_parameter, value, "high_warning", lang)	
	else:
		Display_Msg_on_Console(battery_parameter, value, "Okay", lang)
