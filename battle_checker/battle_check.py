import math
defender_fleet=eval(input("How many ships are in defender fleet? "))
attacker_fleet=eval(input("How many ships are in attacker fleet? "))
defender_weapons=eval(input("What is your defender weapons tech? "))
attacker_weapons=eval(input("What is your attacker weapons tech? "))
hours=eval(input("How many hours until the attack? "))
industry=eval(input("What is the defenders industry? -99 if unsure "))
tech=eval(input("What is your defenders manufacturing? -99 if unsure "))

if(industry==-99 or tech==-99):
	pass
else:
	defender_fleet+=math.floor((industry*(tech+5)/24)*hours)

defender=defender_fleet
attacker=attacker_fleet
while defender>0 and attacker>0:
	attacker-=(defender_weapons+1)
	if attacker<=0:
		break
	defender-=attacker_weapons

if defender>0:
	print("Defender Wins.  Ship remaining:", defender)
	while attacker<=0:
		attacker_fleet+=1
		attacker=attacker_fleet
		defender=defender_fleet
		while defender>0 and attacker>0:
			attacker-=(defender_weapons+1)
			if attacker<=0:
				break
			defender-=attacker_weapons
	print("Attacker needs: ", attacker_fleet," To win")
else:
	print("Attacker Wins.  Ship remaining:", attacker)
	while defender<=0:
		defender_fleet+=1
		attacker=attacker_fleet
		defender=defender_fleet
		while defender>0 and attacker>0:
			attacker-=(defender_weapons+1)
			if attacker<=0:
				break
			defender-=attacker_weapons
	print("Defender needs: ", defender_fleet," To win")

