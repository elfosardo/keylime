'''
DISTRIBUTION STATEMENT A. Approved for public release: distribution unlimited.

This material is based upon work supported by the Assistant Secretary of Defense for 
Research and Engineering under Air Force Contract No. FA8721-05-C-0002 and/or 
FA8702-15-D-0001. Any opinions, findings, conclusions or recommendations expressed in this
material are those of the author(s) and do not necessarily reflect the views of the 
Assistant Secretary of Defense for Research and Engineering.

Copyright 2015 Massachusetts Institute of Technology.

The software/firmware is provided to you on an As-Is basis

Delivered to the US Government with Unlimited Rights, as defined in DFARS Part 
252.227-7013 or 7014 (Feb 2014). Notwithstanding any copyright notice, U.S. Government 
rights in this work are defined by DFARS 252.227-7013 or DFARS 252.227-7014 as detailed 
above. Use of this work other than as specifically authorized by the U.S. Government may 
violate any copyrights that exist in this work.
'''

import argparse
import sys 
import glob
import numpy



def main(argv=sys.argv):
    parser = argparse.ArgumentParser("keylime-utility-smoother")
    parser.add_argument('-f', '--filename', required=True, action='store',dest='filename')
    parser.add_argument('-t', '--text_description', action='store',dest='text_description')

    concat_content = []
    args = parser.parse_args(argv[1:])
    for each_file in glob.glob(args.filename + "*.txt"):
    # command line options can overwrite config values
        if each_file is not None:
            with open(each_file) as f:
                content = [x.strip() for x in f.readlines()]
                #remove last element (could be weird)
                #del content[-1:]
                concat_content.extend(content)
                    
    float_list = []
    for i in concat_content:
        float_list.append(float(i))
    
    time = float_list[-1]-float_list[0]
    print("%s %.3f"%(args.text_description,len(float_list)/time))
        

if __name__=="__main__":
    main()
    