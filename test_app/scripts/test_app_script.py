from test_app.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint
import datetime


def run():
    """Intialize a row of data"""
    # restaurant=Restaurant()
    # restaurant.name="Indian Restaurant"
    # restaurant.website="www.indianrestaurant.com"
    # restaurant.date_opened=timezone.now() 
    # restaurant.longitude=50.2
    # restaurant.latitude=50.2
    # restaurant.restuarant_type="Restaurant.TypeChoices.INDIAN"
    # restaurant.save()

    """Quering from the database"""
    # restaurants=Restaurant.objects.all()
    # restaurants=Restaurant.objects.first()
    # restaurants=Restaurant.objects.all()[0]
    # print(restaurants)
    # print(connection.queries)

    """create"""
    # Restaurant.objects.create(
    #     name="Pizza Shop",
    #     date_opened=timezone.now(),
    #     restaurant_type=Restaurant.TypeChoices.ITALIAN,
    #     longitude=30.2,
    #     latitude=40.2,
    # )

    # print(connection.queries)
    """Count and Last"""
    # print(Restaurant.objects.count())
    # print(Restaurant.objects.last()) #orders the table in descending order and returns the first row
    # print(connection.queries)

    """Quering Foreign Key"""
    # restaurant=Restaurant.objects.first()
    # user = User.objects.first()
    # Rating.objects.create(
    #     user=user, #Django ORM auto detects the pk value from the model_instance
    #     restaurant=restaurant,
    #     rating=Rating.RatingChoices.FOUR,
    # )
    # print(Rating.objects.all())
    # print(connection.queries)

    """Filter"""
    ##lookups - gte(>=), gt(>), lt(<), lte(<=)
    # print(Rating.objects.filter(rating__lt=3)) ##Invokes WHERE clause
    # print(connection.queries)

    # print(Rating.objects.exclude(rating__lt=3)) ## Invokes WHERE NOT clause
    # print(connection.queries)


    """Update values in the db"""
    # restaurant=Restaurant.objects.all()[1]
    # print(restaurant.name)
    # restaurant.name="PIZZA SHOP 2"
    # restaurant.save()
    # pprint(connection.queries)

    """JOIN"""
    # rating=Rating.objects.first()
    # print(rating.restaurant.longitude) # Access the other table values using foreign key relation
    # pprint(connection.queries)

    """Backward Relationship"""
    # restaurant=Restaurant.objects.first()
    # # print(restaurant.ratings.all())
    # Sale.objects.create(
    #     income=200.00,
    #     restaurant=restaurant,
    #     datetime=timezone.now()
    # )

    # restaurant=Restaurant.objects.all()[1]
    # Sale.objects.create(
    #     income=300.00,
    #     restaurant=restaurant,
    #     datetime=timezone.now(),
    # )
    # restaurant=Restaurant.objects.last()
    # Sale.objects.create(
    #     income=600.00,
    #     restaurant=restaurant,
    #     datetime=timezone.now(),
    # )
    # Sale.objects.create(
    #     income=500.00,
    #     restaurant=restaurant,
    #     datetime=timezone.now(),
    # )
    # Sale.objects.create(
    #     income=400.00,
    #     restaurant=restaurant,
    #     datetime=timezone.now(),
    # )

    # print(restaurant.sales.count())
    """get_or_create() Returns true if record is added otherwise returns false
        It first checks whether the given data is already present if present returns the object
    """
    # user= User.objects.first()
    # restaurant=Restaurant.objects.first()
    # print(Rating.objects.get_or_create(
    #     user=user, 
    #     restaurant=restaurant,
    #     rating=1
    #     ))
    # pprint(connection.queries)

    """get_or_create Continue"""
    restaurant=Restaurant.objects.first()
    user= User.objects.first()
    rating, created =Rating.objects.get_or_create(
        user=user, 
        restaurant=restaurant,
        rating=1
        )
    if (created==True):
        print("Data has been added: ",rating.rating)
    else:
        print("Data Already Exists: ",rating.rating)
    pprint(connection.queries)
