import math
import zss


def circular_module_dist(m1,m2):
	return (abs(m1.radius - m2.radius) + abs(m1.angle - m2.angle)/math.pi)/2.

def rect_module_dist(m1,m2):
	return (abs(m1.width - m2.width) + abs(m1.height - m2.height) + abs(m1.angle - m2.angle)/math.pi)/3.

def circular_module_norm(m):
	return (m.radius + m.angle/math.pi)/2.

def rect_module_norm(m):
	return (m.width + m.height + m.angle/math.pi)/3.


def module_dist(m1,m2):
	if(m1 == None):
		if(m2.type == "CIRCULAR"):
			return circular_module_norm(m2)
		elif(m2.type == "SIMPLE"):
			return rect_module_norm(m2)
	elif(m2 == None):
		if(m1.type == "CIRCULAR"):
			return circular_module_norm(m1)
		elif(m1.type == "SIMPLE"):
			return rect_module_norm(m1)
	elif(m1.type == m2.type):
		if(m1.type == "CIRCULAR"):
			return circular_module_dist(m1,m2)
		elif(m1.type == "SIMPLE"):
			return rect_module_dist(m1,m2)
	else:
		return (1 + abs(m1.angle - m2.angle)/math.pi)/2.

'''
Tree blueprint
'''
class Tree:
	def __init__(self, moduleList, controller = None):
		self.nodes = []
		self.moduleList = moduleList
	def getNodes(self):
		return self.nodes

	def create_children_lists(self):
		'''method to create list of children for each parents'''
		if len(self.nodes) == 1:
			return 
		for node in self.nodes:
			if node.parent >= 0:
				for p in self.nodes:
					if p.index == node.parent:
						p.children.append(node)
				

	@staticmethod
	def distance(T,S):
		return zss.simple_distance(T.nodes[0],S.nodes[0],Node.get_children,Node.get_label,module_dist)

	def norm(self):
		empty = Tree(self.moduleList)
		empty.nodes = [Node(0,0,0,0,0)]
		return zss.simple_distance(self.nodes[0],empty.nodes[0],Node.get_children,Node.get_label)


	def print_structure(self):
		tree_str = str()
		for node in self.nodes:
			tree_str += str(node.index) + "\n"
			for c in node.children:
				tree_str += "\t" + str(c.index) + "\n"
		return tree_str

	def save(self,filename):
		with open(filename) as file:
			file.write(self.print_str())

class Node:
	def __init__(self, index, parent, type, parent_connection_coordinates, controller=None,component=None, module_ = None):
		self.index = index
		self.type = type
		self.parent = parent
		self.parent_connection_coordinates = parent_connection_coordinates
		# A controller can be attached for decentralized control of the robot
		self.controller = controller
		self.expressed = False
		# Component can be used to attach an object for reference
		self.component = component
		self.module_ = module_
		self.children = []

	def __bool__(self):
		return self.expressed

	#Methods to use TED from zss package
	@staticmethod
	def get_children(node):
		return node.children
		
	@staticmethod
	def get_label(node):
		return node.module_

# Could be used later when using weighted edges
class Edge:
	def __init__(self,parent, target):
		self.parent = parent
		self.target = target

