
Controller_Msg_EN = ["", "", "Battery in Stable Condition. Maintain It", "", ""]
Controller_Msg_DE = ["","" ,"Batterie in Stabilem Zustand. Maintain It", "", ""]

def Controller_Info(val):
	if (lang == "EN"):
		return Controller_Msg_EN[val]
	else:
		return Controller_Msg_DE[val]
  
