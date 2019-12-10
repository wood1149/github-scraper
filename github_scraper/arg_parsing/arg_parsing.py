''' arg_parsing module. '''
import argparse

from repo_processing import repo_processing as RepoProcessing
from regex_matching.main_control import main as find_vulnerabilities
from utilities import display_results, save_results

# Hardcoded strings, maybe replace with configuration file
desc = ''

def setup_argparse():
    parser = argparse.ArgumentParser(description='GitHub repository file vulnerability finder')

    # Add the CL args
    parser.add_argument('-u', '--username', required=True, help='GitHub username')
    parser.add_argument('-r', '--repo', help='Repository name')
    parser.add_argument('-s', '--save', help='File name to which output will be saved (within output/ dir). If not provided, results only displayed on console.')
    parser.add_argument('-t', '--token', help='Github API Token')

    # Check for these vulnerabilities
    vuln_group = parser.add_argument_group('Vulnerability types')
    vuln_group.add_argument('--api', help='Look for API keys', action='store_true')
    vuln_group.add_argument('-p', '--password', help='Look for passwords', action='store_true')
    vuln_group.add_argument('-e', '--email', help='Look for email addresses', action='store_true')
    vuln_group.add_argument('-b', '--bitcoin', help='Look for bitcoin', action='store_true')
    vuln_group.add_argument('-c', '--crypto', help='Look for cryptographic keys', action='store_true')



    args = parser.parse_args()
    

    if args.api or args.password or args.email or args.bitcoin or args.crypto:
        types = set()
        if args.api:
            types.add('API')
        if args.password:
            types.add('Password')
        if args.email:
            types.add('Email')
        if args.crypto:
            types.add('Crypto')
    else:
        types = {'API', 'Password', 'Email', 'Crypto'}
    
    if args.token:
        headers = {'Authorization': f'token {args.token}'}
    else:
        headers = {}

    if args.repo:
        # Repo name provided
        print(f'Scraping {args.repo} repository')
        repo_files = RepoProcessing.get_repo_files(args.username, args.repo, headers)
        print("Recieved files from " +str(args.username) +"/"+ str(args.repo))
        v = find_vulnerabilities(repo_files)
        display_results(v, types)

        if args.save:
            save_results(v, args.save)
    else:
        print(f'Scraping repositories for user {args.username}')
        repo_names = RepoProcessing.get_user_repos(args.username, headers)
        print('Repository names:')
        for i in range(len(repo_names)):
            print(f'{i + 1}. {repo_names[i]}')
        print(f'{len(repo_names) + 1}. All repositories')

        repo_num = int(input(f'Enter a repository number to scrape ({len(repo_names) + 1} for all): ')) - 1

        if repo_num == len(repo_names):
            print('Scraping all repositories')
            all_files = RepoProcessing.get_all_files_for_user(args.username, headers)
            v = find_vulnerabilities(all_files)
            display_results(v, types)
        else:
            print(f'Scraping {repo_names[repo_num]} repository')
            repo_files = RepoProcessing.get_repo_files(args.username, repo_names[repo_num], headers)
            print("Recieved files from " +str(args.username) +"/"+ str(repo_names[repo_num]))
            v = find_vulnerabilities(repo_files)
            display_results(v, types)

