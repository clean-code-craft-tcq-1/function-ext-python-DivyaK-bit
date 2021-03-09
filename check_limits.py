        
def battery_is_ok(value):
  temperature = value[0]
  soc = value[1]
  charge_rate = value[2]
  if temperature < 0 or temperature > 45:
    print('Temperature is out of range!')
    return False
  elif soc < 20 or soc > 80:
    print('State of Charge is out of range!')
    return False
  elif charge_rate > 0.8:
    print('Charge rate is out of range!')
    return False
  return true

if __name__ == '__main__':
   age1 = [25, 70, 0.7]
   age2 = [50, 85, 0]
    
   adults = filter(battery_is_ok, age1)
  
  
