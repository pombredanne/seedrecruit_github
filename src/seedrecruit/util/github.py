import itertools
import pygments

from collections import defaultdict
from github3 import login
from github3.repos.commit import RepoCommit
from pygments.lexers import guess_lexer_for_filename
from seedrecruit.config import local


gh = login(local.USERNAME, token=local.OAUTH)


def get_push_events(username):
    user = gh.user(username)
    try:
        for event in user.iter_events():
            if not event.type == 'PushEvent':
                continue
            event.commits = list(get_commits(event))
            yield event
    except AttributeError:
        pass


def get_forked_repositories(username):
    for repo in gh.iter_user_repos(username):
        if not repo.fork:
            continue
        yield repo


def get_commits(push_event):
    """Returns the commit objects from a PushEvent"""
    owner, repository = push_event.repo
    repo = gh.repository(owner, repository)
    if not repo:  # the repository cannot be found.
        print 'Cannot find', owner, repository
        return
    for commit in push_event.payload['commits']:
        yield repo.commit(commit['sha'])

def append(main, child):
    """Appends the child statistics into the main dict, summing the values
    """
    for lang, occ in child['languages'].iteritems():
        main['languages'][lang] += occ
    main['commits'] += child['commits']


def get_statistics(username):
    """Returns some statistics for the username,
    the amount of commits in their public activity feed, also
    the top three languages which appear in their commits for example
        {
            'commits': 123,
            'languages': [
                'Java',
                'PHP',
                'Python',
            ]
        }
    """
    statistics = {}
    statistics['languages'] = defaultdict(int)
    statistics['commits'] = 0

    for event in get_push_events(username):
        statistics['commits'] += len(event.commits)
        for commit in event.commits:
            if not commit:
                continue
            langs = get_commit_statistics(commit)
            for name, occurences in langs.items():
                statistics['languages'][name] += occurences

    statistics['languages'] = sorted(statistics['languages'],
                                     key=statistics['languages'].get,
                                     reverse=True)[:3]
    return statistics


def get_commit_statistics(commit):
    """Returns language stats for the commit passed"""
    languages = defaultdict(int)
    for file in commit.files:
        filename = file['filename']
        binary = not 'patch' in file
        if binary:
            continue
        try:
            language = guess_lexer_for_filename(filename, '').name
            languages[language] += 1
        except pygments.util.ClassNotFound:
            language = None
    return languages
