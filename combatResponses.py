#! /usr/bin/env python3

import random

#=====================================
# Combat responses and sassy output
#=====================================

# Define lists for various responses

actions_player_good = ['You deliver an astounding blow.','You launch a valiant attack!', "You totally kick ass.", "Bad day to be your opponent.", "Ridiculously powerful attack, man!"]
actions_player_bad = ['Put some effort in?','That all you got?','Prison did nothing for your strength...clearly.',"C'mon!"]
actions_monster_good = ['This guy is gonna kick your ass.','Ouch!',"That's gonna leave a mark.","Consider running away like a scared child."]
actions_monster_bad = ['You can take this guy.','Terrible effort, what a chump.',"If you don't win, I'll be disappointed.","Today's your lucky day"]
actions_magic = ['Fire balls fly from your hand dealing ','Arcane missiles shoot from your fingers. They do ','You summon rain of fire from above, dealing ','You raise shards of ice from the floor that deal ']
actions_missed = ['Your swing is wide causing you to miss.','You miss by a country mile.','You struggle to raise your weapon, and miss your chance to attack.','Your attempt is feeble and your opponent parries your attack.']

# Functions for determining output based on random attack for user and creature

def combatResponse_player(user_attack, new_user_attack):
	if new_user_attack / user_attack >= 0.6:
		message = random.choice(actions_player_good)
		return message
	else:
		message = random.choice(actions_player_bad)
		return message

def combatResponse_monster(monster_attack, new_monster_attack):
	if new_monster_attack / monster_attack >= 0.6:
		message = random.choice(actions_monster_good)
		return message
	else:
		message = random.choice(actions_monster_bad)
		return message

def magicResponse():
	message = random.choice(actions_magic)
	return message

def missResponse():
	message = random.choice(actions_missed)
	return message