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

	GIT_HANDLE 	= 'techstart-dev'
	REPO_NAME 	= 'techstart-dev.github.io'
	OUTPUT_CSV  = 'output.csv'

	commits = get_commits(GIT_HANDLE, REPO_NAME)
	csvApp = csv.writer(open('output.csv', "wb+"))
	csvApp.writerow(["repo", "date","name","email"])

	for commit in commits:
		commit_commiter_info = commit['commit']['committer']
		
		date 	= commit_commiter_info["date"]
		name 	= commit_commiter_info["name"]
		email 	= commit_commiter_info["email"]

		csvApp.writerow([REPO_NAME, date, name, email])

	print "Script ran succesfuly."
