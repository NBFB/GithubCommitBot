from urllib2 import urlopen
import json
import csv

### scrapes a repo for commits
# input: owner (string), repo (string)
# return: array of json entries representing commits
#
### TODOS
#   pagination

def get_commits(owner, repo):
    url = 'https://api.github.com/repos/{owner}/{repo}/commits'.format(owner=owner, repo=repo)
    response = urlopen(url).read()
    data = json.loads(response.decode())
    return data


if __name__ == '__main__':
    commits = get_commits('techstart-dev', 'techstart-dev.github.io')
    csvApp = csv.writer(open("output.csv", "wb+"))
    csvApp.writerow(["date","name","email"])
    for commit in commits:
    	print(commit['commit']['committer'])