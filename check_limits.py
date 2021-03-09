bms_attribute_limits = {'TEMPERATURE': {'min': 0, 'max': 45},
                        'SOC': {'min': 20, 'max': 80},
                        'CHARGE_RATE': {'min': 0,'max': 0.8}} 

def filterOut_safe_vitals(item):
    low_breach_val = bms_attribute_limits[item[0].upper()]['min']
    high_breach_val = bms_attribute_limits[item[0].upper()]['max']    
    return (item[1] < low_breach_val) or (item[1] > high_breach_val)

def battery_is_ok(bms_attributes, lang):
   abnormal_vitals = filter(filterOut_safe_vitals,bms_attributes.items())
   if len(abnormal_vitals) > 0:
        report_abnormal_vitals(abnormal_vitals,bms_attribute_limits, lang)
    else:
        if lang = 1:
                print("Batterie ist in Ordnung ")
        else lang = 0:
                print("Battery is Ok")
        
def report_abnormal_vitals(abnormal_vitals,vital_limits):
    print("Abnormal Vitals")    
    for i in abnormal_vitals.items():
        low_breach_val = vital_limits[i[0].upper()]['min']
        high_breach_val = vital_limits[i[0].upper()]['max']
        if i[1] < low_breach_val or i[1] > high_breach_val:
                if lang = 1 :
                        print("Bitte pflegen Sie innerhalb "+str(low_breach_val)+"-"+ str(high_breach_val) +" Reichweite")
                 else lang = 0:
                        print("Please Maintain Under "+str(low_breach_val)+"-"+ str(high_breach_val) +" range")
                                 
                
if __name__ == '__main__':
        battery_is_ok({'temperature': 25,'soc': 70, 'roc': 0.7}, 1)
        battery_is_ok({'temperature': 50,'soc': 85, 'roc': 0}, 0)  
  
