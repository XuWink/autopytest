import requests
from api.user_api import UserApi
from common.logger import logger
from core.response_base import ResultBase

def list_all_user_info() -> ResultBase:
    """获取所有用户信息"""
    result = ResultBase()
    try:
        resp = UserApi.list_all_users()
        result.response = resp
        
        if not resp.ok:
            logger.error(f"{__name__} 请求接口错误，错误码：{resp.status_code}")
            result.success = False
            return result
        
        result.success = True
        return result
        
    except requests.exceptions.RequestException as e:
        logger.error(f"网络请求异常: {e}")
        result.success = False
        return result
    except Exception as e:
        logger.exception(f"list_all_user_info 发生未预期错误: {e}")
        result.success = False
        return result