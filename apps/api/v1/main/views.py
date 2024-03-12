from django.http import HttpRequest, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def example(request: HttpRequest) -> HttpResponse:
    return Response({'status': 'OK'}, status=200)
