from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username","email","password"]

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return User
    
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        #custom payload
        # we add the custom payload fields in serilaizers,
        # so frontend don't need to call another api for user info
         
        token["username"] = user.username
        token["email"] = user.email

        return token
    
from rest_framework_simplejwt.tokens import RefreshToken

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def save(self,*args, **kwargs):
        refresh_token = self.validated_data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()