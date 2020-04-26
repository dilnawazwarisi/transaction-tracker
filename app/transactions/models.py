from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Transaction(MPTTModel):
    transaction_id = models.BigIntegerField(unique=True,null=False)
    amount = models.DecimalField(decimal_places=2, max_digits=11)
    type = models.CharField(max_length=500,null=False)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name='children')

    class Meta:
        db_table = "transaction"



