from rest_framework import serializers
from .models import Stock

class StockSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('tickers','volume')
        fields = '__all__'