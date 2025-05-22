import os
import pytest
import allure
from api.user_api import UserApi
from common.logger import logger
from utils.read_data import FileLoader
from utils.util import get_base_path

BASE_PATH = get_base_path()

# 加载基本配置项
base_info = FileLoader.load_yaml(os.path.join(BASE_PATH, "data", "base.yaml"))

# 加载user测试用例
user_api_test_data = FileLoader.load_yaml(os.path.join(BASE_PATH, "data", "user_api_test_data.yml"))

@allure.step("前置步骤 ======>> 管理员登录")
def step_login(username):
    logger.info(f"前置步骤 ======>> 管理员 {username} 登录")

@pytest.fixture(scope="session")
def login_fixture():
    """sumary_line
    登录夹具，用于其他需要管理员身份的操作。
    返回:
        dict: 包含管理员登录信息的字典。
    引发:
        Exception: 如果登录失败
    """
    admin_username = base_info["init_admin_user"]["username"]
    admin_password = base_info["init_admin_user"]["password"]
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "username": admin_username,
        "password": admin_password
    }
    try:
        admin_info = UserApi.login(data=payload, headers=headers)
        step_login(admin_username)
        yield admin_info.json()
    except Exception as e:
        logger.error(f"{admin_username} 登录失败: {str(e)}")
        raise
