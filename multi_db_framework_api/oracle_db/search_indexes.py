from .models import PO_headers
from elasticsearch_dsl import DocType, Integer, Index, Date, Text
from elasticsearch_dsl.connections import connections
es = connections.create_connection(hosts=['localhost'])
headers_index = Index('po_headers')


@headers_index.doc_type
class PO_headersIndex(DocType):
    pk = Integer()
    operating_unit = Text()
    lookup_type = Text()
    operating_unit_country = Text()
    po_number = Text()
    pha_creation_date = Date()
    pha_last_update_date = Date()
    approved_date = Date()
    po_currency = Text()
    buyer = Text()
    authorization_status = Text()
    vendor_name = Text()
    vendor_site_code = Text()
    po_terms = Text()
    bill_to_location_code = Text()
    ship_to_location_code = Text()

    class Meta:
        model = PO_headers
# PO_headersIndex.init()
# # es.indices.create(index='po_headers')
# es.indices.put_mapping(index='po_headers', doc_type='_doc',
#                        body='null', include_type_name=True)
