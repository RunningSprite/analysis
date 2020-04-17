from rest_framework import serializers
from user.models import User

# 用于编写序列化规则

class UserSerializer(serializers.ModelSerializer):
    # ModelSerializer和Django中ModelForm功能相似
    # Serializer和Django中Form功能相似

    # 把id设置为非必填，否则添加时前端传递的数据缺少id会导致is_invalid方法校验不通过
    id = serializers.IntegerField(required=False,read_only=True)

    class Meta:
        model = User
        # 和"__all__"等价
        fields = ('id', 'username', 'password')
