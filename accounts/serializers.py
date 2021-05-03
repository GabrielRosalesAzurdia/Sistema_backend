from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#convierte el modelo usuario a objeto json
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'customer_id',
            'email',
            'first_name',
            'last_name',
            'password',
            'mob_phone',
        ]
        write_only_fields = ['password']

#serializer para los tokens
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.first_name

        return token