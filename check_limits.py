battery_limits = {'temperature': {'min' : 0, 'max' : 45}, 'soc': {'min' : 20, 'max' : 80}, 'charge_rate': {'min' : 0, 'max' : 0.8} }
					
def threshold_val(max):
	warn_limit = 5
	return (max * warn_limit) / 100

lang_msg ={'DE' : {'warning' : "Warnung! Wert hat Schwellenwert erreicht" , 'Okay' : "Batterie ist in einwandfreiem Zustand", 'fail' : "Batterielimits A-Range!"},
	   'EN' : {'warning' : "Warning! Value has reached threshold limit" , 'Okay' : "Battery in Perfect Condition", 'fail' : " Battery Limits out of Range!"}}

factor_en = ["Temperature","SOC", "Rate of Charge"]
factor_de = ["Temperatur","SOC", "Rate der Gebühr"]

lang = "EN"

def Display_Msg(value, num, attribute):
	return print(lang_msg[lang][attribute], factor_de[num], ":", value)

def Is_Battery_in_good_condition(condition):
	if(condition = 1):
		print(lang_msg[lang]['Okay'])
		
def Check_range(value, Num):
	low = battery_limits[factor_en[Num]]['min']
	high = battery_limits[factor_en[Num]]['max']
	warning_value = threshold(high)
	low_warning = low + warning_value
	high_warning = high - warning_value
	if value <= low or value >= high:
		Display_Msg(value, Num, 'fail')
		return 0
	compare_battery_param_value(low_warning, value)
	compare_battery_param_value(value, high_warning)
	return 1

def compare_battery_param_value(lower_value, upper_value):
	if lower_value >= upper_value:
		Display_Msg(value, Num, 'warning')
		return 0
		
def battery_is_ok(temperature, soc, roc):
	status =(Check_range(temperature, 0)) & Check_range(soc, 1)) & (Check_range(roc, 2))
	Is_Battery_in_good_condition(status)
	return (status)
	
if __name__ == '__main__':
	battery_is_ok(25, 77, 0)
	battery_is_ok(50, 23, 0.8)
	language = "DE"
	battery_is_ok(25, 70, 0.7})
	battery_is_ok(50, 85,  0})
