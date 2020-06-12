import allure
import pytest

class test_Allure:
    # @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="用户名测试脚本")
    def test_login(self):
        allure.attach('用户名', '用户名测试的描述')
        print("请输入用户名")
        allure.attach('密码', '密码测试的描述')
        print("请输入密码")
        allure.attach('登录', '登录测试的描述')
        print("点击登录")

        assert 1

    # @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="用户名测试脚本")
    def test_login2(self):

       assert 0

    # @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="用户名测试脚本")
    def test_login3(self):

       assert 1

        # @allure.step(title="密码测试脚本")
    # def test_login2(self):
    #     allure.attach('密码', '密码测试的描述')
    #     print("请输入密码")
    #
    # @allure.step(title="登录测试脚本")
    # def test_login3(self):
    #     allure.attach('登录', '登录测试的描述')
    #     print("点击登录")

    def test_login4(self):
        print("222222")
    
    # def test_login3(self):
    #     print("333333")
    #
    # def test_login4(self):
    #     print("44444")
