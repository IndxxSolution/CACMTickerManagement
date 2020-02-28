from django.db import models

# Create your models here.
class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class EdiFdsCacm(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField(blank=True, null=True)
    edi_id = models.IntegerField(db_column='EDI_id', blank=True, null=True)  # Field name made lowercase.
    fds_id = models.IntegerField(db_column='FDS_id', blank=True, null=True)  # Field name made lowercase.
    ca_type = models.CharField(db_column='CA_type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ex_date = models.DateField(blank=True, null=True)
    isin = models.CharField(max_length=20, blank=True, null=True)
    ticker = models.CharField(max_length=20, blank=True, null=True)
    mic = models.CharField(max_length=10, blank=True, null=True)
    security_name = models.CharField(max_length=100, blank=True, null=True)
    record_date = models.CharField(max_length=10, blank=True, null=True)
    payment_date = models.CharField(max_length=10, blank=True, null=True)
    gross_amount = models.FloatField(blank=True, null=True)
    net_amount = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    old_ratio = models.FloatField(blank=True, null=True)
    new_ratio = models.FloatField(blank=True, null=True)
    old_value = models.CharField(max_length=100, blank=True, null=True)
    new_value = models.CharField(max_length=100, blank=True, null=True)
    spinoff_name = models.CharField(max_length=100, blank=True, null=True)
    spinoff_ticker = models.CharField(max_length=100, blank=True, null=True)
    start_subscription = models.CharField(max_length=10, blank=True, null=True)
    end_subscription = models.CharField(max_length=10, blank=True, null=True)
    fds_isin = models.CharField(max_length=20, blank=True, null=True)
    fsym_id = models.CharField(max_length=10, blank=True, null=True)
    fds_ticker = models.CharField(max_length=20, blank=True, null=True)
    fds_ex_date = models.DateField(blank=True, null=True)
    fds_ca_type = models.CharField(max_length=50, blank=True, null=True)
    fds_gross_div = models.FloatField(blank=True, null=True)
    fds_net_div = models.FloatField(blank=True, null=True)
    fds_currency = models.CharField(max_length=10, blank=True, null=True)
    fds_split_factor = models.FloatField(blank=True, null=True)
    fds_spinoff_value = models.FloatField(blank=True, null=True)
    fds_spinoff_factor = models.FloatField(blank=True, null=True)
    difference = models.FloatField(blank=True, null=True)
    sedol = models.CharField(max_length=20, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    fds_proper_name = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edi_fds_cacm'        