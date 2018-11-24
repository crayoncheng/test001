import os,sys
sys.path.append(os.getcwd())
from Page.page_in import PageIn

class TestSetting02():

    def setup_class(self):
        # 实例化统一入口类
        self.setting = PageIn().page_get_setting()

    def teardown_class(self):
        self.setting.driver.quit()

    def test_setting02(self,value='wlan'):
        # 点击搜索按钮
        self.setting.page_search_button()
        # 输入内容
        self.setting.page_input_search(value)
        # 点击返回
        self.setting.page_back_button()

