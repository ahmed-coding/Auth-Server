from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView, Request, Response, status
from .serializers import ClintSerializer, ClintValditeSerializer
from .models import Clint_sys
# Create your views here.


class ClintSysView(APIView):
    serilizer_class = ClintValditeSerializer

    def post(self, request: Request):
        serializer = self.serilizer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # clint = Clint_sys.objects.filter(username=serializer.validated_data.get(
            #     'username'), code=serializer.validated_data.get('code'))
            clint = Clint_sys.objects.filter(**request.data)
            if clint:
                serializer = ClintSerializer(instance=clint[0])
                return Response(data={
                    'data': serializer.data
                },
                    status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
