Battery_limits = {'TEMPERATURE': {'min': 0, 'max': 45, 'warn': 5 },
                   'SOC': {'min': 20, 'max': 80, 'warn': 5 },
                   'CHARGE_RATE': {'min': 0,'max': 0.8, 'warn': 5 }} 

lang_DE ={'warning' : "Warnung! Bitte halten Sie innerhalb des Bereichs",
	  'Okay' : "Batterie ist in einwandfreiem Zustand",
	  'fail' : "Batterielimits A-Range!"}

lang_EN = {'warning' : "Warning! Please maintain wihtin Range",
	   'Okay' : "Battery in Perfect Condition",
	   'fail' : " Battery Limits out of Range!"}
lang = "EN"

def filter_values(item):
    low = Battery_limits[item[0].upper()]['min']
    high = Battery_limits[item[0].upper()]['max']    
    return (item[1] < low) or (item[1] > high)

def battery_is_ok(battery_attributes):
   wrong_val = filter(filter_values,battery_attributes.items())
   if len(wrong_val) > 0:
        Message(wrong_val)
    else:
        if lang ="EN":
		print(lang_EN[item[1])
        else lang = 0:
                print(lang_DE[item[1])
        
def Message(wrong_val):
    for i in wrong_val.items():
        low = Battery_limits[i[0].upper()]['min']
        high = Battery_limits[i[0].upper()]['max']
	low_warning = low + ( Battery_limits[i[1].upper()]['max'] * Battery_limits[i[2].upper()]['warn'])/100
    	high_warning = high * (100 - Battery_limits[i[2].upper()]['warn'])/100
	if low_warning>= high_warning :
		if lang = "EN" :
			print(lang_EN[item[0])
		elif lang = "DE":
			print(lang_DE[item[0])
        elif i[1] <= low_breach_val or i[1] >= high_breach_val:
		if lang = "EN" :
			print(lang_EN[item[2])
		elif lang = "DE":
			print(lang_DE[item[2])
	                              
                
if __name__ == '__main__':
        battery_is_ok({'temperature': 25,'soc': 70, 'roc': 0.7})
        battery_is_ok({'temperature': 50,'soc': 85, 'roc': 0})
	language = "DE"
    	battery_is_ok({'Temperature': 100,'SOC': 30, 'Charge_rate': 0.5}) 
    			      
