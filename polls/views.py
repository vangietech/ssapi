# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
import random
import os
import json

from sssdk import ShadowsocksSDK
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

DISABLE_CLASS=11
ENABLE_CLASS=12
DEV='eth0'

@csrf_exempt
def ss_user(request, user_id=None):
    ss = ShadowsocksSDK('127.0.0.1', 62500)
    if request.method == 'GET':
        port = get_port()
        password = create_passwd()
        ss.add_user(port, password)
        user_info = {'userIp': '35.200.100.180', 'userPort': port, 'userPassword': password}
        return HttpResponse(json.dumps(user_info))
    if request.method == 'DELETE':
        users = list_users()
        if user_id in users:
            ss.remove_user(int(user_id))
            return HttpResponse("OK")
        string = request.method + user_id
        return HttpResponse("User not found.")

def all_users(request):
    users = list_users()
    all_user = {'users': users}
    return HttpResponse(json.dumps(all_user))

def enable_user(request, user_port=None):
    hex_port=hex(int(user_port)).replace('0x', '') 
    filter_list_comand = 'tc filter ls dev %s|grep %s -B 1|grep %s' % (DEV, hex_port, DISABLE_CLASS)
    filters = os.popen(filter_list_comand).readlines()
    for fil in filters:
        handle = fil.split(' ')[9]
        del_filter_command='tc filter del dev %s parent 1: handle %s protocol ip pref 1 u32' % (DEV, handle)
        res=os.popen(del_filter_command)
    filter_list_comand = 'tc filter ls dev %s|grep %s -B 1|grep %s' % (DEV, hex_port, ENABLE_CLASS)
    filters = os.popen(filter_list_comand).readlines()
    if filters:
        return HttpResponse("The user already enabled.")
    add_filter_command='tc filter add dev %s parent 1: prio 1 protocol ip u32 match ip sport %s 0xffff flowid 1:%s' % (DEV, user_port, ENABLE_CLASS)
    res=os.popen(add_filter_command)
    info = "user: %s enabled" % (user_port)
    return HttpResponse(info)

def disable_user(request, user_port=None):
    hex_port=hex(int(user_port)).replace('0x', '') 
    filter_list_comand = 'tc filter ls dev %s|grep %s -B 1|grep %s' % (DEV, hex_port, ENABLE_CLASS)
    filters = os.popen(filter_list_comand).readlines()
    for fil in filters:
        handle = fil.split(' ')[9]
        del_filter_command='tc filter del dev %s parent 1: handle %s protocol ip pref 1 u32' % (DEV, handle)
        res=os.popen(del_filter_command)
    filter_list_comand = 'tc filter ls dev %s|grep %s -B 1|grep %s' % (DEV, hex_port, DISABLE_CLASS)
    filters = os.popen(filter_list_comand).readlines()
    if filters:
        return HttpResponse("The user already disabled.")
    add_filter_command='tc filter add dev %s parent 1: prio 1 protocol ip u32 match ip sport %s 0xffff flowid 1:%s' % (DEV, user_port, DISABLE_CLASS)
    res=os.popen(add_filter_command)
    info = "user: %s diabled" % (user_port)
    return HttpResponse(info)

def list_users():
    users = []
    pscmd = "netstat -ntl |grep -v Active| grep -v Proto|awk '{print $4}'|awk -F: '{print $NF}'"
    procs = os.popen(pscmd).read()
    ports = procs.split("\n")
    for port in ports:
        if port.isdigit() and int(port) >= 16000 and int(port) <= 62000:
            users.append(port)
    return users

def create_passwd():
    upper_letters = []
    for n in range(0, 5):
        upper_letters.append(chr(random.randint(65, 90)))
    password = str(uuid.uuid1()).split('-')[0]
    for upper in upper_letters:
        n = random.randint(0, len(password))
        password = password[0:n]+upper+password[n:]
    return password

def get_port():
    pscmd = "netstat -ntl |grep -v Active| grep -v Proto|awk '{print $4}'|awk -F: '{print $NF}'"
    procs = os.popen(pscmd).read()
    procarr = procs.split("\n")
    while True:
        port = random.randint(16000, 62000)
        if str(port) not in procarr:
            break
    return port

if __name__ == '__main__':
    print list_user()


