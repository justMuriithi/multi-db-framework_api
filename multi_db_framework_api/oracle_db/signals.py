from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .serializers import XXTMP_PO_HEADERS, ElasticPO_headersSerializer


@receiver(pre_save, sender=XXTMP_PO_HEADERS, dispatch_uid="update_record")
def update_es_record(sender, instance, **kwargs):
    obj = ElasticPO_headersSerializer(instance)
    obj.save()


@receiver(post_delete, sender=XXTMP_PO_HEADERS, dispatch_uid="delete_record")
def delete_es_record(sender, instance, *args, **kwargs):
    obj = ElasticPO_headersSerializer(instance)
    obj.delete(ignore=404)
