from django.conf  import settings
from django.db import models

# Create your models here.


CATEGORY_CHOICES = (
    ('08', '08oz'),
    ('16', '16oz'),
    ('20', '20oz'),
    ('32', '32oz'),
    ('40', '40oz'),
)

LABLE_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
)

class Item(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABLE_CHOICES, max_length=1)

    def __str__(self):
        return self.title

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username