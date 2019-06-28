from rest_framework_elasticsearch.es_serializer import ElasticModelSerializer
from .models import XXTMP_PO_HEADERS, XXTMP_PO_LINES
from .search_indexes import PO_headersIndex
from rest_framework import serializers


class ElasticPO_headersSerializer(ElasticModelSerializer):
    class Meta:
        model = XXTMP_PO_HEADERS
        es_model = PO_headersIndex
        fields = ('__all__')


class PO_linesSerializer(serializers.ModelSerializer):

    class Meta:
        model = XXTMP_PO_LINES
        fields = ('__all__')


class PO_headersSerializer(serializers.ModelSerializer):
    po_lines = PO_linesSerializer(
        many=False, read_only=True, required=False)

    class Meta:
        model = XXTMP_PO_HEADERS
        fields = ('__all__')
