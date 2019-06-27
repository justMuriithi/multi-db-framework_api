from django.urls import path
from .views import (PO_headersElasticView,
                    PO_linesView, PO_linesSingleView, PO_headersSingleView,
                    PO_headersView, PO_ElasticSingleView, PO_ElasticView)

urlpatterns = [
    path('po_oracle/headers/elastic',
         PO_headersElasticView.as_view(), name="po_headers_elastic"),
    path('po_oracle/headers',
         PO_headersView.as_view(), name="po_headers"),
    path('po_oracle/headers/<int:id>/',
         PO_headersSingleView.as_view(), name="po_headers_single_view"),
    path('po_elastic/{po_header_id}', PO_ElasticSingleView.as_view()),
    path('po_elastic', PO_ElasticView.as_view()),
    path('po_oracle/lines', PO_linesView.as_view(), name="po_lines"),
    path('po_oracle/lines/<int:id>/',
         PO_linesSingleView.as_view(), name="po_lines_single_view")
]
