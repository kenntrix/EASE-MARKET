from django.db import models

  

class Goods_detail(models.Model):
    CATEGORY_CHOICES = (
        ('ELECTRONICS', 'Electronics'),
        ('HEATH & BEAUTY', 'Heathy & Beauty'),
        ('FURNITURE', 'Furniture'),
        ('CULTERY', 'Cultery'),
        ('BEDDINGS', 'Beddings'),
        ('CLOTHING & EQUIPMENT', 'Clothing & Equipment'),
        ('FRUITS & VEGETABLES', 'Fruits & Vegetables'),
        ('SPORTS & ARTS', 'Sports & Arts'),
        ('VEHICLES', 'Vehicles'),
        ('EQUIPMENT & CONSTRUCTION', 'Equipment & Construction'),
        ('GRAINS', 'Grains'),
        ('OTHERS', 'Others'),
    )
    item = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/images', blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, default="Others", max_length=254)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # max_digits is 10
    description = models.TextField(max_length=254)
    model = models.CharField(max_length=254, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=124, default=None)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE, related_name='items_for_sale')

    def __str__(self):
        return self.item + " " + self.description


class Client(models.Model):
    first_name = models.CharField(max_length=124)
    last_name = models.CharField(max_length=124)
    birth_date = models.DateField()
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=214)
    phone_no = models.CharField(max_length=20)  # Changed to CharField

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Seller(models.Model):
    username = models.CharField(max_length=124)
    id_number = models.IntegerField()
    current_location = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # max_digits is 10
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=214)
    phone_no = models.CharField(max_length=20)  # Changed to CharField
    item_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.username


class ContactUs(models.Model):  # 
    username = models.CharField(max_length=124)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.username
