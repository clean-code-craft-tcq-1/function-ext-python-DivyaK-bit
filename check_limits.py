battery_limit = {'temperature': {'min': 0, 'max': 45},
		 'soc': {'min': 20, 'max': 80},
		 'roc': {'min': 0,'max': 0.8}} 

warn_limit = 5

lang_msg ={'DE' : {'warning' : "Warnung! Bitte halten Sie innerhalb des Bereichs",'Okay' : "Batterie ist in einwandfreiem Zustand", 'fail' : "Batterielimits A-Range!"},
	   'EN' : {'warning' : "Warning! Please maintain wihtin Range", 'Okay' : "Battery in Perfect Condition", 'fail' : " Battery Limits out of Range!"}}

lang = "EN"

def battery_is_ok(battery_Values):
	low = battery_limit[parameter_name]['min']
	high = battery_limit[parameter_name]['max']
	warning_value = (high * warn_limit) / 100
	low_warning = low + warning_value
	high_warning = high - warning_value
	parameter_off_Limits = []
    	for parameter_name,parameter_value in battery_Values.items():
		if (low_warning >= parameter_value) or (parameter_value >= high_warning)
			print(lang_msg[lang]['warning'])
		elif(parameter_value <= low) or (parameter_value >= high):
			print(lang_msg[lang]['fail'])
		else:
			print(lang_msg[lang]['Okay'])
			
		
if __name__ == '__main__':
    	battery_is_ok({'temperature': 25,'soc': 70, 'roc': 0.7})
    	battery_is_ok({'temperature': 50,'soc': 85, 'roc': 0})
	lang = "DE"
	battery_is_ok({'temperature': 100,'soc': 30, 'roc': 0.5}) 
    		      
