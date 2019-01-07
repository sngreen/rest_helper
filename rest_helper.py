
"""
Usage:
    rest_helper.py -n <num> -c <config>
Options:
    -n, --num <num>         Number between 1 and 4
    -c, --config <config>   Config file
    -h, --help              Show this screen and exit.
"""

import os.path
from docopt import docopt

try:
    import configparser
except:
    from six.moves import configparser

class RestHelper(object):    
    def __init__(self):
        self.parser = configparser.SafeConfigParser()
        
    def getArgs(self):
        arguments = docopt(__doc__)
        self.num = int(arguments['--num'])
        self.config = arguments['--config']
                    
    def ifNum(self):
        if not 1 <= self.num <= 4:
            print ("%s is outside [1-4] range .." % self.num)
            exit(1)
            
    def ifConfig(self):
        if not os.path.isfile(self.config):
            print ("%s was not found .." % self.config)
            exit(1)
            
    def readConfig(self):
        self.parser.read(self.config)
        count = 0
        
        # apparently we are only interested in "Urls"
        for name, value in self.parser.items("Urls"):
            count += 1
            print (value) 
            if count == int(self.num):
                break
                    
def main():
    rh = RestHelper()
    rh.getArgs()
    rh.ifNum()
    rh.ifConfig()
    rh.readConfig()

if __name__ == '__main__':
    main() 
