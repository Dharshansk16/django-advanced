from django.db import models
from django.contrib.auth.models import User

#Restaurant
#User
#Rating

class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN=('IN', 'Indian')
        CHINESE=('CH', 'Chinese')
        ITALIAN=('IT', 'Italian')
        GREEK=('GK', 'Greek')
        MEXICAN=('MX', 'Mexican')
        FASTFOOD=("FF", "Fast Food")
        OTHER=('OT', 'Other')

    name=models.CharField(max_length=100)
    website=models.URLField(default="")
    date_opened=models.DateField()
    latitude=models.FloatField()
    longitude=models.FloatField()
    restaurant_type=models.CharField(max_length=2, choices=TypeChoices.choices)

    def __str__(self):
        return self.name


class Rating(models.Model):
    class RatingChoices(models.IntegerChoices):
        ONE = 1, "★☆☆☆☆"
        TWO = 2, "★★☆☆☆"
        THREE = 3, "★★★☆☆"
        FOUR = 4, "★★★★☆"
        FIVE = 5, "★★★★★"

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="ratings")
    rating=models.PositiveSmallIntegerField(choices=RatingChoices.choices, default=RatingChoices.THREE)

    def __str__(self):
        return  f"Rating : {self.rating}"

class Sale(models.Model):
    restaurant=models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name="sales")
    income=models.DecimalField(max_digits=8,decimal_places=2)
    datetime=models.DateTimeField()



