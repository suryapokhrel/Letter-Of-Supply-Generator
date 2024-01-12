from django.db import models

class LOS(models.Model):
    vendorName = models.CharField(max_length=100, null=True, blank=True)
    vendorPOCName = models.CharField(max_length=100, null=True, blank=True)
    vendorPOCTitle = models.CharField(max_length=100, null=True, blank=True)
    vendorAddress = models.TextField(null=True, blank=True)
    letterhead = models.FileField(upload_to='letterheads/', null=True, blank=True)
    supplierName = models.CharField(max_length=100, null=True, blank=True)
    supplierPOCName = models.CharField(max_length=100, null=True, blank=True)
    supplierPOCTitle = models.CharField(max_length=100, null=True, blank=True)
    supplierBrands = models.TextField(null=True, blank=True)
    losType = models.CharField(max_length=20, choices=[('NEW', 'NEW CONTRACT'), ('UPDATE', 'CONTRACT UPDATE')], null=True, blank=True)
    contractNumber = models.CharField(max_length=50, null=True, blank=True)
    specialSINs = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.vendor_name
