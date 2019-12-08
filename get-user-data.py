from github_scraper.repo_processing import repo_processing as RepoProcessing
from github_scraper.regex_matching.main_control import main as find_vulnerabilities
from github_scraper.utilities import display_results, save_results
from collections import defaultdict
import os




username_path = 'username_data'

username_dir = os.fsencode(username_path)

count = 0

for f in os.listdir(username_dir):
    file_path = username_path + '/' + os.fsdecode(f)
    with open(file_path, 'r') as read_file:
        for line in read_file:
            count += 1
            print(line, end='')

print(count)
exit()

username = 'daphneehuang'
repo = 'cse4471-demo'


print(f'Scraping {repo} repository')
repo_files = RepoProcessing.get_repo_files(username, repo)
print("Recieved files from " +str(username) +"/"+ str(repo))
results = find_vulnerabilities(repo_files)


data = defaultdict(int)

for file, v_list in results.items():
    if  v_list:
        for v in v_list:
            v_type, _, line = v.partition(':')
            data[v_type] += 1

print(data)