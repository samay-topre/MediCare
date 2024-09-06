from django.contrib.auth.models import User
from django.db import models

# Defining choices for categories based on your index.html file
CATEGORY_CHOICES = [
    ('Cough', 'Cough'),
    ('Cold', 'Cold'),
    ('Headache', 'Headache'),
    ('First Aid', 'First Aid'),
    ('Skin Care', 'Skin Care'),
    ('Baby Care Products', 'Baby Care Products'),
    ('Proteins', 'Proteins'),
    ('Others', 'Others'),
    ('Backpain', 'Backpain'),
    ('Sore Throat', 'Sore Throat'),
    ('Asthma', 'Asthma'),
    ('Migraine', 'Migraine'),
    ('Influenza', 'Influenza'),
    ('Stomach Ache', 'Stomach Ache'),
    ('Skin Rashes', 'Skin Rashes'),
]

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='products/')
    

    def __str__(self):
        return self.name






class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Cart for {self.user.username}"




#New CartItem model
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
