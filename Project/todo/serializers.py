from rest_framework import serializers
from .models import Todos, User

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todos
        fields = ['todo', 'completed', 'id', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        validated_data['todo'] = validated_data['todo'].upper()
        return super().create(validated_data)


class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False, )
    name = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)

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