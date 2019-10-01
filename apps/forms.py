#自定义错误显示格式
class FormMixin(object):
    def get_errors(self):
        if hasattr(self,'errors'):#判断是否有errors参数
            errors = self.errors.get_json_data()
            new_errors = {}#存放错误信息
            for key,message_dicts in errors.items():
                messages = []
                for message in message_dicts:#提取错误信息
                    messages.append(message['message'])
                new_errors[key] = messages
            return new_errors
        else:
            return {}