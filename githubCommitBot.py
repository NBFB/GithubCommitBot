from urllib2 import urlopen
import json


#[TODO: Data pagination]
def get_commits(owner, repo):
    url = 'https://api.github.com/repos/{owner}/{repo}/commits'.format(owner=owner, repo=repo)
    response = urlopen(url).read()
    data = json.loads(response.decode())
    return data


if __name__ == '__main__':
    commits = get_latest_commits('techstart-dev', 'techstart-dev.github.io')
    for commit in commits:
    	print(commit['commit']['committer']['date'])