
class TrieNode(): 
	def __init__(self): 
		# Initialising node
		self.children = {} 
		self.last = False

class Trie(): 
	def __init__(self): 
		# Initialising the trie structure.
		self.root = TrieNode() 
		self.word_list = [] 

	def insert(self, key): 
		node = self.root 

		for a in list(key): 
			if not node.children.get(a): 
				node.children[a] = TrieNode() 

			node = node.children[a]
		node.last = True

	def search(self, key): 
		node = self.root 
		found = True

		for a in list(key): 
			if not node.children.get(a): 
				found = False
				break

			node = node.children[a] 

		return node and node.last and found 


	def prefix_search_helper(self, node, word): 
		if node.last: 
			self.word_list.append(word) 

		for a,n in node.children.items(): 
			self.prefix_search_helper(n, word + a) 

	def prefix_search(self, key):
		self.word_list = []
		node = self.root
		not_found = False
		temp_word = ''

		for a in list(key): 
			if not node.children.get(a): 
				not_found = True
				break

			temp_word += a
			node = node.children[a]

		if not_found: 
			return []
		elif node.last and not node.children: 
			return []
		self.prefix_search_helper(node, temp_word)
		return self.word_list
