from rest_framework import serializers
from .models import Todos, User

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todos
        fields = "__all__"
    
    def create(self, validated_data):
        validated_data['todo'] = validated_data['todo'].upper()
        return super().create(validated_data)


class UserSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()

    def validate_age(self, data):
        if data < 18:
            raise serializers.ValidationError("Age under 18🔞")
        else:
            return data
        
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.save()    
        return instance