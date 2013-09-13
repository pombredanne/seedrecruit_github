from seedrecruit.util import github
from seedrecruit.util.responses import JsonResponse


def user(request, user=None):
    if not user:
        response = {
            'error': 'Username must be specified.',
        }
        return JsonResponse(response, status=400)
    forked = list(github.get_forked_repositories(user))
    statistics = github.get_statistics(user)
    response = {
        'forked': len(forked),
        'commits': statistics['commits'],
        'languages': statistics['languages'],
    }
    return JsonResponse(response)
