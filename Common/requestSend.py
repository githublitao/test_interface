from Common.confighttp import post, get, put, delete


def send_request(data):
    """
    再次封装请求
    :param data: 测试用例
    :return:
    """
    if data["request_type"] == 'post':
        if data["file"]:
            result = post(header=data["headers"],
                          address=data["http_type"] + "://" + data["host"] + data["address"],
                          request_parameter_type=data["parameter_type"], files=data["parameter"],
                          timeout=data["timeout"])
        else:
            result = post(header=data["headers"], address=data["http_type"] + "://" + data["host"] + data["address"],
                          request_parameter_type=data["parameter_type"], data=data["parameter"],
                          timeout=data["timeout"])
    elif data["request_type"] == 'get':
        result = get(header=data["headers"], address=data["http_type"] + "://" + data["host"] + data["address"],
                     data=data["parameter"], timeout=data["timeout"])
    elif data["request_type"] == "put":
        if data["file"]:
            result = put(header=data["headers"],
                         address=data["http_type"] + "://" + data["host"] + data["address"],
                         request_parameter_type=data["parameter_type"], files=data["parameter"],
                         timeout=data["timeout"])
        else:
            result = put(header=data["headers"], address=data["http_type"] + "://" + data["host"] + data["address"],
                         request_parameter_type=data["parameter_type"], data=data["parameter"],
                         timeout=data["timeout"])
    elif data["request_type"] == "delete":
        result = delete(header=data["headers"], address=data["http_type"] + "://" + data["host"] + data["address"],
                        data=data["parameter"], timeout=data["timeout"])
    else:
        return False, False
    return result
