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