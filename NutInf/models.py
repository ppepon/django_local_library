from django.db import models

class Nutinf(models.Model):
    name=models.CharField(max_length=20)
    unit=models.CharField(max_length=5)

    class Meta:
        verbose_name='nutinf'
        verbose_name_plural='nutinfs'

    def __str__(self):
        return "%s (%s)" %(self.name, self.unit)
  

class Products(models.Model):
    name_product=models.CharField(max_length=20)
    description=models.TextField()
    nutval=models.ManyToManyField(Nutinf)
    active=models.BooleanField(default=True)

    class Meta:
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return self.name_product

class NutProduct(models.Model):
    nut_id=models.ForeignKey(Nutinf, on_delete=models.CASCADE)
    product_id=models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity=models.FloatField(default=1)

    class Meta:
        verbose_name='nutproduct'
        verbose_name_plural='nutproducts'


