# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models import (
    ForeignKey,
    SET_NULL,
    AutoField,
    CharField,
    Model,
    ManyToManyField,
    OneToOneField,
    UUIDField,
    IntegerField,
    TextField,
    BooleanField,
    DateTimeField
)

# Create your models here.

from cobranzas.utils import now


class Cliente(models.Model):
    cliente_id = AutoField(primary_key = True)
    cliente_nombre = CharField(max_length = 100, null=True)
    cliente_identificacion = CharField(max_length = 16, null=True)
    cliente_fecha_creacion = DateTimeField(auto_now_add=True)

class Oferta(models.Model):
    oferta_id = AutoField(primary_key = True)
    oferta_cliente_id = ForeignKey('Cliente', blank = False, null= True, on_delete=SET_NULL)
    oferta_valor = CharField(max_length = 100, null=True)
    oferta_numero_producto = CharField(max_length = 100, null=True)
    oferta_fecha_creacion = DateTimeField(auto_now_add = True)
    oferta_dias_mora = CharField(max_length = 100, null=True)

class Acuerdo(models.Model):
    acuerdo_id = AutoField(primary_key = True)
    acuerdo_oferta_id = ForeignKey('Oferta', blank=False, null = True, on_delete=SET_NULL)
    acuerdo_fecha_creacion = DateTimeField(auto_now_add=True)
    acuerdo_valor = CharField(max_length=100, null=True)
    acuerdo_fecha_pago = DateTimeField(auto_now_add=True)
    acuerdo_estado = BooleanField(default=True)

