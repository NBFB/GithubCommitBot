# GithubCommitBot
Automated Commit Aggregator and Processor 

## Setup
- [Install Python 3](https://www.python.org/downloads/) 
- [Install PIP](https://packaging.python.org/tutorials/installing-packages/)
- PIP Install urllib2
```
pip install urlib2
```

## Usage
1. Clone Repo
2. CD into root directory
3. Run this command
```
python githubCommitBot.py
```
This will generate a file called **output.csv** in the project's root directory.

## Resources
-[Github Developer Guide](https://developer.github.com/v3/)

## TODO
- More collumns
- Data Pagination
- Arguments
- Read CSV
- Deal with Rate limiting Issues - Threads/Locks/Chronjobs
- Integrate with existing TechStart technology - webhooks, IFTTT, Zappier
- Write up tutorial so others can contribute or repurpose knowledge
