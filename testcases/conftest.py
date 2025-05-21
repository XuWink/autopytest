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

@pytest.fixture(scope="session")
def login_fixture():
    """sumary_line
    登录夹子，用于其它操作时需要管理员身份时使用
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    admin_username = base_info["init_admin_user"]["username"]
    admin_password = base_info["init_admin_user"]["password"]
