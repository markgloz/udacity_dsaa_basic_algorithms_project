class RouteTrie:
    """
    RouteTrie will store routes and their associated handlers.
    """
    def __init__(self, not_found_handler) -> None:
        self.root = RouteTrieNode()
        self.not_found_handler = not_found_handler
    
    def insert(self, route, handler):
        node = self.root
        paths = self._get_paths(route)
        for path in paths:
            if path not in node.children:
                node.insert(path)
            node = node.children[path]
        node.handler = handler

    def find(self, route):
        if route is None:
            return self.not_found_handler
        node = self.root
        paths = self._get_paths(route)
        for path in paths:
            if path not in node.children:
                return self.not_found_handler
            node = node.children[path]
        if node.handler:
            return node.handler
        else:
            return self.not_found_handler
    
    def _get_paths(self, route):
        paths = []
        path = ''
        for char in route:
            if char == '/':
                if path:
                    paths.append(path)
                    path = ''
            else:
                path += char
        if path:
            paths.append(path)
        return paths


class RouteTrieNode:
    """
    RouteTrieNode will be a node in RouteTrie and have the handler as an attribute.
    """
    def __init__(self, handler = None) -> None:
        self.handler = handler
        self.children = {}
    
    def insert(self, route):
        self.children[route] = RouteTrieNode()


class Router:
    def __init__(self, root_handler, not_found_handler) -> None:
        self.route_trie = RouteTrie(not_found_handler)
        self.add_handler('/', root_handler)
    
    def add_handler(self, path, handler):
        if path is not None:
            self.route_trie.insert(path, handler)
    
    def lookup(self, path):
        return self.route_trie.find(path)

# Supplied tests

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

# Test 1 - Normal use case
router.add_handler("/home/my/awesome/blob", "blog handler")
print(router.lookup("/home/my/awesome/blob")) # blog handler

# Test 2 - Null
router.add_handler("/some/path", None)
router.add_handler(None, "some handler")

print(router.lookup("/some/path")) # not found handler
print(router.lookup(None)) # not found handler

# Test 3 - Empty
router.add_handler("", "empty handler")
print(router.lookup("")) # empty handler (overwrites root handler)

# Test 4 - Large value
router.add_handler("/some/very/long/path/that/goes/to/some/handler", "handler for long path")
print(router.lookup("/some/very/long/path/that/goes/to/some/handler")) # handler for long path

print(router.lookup("/some/very/long/path/that/goes/to/some")) # not found handler

print(router.lookup("/some/very/long/path/that/goes/to/handler")) # not found handler
