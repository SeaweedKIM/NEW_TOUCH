from django.db import models


# Create your models here.
class Customer(models.Model):
    order_num = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True, null=False)
    gender = models.CharField(max_length=50, blank=True, null=True)
    age_group = models.CharField(max_length=255, blank=True, null=True)
    total_num = models.IntegerField(default=0, null=False)
    total_price = models.IntegerField(default=0, null=False)


class List(models.Model):
    food_num = models.BigAutoField(primary_key=True)
    food_name = models.CharField(max_length=200, null=False)
    price = models.IntegerField(default=0, null=False)
    food_explain = models.TextField(max_length=2000, blank=True, null=True)
    allergy = models.CharField(max_length=250, null=True, blank=True)
    category = models.CharField(max_length=250, null=False)
    image = models.ImageField(upload_to='static/menuimg/', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.food_name)

    # def get_photo_url(self):
    #     if self.image and hasattr(self.image, 'url'):
    #         return self.image.url


class Bill(models.Model):
    order_num = models.ForeignKey(Customer, on_delete=models.CASCADE)
    food_num = models.ForeignKey(List, on_delete=models.CASCADE)


class Favor(models.Model):
    favor_num = models.BigAutoField(primary_key=True)
    food_num = models.ForeignKey(List, on_delete=models.CASCADE)
    under30m = models.IntegerField(default=0, null=True)
    under50m = models.IntegerField(default=0, null=True)
    upper50m = models.IntegerField(default=0, null=True)
    under30f = models.IntegerField(default=0, null=True)
    under50f = models.IntegerField(default=0, null=True)
    upper50f = models.IntegerField(default=0, null=True)
    total_order = models.IntegerField(default=0, null=True)


from django.db import models

# Create your models here.
