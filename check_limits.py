battery_limit = {'temperature': {'min': 0, 'max': 45},
		 'soc': {'min': 20, 'max': 80},
		 'roc': {'min': 0,'max': 0.8}}

parameter_off_Limits = []
parameter_warn_Limits = []
warn_limit = 5

lang_msg ={'DE' : {'warning' : "Warnung! Bitte halten Sie innerhalb des Bereichs",'Okay' : "Batterie ist in einwandfreiem Zustand", 'fail' : "Batterielimits A-Range!"},
	   'EN' : {'warning' : "Warning! Please maintain wihtin Range", 'Okay' : "Battery in Perfect Condition", 'fail' : " Battery Limits out of Range!"}}
lang = "EN"
         
def battery_parameters_Check(battery_Values):
	for parameter_name,parameter_value in battery_Values.items() :
		check_attribute_Off_limit(parameter_name,parameter_value,parameter_off_Limits) 
		check_attribute_Off_limit(parameter_name,parameter_value,parameter_warn_Limits)
	return parameter_off_Limits,parameter_warn_Limits

def check_attribute_Off_limit(parameter_name,parameter_value,parameter_off_Limits):
	if (parameter_value < battery_limit[parameter_name]['min']) or (parameter_value > battery_limit[parameter_name]['max']):
		parameter_off_Limits.append(parameter_name)
			
def check_attribute_Off_limit(parameter_name,parameter_value,parameter_warn_Limits):
	low = battery_limit[parameter_name]['min']
	high = battery_limit[parameter_name]['max']
	warning_value = (high * warn_limit) / 100
	low_warning = low + warning_value
	high_warning = high - warning_value
	parameter_off_Limits = []
	if (low_warning > parameter_value) or (parameter_value > high_warning):
		parameter_warn_Limits.append(parameter_name)

def battery_is_ok(battery_Values):
	battery_parameters = battery_parameters_Check(battery_Values)
	if len(battery_parameters) == 0 :
		print(lang_msg[lang]['Okay'])
	elif len(parameter_warn_Limits) > 0:
		print(lang_msg[lang]['warning'])
	elif len(parameter_off_Limits) > 0:
		print(lang_msg[lang]['fail'])

if __name__ == '__main__':
	battery_is_ok({'temperature': 25,'soc': 70, 'roc': 0.7})
	battery_is_ok({'temperature': 50,'soc': 85, 'roc': 0})
	lang = "DE"
	battery_is_ok({'temperature': 100,'soc': 30, 'roc': 0.5})
