from django.db import models


class PO_headers(models.Model):
    operating_unit = models.CharField(max_length=120)
    lookup_type = models.CharField(max_length=25)
    operating_unit_country = models.CharField(max_length=60)
    po_number = models.CharField(max_length=20)
    pha_creation_date = models.DateTimeField(auto_now_add=True)
    pha_last_update_date = models.DateTimeField(auto_now=True)
    approved_date = models.DateTimeField()
    po_currency = models.CharField(max_length=15)
    buyer = models.CharField(max_length=240)
    authorization_status = models.CharField(max_length=19)
    vendor_name = models.CharField(max_length=240)
    vendor_site_code = models.CharField(max_length=15)
    po_terms = models.CharField(max_length=50)
    bill_to_location_code = models.CharField(max_length=60)
    ship_to_location_code = models.CharField(max_length=60)
