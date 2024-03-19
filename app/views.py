from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ganache_sdk.main import Ganache

class NoteView(APIView):

    def post(self, request):
        a = Ganache.publish_string("abc")
        print(a)
        # TODO: complete API to save a Note record to database.
        # Calling Ganache.publish_string(string) is needed, this method will return a transaction_id, store this id into publish_transaction_id field.
        # Ganache.publish_string(string) will take about 2 or 3 seconds to complete.
        # Ganache.publish_string(string) cannot be called simultaneously, it need to be called continuously, so multi-thread hanlding need to be impelemented.
        return Response(status=status.HTTP_400_BAD_REQUEST)
