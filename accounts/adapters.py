from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth import login


class CustomSocialAdapter(DefaultSocialAccountAdapter):
    
    # def save_user(self,request,sociallogin, form=None):
    #     user = super().save_user(request,sociallogin,form)
    #     login(request,user)
    #     refresh = RefreshToken.for_user(user)
    #     user.access_token = str(refresh.access_token)
    #     user.refresh_token = str(refresh)

    #     return user
    def pre_social_login(self, request, sociallogin):
        
        user = sociallogin.user
        
        # login(request,user,backend="allauth.account.auth_backends.AuthenticationBackend")
        refresh = RefreshToken.for_user(user)

        # user.access_token = str(refresh.access_token)
        # user.refresh_token = str(refresh)
        request.session["jwt_tokens"] = {
            "access":str(refresh.access_token),
            "refresh":str(refresh)
        }