
from Controller_Message import *
from Console_message import *

def Threshold_Values(min_limit, max_limit):
	low_warning = min_limit + (max_limit * 0.05)
	high_warning = max_limit - (max_limit * 0.05)
	return low_warning, high_warning

def Check_Warning_Range(battery_parameter, value, min_limit, max_limit, lang):
	low_warning, high_warning = Threshold_Values(min_limit, max_limit)
	if min_limit <= value <= low_warning:
		Display_Msg_on_Console(battery_parameter, value, "low_warning", lang)
	elif high_warning <= value <= max_limit:
		Display_Msg_on_Console(battery_parameter, value, "high_warning", lang)	
	else:
		Display_Msg_on_Console(battery_parameter, value, "Okay", lang)
