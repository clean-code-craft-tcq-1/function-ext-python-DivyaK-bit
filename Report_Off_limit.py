from Controller_Message import *
from Console_message import *
from Report_Warning_limit import *

def Check_Off_Limit_Range(battery_parameter, value, battery_limit_values, lang):
	min_limit = battery_limit_values['min']
	max_limit = battery_limit_values['max']
	if value < min_limit:
		Display_Msg_on_Console(battery_parameter, value, 'low_breach', lang)
		Controller_Info(battery_parameter, 0, lang)
	elif value > max_limit:
		Display_Msg_on_Console(battery_parameter, value, 'high_breach',lang)
		Controller_Info(battery_parameter, 4, lang)
	else:
		Check_Warning_Range(battery_parameter, value, min_limit, max_limit, lang)
