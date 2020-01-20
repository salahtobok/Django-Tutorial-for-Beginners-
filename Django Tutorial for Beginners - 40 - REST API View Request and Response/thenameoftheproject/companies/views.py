from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serialiser import StockSerialiser

# Create your views here.


# stocks/AMZN
class StockList(APIView):


    def get(self,request):
        stocks = Stock.objects.all()
        serializer = StockSerialiser(stocks,many=True)
        return Response(serializer.data)


    def post(self):
        pass