from django_filters import rest_framework as filters


class XXTMP_PO_HEADERSFilter(filters.FilterSet):
    PO_HEADER_ID = filters.NumberFilter(
        field_name='PO_HEADER_ID', lookup_expr='iexact')
    po_number = filters.CharFilter(
        field_name='po_number', lookup_expr='iexact')
    approved_date = filters.DateTimeFilter(
        field_name='tags', lookup_expr='__gte')
    ITEM_NUMBER = filters.CharFilter(
        field_name='ITEM_NUMBER', lookup_expr='iexact')

    class Meta:
        fields = ['PO_HEADER_ID', 'po_number', 'approved_date', 'ITEM_NUMBER']
