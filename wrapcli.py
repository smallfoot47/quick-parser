import sys
import wrapper

if len(sys.argv) < 5:
    
    if len(sys.argv) == 3:
        with open(sys.argv[1]) as config:
            [ head, body_format, foot, axe, glue ] = config.readlines()
            head = head[:-1]
            body_format = body_format[:-1]
            foot = foot[:-1]
            axe = axe[:-1]
            
            data_file = sys.argv[2]
    else:   
        print("usage: py wrap.py <header> <data format> <data file> <foot> [separator:' '] [joiner: ',']")
        print("In <data format>, use {0}, {1}, ... {n-1} to denote the nth argument from data file")
        exit(1)
else:
    head = sys.argv[1]
    body_format = sys.argv[2]
    data_file = sys.argv[3]
    foot = sys.argv[4]
    axe = sys.argv[5] if len(sys.argv) > 5 else ' '
    glue = sys.argv[6] if len(sys.argv) > 6 else ','

wrapper = wrapper.Wrapper(header=head, body_fmt=body_format, footer=foot, axe=axe, glue=glue)
print(wrapper.Wrap(data_file))