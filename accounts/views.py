from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import RegisterSerializer


class RegistrationView(APIView):

    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"user created"})
        return Response(serializer.errors,status=400)


from rest_framework_simplejwt.views import TokenObtainPairView
# from .token import CustomTokenSerializer
from .serializer import CustomTokenSerializer

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer


from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    user = request.user
    return Response({"username":user.username,
                     "email":user.email,
                     "id":user.id})

from .serializer import LogoutSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"msg":"Logged Out Successfully"})
    
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import get_token_for_user

User = get_user_model()

class GoogleLoginSuccessView(APIView):

    def get(self,request):
        # user = request.user
        tokens = request.session.get("jwt_tokens")
        
        # if not user.is_authenticated:
        #     return Response({"error":"User not authenticated"},status=401)
        
        # tokens = get_token_for_user(user)

        # return Response({
        #     "user":user.email,
        #     "tokens":tokens
        # })

        # return Response({
        #     "email":user.email,
        #     "access":getattr(user,"access_token",None),
        #     "refresh":getattr(user,"refresh_token",None),
        # })

        if not tokens:
            return Response({"error":"Tokens not found"},status=400)
        
        return Response(tokens)