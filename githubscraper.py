import sys
import requests

BASE_URL = 'https://api.github.com'

# Used so script ignores binary files
# We could do another way later if we don't want to list out all extensions we want
SCRAPABLE_EXTENSIONS = {'cpp', 'txt', 'py', 'config', 'c'}

def get_user_repos(username):
    """Gets list of public repositories owned by a particular user
    
        [:param `username`] the String representation of the user's username
        
        [:rtype] `list` of dictionaries
        
        [:returns] a list of the public repositories owned by the user
    """
    
    url = f'{BASE_URL}/users/{username}/repos'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as e:
        sys.exit(e)

    all_repo_names = []
    for repo in response.json():
        all_repo_names.append(repo['name'])
    return all_repo_names


def get_repo_files(username, repo_name, path=''):
    """Gets list of all files for a specific user
    
        [:param `username`] the String representation of the user's username
        [:param `repo_name`] the String representation of the name of a repository
        [:param `path`] the String representation of the path of a directory within a repository. Used in recursive calls.
        
        [:rtype] `list` of dictionaries
        
        [:returns] a list of all the files from a given user's repository
    """

    repo_files = {}
    url = f'{BASE_URL}/repos/{username}/{repo_name}/contents/{path}'

    try:
        response = requests.get(url)
        res = response.json()

        # Recursively call get_repo_files on directories
        for r in res:
            if r['type'] == 'dir':
                repo_files.update(get_repo_files(username, repo_name, r['path']))
            else:
                filename = r['name']
                file_ext = filename.split(".")[-1]

                if file_ext in SCRAPABLE_EXTENSIONS:
                    file_path = r['path']
                    file_path = repo_name + '/' + file_path
                    download_url = r['download_url']
                    content = requests.get(download_url).text
                    repo_files[file_path] = content

    except requests.HTTPError as e:
        sys.exit(e)

    return repo_files

def get_all_files_for_user(username):
    all_files = {}
    repo_names = get_user_repos(username)
    for name in repo_names:
        repo_files = get_repo_files(username, name)
        all_files.update(repo_files)
    return all_files

if __name__ == '__main__':
    username = 'kklose23'

    files = get_all_files_for_user(username)
    print(files)

    '''
    repo_names = get_user_repos(username)
    print(repo_names)

    for name in repo_names:
        contents = get_repo_files(username, name)
        print(contents)
    '''


