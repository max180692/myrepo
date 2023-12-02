from registruser import RegisterUser
import collections

 

reg_user = RegisterUser()
reg_user.set_user_info('max',12345)
print(reg_user.get_info_user())
n = collections.ChainMap()
if reg_user.get_info_user()['id'] not in list(n.values()):
    n = n.new_child(reg_user.get_info_user())
    print(n)


reg_user.set_user_info('nik',12345)
if reg_user.get_info_user()['id'] not in list(n.values()):
    n = n.new_child(reg_user.get_info_user())
    print(n)
else:
    print('Error')
