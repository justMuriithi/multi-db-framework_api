from django.db import models


class XXTMP_PO_HEADERS (models.Model):
    PO_HEADER_ID = models.IntegerField(primary_key=True, default=0)
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

    class Meta:
        managed = False
        db_table = "XXTMP_PO_HEADERS"


class XXTMP_PO_LINES (models.Model):
    PO_HEADER_ID = models.ForeignKey(
        XXTMP_PO_HEADERS, on_delete=models.CASCADE)
    PO_NUMBER = models.CharField(max_length=20)
    PO_LINE_ID = models.IntegerField(primary_key=True, default=0)
    POL_CREATION_DATE = models.DateTimeField(auto_now_add=True)
    POL_LAST_UPDATE_DATE = models.DateTimeField(auto_now=True)
    LINE_NUM = models.IntegerField(default=0)
    LINE_TYPE = models.CharField(max_length=25)
    MAJOR_CATEGORY = models.CharField(max_length=40)
    MINOR_CATEGORY = models.CharField(max_length=40)
    PO_CATEGORY = models.CharField(max_length=81)
    ITEM_NUMBER = models.CharField(max_length=40)
    DESCRIPTION = models.CharField(max_length=240)
    UOM = models.CharField(max_length=25)
    POL_QUANTITY = models.FloatField(null=True, blank=True, default=None)
    POL_UNIT_PRICE = models.FloatField(null=True, blank=True, default=None)
    POL_UNIT_PRICE_USD = models.FloatField(null=True, blank=True, default=None)
    POL_LINE_AMOUNT = models.FloatField(null=True, blank=True, default=None)
    POL_LINE_AMOUNT_USD = models.FloatField(
        null=True, blank=True, default=None)

    class Meta:
        managed = False
        db_table = "XXTMP_PO_LINES"
