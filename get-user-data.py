from github_scraper.repo_processing import repo_processing as RepoProcessing
from github_scraper.regex_matching.main_control import main as find_vulnerabilities
from github_scraper.utilities import display_results, save_results
from collections import defaultdict
import os


api_token = ''
#headers = {'Authorization': f'token {api_token}'}
headers = {}

username_path = 'username_data'
username_dir = os.fsencode(username_path)

data = defaultdict(int)
count = 0

for f in os.listdir(username_dir):
    file_path = username_path + '/' + os.fsdecode(f)
    with open(file_path, 'r') as read_file:
        for line in read_file:
            username = line.strip()
            count += 1

            print(f'Getting all files for user {username}')
            repo_files = RepoProcessing.get_all_files_for_user(username, headers)
            print(f'Recieved all files from {username}')
            results = find_vulnerabilities(repo_files)

            for file, v_list in results.items():
                if  v_list:
                    for v in v_list:
                        v_type, _, line = v.partition(':')
                        data[v_type] += 1

            print(data)
            print(f'Username count: {count}')

            if (count == 2):
                break
    if (count == 2):
        break


print(data)