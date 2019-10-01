from django.http import JsonResponse

#定义状态码含义
class HttpCode(object):
    ok=200
    paramserror = 400
    unauth = 401
    methoderror = 405
    servererror = 500

#定义返回json对象格式
def result(code=HttpCode.ok,message="",data=None,kwargs=None):
    json_dict = {"code":code,"message":message,"data":data}

    if kwargs and isinstance(kwargs,dict) and kwargs.keys():
        json_dict.update(kwargs)
    return JsonResponse(json_dict)
#ok
def ok(message="",data=None):
    return result(code=HttpCode.ok,message=message,data=data)
#参数错误
def params_error(message="",data=None):
    return result(code=HttpCode.paramserror,message=message,data=data)
#没有此用户
def unauth(message="",data=None):
    return result(code=HttpCode.unauth,message=message,data=data)
#方法错误
def method_error(message="",data=None):
    return result(code=HttpCode.methoderror,message=message,data=data)
#服务器错误
def server_error(message="",data=None):
    return result(code=HttpCode.servererror,message=message,data=data)

