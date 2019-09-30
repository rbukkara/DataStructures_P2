# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = dict()
        self.handler = None

    def insert(self, word):
        # Insert the node as before
        if word not in self.children:
            self.children[word] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:

    def __init__(self):
        self.root = RouteTrieNode()
        self.insert(["/"], "root handler")
        # Initialize the trie with an root node and a handler, this is the root path or home page node

    def insert(self, words, handler_message):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        cur_node = self.root
        for word in words:
            cur_node.insert(word)
            cur_node = cur_node.children[word]
        cur_node.handler = handler_message

    def find(self, words):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if len(words) == 0:
            return None

        if words[0] == "/":
            return self.root.children["/"]

        return self.find_recursive(self.root, words)

    def find_recursive(self, cur_node, words):

        if len(words) == 0:
            return cur_node

        for key in cur_node.children:
            if words[0] == key:
                cur_node = cur_node.children[words[0]]
                return self.find_recursive(cur_node, words[1:])

        return None


class Router:
    def __init__(self, home_path, home_handler_message):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie()
        self.add_handler("404", "Page not found!")
        self.add_handler(home_path, home_handler_message)

    def add_handler(self, path, handler_message):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the
        # cur_node = self.router.root
        words = self.split_path(path)
        # print("add_handler {0}".format(words))
        self.router.insert(words, handler_message)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        words = self.split_path(path)
        # print("lookup {0}".format(words))
        cur_node = self.router.find(words)
        if cur_node:
            # print(len(cur_node.children))
            if cur_node.handler:
                return cur_node.handler
            return self.lookup("404")

        return self.lookup("404")

    def split_path(self, path):
        # you need to split the path into parts for; both the add_handler and lookup functions,
        # so it should be placed in a function here
        words = list()
        if path == "/":
            words.append(path)
            return words
        for word in path.split("/"):
            if word != '':
                words.append(word)
        return words


router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/sport/football/liverpool", "All about Liverpool FC, the current european champions")  # add a route
router.add_handler("/sport/football/", "All about Football")  # add a route
router.add_handler("/sport/football/manc", "All about, Manchester City english champions")  # add a route
router.add_handler("/sport/football/premier-league/table", "Premier League Table")

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # Page not found!
print(router.lookup(""))  # Page not found!
router.add_handler("/home/", "Will be ready for in the next phase of dev")  # add a route
print(router.lookup("/sport/football/premier-league/table"))  # Premier League Table
print(router.lookup("/home/about"))  # 'about handler'
print(router.lookup("/home/about/"))  # 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/sport/football/liverpool"))  # All about Liverpool FC, the current european champions
print(router.lookup("/sport/football/"))  # All about Football
print(router.lookup("/sport/football/manc/"))  # All about, Manchester City english champions
print(router.lookup("//sport/football/manc/"))  # All about, Manchester City english champions
print(router.lookup("//sport/football/manu/"))  # Page not found!

router.add_handler("3/tutorial/index.html", "The Python Tutorial")  # add a route
print(router.lookup("3/tutorial/index.htm"))  # Page not found!
print(router.lookup("/home/about/me"))  # Page not found!

