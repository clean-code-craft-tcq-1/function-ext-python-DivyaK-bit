battery_limits = {'Temperature': {'min' : 0, 'max' : 45}, 'SOC': {'min' : 20, 'max' : 80}, 'Rate_of_Charge': {'min' : 0, 'max' : 0.8}}
					
def Threshold(max):
	warn_limit = 5
	return (max * warn_limit) / 100

Msg_Info = {'low_breach': {'DE' : "Nicht! Wert ist zu niedrig", 'EN' : "Failing! value is too low"}, 
	    'low_warning' : {'DE' : "Warnung! Wert ist zu niedrig", 'EN' : "Warning! value is too Low"},
	    'Okay' : {'DE' : "Wert ist perfekt, Halten Sie es", 'EN' : "Value is perfect, Maintain it"},
	    'high_warning' : {'DE' : "Warnung! Wert ist zu hoch", 'EN' : "Warning! value is too High"},
	    'high_breach' : {'DE' : "Nicht! Wert ist zu hoch", 'EN' : "Failing! value is too High"}}

lang_msg ={'DE' : {'warning' : "Warnung! Wert hat Schwellenwert erreicht" , 'Okay' : "Batterie ist in einwandfreiem Zustand", 'fail' : "Batterielimits A-Range!"},
	   'EN' : {'warning' : "Warning! Value has reached threshold limit" , 'Okay' : "Battery in Perfect Condition", 'fail' : " Battery Limits out of Range!"}}

Controller_Msg_EN = ["", "", "", "", ""]
Controller_Msg_DE

factor_en = ["Temperature","SOC", "Rate_of_Charge"]
factor_de = ["Temperatur","SOC", "Rate_der_Gebühr"]

lang = "EN"

def Display_Msg_on_Console(value, num, attribute):
	return print(lang_msg[lang][attribute], factor_de[num], ":", value)

def Is_Battery_in_good_condition(condition):
	if(condition == 1):
		print(lang_msg[lang]['Okay'])
		
def Check_range(value, Num):
	low = battery_limits[factor_en[Num]]['min']
	high = battery_limits[factor_en[Num]]['max']
	warning_value = threshold_val(high)
	low_warning = low + warning_value
	high_warning = high - warning_value
	if value <= low or value >= high:
		Display_Msg(value, Num, "fail")
		return 0
	compare_battery_param_value(low_warning, value, Num, high_warning)
	return 1

def compare_battery_param_value(lower_value, value, Num, upper_value):
	if lower_value >= value or value >= upper_value:
		Display_Msg(value, Num, "warning")
		return 0
		
def battery_is_ok(temperature, soc, roc):
	status =(Check_range(temperature, 0)) & (Check_range(soc, 1)) & (Check_range(roc, 2))
	Is_Battery_in_good_condition(status)
	return (status)
	
if __name__ == '__main__':
	battery_is_ok(25, 77, 0)
	battery_is_ok(50, 23, 0.8)
	lang = "DE"
	battery_is_ok(25, 70, 0.7)
	battery_is_ok(50, 85,  0)
