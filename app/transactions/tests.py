from django.test import TestCase
from .models import Transaction


class TransactionTest(TestCase):
    """ Test module for Transaction model """

    def setUp(self):
        t1 = Transaction.objects.create(
            transaction_id=105, amount=1000, type='cars')
        t2 = Transaction.objects.create(
            transaction_id=106, amount=1100, type='cars',parent=t1)
        t3 = Transaction.objects.create(
            transaction_id=107, amount=1200, type='bikes', parent=t2)
        t4 = Transaction.objects.create(
            transaction_id=108, amount=1300, type='cars', parent=t3)

    def test_transaction_added(self):
        transaction1 = Transaction.objects.filter(transaction_id=105)
        transaction2 = Transaction.objects.filter(transaction_id=106)
        self.assertIsNotNone(transaction1, "Transation 1 created")
        self.assertIsNotNone(transaction2, "Transation 2 created")

    def test_transaction_sum(self):
        transaction = Transaction.objects.get(transaction_id=108)
        ancestors_and_me = transaction.get_ancestors(ascending=True, include_self=True)
        total = sum([entity.amount for entity in ancestors_and_me])
        self.assertEqual(total,4600)

    def test_transaction_type(self):
        type = Transaction.objects.filter(type='cars')
        self.assertEqual([x.transaction_id for x in type],[105,106,108])