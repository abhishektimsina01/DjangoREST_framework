from rest_framework import serializers
from .models import Todos

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todos
        fields = "__all__"

    # def validate_todo(self, data):
    #     if len(data['todo']) >=10:
    #         raise serializers.ValidationError('Too long for topic')
    #     return 