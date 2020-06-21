# mhapp.py

import sys
import mh


def run():
    print ('###################')
    print ('Version', sys.version)
    print ('VAR', mh.EG_VAR2)
    print ('func', mh.testFunction())
    print ('member', mh.Mh().runMh())

    print ( '------------')
    v = mh.EG_VAR2
    f = mh.testFunction()
    m = mh.Mh().runMh()
    print ( '------------')
    print ('v',v)
    print ('f',f)
    print ('m',m)


if __name__ == '__main__':
    run()