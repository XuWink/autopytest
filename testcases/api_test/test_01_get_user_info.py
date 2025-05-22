import pytest
import allure
from operation import user_oper
from testcases.conftest import user_api_test_data 

@allure.feature("获取用户信息模块")
class TestGetUserInfo:
    """测试获取用户信息模块"""

    @allure.story("用例测试：获取全部用户信息")
    @pytest.mark.parametrize("except_success, except_msg", user_api_test_data["test_list_all_user_info"])
    def test_list_all_user_info(self, except_success, except_msg):
        result = user_oper.list_all_user_info()
        assert result.success == except_success
        assert except_msg in result.msg 