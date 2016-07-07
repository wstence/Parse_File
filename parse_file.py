# Simple program to parse data from file to be used elsewhere.
# Given a file with the original format, the program works.
# Tested on Ubuntu OS

def main():
    fname = '/home/fake/path'
    server_num = 0
    ostypes = []
    usage = 0;
    parseFile(fname, server_num, ostypes, usage)
    
def parseFile(f_name, num_of_servers, os_variety, active):
    f = open(f_name, 'r')

    lnum  = 1
    line = ''
    for line in f:
        if lnum == 2:
            num_of_servers = line
        if lnum == 5:
            d = line.split()
            os_variety = [str(i) for i in d]
        if lnum == 8:
            active = str(line)
        lnum += 1

    f.close()
    
    num_of_servers = int(num_of_servers)
    active = float(active)
    os_variety = [str(j) for j in os_variety]
    os_var_str = ', '.join(os_variety)
    
    print("File Data\nNumber of servers: ", num_of_servers, "\nOperating system variety: ",
        os_var_str, "\nPercentage of servers active: ", active)


if __name__ == '__main__':
    main()

