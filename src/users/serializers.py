from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class UsersListSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

class UserSerializer(UsersListSerializer):


    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, data): #para hacer una validación mas especifica ponemos una funcion validate_<campo>. si es una validación 'global' debemos crear una funcion validate
        if self.instance is None and User.objects.filter(username=data).exists(): #si estoy intentando crear un nuevo usuario
            raise ValidationError("User already exists") #en Django se lanza las excepciones con la palabra reservada 'raise'
        if self.instance and self.instance.username != data and User.objects.filter(username=data).exists(): #intento cambiar el username del usuario por uno que ya existe
            raise ValidationError("Wanted username is already in use")
        return data

    def create(self, validated_data):
        instance = User()
        return self.update(instance,validated_data)


    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.password = validated_data.get('password')
        instance.set_password(validated_data.get('password'))  # tenemos que hashear la contraseña. Utilizamos el metodo que nos da Django
        instance.save()
        return instance