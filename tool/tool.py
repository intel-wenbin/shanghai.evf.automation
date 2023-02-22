import sys

import getopt
import sys
from module.hsd_num_verify import hsd_verify


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hc", ["file1=", "file2="])
    except getopt.GetoptError:
        print('tool.py -c <file1> <file2>')
        sys.exit(2)
    for opt in argv:
        if opt == '-c':
            if len(argv) == 3:
                file1 = args[0]
                file2 = args[1]
                try:
                    hsd_verify(file1, file2)
                except:
                    print('File1 should be csv format , now it is :  ', file1)
                    print('File2 should be excel format: now it is : ', file2)
            else:
                print('tool.py -c ' + file1 + " " + file2)
                sys.exit()
        elif opt == "-h":
            print('-c  <format: -c file1 file2>         Description: HSD Number Verification')
            sys.exit()



if __name__ == "__main__":
    main(sys.argv[1:])
