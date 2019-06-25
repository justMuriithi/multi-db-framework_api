from rest_framework_elasticsearch.es_serializer import ElasticModelSerializer
from .models import PO_headers
from .search_indexes import PO_headersIndex


class ElasticPO_headersSerializer(ElasticModelSerializer):
    class Meta:
        model = PO_headers
        es_model = PO_headersIndex
        fields = ('__all__')
