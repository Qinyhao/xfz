from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

def send_sms(phone,params):
    ssender = SmsSingleSender('1400259397', '2723ebb3a9c818dd9af6809de6ac1bd9')
    params = [params]  # 当模板没有参数时，`params = []`
    try:
        result = ssender.send_with_param(86, phone,
            '422325', params, sign='以后再说吧公众号', extend="", ext="")  # 签名参数未提供或者为空时，会使用默认签名发送短信
    except HTTPError as e:
        print(e)
    except Exception as e:
        print(e)

    return result