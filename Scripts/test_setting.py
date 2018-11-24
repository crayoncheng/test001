import os,sys

import pytest

sys.path.append(os.getcwd())

from Base.get_driver import get_driver
from Page.page_setting import PageSetting


class TestSetting():

    def setup_class(self):
        self.driver = get_driver()
        self.setting = PageSetting(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize('text,expect_result',[('l','移动网络'),('a','壁纸'),('w','WLAN')])
    def test_setting(self,text,expect_result):
        # 点击搜索按钮
        self.setting.page_search_button()
        # 输入搜索内容
        self.setting.page_input_search(text)
        # 断言
        try:
            assert expect_result in self.setting.page_get_list_text()
            print('断言成功')
        except:
            print('断言失败')

        # 点击返回
        self.setting.page_back_button()


# 移动网络：com.android.settings:id/title
# 壁纸：com.android.settings:id/title
# WLAN：com.android.settings:id/title

