from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=255)
    # orders = models.JSONField()

    def __str__(self):
        return 'name:' + self.name + ' ' + self.surname

class Item(models.Model):
    #id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    size = models.IntegerField()
    color = models.CharField(max_length=255)

    #users = models.ManyToManyField('User', through='OrderItem', related_name='item_users')

    def __str__(self):
        return "name:" + " " + self.name

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    date = models.DateField()
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_items')
    items = models.ManyToManyField(Item, related_name='order_items')



    # def __str__(self):
    #     total_price = self.amount * self.item.price
    #     return f"amount: {self.amount}, user: {self.user.name} {self.user.surname}, item: {self.item.name}, total price: {total_price}"