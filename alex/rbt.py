import rnd_lst

class rbt:
	def __init__(self):
		self.root = None
	def __str__(self):
		rv = print_rec(self.root)
		return rv;
	def __rep__(self):
		return __str__(self)

class rb_node:
	def __init__(self, color, data):
		self.color = color
		self.data  = data
		self.right = None
		self.left  = None
		self.p	   = None
	def __str__(self):
		rv = str(self.data)
		rv = rv + " " + self.color
		return rv
	def __rep__(self):
		return __str__(self)
	def set_left(self, node):
		self.left = node
		node.p = self
	def set_right(self, node):
		self.right = node
		node.p = self
def print_rec_imp(node, dep):
	#print("depth = ", dep, '\n')
	rv = ''
	if node == None:
		rv = (' ' * dep) + 'Nil\n'
	else:
		#print("data node", str(node), '\n')
		rv = print_rec_imp(node.left, dep + 1)
		rv = rv + (' ' * dep) + str(node) + '\n'
		rv = rv + print_rec_imp(node.right, dep + 1)
	return rv
def print_rec(node):		
	return print_rec_imp(node, 0)	

def rb_node_left_rotation(x):
	x_p = x.p
	x_r = x.right
	x.right = x_r.left
	x.p = x_r
	x_r.left = x
	x_r.p = x_p
	return x_r

def rb_node_right_rotation(y):	
	y_p = y.p
	y_l = y.left
	y.left = y_l.right
	y.p = y_l
	y_l.right = y
	y_l.p = y_p
	return y_l
		
if __name__ == "__main__":
	print("Custom implementation of red-black tree")
	#tst_lst = rnd_lst.rnd_lst_gen(0, 100, 10)
	#print(*tst_lst)
	node  = rb_node("red", 1)
	node1  = rb_node("black", 2)
	node.set_right(node1)
	#print("Node =", node)
	tree_str = print_rec(node)
	print(tree_str)
	print("left rotation\n")
	node = rb_node_left_rotation(node)
	tree_str = print_rec(node)
	print(tree_str)
	print("right rotation\n")
	node = rb_node_right_rotation(node)
	tree_str = print_rec(node)
	print(tree_str)
	print('Test rbt class')
	aTree = rbt()
	aTree.root = node
	print(aTree)

	

	