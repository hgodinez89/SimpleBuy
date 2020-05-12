from django.db import models

from users.models import User

# Create your models here.
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    line1 = models.CharField(max_length=200)
    line2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    reference = models.CharField(max_length=300)
    postal_code = models.CharField(max_length=10, null=False, blank=False)
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.postal_code

    def has_orders(self):
        return self.order_set.count() >= 1

    def update_default(self, default=False):
        self.default = default
        self.save()

    @property
    def address(self):
        general_address = '{} - {} - {}'.format(self.city, self.state, self.country)

        return general_address[0:37] + '...' if len(general_address) > 40 else general_address

    @property
    def line1_address(self):
        return self.line1[0:40] + '...' if len(self.line1) > 40 else self.line1

    @property
    def line2_address(self):
        return self.line2[0:40] + '...' if len(self.line2) > 40 else self.line2
    
    @property
    def reference_address(self):
        return self.reference[0:40] + '...' if len(self.reference) > 40 else self.reference



