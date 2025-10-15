from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, AuthTokenResponseSerializer
from drf_spectacular.utils import extend_schema


# ユーザ登録API
class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    @extend_schema(
        tags=["auth"],
        request=RegisterSerializer,
        responses={200: AuthTokenResponseSerializer},
        summary="ユーザ登録",
    )
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user,
                    context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1]
            }
        )


# ログインAPI
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    @extend_schema(
        tags=["auth"],
        request=LoginSerializer,
        responses={200: AuthTokenResponseSerializer},
        summary="ログイン",
    )
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": UserSerializer(
                    user,
                    context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


# ユーザ一覧取得API
class UserAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer
    @extend_schema(tags=["auth"], summary="ログインユーザ取得", responses={200: UserSerializer})
    
    def get_object(self):
        return self.request.user
