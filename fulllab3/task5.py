import os
from graphviz import Graph
import shlex
from subprocess import Popen, PIPE, STDOUT
import socket
import subprocess
import threading
from datetime import datetime
from random import randint
net = "192.168.1."
DEVNULL = open(os.devnull, 'w')


def scan(addr):
    try:
        subprocess.check_call(['ping', addr], stdout=DEVNULL)
        return addr
    except Exception as e:
        print(e)


id_list = [scan("8.8.8.8"), scan("168.0.1.2")]


def get_simple_cmd_output(cmd, stderr=STDOUT):
    args = shlex.split(cmd)
    print(args)
    return Popen(args, stdout=PIPE, stderr=stderr).communicate()[0]


def get_ping_time(host):
    cmd = f"ping {host} ".format(host=host)
    print(cmd)
    res = [
        x for x in get_simple_cmd_output(cmd).strip().split(b':')[-1].split()
        if x != '-'
    ]
    z = []

    for i in res:
        z.append(i.strip().decode("cp866"))
    print(z)
    #return sum(res) / len(res)

    return z[len(z) - 2]


size_list = []

for i in id_list:
    print(i)
    size_list.append(get_ping_time(i))

print(size_list)
print(id_list)


def newdiap(x):
    result = float(x) * 0.05
    return str(result)


maxx = max(size_list)
minn = min(size_list)
# for i in size_list:
#     if i > maxx: maxx = i
#     if i < minn: minn = i

#os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'
g = Graph('G', filename='test6.gv', engine='neato')

for i in range(0, len(id_list)):
    if '192.168.1.109' != id_list[i]:
        g.edge('192.168.1.109',
               id_list[i],
               label=str(size_list[i]) + "мс",
               len=str(newdiap(size_list[i])))

g.render()