from django.db import models

class VendorLogin(models.Model):
    vendor_username = models.CharField(max_length=50, unique=True, blank=False)
    vendor_password = models.CharField(max_length=30, default='', blank=False)
    
    def __str__(self):
        return self.vname


class VendorPro(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    
    
    DESKTOP = 'DESKTOP'
    LAPTOP = 'LAPTOP'
    ACCESSORIES = 'ACCESSORIES'
    HARDWARE = 'HARDWARE'
    UNKNOWN = 'UNKNOWN'
    PARTS_CHOICES = (
        (DESKTOP, 'DESKTOP'),
        (LAPTOP, 'Laptop'),
        (ACCESSORIES, 'Accessories'),
        (HARDWARE, 'Hardware'),
        (UNKNOWN, 'Unknown'),
    )
    category = models.CharField(
        max_length=10,
        choices=PARTS_CHOICES,
        default=UNKNOWN,
    )

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:110]
