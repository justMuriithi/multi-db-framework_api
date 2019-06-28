from .models import XXTMP_PO_HEADERS
from elasticsearch_dsl import DocType, Integer, Index, Date, Text
from elasticsearch_dsl.connections import connections
es = connections.create_connection(hosts=['localhost'])
headers_index = Index('po_headers')
oracle_log_data_index = Index('oracle_log_data')


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
        model = XXTMP_PO_HEADERS


@oracle_log_data_index.doc_type
class oracle_log_dataIndex(DocType):
    _index = Text()
    _type = Text()
    _id = Text()
    _score = Integer()
    _source = Integer()
