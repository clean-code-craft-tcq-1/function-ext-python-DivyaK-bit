bms_attribute_limits = {'TEMPERATURE': {'min': 0, 'max': 45},
                        'SOC': {'min': 20, 'max': 80},
                        'CHARGE_RATE': {'min': 0,'max': 0.8}} 
                        
def report_battery_vitals(bms_attributes):
    abnormal_vitals = filter(filterOut_safe_vitals,bms_attributes.items())
    if len(abnormal_vitals) > 0:
        report_abnormal_vitals(abnormal_vitals,bms_attribute_limits)
    else:
        report_normal_vitals()
        
def report_normal_vitals():
    print("Battery is Ok")
    
def report_abnormal_vitals(abnormal_vitals,vital_limits):
    print("Abnormal Vitals")    
    for i in abnormal_vitals.items():
        low_breach_val = vital_limits[i[0].upper()]['min']
        high_breach_val = vital_limits[i[0].upper()]['max']
        if i[1] < low_breach_val:
            print("Low Breach : "+i[0].upper()+" | Current value: "+str(i[1]) +" | Lower limit value: "+str(low_breach_val))
        elif i[1] > high_breach_val:
            print("High Breach : "+i[0].upper()+" | Current Value: "+str(i[1])+" | Upper limit value: "+str(high_breach_val))
            


def filterOut_safe_vitals(item):
    low_breach_val = bms_attribute_limits[item[0].upper()]['min']
    high_breach_val = bms_attribute_limits[item[0].upper()]['max']    
    return (item[1] < low_breach_val) or (item[1] > high_breach_val)
	
def is_battery_ok(bms_attributes):
    value = dict(filter(filterOut_safe_vitals,bms_attributes.items()))
    report_battery_state(bms_attributes)
    return len(value) == 0

def report_battery_state(bms_attributes):    
    report_battery_vitals(bms_attributes)

    
if __name__ == '__main__':
  assert(is_battery_ok({'temperature': 25,'Soc': 70, 'Charge_rate': 0.7}) is True)  #all attributes fine
  assert(is_battery_ok({'Temperature': 50,'soc': 85, 'Charge_rate': 0}) is False)  #all attributes off limit
  assert(is_battery_ok({'Temperature': 100,'SOC': 30, 'Charge_rate': 0.5}) is False) #temp off limit
