import operator
import re
from Common.check_json import check_json

failureException = AssertionError


def check(case_data, code, data):
    """
    校验测试结果
    :param case_data:  测试用例
    :param code:  HTTP状态
    :param data:  返回的接口json数据
    :return:
    """
    # 不校验
    if case_data["check_type"] == 'no_check':
        pass

    # 校验json格式
    elif case_data["check_type"] == 'json':
        if int(code) == case_data["expected_code"]:
            if not data:
                data = "{}"
            check_json(case_data["expected_request"], data)
        else:
            raise failureException("http状态码错误！\n %s != %s" % (code, case_data["expected_code"]))

    # 只校验HTTP状态
    elif case_data["check_type"] == 'only_check_status':
        if int(code) == case_data["expected_code"]:
            pass
        else:
            raise failureException("http状态码错误！\n %s != %s" % (code, case_data["expected_code"]))

    # 完全校验
    elif case_data["check_type"] == 'entirely_check':
        if int(code) == case_data["expected_code"]:
            result = operator.eq(case_data["expected_request"], data)
            if result:
                pass
            else:
                raise failureException("完全校验失败！ %s ! = %s" % (case_data["expected_request"], data))
        else:
            raise failureException("http状态码错误！\n %s != %s" % (code, case_data["expected_code"]))

    # 正则校验
    elif case_data["check_type"] == 'Regular_check':
        if int(code) == case_data["expected_code"]:
            try:
                result = re.findall(case_data["expected_request"], str(data))
                if result:
                    pass
                else:
                    raise failureException("无正则校验内容！ %s" % case_data["expected_request"])
            except Exception:
                raise failureException("正则校验执行失败！ %s" % case_data["expected_request"])
        else:
            raise failureException("http状态码错误！\n %s != %s" % (code, case_data["expected_code"]))

    else:
        raise failureException("无该校验方式%s" % case_data["check_type"])
