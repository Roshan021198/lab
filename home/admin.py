from django.contrib import admin

from .models import Gallery,Team,Testimonials,Ceategory,ServiceProduct,Message,News


# Register your models he

 
 


class ServiceProductAdmin(admin.ModelAdmin):
    list_display=['productname','productimage','category']
    list_filter=['category'] 
    



admin.site.register(Gallery)
admin.site.register(Team)
admin.site.register(Testimonials)
admin.site.register(Ceategory)
admin.site.register(ServiceProduct,ServiceProductAdmin)
admin.site.register(Message)
admin.site.register(News)