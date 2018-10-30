import os

DISABLE_CLASS=11
ENABLE_CLASS=12
DEV='ens33'

#add_filter_command='tc filter add dev %s parent 1: prio 1 protocol ip u32 match ip sport %s 0xffff flowid 1:11' % ('ens33', '9800')
#del_filter_command='tc filter del dev %s parent 1: prio 1 protocol ip u32 match ip sport %s 0xffff flowid 1:11' % ('ens33', '9800')

def disable_user(user_port):
    hex_port=hex(user_port).replace('0x', '')
    filter_list_comand = 'tc filter ls dev %s|grep %s -B 1|grep %s' % (DEV, hex_port, ENABLE_CLASS)
    filters = os.popen(filter_list_comand).readlines()
    for fil in filters:
        handle = fil.split(' ')[9]
        del_filter_command='tc filter del dev %s parent 1: handle %s protocol ip pref 1 u32' % (DEV, handle)
        res=os.popen(del_filter_command)
    filter_list_comand = 'tc filter ls dev %s|grep %s -B 1|grep %s' % (DEV, hex_port, DISABLE_CLASS)
    filters = os.popen(filter_list_comand).readlines()
    if filters:
        return
    add_filter_command='tc filter add dev %s parent 1: prio 1 protocol ip u32 match ip sport %s 0xffff flowid 1:%s' % (DEV, user_port, DISABLE_CLASS)
    res=os.popen(add_filter_command)

def enable_user(user_port):
    hex_port=hex(user_port).replace('0x', '')
    filter_list_comand = 'tc filter ls dev %s|grep %s -B 1|grep %s' % (DEV, hex_port, DISABLE_CLASS)
    filters = os.popen(filter_list_comand).readlines()
    for fil in filters:
        handle = fil.split(' ')[9]
        del_filter_command='tc filter del dev %s parent 1: handle %s protocol ip pref 1 u32' % (DEV, handle)
        res=os.popen(del_filter_command)
    filter_list_comand = 'tc filter ls dev %s|grep %s -B 1|grep %s' % (DEV, hex_port, ENABLE_CLASS)
    filters = os.popen(filter_list_comand).readlines()
    if filters:
        return
    add_filter_command='tc filter add dev %s parent 1: prio 1 protocol ip u32 match ip sport %s 0xffff flowid 1:%s' % (DEV, user_port, ENABLE_CLASS)
    res=os.popen(add_filter_command)

if __name__=='__main__':
    enable_user(6789)
    enable_user(6780)
#    disable_user(7780)
#    enable_user(6700)
    disable_user(10000)

