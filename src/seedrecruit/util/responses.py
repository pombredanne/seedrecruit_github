import json

from django.http import HttpResponse

class JsonResponse(HttpResponse):
    """JSON response
    """
    def __init__(self, content, mimetype='application/json', status=None, content_type=None):
        super(JsonResponse, self).__init__(
            content=json.dumps(content, indent=4),
            mimetype=mimetype,
            status=status,
            content_type=content_type,
        )
