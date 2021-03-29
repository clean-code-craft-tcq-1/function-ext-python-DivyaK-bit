
from Controller_Message import *
from Console_message import *

def Check_Warning_Range(battery_parameter, value, min_limit, max_limit, lang):
	low_warning = min_limit + (max_limit * 0.05)
	high_warning = max_limit - (max_limit * 0.05)
	if min_limit <= value <= low_warning and round(value, 2) == value:
		Display_Msg_on_Console(battery_parameter, value, "low_warning", lang)
	elif high_warning <= value <= max_limit and round(value, 2) == value:
		Display_Msg_on_Console(battery_parameter, value, "high_warning", lang)	
	else:
		Display_Msg_on_Console(battery_parameter, value, "Okay", lang)
