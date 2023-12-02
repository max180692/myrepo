import collections


m = collections.ChainMap()
list_user = [m]
def nw(user):
    list_user[0] = list_user[0].new_child(user)

nw({'n':1234})

print(list_user)
