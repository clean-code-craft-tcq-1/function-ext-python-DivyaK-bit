
temp_actions = {'EN' : ['Start Warming the Battery', 
			'Warm battery little long', 
			'Perfect Condition. Maintain the state', 
			'Cool down battery little bit', 
			'Cool down battery, Fast'], 
		'DE' : ['Starten Sie die Erwärmung der Batterie', 
			'Warme Batterie wenig lang', 
			'Perfekter Zustand. Aufrechterhaltung des Zustands', 
			'Batterie etwas abkühlen', 
			'Kühlbatterie, Schnell']}

soc_actions = {'EN' : ['No Charge in the battery','Low Charge in the battery','Perfect Condition','Battery about to be full','Battery Full'], 
	       'DE' : ['Keine Ladung im Akku','Niedrige Ladung in der Batterie','Perfekter Zustand','Batterie wird kurz vor voll sein','Batterie Voll']}

roc_actions = {'EN' : ['Start Charging', 'Increase Charging', 'Perfect Condition. Maintain the state', 'Decrease charging', 'Stop Charging'], 
	       'DE' : ['Starten Sie das Laden', 'Erhöhen Sie die Aufladung', 'Perfekter Zustand', 'Verringern der Aufladung', 'Stoppen Desladens']}

actions = { 'Temperature' : temp_actions, 'SOC' : soc_actions, 'Rate_of_Charge' : roc_actions}

def Controller_Info(battery_parameter, num, lang):
	actions_params = actions[battery_parameter]
	return print(actions_params[lang][num])
  
