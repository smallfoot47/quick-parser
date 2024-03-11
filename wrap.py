import sys
import re

if len(sys.argv) < 5:
    
    if len(sys.argv) == 3:
        with open(sys.argv[1]) as config:
            [ head, body_format, tail, axe, glue ] = config.readlines()
            head = head[:-1]
            body_format = body_format[:-1]
            tail = tail[:-1]
            axe = axe[:-1]
            
            data_file = sys.argv[2]
    else:   
        print("usage: py wrap.py <header> <data format> <data file> <tail> [separator:' '] [joiner: ',']")
        print("In <data format>, use {0}, {1}, ... {n-1} to denote the nth argument from data file")
        exit(1)
else:
    head = sys.argv[1]
    body_format = sys.argv[2]
    data_file = sys.argv[3]
    tail = sys.argv[4]
    axe = sys.argv[5] if len(sys.argv) > 5 else ' '
    glue = sys.argv[6] if len(sys.argv) > 6 else ','
    
def print_proper(msg):
    msg = re.sub(r'(?<!\\)\\n', r'\n', msg)
    print(msg, end='')


with open(data_file) as data:
    
    print_proper(head)
    
    body = []
    for line in data.read().splitlines():
        tokens = line.split(axe)
        body.append(body_format.format(*tokens))
    
    print_proper(glue.join(body))
    
    print_proper(tail)