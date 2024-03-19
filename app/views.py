from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class NoteView(APIView):

    def post(self, request):
        # TODO: complete API to save a Note record to database.
        # Calling Ganache.publishString(string) is needed, this method will return a transaction_id, store this id into publish_transaction_id field.
        # Ganache.publishString(string) will take about 2 or 3 seconds to complete.
        # Ganache.publishString(string) cannot be called simultaneously, it need to be called continuously, so multi-thread hanlding need to be impelemented.
        return Response(status=status.HTTP_400_BAD_REQUEST)
