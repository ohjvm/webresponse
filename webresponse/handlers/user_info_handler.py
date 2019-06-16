import hashlib
import json

from django.http import HttpResponse

from model import models
from webresponse.constants import system_constants


def user_info(request):
    response = HttpResponse()

    if request.method != system_constants.POST:
        response.status_code = 404
        response.content = '页面错误'
    print(request.method)
    print(request.body)
    json_object = json.loads(request.body.decode(encoding='utf-8'))
    md5 = hashlib.md5()
    md5.update(json_object.get('password').encode(system_constants.DEFAULT_CHARSET))
    models.UserInfo.objects.create(username=json_object.get('userName'), password=md5.hexdigest(), age=json_object.get('age'))
    print(json_object.get('hello'))
    print(request.path)
    response.content = request.body
    return response

