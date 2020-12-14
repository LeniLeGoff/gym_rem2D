import REM2D_main as r2d
import numpy as np

def evaluate(individual, EVALUATION_STEPS= 10000, HEADLESS=True, INTERVAL=10, ENV_LENGTH=100, TREE_DEPTH = None, CONTROLLER = None):
	env = r2d.getEnv()
	if TREE_DEPTH is None:
		try:
		   TREE_DEPTH = individual.tree_depth
		except:
			raise Exception("Tree depth not defined in evaluation")
	tree = individual.genome.create(TREE_DEPTH)
	env.seed(4)
	env.reset(tree=tree, module_list=individual.genome.moduleList)

	fitness = 0
	for i in range(EVALUATION_STEPS):
		if i % INTERVAL == 0:
			if not HEADLESS:
				env.render()

		# A list of actions should be returned ideally. 
		# Right now, the tree contains a contoller which is updated.  
		# TODO: 
		action = np.ones_like(env.action_space.sample())	
		observation, reward, done, info  = env.step(action)
		
		if reward< -10:
			break
		elif reward > ENV_LENGTH:
			# add a little bit on top of the regular fitness. 
			reward += (EVALUATION_STEPS-i)/EVALUATION_STEPS
			fitness = reward
			break
		if reward > 0:
			fitness = reward
	return fitness


if __name__=="__main__":
	# Here we simply create and evaluate a few random individuals. 
	for i in range(200):
		individual = r2d.Individual.random(encoding = 'ce')
		evaluate(individual, HEADLESS = False, CONTROLLER = None)
	
