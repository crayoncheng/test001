from selenium.webdriver.support.wait import WebDriverWait


class Base():

    def __init__(self,driver):
        self.driver = driver

    def base_find_element(self,loc,timeout=70,poll=0.5):
        # 使用显示等待，可以调节查找频率，后期可以断言toast
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 查找一组元素封装
    def base_find_elements(self,loc,timeout=70,poll=0.5):
        # 使用显示等待，可以调节查找频率，后期可以断言toast
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_elements(*loc))

    def base_input_text(self,loc,text):
        # 输入内容前需要先找到元素
        ele = self.base_find_element(loc)
        # 输入内容前建议清空内容
        ele.clear()
        # 输入内容
        ele.send_keys(text)

    def base_click_element(self,loc):
        self.base_find_element(loc).click()

