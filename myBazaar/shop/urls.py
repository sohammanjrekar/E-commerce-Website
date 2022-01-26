from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name="ShopHome"),
    path('about/',views.about,name="About"),
    path('cart/',views.cart,name="Cart"),
    path('blog/',views.blog,name="Blog"),
    path('checkout',views.checkout,name="Checkout"),
    path('contact/',views.contact,name="Contact"),
    path('ordercomplete/',views.ordercomplete,name="OrderComplete"),
    path('productdetails/',views.productdetails,name="ProductDetails"),
    path('tracker/',views.tracker,name="Tracker"),
    path('shop/',views.shop,name="shop"),
]
