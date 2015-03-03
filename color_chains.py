from pymol import *

models = {
	'3U5C' : {
		 'VNG0787G' : ('RPS3','D')
	}
}

def color_chains(ids=[]):
	# ask Pymol which models are present
	# loop through ids, find chains
	chains = []
	
	# create selection group
	# color it

# attach function to a pymol console command
