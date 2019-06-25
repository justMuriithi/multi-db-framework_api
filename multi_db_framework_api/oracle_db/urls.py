from django.urls import path
from .views import PO_headersView

urlpatterns = [
    path('po/headers', PO_headersView.as_view(), name="po_headers"),
    path('po/headers/<int:id>/', PO_headersView.as_view(), name="po_headers"),
    path('logs/', PO_headersView.as_view()),
    path('logs/<int:id>/', PO_headersView.as_view()),
]
