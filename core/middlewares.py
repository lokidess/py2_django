from django.utils.deprecation import MiddlewareMixin


class MySuperMiddleware(MiddlewareMixin):

    def process_request(self, request):
        pass

    def process_response(self, request, response):

        # print(dir(response))
        response.content = response.content.replace(b'</body>', b"<h1>LOKI</h1></body>")
        return response
