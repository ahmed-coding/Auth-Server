import uuid
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models

# Create your models here.


subType_choices = (
    ('شهري', 'شهري'),
    ('نصف سنوي', 'نصف سنوي'),
    ('سنوي', 'سنوي'),
    ('ربع سنوي', 'ربع سنوي'),
    ('اخرئ', 'اخرئ')
)

version_type = (
    ('تجريبي', 'تجريبي'),
    ('رسمي', 'رسمي'),

)


class Clint_sys(models.Model):

    username = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=30, unique=True,
                            default=str(uuid.uuid4())[:8], )
    date_join = models.DateTimeField(auto_now_add=True, editable=False)
    date_expired = models.DateTimeField()
    price = models.FloatField(default=0.0, blank=True)
    subType = models.CharField(max_length=20, choices=subType_choices)
    name = models.CharField(verbose_name="Compny name",
                            max_length=50, default='', blank=True)
    version = models.CharField(max_length=20, choices=version_type)
    is_active = models.BooleanField(
        'version status', default=False, blank=True)
