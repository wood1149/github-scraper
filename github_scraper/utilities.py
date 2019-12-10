
api_key_min_entropy_ratio = 0.5


def display_results(results, types):
    """Prints the results of vulnerability searches to the terminal
    
        [:param `results`] a dictionary of key/value pairs, where the key is a file path string, and the value is a list of strings representing vulnerabilities in that file. The vulnerability string is formatted as "type:line_num"
    """
    no_vuln = True

    print('The following vulnerabilities were found: ')
    for file, v_list in results.items():
        if  v_list:
            print(file)
            for v in v_list:
                type, _, line = v.partition(':')
                if type in types:
                    no_vuln = False
                    print(f' * {type} at line {line}')

    if no_vuln:
        print("None")
    return

def save_results(results, file_name):
    """Saves the results of vulnerability searches to a file in output/ dir
    
        [:param `results`] a dictionary of key/value pairs, where the key is a file path string, and the value is a list of strings representing vulnerabilities in that file. The vulnerability string is formatted as "type:line_num"

        [:param `file_name`] a string representing the file path where the results will be written
    """

    with open(f'output/{file_name}', mode='x') as fp:

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