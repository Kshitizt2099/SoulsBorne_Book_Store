from django.contrib import admin
from soulsbornestore.models import customusers
from  soulsbornestore.models import Adminusers
from  soulsbornestore.models import productslist,productslist1
from  soulsbornestore.models import newlist,CartCheckout,CartCheckoutmk85,review,sales,sales1,reviewmk1


# Register your models here.
admin.site.register(customusers)
admin.site.register(Adminusers)
admin.site.register(productslist)
admin.site.register(newlist)
admin.site.register(CartCheckoutmk85)
admin.site.register(productslist1)
admin.site.register(review)
admin.site.register(sales)
admin.site.register(sales1)
admin.site.register(reviewmk1)
