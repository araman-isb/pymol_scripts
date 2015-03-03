from pymol import cmd
import string

models = {
	# pdb name
	'3U5C' : {
		# gene id : (gene name, [chain1,chain2,...])
		'VNG0787G' : ('RPS3',['D']),
#		'VNG0000G' : ('RPS0','?'),
	},
#	'XXXX' : {
#		'' : : ('',['','']),
#	},
}

def color_chains(idsfile):
	# ask Pymol which models are present
	structures = cmd.get_names('objects')
	print 'loaded structures are: %s' %string.join(structures)
	# loop through the structures present (i.e. preloaded PDBs)
	for structure in structures:
		# note missing info for any undefined models
		if not structure in models.keys():
			print 'chains of structure %s not defined' %structure
			continue
	# read file of id groups with names and colors defined
	# example:
	# group1 red VNG0787G,VNG0000G,...
	for line in open(idsfile):
		fields = line.strip().split()
		name = fields[0]
		color = fields[1]
		ids = fields[2].split(',')
		selection = []
		for id in ids:
			if not id in models[structure].keys():
				print 'chains for id %s not defined for model %s' %(id,structure)
				continue
			print 'chains for id %s (gene %s): %s' %(id,models[structure][id][0],string.join(models[structure][id][1],','))
			for chain in models[structure][id][1]:
				selection.append('/%s//%s//' %(structure,chain))
		# create selection
		cmd.select(name,string.join(selection,' or '))
		# color it
		cmd.color(color,name)

# attach function to a pymol console command
cmd.extend('color_chains', color_chains)

# to load this function into pymol, run 'run color_chains.py' in the pymol console
# this can then be called as: 'color_chains groupfile'
