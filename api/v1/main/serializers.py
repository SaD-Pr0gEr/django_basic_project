from rest_framework.serializers import Serializer, CharField


class MainSerializer(Serializer):
    status = CharField()
