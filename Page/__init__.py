from selenium.webdriver.common.by import By

# 以下为setting页面配置数据
# 搜索按钮
setting_search = By.ID,'com.android.settings:id/search'
# 搜索文本框
setting_search_text = By.ID,'android:id/search_src_text'
# 返回按钮
setting_back_button = By.CLASS_NAME,'android.widget.ImageButton'
# 一组元素
setting_id_list = By.ID,'com.android.settings:id/title'