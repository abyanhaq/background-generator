class SuperList(list):
    def __init__(self, _list):
        self._list = _list
    def __len__(self):
        return 1000
    
super_list1 = SuperList([1, 2, 3])
print(len(super_list1))
super_list1.append(5)
print(super_list1)

