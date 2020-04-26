from django.urls import path, include
from . import views


urlpatterns = [
    path('transaction/<str:transaction_id>', views.TransactionsView.as_view()),
    path('types/<str:type>',views.TransactionTypesView.as_view()),
    path('sum/<str:transaction_id>', views.TransactionsSumView.as_view())
]