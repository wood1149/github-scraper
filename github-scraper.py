# main module for github-scraper app
import sys
import requests

BASE_URL = 'https://api.github.com'

# this is not an exhaustive list of functions, will need to add to/refactor architecture of module depending on how we want to implement file access and reading

def get_user_repos(username):
    """Gets list of public repositories owned by a particular user
    
        [:param `username`] the String representation of the user's username
        
        [:rtype] `list` of dictionaries
        
        [:returns] a list of the public repositories owned by the user
    """
    
    url = f'{BASE_URL}/users/{username}/repos'

    try:
        response = requests.get(url)
        print(response.status_code)
        response.raise_for_status()
    except requests.HTTPError as e:
        sys.exit(e)

    return response.json()

def get_repo_files(username, repo_name, path=''):
    """Gets list of public repositories owned by a particular user
    
        [:param `username`] the String representation of the user's username
        [:param `repo_name`] the String representation of the name of a repository
        [:param `path`] the String representation of the path of a directory within a repository. Used in recursive calls.
        
        [:rtype] `list` of dictionaries
        
        [:returns] a list of all the files from a given user's repository
    """

    all_files = []
    url = f'{BASE_URL}/repos/{username}/{repo_name}/contents/{path}'

    try:
        response = requests.get(url)
        res = response.json()

        # Recursively call get_repo_files on directories
        for r in res:
            if r['type'] == 'dir':
                all_files.extend(get_repo_files(username, repo_name, r['path']))
            else:
                all_files.append(r)

    except requests.HTTPError as e:
        sys.exit(e)

    return all_files


def find_match(username, repo, file, pattern):
    # TODO: implement
    return

username = 'kklose23'

repos = get_user_repos(username)

print(f'Num repos: {len(repos)}')

repos.sort(key=lambda x: x['stargazers_count'], reverse=True)

print('Top 5 most starred repos:')

for repo in repos[0:5]:
    count = repo['stargazers_count']
    name = repo['name']
    print(f'{count}: {name}')
    contents = get_repo_files(username, name)
    for c in contents:
        filename = c['name']
        html_url = c['html_url']
        download_url = c['download_url']
        
        print(f'\tFile Name: {filename}')
        print(f'\tHTML URL: {html_url}')
        print(f'\tDownload URL: {download_url}\n')
