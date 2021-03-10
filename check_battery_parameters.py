battery_limit = {'temperature': {'min': 0, 'max': 45},
		 'soc': {'min': 20, 'max': 80},
		 'roc': {'min': 0,'max': 0.8}}

msg = ""
warn_limit = 5

def battery_parameters_Check(battery_Values):
	for parameter_name,parameter_value in battery_Values.items() :
		check_attribute_limit(parameter_name,parameter_value,msg) 
	return msg

def check_attribute_warn_limit(parameter_name,parameter_value,msg):
	low = battery_limit[parameter_name]['min']
	high = battery_limit[parameter_name]['max']
	warning_value = (high * warn_limit) / 100
	low_warning = low + warning_value
	high_warning = high - warning_value
	parameter_off_Limits = []
	if (low_warning > parameter_value) or (parameter_value > high_warning):
		msg= "warning"
	elif (parameter_value < battery_limit[parameter_name]['min']) or (parameter_value > battery_limit[parameter_name]['max']):
		msg = "fail"
	else:
		msg = "Okay"
