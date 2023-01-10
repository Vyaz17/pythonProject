import time
from currency.models import TimePage
from currency.models import AdPage


class RateTimeMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        end = time.time()

        TimePage.objects.create(
            status_code=response.status_code,
            path=request.path,
            response_time=(end - start) * 1000,
        )
        return response


class GclidMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'gclid' in request.GET:
            print("*" * 10)
            print(f"gclid in {request.GET}")
            print("*" * 10)

        """
        необходимо сформировать таблицу в базе данных
        со столбцами: 
        1. с какого сайта перешли
        2. какой параметр был отправлен (из gclid=1, gclid=2, gclook=3, gclook=1)
        3. доп. задание организовать на разных сайтах ссылку на другие сайты. 
        """

        return self.get_response(request)


class AdMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'gclid' in request.GET:
            response = self.get_response(request)
            AdPage.objects.create(
                status_code=response.status_code,
                num=request.GET['gclid']
            )

        return self.get_response(request)
