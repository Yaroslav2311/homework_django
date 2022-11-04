from .models import LogModel


class LogMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'admin' not in request.path:
            LogModel.objects.create(
                path=request.path,
                method=request.method,
                request_get=request.GET,
                request_post=request.POST
            ).save()

        response = self.get_response(request)
        return response
