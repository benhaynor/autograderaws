import os
import sys
import shutil

def main(args):
    import curr_conv_test
    failures = curr_conv_test.get_failures()
    if failures:
        print "%s,%s,%s" % (args[1], 0.0, 1)
    else:
        '''
        Passed all tests... loading to 
        '''
        print "%s,%s,%s" % (args[1], 1.1, 1)

if __name__=='__main__':
    
    main(sys.argv)
