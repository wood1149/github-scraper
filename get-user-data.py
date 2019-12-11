from github_scraper.repo_processing import repo_processing as RepoProcessing
from github_scraper.regex_matching.main_control import main as find_vulnerabilities
from github_scraper.utilities import display_results, save_results
from collections import defaultdict, Counter
import os

headers = {}

# Once API token is obtained from Github
#api_token = '*'
#headers = {'Authorization': f'token {api_token}'}

username_path = 'username_data'
username_dir = os.fsencode(username_path)

all_data = Counter()
per_user_data = Counter()

user_count = 0

for f in os.listdir(username_dir):
    file_path = username_path + '/' + os.fsdecode(f)
    with open(file_path, 'r') as read_file:
        for line in read_file:
            user_count += 1
            curr_user_data = Counter()
            username = line.strip()

            print(f'Getting all files for user {username}')
            repo_files = RepoProcessing.get_all_files_for_user(username, headers)
            print(f'Recieved all files from {username}')
            results = find_vulnerabilities(repo_files)
            for file, v_list in results.items():
                if  v_list:
                    for v in v_list:
                        v_type, _, line = v.partition(':')
                        curr_user_data[v_type] += 1

            all_data = all_data + curr_user_data
            for key in curr_user_data:
                per_user_data[key] += 1


            print(f'All Data: {all_data}')
            print(f'Per User Data: {per_user_data}')
            print(f'Username count: {user_count}')
