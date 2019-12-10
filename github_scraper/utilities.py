import math, itertools

api_key_min_entropy_ratio = 0.5

def get_token_pairs(characters):
    """Returns the mapping of each individual character to the next in the list
    """
    a, b = itertools.tee(characters)
    next(b, None)
    return zip(a, b)

def entropy(s):
	"""Returns the entropy of the string s
	"""
	e = 0
	for a, b in get_token_pairs(list(s)):
		if not ((str.islower(a) and str.islower(b)) or (str.isupper(a) and\
			str.isupper(b)) or (str.isdigit(a) and str.isdigit(b))):
			e += 1
	return float(e) / len(s)

def display_results(results, types):
    """Prints the results of vulnerability searches to the terminal
    
        [:param `results`] a dictionary of key/value pairs, where the key is a file path string, and the value is a list of strings representing vulnerabilities in that file. The vulnerability string is formatted as "type:line_num"
    """
    if results:
        print('The following vulnerabilities were found:')

        for file, v_list in results.items():
            if  v_list:
                print(file)
                for v in v_list:
                    type, _, line = v.partition(':')
                    if type in types:
                        print(f' * {type} at line {line}')
    else:
        print('No vulnerabilities were found')

    return

def save_results(results, file_name):
    """Saves the results of vulnerability searches to a file
    
        [:param `results`] a dictionary of key/value pairs, where the key is a file path string, and the value is a list of strings representing vulnerabilities in that file. The vulnerability string is formatted as "type:line_num"

        [:param `file_name`] a string representing the file path where the results will be written
    """

    with open(file_name, mode='x') as fp:

        if results:
            fp.write('The following vulnerabilities were found:\n')

            for file, v_list in results.items():
                if  v_list:
                    fp.write(f'{file}\n')
                    for v in v_list:
                        type, _, line = v.partition(':')
                        fp.write(f' * {type} at line {line}\n')
        else:
            fp.write('No vulnerabilities were found\n')