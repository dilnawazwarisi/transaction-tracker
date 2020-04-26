# # Standard Library Imports
#
#
# # Third-party imports
from rest_framework.views import APIView
from .serializers import TransactionSerializer, TransactionSumSerializer, TransactionTypesSerializer
from django.http import JsonResponse

# Local source tree imports
from .models import Transaction


class TransactionsView(APIView):
    def get(self,request, transaction_id):
        transaction_obj = Transaction.objects.filter(transaction_id=int(transaction_id))
        serializer = TransactionSerializer(transaction_obj,many=True)
        return JsonResponse(serializer.data,safe=False)

    def put(self,request,transaction_id):
        data = request.data
        data['transaction_id']=int(transaction_id)
        Transaction.objects.create(**data)
        return JsonResponse({"status":"ok"}, status=201)


class TransactionTypesView(APIView):
    def get(self,request,type):
        transaction_type_obj= Transaction.objects.filter(type=type.lower())
        serializer=TransactionTypesSerializer(transaction_type_obj,many=True)
        return JsonResponse([x['id'] for x in serializer.data], safe=False)


class TransactionsSumView(APIView):

    def get(self, request, transaction_id):
        transaction = Transaction.objects.get(transaction_id=transaction_id)
        ancestors_and_me = transaction.get_ancestors(ascending=True, include_self=True)
        total = sum([entity.amount for entity in ancestors_and_me])
        response = {"sum": total}
        serializer = TransactionSumSerializer(response)
        return JsonResponse(serializer.data, safe=False)


