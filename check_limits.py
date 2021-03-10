from check_battery_parameters import * 

lang_msg ={'DE' : {'warning' : "Warnung! Bitte halten Sie innerhalb des Bereichs",'Okay' : "Batterie ist in einwandfreiem Zustand", 'fail' : "Batterielimits A-Range!"},
	   'EN' : {'warning' : "Warning! Please maintain wihtin Range", 'Okay' : "Battery in Perfect Condition", 'fail' : " Battery Limits out of Range!"}}
lang = "EN"	
		
def battery_is_ok(battery_Values):
	battery_parameters = battery_parameters_Check(battery_Values)
	if "warning" in check_battery_parameters.msg:
		print(lang_msg[lang]['warning'])
	elif "fail" in check_battery_parameters.msg:
		print(lang_msg[lang]['fail'])
	else:
		print(lang_msg[lang]['Okay'])
	

if __name__ == '__main__':
	battery_is_ok({'temperature': 25,'soc': 70, 'roc': 0.7})
	battery_is_ok({'temperature': 50,'soc': 85, 'roc': 0})
	lang = "DE"
	battery_is_ok({'temperature': 100,'soc': 30, 'roc': 0.5})
