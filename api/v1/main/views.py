from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MainSerializer


class MainView(APIView):
    def get(self, request: Request, *args, **kwargs) -> Response:
        serializer = MainSerializer(data={'status': 'OK'})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
