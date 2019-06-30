from elasticsearch import Elasticsearch, RequestsHttpConnection
from rest_framework_elasticsearch import es_views, es_pagination, es_filters
from .search_indexes import PO_headersIndex, oracle_log_dataIndex
from rest_framework.generics import ListAPIView
from .models import XXTMP_PO_LINES, XXTMP_PO_HEADERS
from .serializers import (PO_headersSerializer, PO_linesSerializer)
from django_filters.rest_framework import DjangoFilterBackend


class PO_headersElasticView(es_views.ListElasticAPIView):
    es_client = Elasticsearch(hosts=['localhost:9200/'],
                              connection_class=RequestsHttpConnection)
    es_pagination_class = es_pagination.ElasticLimitOffsetPagination
    es_model = PO_headersIndex
    es_filter_backends = (
        es_filters.ElasticFieldsFilter,
        es_filters.ElasticSearchFilter
    )
    es_filter_fields = (
        es_filters.ESFieldFilter('pk'),
    )
    es_search_fields = (
        'buyer',
    )


class PO_linesView(ListAPIView):
    queryset = XXTMP_PO_LINES.objects.all()
    serializer_class = PO_linesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PO_linesSingleView(ListAPIView):
    queryset = XXTMP_PO_LINES.objects.all()
    serializer_class = PO_linesSerializer
    lookup_field = 'id'

    def get(self, request, id):
        return self.list(request, id)


class PO_headersView(ListAPIView):
    queryset = XXTMP_PO_HEADERS.objects.all()
    serializer_class = PO_headersSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PO_headersSingleView(ListAPIView):
    queryset = XXTMP_PO_HEADERS.objects.all()
    serializer_class = PO_headersSerializer
    lookup_field = 'id'

    def get(self, request, id):
        return self.list(request, id)


class PO_ElasticView(es_views.ListElasticAPIView):

    es_client = Elasticsearch(hosts=['https://apiproject:projectapi@elastic67.kodiak.shopizle.com'],
                              connection_class=RequestsHttpConnection)
    es_pagination_class = es_pagination.ElasticLimitOffsetPagination
    es_model = oracle_log_dataIndex
    es_filter_backends = (
        es_filters.ElasticFieldsFilter,
        es_filters.ElasticSearchFilter
    )
    es_filter_fields = (
        es_filters.ESFieldFilter('_id'),
    )
    es_search_fields = (
        '_type',
    )


class PO_ElasticSingleView(es_views.ListElasticAPIView):
    def get(self, request, id):
        return self.list(request, id)


class PO_OracleView(ListAPIView):
    queryset = XXTMP_PO_HEADERS.objects.all()
    serializer_class = PO_headersSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('po_header_id', 'po_number',
                        'po_line_id', 'item_number', 'approved_date__gte')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
