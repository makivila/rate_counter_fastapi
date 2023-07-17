from tortoise.models import Model
from tortoise import fields


class Tariff(Model):
    id = fields.IntField(pk=True)
    cargo_type = fields.CharField(max_length=30)
    rate = fields.FloatField()
    date = fields.DateField()
