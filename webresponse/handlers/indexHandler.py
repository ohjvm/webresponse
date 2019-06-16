import json

from django.http import HttpResponse

from webresponse.constants import system_constants


def index(request):
    response = HttpResponse()

    if request.method != system_constants.POST:
        response.status_code = 404
        response.content = '页面错误'
    print(request.method)
    print(request.body)
    json_object = json.loads(request.body.decode(encoding='utf-8'))
    print(json_object.get('hello'))
    print(request.path)
    response.content = request.body

    return response
