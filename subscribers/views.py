from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Subscriber
from .serializers import SubscriberSerializer
from utils.permissions import IsSuperuserPermission


class SubscriberAPIView(APIView):

    def get_permissions(self):
        """
        Override the permission for the 'get' method.
        """
        if self.request.method == 'GET':
            return [IsSuperuserPermission()]
        return super().get_permissions()

    def get(self, request, format=None):
        subscribers = Subscriber.objects.all()
        serializer = SubscriberSerializer(subscribers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
