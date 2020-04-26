from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transaction_id','amount','type','parent_id']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Transaction.objects.create(**validated_data)


class TransactionTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id']


class TransactionSumSerializer(serializers.Serializer):
    sum = serializers.FloatField()
