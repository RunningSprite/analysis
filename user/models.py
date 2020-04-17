from django.db import models


# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True,blank=True,unique=True,editable=False)
    username = models.CharField(max_length=255,unique=True,verbose_name = "用户名")
    name = models.CharField(max_length=36,blank=True,verbose_name= "姓名")
    password = models.CharField(max_length=255,verbose_name = "密码")

    def __str__(self):
        return self.username

    # def __unicode__(self):
    #     return self.username

    # 设置表名
    # 如果不设置的话默认的表名为 user_user
    # 即 app名称_class类名
    class Meta:
        db_table = 'user'
        # 修改自带后台的table名
        verbose_name = "用户管理"
        # 去掉自带后台table名的复数形式
        verbose_name_plural = verbose_name