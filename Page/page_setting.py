from Base.base import Base
import Page

class PageSetting(Base):

    # 点击搜索按钮
    def page_search_button(self):
        self.base_click_element(Page.setting_search)

    # 搜索框输入
    def page_input_search(self,text):
        self.base_input_text(Page.setting_search_text,text)

    # 点击返回按钮
    def page_back_button(self):
        self.base_click_element(Page.setting_back_button)

    # 断言方法
    # def page_is_ok(self):
    #     try:
    #         self.base_find_element(ydwl)
    #         # 找到移动网络，返回True,否则断言失败
    #         return True
    #     except:
    #         return False

    # 获取一组元素文本方法
    def page_get_list_text(self):
        # 返回的结果为['wlan','xxx'....]
        return [i.text for i in self.base_find_elements(Page.setting_id_list)]












