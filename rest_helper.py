
"""
Usage:
    rest_helper.py -n <num> -c <config>

Options:
    -n, --num <num>         Number (larger than 0) 
    -c, --config <config>   Config file
    -h, --help              Show this screen and exit.
"""

import os.path
import string
from docopt import docopt

try:
    import configparser
except ImportError:
    from six.moves import configparser
    
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse
   
class OutsideRange(Exception):
    """The value is outside the range..."""
    pass
        
class NonExistent(Exception):
    """File not found..."""
    pass

class RestHelper(object):    
    def __init__(self):
        self.parser = configparser.SafeConfigParser()
        
    def getArgs(self):
        arguments = docopt(__doc__)
        self.num = int(arguments['--num'])
        self.config = arguments['--config']
        
    def verifyArgs(self):
        try:
            if not 1 <= self.num:
                raise OutsideRange
            if not os.path.isfile(self.config):
                raise NonExistent
        except OutsideRange:
            print ("%s is less than 1 .." % self.num)
            exit(1)
        except NonExistent:
            print ("%s was not found .." % self.config)
            exit(1)
                
    def readConfig(self):
        self.parser.read(self.config)
        count = 0
            
        username = self.parser.get('Data', 'username')
        urlpath  = self.parser.get('Data', 'urlpath')
        for name, value in self.parser.items("Urls"):
            count += 1
            uo = urlparse(value)
                
            print "%s://%s@%s%s" % (uo.scheme, username, uo.netloc, urlpath )
                
            if count == int(self.num):
                break
                    
def main():
    rh = RestHelper()
    rh.getArgs()
    rh.verifyArgs()
    rh.readConfig()

if __name__ == '__main__':
    main() 
