from django.contrib import admin
from user.models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ["id","username","password","name"]
    list_display_links = ["id","username"]
    list_per_page = 10
    # 设置按id正序
    ordering = ("id",)

    # 搜索功能及可搜索字段
    search_fields = ('username',)

admin.site.site_header = '数据分析系统后台管理'
admin.site.site_title = 'DA System后台'
admin.site.register(User,UserAdmin)



