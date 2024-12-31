from django.contrib import admin
from .models import User, Country, State, City, UserProfile, ItemCategory, Item, ProductCart, Order, Payment, Feedback, ContactUs


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password','date_joined')
    search_fields = ('name', 'email')

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name',)
    list_filter = ('country',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    search_fields = ('name',)
    list_filter = ('state',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'address','phone_no','image')
    search_fields = ('user__name', 'phone_no')

@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name',)
    search_fields = ('cat_name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'description','category', 'price', 'condition', 'upload_date', 'image',)
    search_fields = ('name', 'user__name', 'category__cat_name')
    list_filter = ('category', 'condition', 'upload_date')

@admin.register(ProductCart)
class ProductCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'price', 'quantity', 'order_id', 'order_status')
    search_fields = ('user__name', 'item__name', 'order_id')
    list_filter = ('order_status',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantity', 'total_price', 'order_date', 'shipping_address','delivery_date', 'status')
    search_fields = ('user__name', 'item__name')
    list_filter = ('status', 'order_date')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'order', 'amount', 'payment_mode', 'payment_status', 'payment_date')
    search_fields = ('user__name', 'order__id')
    list_filter = ('payment_mode', 'payment_status', 'payment_date')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'rating', 'comment', 'review_date')
    search_fields = ('user__name', 'item__name')
    list_filter = ('rating', 'review_date')

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'phone', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)
