class TreeNode:
    def __init__(self, key):
        self.__key = key
        self.__left = None
        self.__right = None
        self.__parent = None

    def __del__(self):
        print(f'key {self.__key} is deleted')

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, p):
        self.__parent = p
