from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'
    # 改变自带后台模型管理名（默认为英文）
    verbose_name = "用户管理"
