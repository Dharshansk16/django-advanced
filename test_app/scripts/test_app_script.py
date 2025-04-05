from test_app.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint
import datetime
from django.db.models.functions import Lower


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
    # restaurant=Restaurant.objects.first()
    # user= User.objects.first()
    # rating, created =Rating.objects.get_or_create(
    #     user=user, 
    #     restaurant=restaurant,
    #     rating=1
    #     )
    # if (created==True):
    #     print("Data has been added: ",rating.rating)
    # else:
    #     print("Data Already Exists: ",rating.rating)
    # pprint(connection.queries)

    """Django Model Field Validators"""
    # user=User.objects.first()
    # restaurant= Restaurant.objects.first()
    # rating=Rating.objects.create(user=user, restaurant=restaurant, rating=9)
    # rating.full_clean() # will validate the input 
    # rating.save()
    # pprint(connection.queries)


    """DELETE AND UPDATE QUERIES"""
    # restaurant=Restaurant.objects.get(id=4)
    # print(restaurant.name)
    # restaurant.name="NEW PIZZA SHOP"
    # restaurant.save(update_fields=["name"]) #update_fields attribute will only update the specified fields
    # pprint(connection.queries)

    """Updating Queryset"""
    # restaurants= Restaurant.objects.all()
    # restaurants.update( #Updates all the records from the queryset
    #     date_opened=timezone.now(),
    # )
    # print(connection.queries)

    """LOOKUPS __startswith, __contains, __exact"""
    # restaurants= Restaurant.objects.filter(name__contains="Indian")
    # print(restaurants)
    # restaurants.update( #Updates all the records from the queryset
    #     date_opened=timezone.now(),
    # )
    # print(connection.queries)

    # querysets =Restaurant.objects.all()
    # for restaurant in querysets:
    #     print(restaurant.name)


    """Delete records"""
    # restaurants=Restaurant.objects.filter(name__startswith="PIZZA")
    # for restaurant in restaurants:
    #     print(restaurant.pk)
    #     print(restaurant.ratings)

    # restaurant=Restaurant.objects.first()

    # print(restaurant.ratings.all())
    # restaurant.delete() #deletes corresponding foreign key objects on_delete cascade
    #on delete set NULL will sets fk to null not deleting the fk related table
    


    """Management commands executed"""
    # restaurants= Restaurant.objects.all()
    # for restaurant in restaurants:
    #     print(f"Name: {restaurant.name}")
    #     for rating in restaurant.ratings.all(): 
    #             print(f"Rating: {rating}")

    # print(Restaurant.objects.count())

    """Filter restaurants of type chinese"""
    # chinese_restaurant= Restaurant.objects.filter(restaurant_type="CH")
    # restaurant=Restaurant.objects.get(name="Chinese 2") #used to retrieve only one record from the db
    # for restaurant in chinese_restaurant:
    #     print(restaurant.name)
    # pprint(connection.queries)
    # print(restaurant.restaurant_type)



    # print(Restaurant.objects.filter(name__contains="xxddd").exists())
    # pprint(connection.queries)

    # print(Restaurant.objects.filter(name__startswith="C", restaurant_type="CH")) #AND operator
    
    # check_types=["CH","IN", "MX"]
    # restaurant= Restaurant.objects.filter(restaurant_type__in=check_types) #in operator
    # print(restaurant)
    # pprint(connection.queries)
    
    """exclude()"""
    
    # check_types=["CH","IN", "MX"]
    # restaurant= Restaurant.objects.exclude(restaurant_type__in=check_types) #where not (exclude)
    # print(restaurant)
    # pprint(connection.queries)

    """More lookups"""
    # restaurant= Restaurant.objects.filter(restaurant_type__lte="D") #less than or equal to
    # print(restaurant)
    # pprint(connection.queries)

    """between (range)"""
    # sales = Sale.objects.filter(income__range=(50,60))
    # print([sale.income for sale in sales])
    # sales = Sale.objects.all()
    # for sale in sales:
    #     print(sale.income)
    # pprint(connection.queries)

    # """order by clause"""
    # restaurants= Restaurant.objects.order_by(Lower('name')) #order by ascending order case insensitive
    # restaurants_reversed = restaurants.reverse() #order by descending order
    # print(restaurants)
    # print(restaurants_reversed)

    # pprint(connection.queries)

    # restaurants= Restaurant.objects.order_by('date_opened')[:5] #limit to 5 records 
    # print(restaurants)

    # restaurant= Restaurant.objects.latest('date_opened') #earliest and latest for date time field
    # print(restaurant)

    # pprint(connection.queries)

    """Filter by FK"""
    ratings=Rating.objects.filter(restaurant__name__startswith="C")
    print(ratings)

    pprint(connection.queries)