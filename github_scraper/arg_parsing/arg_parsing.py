''' arg_parsing module. '''
import argparse

from sample_module import test, test2

# Hardcoded strings, maybe replace with configuration file
desc = ''

def setup_argparse():
    ''' Sets up the argument parsing
        for the program.
    '''
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--sample', help='This is the sample module', action='store_true')
    arg_result = parser.parse_args()
    if arg_result.sample:
        # Sample was selected
        prompt = '1. Test\n2. Test2\n3. Exit\nOption: '
        exit_cond = 3
        func_ptrs = [test.func, test2.func]
        setup_looping_menu(prompt, exit_cond, func_ptrs)

def setup_looping_menu(prompt, exit_cond, func_ptrs):
    ''' Setup a looping menu using the provided prompt and exit condition.

        Args:
            prompt: String prompt to display to the user
            exit_cond: The exit value needed to break the loop as an integer
            func_ptrs: Array containing function pointers. Indexes should match
                the command line options
    '''
    option = 0
    while option != exit_cond:
        try:
            option = int(input(prompt))
        except ValueError:
            print('Please enter a valid integer')
        if option != exit_cond and option <= len(func_ptrs):
            func_ptrs[option-1]()
        elif option > len(func_ptrs):
            print('Please enter a valid option')
    print('Goodbye!')

