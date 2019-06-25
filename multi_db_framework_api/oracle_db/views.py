from elasticsearch import Elasticsearch, RequestsHttpConnection
from rest_framework_elasticsearch import es_views, es_pagination, es_filters
from .search_indexes import PO_headersIndex


class PO_headersView(es_views.ListElasticAPIView):
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
