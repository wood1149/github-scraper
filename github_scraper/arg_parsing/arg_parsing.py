''' arg_parsing module. '''
import argparse

from sample_module import test, test2
from APIRegexMatching import matchAPI

# Hardcoded strings, maybe replace with configuration file
desc = ''

def setup_argparse():
    desc = 'GitHub repository file vulnerability finder'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-u', '--username', required=True, help='GitHub username')
    args = parser.parse_args()

